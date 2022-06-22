import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", False)
    secret: str = os.getenv("SECRET_KEY", "brilliant")
    expiration: int = os.getenv("EXPIRATION_TIME", 3000)
    rmq_user: str = os.getenv("RABBIT_USER", "test")
    rmq_pass: str = os.getenv("RABBIT_PASS", "test")
    rmq_host: str = os.getenv("RABBIT_HOST","localhost")


@lru_cache
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()