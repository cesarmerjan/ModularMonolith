from typing import Type

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


class DatabaseDriver:

    __slots__ = (
        "engine",
        "session_factory",
    )

    def __init__(self, database_url: URL) -> "DatabaseDriver":
        self.engine = self._create_engine(database_url)
        self.session_factory = self._create_session_factory(self.engine)

    def _create_engine(self, database_url: URL) -> Engine:
        engine = create_engine(database_url)
        return engine

    def _create_session_factory(self, engine: Engine) -> sessionmaker:
        session_factory = sessionmaker(
            bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
        )
        return session_factory

    def get_session(self) -> Session:
        return self.session_factory()

    def create_schema(self, name: str) -> None:
        with self.engine.begin() as connection:
            connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {name};"))

    def drop_schema(self, name: str) -> None:
        with self.engine.begin() as connection:
            connection.execute(text(f"DROP SCHEMA IF EXISTS {name};"))
