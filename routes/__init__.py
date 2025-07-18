from .main import main_bp
from .about import about_bp
from .apps import apps_bp 
from .blogs import blogs_bp 


def register_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(apps_bp)
    app.register_blueprint(blogs_bp)