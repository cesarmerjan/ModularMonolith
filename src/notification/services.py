from src._shared.database.repository import DatabaseRepository
from src._shared.database.unit_of_work import DatabaseUnitOfWork
from src._shared.events.schemas import VerifyUserMessageSchema
from src.authentication.facade import AuthenticationFacade
from src.notification.models import VerificationLinkModel


def get_user_uuid(unit_of_work: DatabaseUnitOfWork, hexcode: str) -> str:
    with unit_of_work:
        repository = DatabaseRepository(unit_of_work.session)
        record = repository.get_where(VerificationLinkModel, hexcode=hexcode)
        user_uuid = record.user_uuid
    return user_uuid


def verify_user(
    unit_of_work: DatabaseUnitOfWork,
    hexcode: str,
) -> None:
    user_uuid = get_user_uuid(unit_of_work, hexcode)
    AuthenticationFacade.set_user_as_verified(unit_of_work, user_uuid)


def send_verification_email(
    unit_of_work: DatabaseUnitOfWork,
    user_message: VerifyUserMessageSchema,
) -> None:
    with unit_of_work:
        repository = DatabaseRepository(unit_of_work.session)
        record = VerificationLinkModel(user_uuid=user_message.uuid)
        repository.add(record)
        unit_of_work.commit()

    print(f"http://localhost:5000/verify-user/{record.hexcode}")
