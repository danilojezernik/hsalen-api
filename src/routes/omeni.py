import json

from bson.json_util import dumps
from flask import Blueprint

from src.database import db

omeni_bp = Blueprint('omeni', __name__)


@omeni_bp.route('/api/omeni', methods=['GET'])
def get_omeni():
    omeni = dumps(db.proces.jaz.find())
    return json.loads(omeni)


@omeni_bp.route('/api/mediji', methods=['GET'])
def get_mediji():
    mediji = dumps(db.proces.mediji.find())
    return json.loads(mediji)


