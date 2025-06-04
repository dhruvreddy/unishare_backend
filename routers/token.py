from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from repositories import get_token_di
from utils import get_db

router = APIRouter(
    tags=["Token"]
)

@router.post("/token")
def get_token_api(token = Depends(get_token_di)):
    return token