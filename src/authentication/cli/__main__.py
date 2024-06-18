from src.authentication.cli.factory import cli
from src.authentication.settings import DOMAIN_NAME
from src.contexts import DatabaseContext

if __name__ == "__main__":
    cli(obj=DatabaseContext(DOMAIN_NAME))
