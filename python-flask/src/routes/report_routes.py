from flask import Blueprint
from flask_login import login_required

from src.handlers.report_handler import ReportHandler


report_blueprint = Blueprint("report", __name__, url_prefix="/reports")


@report_blueprint.route("", methods=["GET"])
@report_blueprint.route("/", methods=["GET"])
@login_required
def reports_index():
    return ReportHandler.index()


@report_blueprint.route("", methods=["POST"])
@report_blueprint.route("/", methods=["POST"])
@login_required
def generate_report():
    return ReportHandler.generate()


@report_blueprint.route("/<int:report_id>", methods=["GET"])
@report_blueprint.route("/<int:report_id>/", methods=["GET"])
@login_required
def get_report(report_id):
    return ReportHandler.get(report_id)
