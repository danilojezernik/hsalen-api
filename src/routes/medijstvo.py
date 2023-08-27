import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db
from src.operation_id import operation_id_callback

medijstvo_bp = APIBlueprint('medijstvo', __name__, operation_id_callback=operation_id_callback)


@medijstvo_bp.get('/api/medijstvo')
def get_medijstvo():
    medijstvo = dumps(db.proces.medijstvo.find())
    return json.loads(medijstvo)
