import os

from src._shared.utils import load_environment_variables

ENVIRONMENT = "local"

ROOT_DIRECTORY: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_environment_variables(ROOT_DIRECTORY)

SHARED_MODELES_NAMES = ("facade", "interface", "contexts")
