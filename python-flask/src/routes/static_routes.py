import os

from flask import Blueprint, request
from werkzeug.exceptions import InternalServerError

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


@static_blueprint.route("/login", methods=["POST"])
def login():
    return StaticHandler.login(request.form)


@static_blueprint.route("/logout", methods=["POST"])
def logout():
    return StaticHandler.logout()


def handle_http_error(error):
    return StaticHandler.error(error)


def handle_other_error(error):
    if os.environ.get("FLASK_ENV") == "production":
        return StaticHandler.error(
            InternalServerError(description="An unknown error has occurred.")
        )
    else:
        raise(error)
