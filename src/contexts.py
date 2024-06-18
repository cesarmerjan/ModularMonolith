from src._shared.database.driver import DatabaseDriver
from src._shared.database.orm import ORM
from src._shared.database.unit_of_work import DatabaseUnitOfWork
from src._shared.settings import DOMAIN_NAME, DatabaseConfig


class DatabaseContext:

    _DRIVER = DatabaseDriver(DatabaseConfig.to_url())

    def __init__(self, domain: str) -> None:
        self._create_schema(DOMAIN_NAME)
        self._create_schema(domain)
        self._create_tables()

    def _create_tables(self) -> None:
        ORM.create_all_tables(self._DRIVER.engine)

    def _create_schema(self, domain: str) -> None:
        self._DRIVER.create_schema(domain)

    @property
    def unit_of_work(self) -> DatabaseUnitOfWork:
        return DatabaseUnitOfWork(self._DRIVER.session_factory)
