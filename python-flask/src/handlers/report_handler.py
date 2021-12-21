from flask import render_template


class ReportHandler():
    @classmethod
    def index(cls):
        return render_template("static/about.html")

    @classmethod
    def generate(cls):
        return render_template("static/about.html")

    @classmethod
    def get(cls):
        return render_template("static/about.html")
