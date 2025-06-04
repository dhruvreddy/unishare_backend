from abc import ABC, abstractmethod
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from models import UserModel
from utils import PasswordHash, Token, get_db

oauth = OAuth2PasswordBearer(tokenUrl="/token")

class AuthRepository(ABC):
    @staticmethod
    @abstractmethod
    def get_token(user_details: OAuth2PasswordRequestForm, session: Session):
        pass

    @staticmethod
    @abstractmethod
    def get_current_user(session: Session, token: str):
        pass


class AuthRepositoryImpl(AuthRepository):
    @staticmethod
    def get_token(user_details: OAuth2PasswordRequestForm, session: Session):
        user = session.query(UserModel).filter(UserModel.email == user_details.username).first()
        if not user:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        if not PasswordHash.verify_hash(user_details.password, str(user.password)):
            raise HTTPException(
                status.HTTP_401_UNAUTHORIZED,
                detail="Password incorrect"
            )

        user_dict = {
            "sub": user_details.username,
            "name": user.full_name
        }
        token = Token.jwt_encode(user_dict)

        return {
            "access_token": token,
            "token_type": "Bearer"
        }

    @staticmethod
    def get_current_user(session: Session, token: str):
        try:
            payload = Token.jwt_decode(token)
            email = payload.get("sub")
            if email is None:
                raise HTTPException(
                    status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token payload"
                )
            user = session.query(UserModel).filter(UserModel.email == email).first()
            if not user:
                raise HTTPException(
                    status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            return user
        except JWTError:
            raise HTTPException(
                status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )
        except Exception:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )

def get_token_di(
    user_details: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_db)
):
    return AuthRepositoryImpl.get_token(user_details, session)

def get_current_user_di(
    session: Session = Depends(get_db),
    token: str = Depends(oauth)
):
    return AuthRepositoryImpl.get_current_user(session, token)
