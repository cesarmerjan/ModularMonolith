import threading

from time import sleep

from src._shared.events import services as events_services
from src._shared.events.domain import EventTypeChoices
from src._shared.events.schemas import VerifyUserMessageSchema
from src.contexts import DatabaseContext
from src.notification import services as notification_services
from src.notification.settings import DOMAIN_NAME


class VerifyUserDaemon:
    def __init__(
        self,
        database_context: DatabaseContext,
        waiting_seconds: int = 5,
    ) -> None:
        self._waiting_seconds = waiting_seconds
        self.database_context = database_context

    def run(self):
        while True:
            try:
                for message in events_services.poll_messages(
                    self.database_context.unit_of_work,
                    EventTypeChoices.VERIFY_USER,
                ):
                    user_message = VerifyUserMessageSchema(**message)
                    notification_services.send_verification_email(
                        self.database_context.unit_of_work,
                        user_message,
                    )
            except Exception:
                pass
            sleep(self._waiting_seconds)


daemon = threading.Thread(
    target=VerifyUserDaemon(
        DatabaseContext(DOMAIN_NAME),
    ).run,
    daemon=True,
)
