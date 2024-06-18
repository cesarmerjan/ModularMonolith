import uuid

from sqlalchemy import Column, DateTime, String, func


def generate_uuid():
    return str(uuid.uuid4())


class BaseModel:

    __table_args__ = {
        "extend_existing": True,
    }

    uuid = Column(String(36), primary_key=True, default=generate_uuid)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())

    def __repr__(self) -> str:
        message = f"<{self.__class__.__qualname__} {self.uuid}>"
        return message
