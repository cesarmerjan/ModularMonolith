import os
from typing import Optional

from src._shared.utils import load_environment_variables
from src.settings import ENVIRONMENT, ROOT_DIRECTORY

DOMAIN_NAME = "notification"
DOMAIN_PATH = os.path.join(ROOT_DIRECTORY, f"src/{DOMAIN_NAME}/")

load_environment_variables(DOMAIN_PATH)


class ApiSettings:
    DEBUG: bool = ENVIRONMENT.lower() in ("local", "test")
    DOCS_URL: Optional[str] = "/" if ENVIRONMENT.lower() in ("local", "test") else None


class ApiServerSettings:
    WORKERS: int = int(os.getenv("NOTIFICATION_API_SERVER_WORKERS", "1"))
    PORT: int = int(os.getenv("NOTIFICATION_API_SERVER_PORT", "5000"))
    HOST: str = os.getenv("NOTIFICATION_API_SERVER_HOST", "127.0.0.1")
    RELOAD: bool = ENVIRONMENT.lower() in ("local", "test")
