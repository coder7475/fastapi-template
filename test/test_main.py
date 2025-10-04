import pytest
from httpx import AsyncClient, ASGITransport
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

# Use pytest-asyncio for async test functions
@pytest.mark.asyncio
async def test__get_root():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


# @pytest.mark.asyncio
# async def test_read_item():
#     async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
#         response = await ac.get("/items/123?q=testing")
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 123, "q": "testing"}
