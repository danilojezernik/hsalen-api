import json

from bson.json_util import dumps
from flask import Blueprint, jsonify

from src.database import db

regresija_bp = Blueprint('regresija', __name__)


@regresija_bp.route('/api/regresija')
def get_regresija():
    regresija = dumps(db.proces.regresija.find())
    return json.loads(regresija)
