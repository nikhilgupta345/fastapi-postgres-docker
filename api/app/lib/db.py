from contextlib import contextmanager
from typing import List

import psycopg2

from ..config import settings
from ..models.item import Item, ItemCreate


@contextmanager
def get_db_conn():
    with psycopg2.connect(settings.postgres_dsn) as conn:
        yield conn


def create_item(item: ItemCreate) -> Item:
    query = 'INSERT INTO Item (Name, Description, Price) VALUES (%s, %s, %s) RETURNING ID;'

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                query,
                (item.name, item.description, item.price)
            )
            conn.commit()

            item_id = cursor.fetchone()[0]

            new_item = Item.construct(**item.dict())
            new_item.id = item_id

            return new_item


def get_all_items() -> List[Item]:
    query = 'SELECT * FROM Item;'

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            print(rows)
            return [Item.parse_obj(dict(zip(columns, row))) for row in rows]
