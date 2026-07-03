from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from secrets import token_urlsafe

from hashlib import sha256


_password_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return _password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return _password_hasher.verify(password_hash, password)
    except VerifyMismatchError:
        return False


def generate_secret(length: int = 64) -> str:
    return token_urlsafe(length)


def sha256_hash(value: str) -> str:
    return sha256(value.encode()).hexdigest()
