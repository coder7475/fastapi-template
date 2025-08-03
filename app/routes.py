from fastapi import APIRouter, HTTPException
from typing import Optional, List

from app.schemas import Item
from app.models import items_db


router = APIRouter()

# API routes
# Root route
@router.get("/")
async def get_route():
    return {"message": "Hello, World!"}

# GET method to retrieve all items
@router.get("/items/", response_model=List[Item])
async def read_items():
    return items_db

# path parameter - get item by id
@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items_db:
         if item.id == item_id:
              return item
         
    raise HTTPException(status_code=400, detail="item not found")

# POST method to create a new item
@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    items_db.append(item)    
    return item

# PUT method to update an existing item by ID
@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
        
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE method to remove an item by ID
@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"detail": "Item deleted"}
        
    raise HTTPException(status_code=404, detail="Item not found")

# query parameter
@router.get("/filter/")
# ?category=...&price_lt=...
async def filter_items(category: str, price_lt: float):
	return {
		"category": category,
		"price_less_than": price_lt
	}

# search params
@router.get("/search/")
async def search_items(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    # Example data
    all_items = [{"item_id": "123"}, {"item_id": "456"}, {"item_id": "789"}, {"item_id": "101"}]
    # Optionally filter by q (mocked)
    filtered_items = [item for item in all_items if not q or q in item["item_id"]]
    # Apply skip and limit
    paginated_items = filtered_items[skip:skip + limit]
    results = {"items": paginated_items}
    if q:
        results.update({"q": q})
    results.update({"skip": skip, "limit": limit})
    return results