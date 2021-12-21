from flask_login import LoginManager

from src.data_model.models.user import User

login_manager = LoginManager()
login_manager.login_view = "static.index"


@login_manager.user_loader
def load_user(user_id):
    return User()
