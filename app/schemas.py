# Pydantic schemas for request/response validation
from pydantic import BaseModel
from typing import List

# Define a Pydantic model for the item
class Item(BaseModel):
    id: int
    name: str
    description: str = None

class ItemResponse(BaseModel):
    version: str
    items: List[Item]

# This defines the public API of the module; only 'Item' will be imported with 'from app.schemas import *'
__all__ = ["Item"]

# The class defines a Todo model with title, description, completed status, and an ID for database
# operations.
# Validation for Todo Table
class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True
