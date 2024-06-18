from dataclasses import asdict, dataclass


class BaseSchema:

    @property
    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class VerifyUserMessageSchema(BaseSchema):
    uuid: str
    email: str
