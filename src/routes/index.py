import json

from bson.json_util import dumps
from flask import Blueprint

from src.database import db

index_bp = Blueprint("index", __name__)


@index_bp.get("/api/index")
def get_index():
    index_txt = dumps(db.proces.index.find())
    return json.loads(index_txt)


@index_bp.route("/api/index/knjiga", methods=['GET'])
def get_knjiga():
    knjiga = dumps(db.proces.knjiga.find())
    return json.loads(knjiga)