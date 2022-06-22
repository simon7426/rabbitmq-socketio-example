import os


class BaseConfig:
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "my_precious")
    SOCKETIO_MESSAGE_QUEUE = os.environ.get(
        "SOCKETIO_MESSAGE_QUEUE", "redis://127.0.0.1:6379/0"
    )

    # Force all queues to be explicitly listed in `CELERY_TASK_QUEUES` to help prevent typos
    ERROR_404_HELP = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestingConfig(BaseConfig):
    TESTING = True
    SOCKETIO_MESSAGE_QUEUE = None


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
