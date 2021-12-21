from flask import Blueprint

from src.handlers.static_handler import StaticHandler


static_blueprint = Blueprint("static", __name__)


@static_blueprint.route("/", methods=["GET"])
@static_blueprint.route("/login", methods=["GET"])
def index():
    return StaticHandler.index()

@static_blueprint.route("/about", methods=["GET"])
@static_blueprint.route("/about/", methods=["GET"])
def about():
    return StaticHandler.about()