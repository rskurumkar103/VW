from flask import Blueprint, request, session, jsonify, render_template

auth_bp = Blueprint("auth", __name__, template_folder="../templates")

# Dummy login page (optional)
@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

# Login API
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username required"}), 400

    session["username"] = username
    return jsonify({"message": f"Logged in as {username}"})