# Main entry point of the FastAPI app
from fastapi import FastAPI
from app.routes import router

app = FastAPI()
app.include_router(router)
