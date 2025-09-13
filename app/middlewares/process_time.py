import time
from fastapi import Request

async def process_time_middleware(request: Request, call_next):
    """
    Middleware that measures and logs the processing time for each HTTP request.

    - Adds an `X-Process-Time` header to the response with the elapsed time (in seconds).
    - Logs the request path and processing time to the console.

    Args:
        request (Request): The incoming HTTP request.
        call_next (Callable): The function that forwards the request to the next middleware or endpoint.

    Returns:
        Response: The HTTP response with the added `X-Process-Time` header.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    response.headers["X-Process-Time"] = str(process_time)
    print(f"Request to {request.url.path} took {process_time:.4f} seconds")

    return response
