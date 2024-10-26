from pydantic import BaseModel, ConfigDict,EmailStr


class CreateProduct(BaseModel):
    name: str
    description: str
    price : str
    stock : str
    
    model_config = ConfigDict(
        from_attributes=True,
    )


class UpdateProduct(BaseModel):
    name: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class ProductResponse(BaseModel):
    id: int
    name: str

    class config:
        orm_mode = True


    
