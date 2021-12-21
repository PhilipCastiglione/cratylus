import os

SECRET_KEY = os.environ.get("SECRET_KEY")
DB_USER = os.environ.get("DB_USER")
DB_PW = os.environ.get("DB_PW")
DB_HOST = os.environ.get("DB_HOST")
DB_PREFIX = os.environ.get("DB_PREFIX")
FLASK_ENV = os.environ.get("FLASK_ENV")

DB_NAME = f"{DB_PREFIX}{FLASK_ENV}"
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PW}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = FLASK_ENV != "production"
