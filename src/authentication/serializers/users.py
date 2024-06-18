from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: str


class UserIn(UserBase):
    password: str = Field(..., min_length=8)


class UserOut(UserBase):
    uuid: str

    class Config:
        orm_mode = True
