from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/all', methods=['GET'])
def api_list():
    return {"code": 0, "msg": "", "result": "all"}
