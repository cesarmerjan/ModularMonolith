from typing import Union

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.session import Session


class DatabaseUnitOfWork:

    __slots__ = ("_session_factory", "session")

    def __init__(self, session_factory: Union[sessionmaker, scoped_session]) -> None:
        self._session_factory = session_factory
        self.session = None

    def __enter__(self) -> "DatabaseUnitOfWork":
        self.session: Session = self._session_factory()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type:
            self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
