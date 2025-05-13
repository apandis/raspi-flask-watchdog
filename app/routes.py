from flask import Blueprint, render_template, jsonify
from .monitor import check_all

# UI blueprint\ nui_bp = Blueprint('ui', __name__)
# API blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')

@ui_bp.route('/')
def index():
    return render_template('index.html', status=check_all())

@api_bp.route('/status')
def status():
    return jsonify(check_all())