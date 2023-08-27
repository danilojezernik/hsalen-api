import json

from bson.json_util import dumps
from flask import Blueprint, jsonify
from flask_openapi3 import APIBlueprint

from src.database import db
from src.operation_id import operation_id_callback

regresija_bp = APIBlueprint('regresija', __name__, operation_id_callback=operation_id_callback)


@regresija_bp.get('/api/regresija')
def get_regresija():
    regresija = dumps(db.proces.regresija.find())
    return json.loads(regresija)
