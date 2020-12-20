from typing import List

from fastapi import APIRouter, HTTPException

from ..lib import db
from ..models.item import ItemCreate, Item

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.get("/", response_model=List[Item])
async def get_all_items() -> List[Item]:
    return db.get_all_items()


@router.get("/{item_id}")
async def get_item_by_id(item_id: int) -> Item:
    item = db.get_item_by_id(item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@router.post("/", response_model=Item)
async def create_item(item: ItemCreate) -> Item:
    item = db.create_item(item)
    return item
