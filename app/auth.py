from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    # Mock user, in real apps use DB
    if username == "agent" and password == "123":
        access_token = create_access_token(identity={"username": username, "role": "agent"})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad credentials"}), 401
