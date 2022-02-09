from flask import Flask
from flask_api import FlaskAPI

from . import api, auth, platform, schedule, db


def create_app():
    app = FlaskAPI(__name__)

    api.init_app(app)
    auth.init_app(app)
    db.init_app(app)
    platform.init_app(app)
    schedule.init_app(app)

    return app
