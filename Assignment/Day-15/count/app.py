from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    username = request.cookies.get("username")

    if request.method == "POST":
        username = request.form.get("username")

    # Get visit count from cookie (default = 0)
    visit_count = int(request.cookies.get("visit_count", 0))

    # Increase count
    visit_count += 1

    resp = make_response(render_template("index.html", name=username, count=visit_count))

    if username:
        resp.set_cookie("username", username)

    resp.set_cookie("visit_count", str(visit_count))

    return resp


if __name__ == "__main__":
    app.run(debug=True)