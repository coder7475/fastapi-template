# API routes
from typing import Optional
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_route():
    return {"message": "Hello, World!"}

# path parameter
@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {
        "item_id": item_id
    }

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