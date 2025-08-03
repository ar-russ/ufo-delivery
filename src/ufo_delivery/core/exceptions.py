from fastapi.exceptions import HTTPException


class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            401,
            "Failed to validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )


class UserAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(400, "User already exists")


class InsufficientRightsException(HTTPException):
    def __init__(self):
        super().__init__(403, "Insufficient rights for this action")


class UserNotFound(HTTPException):
    def __init__(self):
        super().__init__(404, "User not found")


class ItemNotFound(HTTPException):
    def __init__(self):
        super().__init__(404, "Item not found")


class OrderNotFound(HTTPException):
    def __init__(self):
        super().__init__(404, "Orden not found")


class ItemNotInOrder(HTTPException):
    def __init__(self):
        super().__init__(404, "Item not in Order")


class OrderIsEmpty(HTTPException):
    def __init__(self):
        super().__init__(400, "Order is empty")
