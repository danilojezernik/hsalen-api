import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db
from src.operation_id import operation_id_callback

hipnoterapija_bp = APIBlueprint("hipnoterapija", __name__, operation_id_callback=operation_id_callback)


@hipnoterapija_bp.get("/api/hipnoterapija")
def get_hipnoterapija():
    hipnoterapija = dumps(db.proces.hipnoterapija.find())
    return json.loads(hipnoterapija)
