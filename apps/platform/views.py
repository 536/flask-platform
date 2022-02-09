from flask import Blueprint, render_template, request

bp = Blueprint('platform', __name__, url_prefix='/platform', static_folder='static', template_folder='templates')


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', **{
        'host': request.headers['Host']
    })
