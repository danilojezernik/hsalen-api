import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db

hipnoterapija_bp = APIBlueprint("hipnoterapija", __name__)


@hipnoterapija_bp.get("/api/hipnoterapija")
def get_hipnoterapija():
    hipnoterapija = dumps(db.proces.hipnoterapija.find())
    return json.loads(hipnoterapija)
