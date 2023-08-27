from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint

admin_bp = APIBlueprint("admin", __name__)


# ADMIN
@admin_bp.post("/api/admin")
@jwt_required()
def admin():
    return jsonify({'msg': 'Ste vpisani!'})
