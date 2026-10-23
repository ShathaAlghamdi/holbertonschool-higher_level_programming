#!/usr/bin/env python3
"""API security using Basic Auth and JWT."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)

    if user and check_password_hash(user["password"], password):
        return username

    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if (
        user is None
        or not check_password_hash(user["password"], password)
    ):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    return jsonify(access_token=token), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token"}), 401


if __name__ == "__main__":
    app.run()
