# Main entry point of the FastAPI app
from fastapi import FastAPI
from app.routes import router
from app.middlewares import MIDDLEWARES
from app.exceptions.custom_exceptions import CustomException
from app.exceptions.custom_handler import custom_exception_handler

app = FastAPI()

app.add_exception_handler(CustomException, custom_exception_handler)

for middleware in MIDDLEWARES:
    app.middleware("http")(middleware)

app.include_router(router)

