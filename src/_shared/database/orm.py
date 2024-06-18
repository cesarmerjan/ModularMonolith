from typing import Set

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeMeta, clear_mappers, declarative_base


class ORM:

    METADATA: MetaData = MetaData()
    BASE: DeclarativeMeta = declarative_base(metadata=METADATA)
    MODELS: Set[DeclarativeMeta] = set()

    @classmethod
    def register_model(cls, model: DeclarativeMeta) -> None:
        cls.MODELS.add(model)

    @classmethod
    def unregister_all_models(cls) -> None:
        cls.MODELS = set()
        clear_mappers()

    @classmethod
    def create_all_tables(cls, engine) -> None:
        cls.METADATA.create_all(engine)

    @classmethod
    def drop_all_tables(cls, engine) -> None:
        cls.METADATA.drop_all(engine)
