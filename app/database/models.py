# Database models (if using SQLAlchemy, etc.)
from typing import List
from app.schemas import Item
from app.database.database import Base
from sqlalchemy import Column, Integer, String, Boolean

# In-memory storage for items
__all__ = ["items_db"]

items_db: List[Item] = [
    Item(id=1, name="Item One", description="This is the first item."),
    Item(id=2, name="Item Two", description="This is the second item."),
    Item(id=3, name="Item Three", description="This is the third item."),
]

# SQLAlchemy Models
class Todo(Base):
    '''
    This code defines a Todo model for a SQLAlchemy ORM, representing a table in the database:

    Table Name: __tablename__ = "todos" specifies the table name as todos.
    Columns:
        id: An integer primary key, with index=True for faster queries.
        title: A string for the task title, indexed for quick searches.
        description: A string to describe the task, also indexed.
        completed: A Boolean indicating if the task is complete, defaulting to False.
    '''
    
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)