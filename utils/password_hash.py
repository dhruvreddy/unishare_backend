from passlib.context import CryptContext
from passlib.hash import bcrypt

class PasswordHash():
    _context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def get_hash(password: str) -> str:
        return PasswordHash._context.hash(password)

    @staticmethod
    def verify_hash(password: str, password_hash: str) -> bool:
        return PasswordHash._context.verify(password, password_hash)
