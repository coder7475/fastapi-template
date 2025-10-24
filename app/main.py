# Main entry point of the FastAPI app
from fastapi import FastAPI
from app.middlewares import MIDDLEWARES
from app.exceptions.custom_exceptions import CustomException
from app.exceptions.custom_handler import custom_exception_handler

from app.routes.v1.routes import router as v1_routes
from app.routes.v2.routes import router as v2_routes


# Initialize App
app = FastAPI()

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


