from flask import Blueprint, request
from flask_login import login_required

from src.handlers.meal_handler import MealHandler


meal_blueprint = Blueprint("meal", __name__, url_prefix="/meals")


@meal_blueprint.route("", methods=["GET"])
@meal_blueprint.route("/", methods=["GET"])
@login_required
def list_meals():
    return MealHandler.list()


@meal_blueprint.route("/new", methods=["GET"])
@meal_blueprint.route("/new/", methods=["GET"])
@login_required
def new_meal():
    return MealHandler.new()


@meal_blueprint.route("", methods=["POST"])
@meal_blueprint.route("/", methods=["POST"])
@login_required
def create_meal():
    return MealHandler.create(request.form)


@meal_blueprint.route("/<int:meal_id>", methods=["GET"])
@meal_blueprint.route("/<int:meal_id>/", methods=["GET"])
@login_required
def get_meal(meal_id):
    return MealHandler.get(meal_id)


@meal_blueprint.route("/<int:meal_id>/edit", methods=["GET"])
@meal_blueprint.route("/<int:meal_id>/edit/", methods=["GET"])
@login_required
def edit_meal(meal_id):
    return MealHandler.edit(meal_id)


@meal_blueprint.route("/<int:meal_id>", methods=["POST", "PUT", "PATCH"])
@login_required
def update_meal(meal_id):
    return MealHandler.update(meal_id, request.form)


@meal_blueprint.route("/<int:meal_id>", methods=["DELETE"])
@meal_blueprint.route("/<int:meal_id>/delete", methods=["POST"])
def delete_meal(meal_id):
    return MealHandler.delete(meal_id)
