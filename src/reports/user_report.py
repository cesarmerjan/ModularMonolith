import os
from src.authentication.facade import AuthenticationFacade
from src.contexts import DatabaseContext
from src.settings import ROOT_DIRECTORY

DOMAIN_NAME = "reports"
REPORT_DIRECTORY = os.path.join(ROOT_DIRECTORY, f"src/{DOMAIN_NAME}/data")

database_context = DatabaseContext(DOMAIN_NAME)


def generate_report(user_uuid: str):
    user_data = AuthenticationFacade.get_user_by_id(
        database_context.unit_of_work,
        user_uuid,
    )
    with open(f"{REPORT_DIRECTORY}/user_report.txt", "a+") as _file:
        _file.write("\n".join([f"{key}: {value}" for key, value in user_data.items()]))


if __name__ == "__main__":
    user_uuid = "510d761f-56b0-4db9-8294-61dcb740cc74"
    generate_report(user_uuid)
