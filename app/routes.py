from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mongo

api_bp = Blueprint("api", __name__)

@api_bp.route("/lead", methods=["POST"])
@jwt_required()
def add_lead():
    user = get_jwt_identity()
    if user["role"] != "agent":
        return {"msg": "Forbidden"}, 403

    data = request.json
    mongo.db.leads.insert_one(data)
    return {"msg": "Lead added"}, 201
