from dotenv import load_dotenv
from flask import Flask
from werkzeug.exceptions import HTTPException

from src.data_model.models.base import db
from src.routes import static_routes, meal_routes, report_routes
from src.authentication import login_manager

load_dotenv()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    app.register_blueprint(static_routes.static_blueprint)
    app.register_blueprint(meal_routes.meal_blueprint)
    app.register_blueprint(report_routes.report_blueprint)

    app.register_error_handler(HTTPException, static_routes.handle_http_error)
    app.register_error_handler(Exception, static_routes.handle_other_error)

    db.init_app(app)
    login_manager.init_app(app)
    
    return app
