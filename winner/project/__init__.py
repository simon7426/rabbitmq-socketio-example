import os

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from project.config import config

socketio = SocketIO()
cors = CORS()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    socketio.init_app(
        app,
        message_queue=app.config["SOCKETIO_MESSAGE_QUEUE"],
        cors_allowed_origins="*",
    )

    cors.init_app(app)

    from project.api import api

    api.init_app(app)

    # from project.api.events import socketio_instance

    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
