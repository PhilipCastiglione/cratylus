from dotenv import load_dotenv
from flask import Flask

from .routing import create_routes

load_dotenv()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    create_routes(app)

    return app
