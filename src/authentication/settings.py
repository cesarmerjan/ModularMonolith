import os

from src._shared.utils import load_environment_variables
from src.settings import ROOT_DIRECTORY

DOMAIN_NAME = "authentication"
DOMAIN_PATH = os.path.join(ROOT_DIRECTORY, f"src/{DOMAIN_NAME}/")

load_environment_variables(DOMAIN_PATH)
