class CustomException(Exception):
    """
    Custom exception class for application-specific errors.

    Attributes:
        name (str): A name or identifier for the error.
    """
    def __init__(self, name: str):
        self.name = name
