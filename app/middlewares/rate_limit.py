import time
from fastapi import Request
from fastapi.responses import JSONResponse

requests = {}
RATE_LIMIT = 5   # Maximum number of requests allowed
RATE_TIME = 10   # Time window in seconds


async def rate_limit_middleware(request: Request, call_next):
    """
    Middleware that enforces a simple IP-based rate limit.

    - Tracks requests per client IP in memory.
    - Limits each client to `RATE_LIMIT` requests within `RATE_TIME` seconds.
    - Returns HTTP 429 (Too Many Requests) if the limit is exceeded.
    - Otherwise, forwards the request to the next middleware or endpoint.

    Args:
        request (Request): The incoming HTTP request.
        call_next (Callable): The function that forwards the request to the next middleware or endpoint.

    Returns:
        Response: 
            - 429 JSONResponse if the rate limit is exceeded.
            - Normal response from the next middleware/endpoint otherwise.
    """
    client_ip = request.client.host
    
    if client_ip in requests:
        # Remove old requests outside the RATE_TIME window
        current_time = time.time()
        requests[client_ip] = [
            req_time for req_time in requests[client_ip]
            if current_time - req_time < RATE_TIME
        ]

        if len(requests[client_ip]) >= RATE_LIMIT:
            return JSONResponse(
                status_code=429,
                content={"message": "Too many requests"}
            )
    else:
        requests[client_ip] = []

    requests[client_ip].append(time.time())
    return await call_next(request)
