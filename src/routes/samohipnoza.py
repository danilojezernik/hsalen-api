from flask import Blueprint, jsonify

samohipnoza_bp = Blueprint('samohipnoza', __name__)


@samohipnoza_bp.route('/api/samohipnoza')
def get_samohipnoza():
    return jsonify({'stran': 'SAMOHIPNOZA'})
