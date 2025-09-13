from fastapi import Request
from fastapi.responses import JSONResponse
from .custom_exceptions import CustomException

async def custom_exception_handler(request: Request, exc: CustomException):
    """
    Handles CustomException and returns a JSON response.

    Args:
        request (Request): The incoming HTTP request.
        exc (CustomException): The raised custom exception.

    Returns:
        JSONResponse: Response with status code 418 and a custom message.
    """
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something wrong."},
    )
