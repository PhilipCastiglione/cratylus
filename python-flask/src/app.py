from dotenv import load_dotenv
from flask import Flask

from src.routes import static_routes, meal_routes, report_routes
from src.authentication import login_manager

load_dotenv()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    app.register_blueprint(static_routes.static_blueprint)
    app.register_blueprint(meal_routes.meal_blueprint)
    app.register_blueprint(report_routes.report_blueprint)

    login_manager.init_app(app)
    
    return app
