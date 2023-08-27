from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint

from src.operation_id import operation_id_callback

admin_bp = APIBlueprint("admin", __name__, operation_id_callback=operation_id_callback)


# ADMIN
@admin_bp.post("/api/admin")
@jwt_required()
def admin():
    return jsonify({'msg': 'Ste vpisani!'})
