import os
from enum import Enum

from sqlalchemy.engine import URL

from src._shared.utils import load_environment_variables
from src.settings import ROOT_DIRECTORY

DOMAIN_NAME = "_shared"
DOMAIN_PATH = os.path.join(ROOT_DIRECTORY, f"src/{DOMAIN_NAME}/")

load_environment_variables(DOMAIN_PATH)


class DatabaseConfig:
    DIALECT = os.environ.get("DATABASE_DIALECT")
    DRIVER = os.environ.get("DATABASE_DRIVER")
    HOST = os.environ.get("DATABASE_HOST")
    PORT = (
        int(os.environ.get("DATABASE_PORT"))
        if os.environ.get("DATABASE_PORT")
        else None
    )
    NAME = os.environ.get("DATABASE_NAME")
    USERNAME = os.environ.get("DATABASE_USERNAME")
    PASSWORD = os.environ.get("DATABASE_PASSWORD")

    @classmethod
    def to_url(cls) -> URL:
        protocol = f"{cls.DIALECT}+{cls.DRIVER}" if cls.DRIVER else cls.DIALECT
        return URL.create(
            protocol,
            username=cls.USERNAME,
            password=cls.PASSWORD,
            host=cls.HOST,
            port=cls.PORT,
            database=cls.NAME,
        )
