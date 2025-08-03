from uuid import uuid4
from datetime import datetime, timedelta, timezone

from passlib.context import CryptContext
from jwt import encode

from config.config import settings


class AuthenticationManager:
    def __init__(self, context: CryptContext):
        self._context = context

    @staticmethod
    def create_access_token(data: dict, expires_in: int = settings.auth.access_token_ttl) -> str:
        """
        Creates JWT Access Token.

        Args:
            data: Data to encode in token.
            expires_in: Amount of minutes until fresh token will expire.

        Returns:
            JWT Access token.
        """
        data_to_encode = data.copy()
        data_to_encode.update(
            {
                "jti": str(uuid4()),
                "iat": datetime.now(timezone.utc),
                "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_in),
            }
        )

        return encode(
            data_to_encode,
            key=settings.auth.secret_key,
            algorithm=settings.auth.algorithm
        )

    def hash_password(self, password: str) -> str:
        """
        Hashes given plain password.
        """
        return self._context.hash(password)

    def is_password_valid(self, plain_password: str, hashed_password: str) -> bool:
        """
        Validates given plain password against hashed one.
        """
        return self._context.verify(plain_password, hashed_password)
