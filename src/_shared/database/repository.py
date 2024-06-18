from typing import List, Type, Union

from sqlalchemy.orm.scoping import ScopedSession
from sqlalchemy.orm.session import Session

from src._shared.database.orm import ORM


class DatabaseRepository:

    __slots__ = ("_session",)

    def __init__(self, session: Union[Session, ScopedSession]) -> None:
        self._session = session

    def add(self, model: ORM.BASE) -> ORM.BASE:
        self._session.add(model)
        self._session.flush()
        return model

    def add_all(self, models: List[ORM.BASE]) -> ORM.BASE:
        self._session.add_all(models)
        self._session.flush()
        return models

    def get_where(self, Model: Type[ORM.BASE], **kwargs) -> ORM.BASE:
        return self._session.query(Model).filter_by(**kwargs).one()

    def get_all(self, Model: Type[ORM.BASE]) -> List[ORM.BASE]:
        return self._session.query(Model).all()

    def delete(self, model: ORM.BASE) -> None:
        self._session.delete(model)
        self._session.flush()

    def update(self, model: ORM.BASE, **kwargs) -> ORM.BASE:
        for attr, value in kwargs.items():
            setattr(model, attr, value)
        self._session.add(model)
        self._session.flush()
        return model
