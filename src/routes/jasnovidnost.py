import json

from bson.json_util import dumps
from flask import Blueprint

from src.database import db

jasnovidnost_bp = Blueprint('jasnovidnost', __name__)


@jasnovidnost_bp.route('/api/jasnovidnost')
def get_jasnovidnost():
    jasnovidnost = dumps(db.proces.jasnovidnost.find())
    return json.loads(jasnovidnost)
