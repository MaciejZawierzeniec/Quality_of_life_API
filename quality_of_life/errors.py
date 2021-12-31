from typing import Dict


class BadRequestError(Exception):
    """Client side error"""

    def __init__(self, message="Invalid request"):
        super().__init__(message)


class DomainError(BadRequestError):
    def __init__(self, message: str = "", content: Dict = None):
        self.message = message
        self.content = content if content else {}
