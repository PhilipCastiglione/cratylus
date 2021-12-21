from flask import render_template


class StaticHandler():
    @classmethod
    def index(cls):
        return render_template("static/index.html")

    @classmethod
    def about(cls):
        return render_template("static/about.html")
