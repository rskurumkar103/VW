from flask import Flask, render_template

app = Flask(__name__)

@app.route("/students")
def show_students():
    students = [
        {"name": "RK", "marks": 88},
        {"name": "SK", "marks": 77},
        {"name": "XYZ", "marks": 45},
        {"name": "Rohan", "marks": 30}
    ]
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)