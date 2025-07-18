from flask import Blueprint, render_template

apps_bp = Blueprint('apps', __name__)

@apps_bp.route('/apps')
def apps():
    return render_template('apps.html')