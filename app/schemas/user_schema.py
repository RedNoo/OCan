from pydantic import BaseModel, ConfigDict,EmailStr


class CreateUser(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class UpdateUser(BaseModel):
    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True,
    )


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class config:
        orm_mode = True


