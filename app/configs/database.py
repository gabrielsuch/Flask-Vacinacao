from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.db = db

    from app.models.vaccination_models import Vaccination