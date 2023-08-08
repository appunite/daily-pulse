"""The app module, containing the app factory function."""
import os

from flask import Flask
from daily_pulse.handler import handler
from daily_pulse.config import ProdConfig

def create_app(config_object=ProdConfig):
    app = Flask(__name__.split('.')[0], instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    handler(app)

    return app
