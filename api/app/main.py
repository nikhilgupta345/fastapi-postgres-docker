from typing import Optional

from fastapi import FastAPI

from .routes import items

app = FastAPI()
app.include_router(items.router)
