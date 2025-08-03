from passlib.context import CryptContext


def get_context() -> CryptContext:
    """
    Constructs a passlib.CryptContext object needed for most
    password operations, such as hashing, verifying etc.

    Returns:
        New passlib.CryptContext object
    """
    return CryptContext(schemes=["bcrypt"], deprecated="auto")
