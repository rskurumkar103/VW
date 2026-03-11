from flask import render_template, request, redirect
from . import hr_bp

@hr_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")
    username = request.cookies.get("username")

    if not role or role != "hr":
        return redirect("/login")

    return render_template("hr_dashboard.html", name=username)