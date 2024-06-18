from src.contexts import DatabaseContext
from src._shared.database.unit_of_work import DatabaseUnitOfWork
from src.authentication.services import user_services


class AuthenticationFacade:

    @staticmethod
    def set_user_as_verified(
        unit_of_work: DatabaseUnitOfWork,
        user_uuid: str,
    ) -> None:
        return user_services.set_user_as_verified(
            unit_of_work,
            user_uuid,
        )

    @staticmethod
    def get_user_by_id(
        unit_of_work: DatabaseUnitOfWork,
        user_uuid: str,
    ) -> dict:
        return user_services.get_user_by_id(
            unit_of_work,
            user_uuid,
        )
