# Pydantic schemas for request/response validation
from pydantic import BaseModel

# Define a Pydantic model for the item
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# This defines the public API of the module; only 'Item' will be imported with 'from app.schemas import *'
__all__ = ["Item"]
