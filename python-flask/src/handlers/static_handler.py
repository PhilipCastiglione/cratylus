from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from is_safe_url import is_safe_url

from src.data_model.models.base import db
from src.data_model.models.user import User


class StaticHandler():
    @classmethod
    def index(cls, form_values=None):
        return render_template("static/index.html", form_values=form_values or {})

    @classmethod
    def about(cls):
        return render_template("static/about.html")

    @classmethod
    def login(cls, login_params):
        email = login_params.get("email")
        password = login_params.get("password")
        next = login_params.get("next")
        remember = login_params.get("remember")

        login_errors = []

        if not email:
            login_errors.append("email is required")
        
        if not password:
            login_errors.append("password required")
        
        user = User.query.filter_by(email=email).first()

        if not user:
            login_errors.append("no user with this email")

        if user and not user.authenticate(password):
            login_errors.append("password was incorrect")

        if login_errors:
            flash(f"Login failed: {', '.join(login_errors)}")

            return cls.index(form_values=login_params)
        
        login_user(user, remember=bool(remember))
        user.authenticated = True
        db.session.add(user)
        db.session.commit()

        if next and is_safe_url(next, request.host):
            return redirect(next)
        else:
            return redirect(url_for("static.index"))

    @classmethod
    def logout(cls):
        user = current_user._get_current_object()
        logout_user()
        if (user and user.id):
            user.authenticated = False
            db.session.add(user)
            db.session.commit()

        return redirect(url_for("static.index"))

    @classmethod
    def error(cls, error):
        return render_template("static/error.html", error=error)
