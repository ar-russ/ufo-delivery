from fastapi import Depends
from passlib.context import CryptContext

from src.core.security import AuthenticationManager
from src.core.dependencies.auth.context import get_context

def get_authentication_manager(
        context: CryptContext = Depends(get_context)
) -> AuthenticationManager:
    """
    Constructs an AuthenticationManager instance with injected
    passlib.CryptContext.
    """
    return AuthenticationManager(context)
