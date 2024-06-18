from typing import Iterator

from src._shared.database.unit_of_work import DatabaseUnitOfWork
from src._shared.events.domain import EventTypeChoices
from src._shared.events.models import EventModel
from src._shared.events.repository import EventsRepository


def send_message(
    unit_of_work: DatabaseUnitOfWork,
    message: dict,
    event_type: EventTypeChoices,
) -> None:
    with unit_of_work:
        repository = EventsRepository(unit_of_work.session, event_type)
        event = EventModel(message, event_type)
        repository.send_message(event)
        unit_of_work.commit()


def poll_messages(
    unit_of_work: DatabaseUnitOfWork,
    event_type: EventTypeChoices,
    max_amount: int = 5,
) -> Iterator[dict]:
    with unit_of_work:
        repository = EventsRepository(unit_of_work.session, event_type)
        for event in repository.poll_messages(max_amount):
            yield event.payload
