# Main entry point of the FastAPI app
from fastapi import FastAPI
from app.routes import router
from app.middlewares import MIDDLEWARES

app = FastAPI()

for middleware in MIDDLEWARES:
    app.middleware("http")(middleware)

app.include_router(router)

