import os

from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_openapi3 import APIBlueprint

from src.operation_id import operation_id_callback

login_bp = APIBlueprint("login", __name__, operation_id_callback=operation_id_callback)

db_username = os.getenv('UPORABNIK')
db_geslo = os.getenv('GESLO')


# LOGIN
@login_bp.post("/api/login")
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if username != db_username or password != db_geslo:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
