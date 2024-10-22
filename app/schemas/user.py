from pydantic import BaseModel, ConfigDict


class CreateUser(BaseModel):
    email: str
    password: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class User(BaseModel):
    id: int
    email: str

    class config:
        orm_mode = True
