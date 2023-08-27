import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db
from src.operation_id import operation_id_callback

index_bp = APIBlueprint("index", __name__, operation_id_callback=operation_id_callback)


@index_bp.get("/api/index")
def get_index():
    index_txt = dumps(db.proces.index.find())
    return json.loads(index_txt)


@index_bp.get("/api/index/knjiga")
def get_knjiga():
    knjiga = dumps(db.proces.knjiga.find())
    return json.loads(knjiga)