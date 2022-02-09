import atexit

from flask import Flask

from . import events, settings, tasks
from .extensions import scheduler


def init_app(app: Flask):
    app.config.from_object(settings)

    scheduler.init_app(app)
    scheduler.start()

    atexit.register(scheduler.shutdown)
