from typing import Iterator, Union

from sqlalchemy.orm.scoping import ScopedSession
from sqlalchemy.orm.session import Session

from src._shared.events.domain import EventTypeChoices
from src._shared.events.models import EventModel


class EventsRepository:

    def __init__(
        self,
        session: Union[Session, ScopedSession],
        type_: EventTypeChoices,
    ) -> None:
        self._session = session
        self.type = type_

    def send_message(
        self,
        event: EventModel,
    ) -> None:
        self._session.add(event)
        self._session.flush()
        return event

    def poll_messages(self, max_amout: int = 5) -> Iterator[EventModel]:
        query = (
            self._session.query(EventModel)
            .filter_by(
                type=self.type,
                read=False,
            )
            .limit(max_amout)
        )

        for event in query.all():
            yield event
            event.read = True
            self._session.add(event)
            self._session.flush()
            self._session.commit()
