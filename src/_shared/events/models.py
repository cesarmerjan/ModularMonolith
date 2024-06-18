import base64
import json

from sqlalchemy import Boolean, Column, Enum, Integer, String

from src._shared.database.orm import ORM
from src._shared.events.domain import EventTypeChoices
from src._shared.settings import DOMAIN_NAME


class EventModel(ORM.BASE):
    __tablename__ = "events"
    __table_args__ = {
        "schema": DOMAIN_NAME,
    }

    def __init__(self, payload: dict, type_: EventTypeChoices) -> "EventModel":
        encoded_payload = json.dumps(payload).encode()
        self._payload = base64.b64encode(encoded_payload).decode()
        self.type = type_
        self.read = False

    id = Column(Integer, primary_key=True, autoincrement=True)
    _payload = Column(String, nullable=False)
    type = Column(Enum(EventTypeChoices), nullable=False)
    read = Column(Boolean, default=False)

    @property
    def payload(self) -> dict:
        decoded_payload = base64.b64decode(self._payload).decode()
        return json.loads(decoded_payload)


ORM.register_model(EventModel)
