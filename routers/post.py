from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from repositories.post_repository import PostRepositoryImpl
from schemas import PostSchema
from utils.database import get_db
from repositories import get_all_user_post_di

router = APIRouter(
    prefix="/posts",
    tags=["Post"]
)


@router.post("/add_post")
def add_post_api(post: PostSchema, session: Session = Depends(get_db)):
    return PostRepositoryImpl.add_post(post=post, session=session)

@router.get("/all_posts")
def get_all_post_api(session: Session = Depends(get_db)):
    return PostRepositoryImpl.get_all_post(session)

@router.get("/get_all_user_post")
def get_all_user_post_api(user_post = Depends(get_all_user_post_di)):
    return user_post