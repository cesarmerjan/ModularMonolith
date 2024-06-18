import uuid

from sqlalchemy import Column, String

from src._shared.database.models import BaseModel
from src._shared.database.orm import ORM
from src.notification.settings import DOMAIN_NAME


class VerificationLinkModel(BaseModel, ORM.BASE):
    __tablename__ = "verification_links"
    __table_args__ = {
        "schema": DOMAIN_NAME,
    }

    def __init__(self, user_uuid: str) -> None:
        self.user_uuid = user_uuid
        self.hexcode = str(uuid.uuid4().hex)

    user_uuid = Column(String(50), nullable=False)
    hexcode = Column(String(32), nullable=False)


ORM.register_model(VerificationLinkModel)
