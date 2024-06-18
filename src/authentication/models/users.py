from sqlalchemy import Boolean, Column, String

from src._shared.database.models import BaseModel
from src._shared.database.orm import ORM
from src.authentication.settings import DOMAIN_NAME


class UserModel(BaseModel, ORM.BASE):
    __tablename__ = "users"
    __table_args__ = {
        "schema": DOMAIN_NAME,
    }

    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)


ORM.register_model(UserModel)
