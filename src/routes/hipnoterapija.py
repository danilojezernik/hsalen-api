import json

from bson.json_util import dumps
from flask import Blueprint, jsonify

from src.database import db

hipnoterapija_bp = Blueprint("hipnoterapija", __name__)


@hipnoterapija_bp.route("/api/hipnoterapija", methods=['GET'])
def get_hipnoterapija():
    hipnoterapija = dumps(db.proces.hipnoterapija.find())
    return json.loads(hipnoterapija)
