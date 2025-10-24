# Main entry point of the FastAPI app
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from app import schemas
from app.database import models
from app.middlewares import MIDDLEWARES
from app.exceptions.custom_exceptions import CustomException
from app.exceptions.custom_handler import custom_exception_handler

from app.routes.v1.routes import router as v1_routes
from app.routes.v2.routes import router as v2_routes
from app.database.database import Base, SessionLocal, engine
from sqlalchemy.orm import Session

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI App
app = FastAPI()

# Get database session
def get_db():
    """
    The `get_db` function returns a database session that is closed after its use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Exception handling
app.add_exception_handler(CustomException, custom_exception_handler)

# Middlewares
for middleware in MIDDLEWARES:
    app.middleware("http")(middleware)

# Routes
# Root route
@app.get("/")
async def get_route():
    return {
        "message": "FastAPI Template",
        "available_versions": ["v1", "v2"],
        "current_version": "v2",
        "deprecated_versions": ["v1"]
    }

# Versioned Router
app.include_router(v1_routes, prefix="/v1")
app.include_router(v2_routes, prefix="/v2")

# Routes that interact with sqlite through sqlalchemy
@app.post("/todos", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=schemas.Todo)
def update_todo(todo_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"detail": "Todo deleted"}

@app.get("/todos/", response_model=List[schemas.Todo])
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return todos