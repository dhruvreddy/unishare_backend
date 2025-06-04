from datetime import datetime
from typing import List

from sqlalchemy import Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base
# from .subscription_model import SubscriptionModel
# from .user_model import UserModel


# CREATE TABLE posts (
#     id SERIAL PRIMARY KEY,
#     user_id INT NOT NULL,
#     title VARCHAR(255) NOT NULL,
#     description TEXT NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
# );

class PostModel(Base):
    __tablename__ = "posts"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user_models: Mapped["UserModel"] = relationship("UserModel", back_populates="post_models")
    subscription_models: Mapped[List["SubscriptionModel"]] = relationship("SubscriptionModel", back_populates="post_models")

    def __init__(self, user_id, title, description):
        self.user_id = user_id
        self.title = title
        self.description = description