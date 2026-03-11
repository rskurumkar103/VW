from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    role = request.args.get("role", "employee").lower()

    if role == "admin":
        sections = ["User Management", "System Reports"]
        fields = ["Username", "Email", "Role", "Status"]
        action_buttons = ["Add User", "Delete User", "Generate Report"]

    elif role == "manager":
        sections = ["Employee Management", "Reports"]
        fields = ["Employee Name", "Department", "Status"]
        action_buttons = ["Add Employee", "Delete Employee"]

    else:  # employee
        sections = ["Employee Services"]
        fields = ["Employee ID", "Date", "Status"]
        action_buttons = ["Mark Attendance", "Raise Leave"]

    return render_template(
        "index.html",
        role=role.capitalize(),
        sections=sections,
        fields=fields,
        action_buttons=action_buttons
    )

if __name__ == "__main__":
    app.run(debug=True)