from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str
    price: float


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
