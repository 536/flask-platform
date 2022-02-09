from flask import Flask

from . import settings
from .extensions import db


def init_app(app: Flask):
    app.config.from_object(settings)

    db.init_app(app)
