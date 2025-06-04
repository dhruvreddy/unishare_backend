from abc import ABC, abstractmethod
from typing import Any
from sqlalchemy.orm import Session

from utils.password_hash import PasswordHash
from schemas.user_schema import UserSchema
from models.user_model import UserModel

class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user: UserSchema, session: Session) -> Any:
        pass

    @abstractmethod
    def get_user(self, user_id: int, session: Session) -> Any:
        pass

    @abstractmethod
    def update_user(self, user_id: int, session: Session) -> Any:
        pass

    @abstractmethod
    def delete_user(self, user_id: int, session: Session) -> Any:
        pass


class UserRepositoryImpl(UserRepository):
    def add_user(self, user: UserSchema, session: Session) -> Any:
        new_user = UserModel(
            full_name=user.full_name,
            email=user.email,
            password=PasswordHash.get_hash(user.password)
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    def get_user(self, user_id: int, session: Session) -> Any:
        return session.query(UserModel).filter(UserModel.id == user_id).first()

    def update_user(self, user_id: int, session: Session) -> Any:
        pass

    def delete_user(self, user_id: int, session: Session) -> Any:
        pass
