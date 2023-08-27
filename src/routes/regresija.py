import json

from bson.json_util import dumps
from flask import Blueprint, jsonify
from flask_openapi3 import APIBlueprint

from src.database import db

regresija_bp = APIBlueprint('regresija', __name__)


@regresija_bp.get('/api/regresija')
def get_regresija():
    regresija = dumps(db.proces.regresija.find())
    return json.loads(regresija)
