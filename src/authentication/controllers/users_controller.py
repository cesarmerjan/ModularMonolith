from src.contexts import DatabaseContext
from src._shared.database.unit_of_work import DatabaseUnitOfWork
from src._shared.events import services as events_services
from src._shared.events.domain import EventTypeChoices
from src._shared.events.schemas import VerifyUserMessageSchema
from src.authentication.presenters.stdout_presenter import StdoutPresenter
from src.authentication.serializers.users import UserIn
from src.authentication.services import user_services


class UsersController:
    def __init__(self, database_context: DatabaseContext, presenter: StdoutPresenter):
        self.database_context = database_context
        self.presenter = presenter

    def create_user(self, name: str, email: str, password: str) -> None:
        try:
            unit_of_work = self.database_context.unit_of_work
            user_in = UserIn(name=name, email=email, password=password)
            user_uuid = user_services.create_user(unit_of_work, user_in)

            verify_user_message = VerifyUserMessageSchema(user_uuid, email)
            events_services.send_message(
                unit_of_work,
                verify_user_message.as_dict,
                EventTypeChoices.VERIFY_USER,
            )

            self.presenter.render({"message": "user created successfully"}, "success")
        except Exception as error:
            self.presenter.render({"message": str(error)}, "error")

    def get_user_by_uuid(self, user_uuid: str) -> dict:
        try:
            unit_of_work = self.database_context.unit_of_work
            user_data = user_services.get_user_by_id(unit_of_work, user_uuid)
            self.presenter.render(user_data, "success")
        except Exception as error:
            self.presenter.render({"message": str(error)}, "error")
