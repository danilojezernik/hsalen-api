import json

from bson.json_util import dumps
from flask import Blueprint

from src.database import db

index_bp = Blueprint("index", __name__)


@index_bp.route("/api/index", methods=['GET'])
def get_index():
    index = dumps(db.proces.index.find())
    return json.loads(index)


@index_bp.route("/api/index/knjiga", methods=['GET'])
def get_knjiga():
    knjiga = dumps(db.proces.knjiga.find())
    return json.loads(knjiga)