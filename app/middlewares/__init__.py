from .process_time import process_time_middleware
from .rate_limit import rate_limit_middleware

# List of all middlewares to register
MIDDLEWARES = [
    process_time_middleware,
    rate_limit_middleware,
]
