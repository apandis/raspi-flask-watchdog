from flask import Blueprint, render_template, jsonify
from .monitor import check_all

# UI blueprint

ui_bp = Blueprint('ui', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

@ui_bp.route('/')
def index():
    """Render the main status dashboard."""
    return render_template('index.html', status=check_all())

@api_bp.route('/status')
def status():
    """Return JSON with current status of targets."""
    return jsonify(check_all())