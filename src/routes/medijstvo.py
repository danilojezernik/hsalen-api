import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db

medijstvo_bp = APIBlueprint('medijstvo', __name__)


@medijstvo_bp.get('/api/medijstvo')
def get_medijstvo():
    medijstvo = dumps(db.proces.medijstvo.find())
    return json.loads(medijstvo)
