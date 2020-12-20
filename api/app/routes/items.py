from typing import List

from fastapi import APIRouter

from ..lib import db
from ..models.item import ItemCreate, Item

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.get("/", response_model=List[Item])
async def get_all_items() -> List[Item]:
    return db.get_all_items()


@router.post("/", response_model=Item)
async def create_item(item: ItemCreate) -> Item:
    item = db.create_item(item)
    return item
