# project/app/config.py


import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: int = os.getenv("TESTING", 0)  # type: ignore
    database_url: AnyUrl = os.environ.get("DATABASE_URL")  # type: ignore

    # Authentication settings
    gold_user: str = "admin"
    gold_password: str = "pass"
    secret_key: str = "S3cr3t"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
