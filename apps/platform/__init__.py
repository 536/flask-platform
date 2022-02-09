from flask import Flask

from . import settings
from .views import bp


def init_app(app: Flask):
    app.config.from_object(settings)

    app.register_blueprint(bp)
