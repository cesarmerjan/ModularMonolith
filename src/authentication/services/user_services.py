from src._shared.database.repository import DatabaseRepository
from src._shared.database.unit_of_work import DatabaseUnitOfWork
from src.authentication.models.users import UserModel
from src.authentication.serializers.users import UserIn, UserOut
from src.authentication.services import security_services


def _create_user(name: str, email: str, password: str) -> UserModel:
    hashed_password = security_services.generate_password_hash(password)

    user_model = UserModel(
        name=name,
        email=email,
        hashed_password=hashed_password,
    )
    return user_model


def create_user(
    unit_of_work: DatabaseUnitOfWork,
    user_in: UserIn,
) -> str:

    user_model = _create_user(user_in.name, user_in.email, user_in.password)

    with unit_of_work:
        repository = DatabaseRepository(unit_of_work.session)
        repository.add(user_model)
        unit_of_work.commit()

    return user_model.uuid


def get_user_by_id(unit_of_work: DatabaseUnitOfWork, user_uuid: str) -> dict:
    with unit_of_work:
        repository = DatabaseRepository(unit_of_work.session)
        user_model = repository.get_where(UserModel, uuid=user_uuid)
        user_data = UserOut.from_orm(user_model)
    return user_data.dict()


def set_user_as_verified(unit_of_work: DatabaseUnitOfWork, user_uuid: str) -> None:
    with unit_of_work:
        repository = DatabaseRepository(unit_of_work.session)
        user_model = repository.get_where(UserModel, uuid=user_uuid)
        repository.update(user_model, is_verified=True)
        unit_of_work.commit()
    return None
