from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    error = ""
    success = ""

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # Validation
        if not email or not password:
            error = "Fields should not be blank"

        elif "@" not in email:
            error = "Email should have @ symbol"

        elif len(password) < 5 or len(password) > 8:
            error = "Password should be at least 5 and maximum 8 characters long"

        else:
            success = "Form submitted successfully!"

    return render_template("index.html", error=error, success=success)


if __name__ == "__main__":
    app.run(debug=True)