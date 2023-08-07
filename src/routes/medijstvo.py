import json

from bson.json_util import dumps
from flask import Blueprint, jsonify

from src.database import db

medijstvo_bp = Blueprint('medijstvo', __name__)


@medijstvo_bp.route('/api/medijstvo')
def get_medijstvo():
    medijstvo = dumps(db.proces.medijstvo.find())
    return json.loads(medijstvo)
