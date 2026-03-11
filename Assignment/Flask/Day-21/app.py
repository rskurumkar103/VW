from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)

# Load conf
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'Admin', 'Manager', or 'Employee'

# Define the Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    manager = db.relationship('Employee', remote_side=[id], backref='team')
    user = db.relationship('User', backref='employee')

# Role-based access control decorator
def requires_role(role):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if 'role' not in session or session['role'] != role:
                return redirect(url_for('login'))  # Redirect to login if not authorized
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query database for user
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):  # Check password
            session['user_id'] = user.id
            session['role'] = user.role  # Store role in session
            return redirect(url_for('view_all_employees'))  # Redirect to employee list
        else:
            flash('Invalid credentials, please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

# View all employees (Admin & Manager only)
@app.route('/employees')
@requires_role('Admin')  # Only Admin can access this route
@requires_role('Manager')  # Managers can view all employees
def view_all_employees():
    employees = Employee.query.all()  # Get all employees from the database
    return render_template('employees.html', employees=employees)

# View employee profile (Employee can view and edit own profile)
@app.route('/employee/<int:id>')
def employee_profile(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    employee = Employee.query.filter_by(id=id).first()

    if not employee:
        flash('Employee not found')
        return redirect(url_for('view_all_employees'))

    # Check if user is employee and owns this profile
    if session['role'] == 'Employee' and employee.user_id != session['user_id']:
        return redirect(url_for('home'))  # Prevent accessing other profiles
    
    return render_template('employee_profile.html', employee=employee)

# Edit employee details (Admin can edit any employee; Employees can edit only their own profile)
@app.route('/employee/<int:id>/edit', methods=['GET', 'POST'])
def edit_employee(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    employee = Employee.query.filter_by(id=id).first()
    
    if not employee:
        flash('Employee not found')
        return redirect(url_for('view_all_employees'))

    if session['role'] == 'Employee' and employee.user_id != session['user_id']:
        return redirect(url_for('home'))  # Prevent employees from editing others' profiles

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.department = request.form['department']
        db.session.commit()  # Save changes to the database
        flash('Employee updated successfully!')
        return redirect(url_for('employee_profile', id=employee.id))

    return render_template('edit_employee.html', employee=employee)

# Delete employee (Admin only)
@app.route('/employee/<int:id>/delete')
@requires_role('Admin')  # Only Admin can delete an employee
def delete_employee(id):
    employee = Employee.query.filter_by(id=id).first()
    
    if employee:
        db.session.delete(employee)
        db.session.commit()
        flash('Employee deleted successfully!')
    else:
        flash('Employee not found')
    
    return redirect(url_for('view_all_employees'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    return redirect(url_for('home'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)