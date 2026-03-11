from flask import render_template, request, redirect, make_response
from . import auth_bp
from datetime import datetime, timedelta

# Dummy users
users = {
    "admin": "admin",
    "employee": "employee",
    "hr": "hr"
}

@auth_bp.route("/", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        remember = request.form.get("remember")

        if username and role in users:

            resp = make_response(redirect(f"/{role}/dashboard"))

            # Cookie expiry
            if remember:
                expiry = datetime.now() + timedelta(days=7)
                resp.set_cookie("username", username, expires=expiry)
                resp.set_cookie("user_role", role, expires=expiry)
            else:
                resp.set_cookie("username", username)
                resp.set_cookie("user_role", role)

            return resp

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    resp = make_response(redirect("/login"))
    resp.delete_cookie("username")
    resp.delete_cookie("user_role")
    return resp