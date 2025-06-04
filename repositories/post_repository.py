from abc import ABC, abstractmethod

from fastapi import status, Depends
from sqlalchemy.orm import Session

from models import PostModel, SubscriptionModel, UserModel
from schemas import PostSchema, PostReturnFullWithUser
from repositories import get_current_user_di
from utils import get_db


class PostRepository(ABC):
    @staticmethod
    @abstractmethod
    def add_post(post: PostSchema, session: Session):
        pass

    @staticmethod
    @abstractmethod
    def get_all_post(session: Session):
        pass

    @staticmethod
    @abstractmethod
    def get_all_user_post(session: Session, user: UserModel):
        pass

    @abstractmethod
    def get_user_post(self, session: Session):
        pass


class PostRepositoryImpl(PostRepository):
    @staticmethod
    def add_post(post: PostSchema, session: Session):
        try:
            new_post = PostModel(
                user_id=post.user_id,
                title=post.title,
                description=post.description
            )
            session.add(new_post)
            session.flush()
            new_subscription = SubscriptionModel(
                user_id=post.user_id,
                post_id=new_post.id
            )
            session.add(new_subscription)
            session.commit()
            session.refresh(new_post)
            return status.HTTP_201_CREATED
        except Exception as e:
            session.rollback()
            raise e

    @staticmethod
    def get_all_post(session: Session):
        posts = session.query(PostModel, UserModel).join(SubscriptionModel,PostModel.id == SubscriptionModel.post_id).join(UserModel,UserModel.id == SubscriptionModel.user_id).all()
        all_post = [
            PostReturnFullWithUser(
                id=post.id,
                user_id=post.user_id,
                title=post.title,
                description=post.description,
                created_at=post.created_at,
                full_name=user.full_name,
                email=user.email
            ).model_dump(mode="json")
            for post, user in posts
        ]
        return all_post

    @staticmethod
    def get_all_user_post(session: Session, user: UserModel):
        posts = (
            session.query(PostModel, UserModel)
            .join(SubscriptionModel, PostModel.id == SubscriptionModel.post_id)
            .join(UserModel, UserModel.id == SubscriptionModel.user_id)
            .filter(UserModel.id == user.id)
            .all()
        )
        all_post = [
            PostReturnFullWithUser(
                id=post.id,
                user_id=post.user_id,
                title=post.title,
                description=post.description,
                created_at=post.created_at,
                full_name=user.full_name,
                email=user.email
            ).model_dump(mode="json")
            for post, user in posts
        ]
        return all_post

    def get_user_post(self, session: Session):
        pass


def get_all_user_post_di(session: Session = Depends(get_db), user: UserModel = Depends(get_current_user_di)):
    return PostRepositoryImpl.get_all_user_post(session, user)