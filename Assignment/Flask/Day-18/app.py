from flask import Flask

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return {
        "number1": num1,
        "number2": num2,
        "sum": result
    }

if __name__ == "__main__":
    app.run(debug=True)