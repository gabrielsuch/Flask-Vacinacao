from flask import Flask
from app.routes.vaccinations_routes import bp


def init_app(app: Flask):
    app.register_blueprint(bp)