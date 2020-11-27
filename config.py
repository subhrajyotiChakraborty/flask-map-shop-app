import os

DEBUG = False
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL", "sqlite:///data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
SECRET_KET = os.environ.get("SECRET_KEY")
