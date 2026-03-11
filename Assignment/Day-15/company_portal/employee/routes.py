from flask import render_template, request, redirect
from . import employee_bp

@employee_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")
    username = request.cookies.get("username")

    if not role or role != "employee":
        return redirect("/login")

    return render_template("employee_dashboard.html", name=username)