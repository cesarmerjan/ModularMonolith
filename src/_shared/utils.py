import os

from dotenv import load_dotenv


def load_environment_variables(
    path_to_dotenv_file: str,
    dotenv_file_name: str = ".env",
) -> None:
    dotenv_path = os.path.join(path_to_dotenv_file, dotenv_file_name)
    load_dotenv(dotenv_path)
