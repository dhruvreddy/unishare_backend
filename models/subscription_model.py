from datetime import datetime

from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from models.base_model import Base


# from .post_model import PostModel
# from .user_model import UserModel


# CREATE TABLE subscriptions (
#     user_id INT NOT NULL,
#     post_id INT NOT NULL,
#     subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (user_id, post_id),
#     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
#     FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
# );

class SubscriptionModel(Base):
    __tablename__ = "subscriptions"
    __table_args__ = {"extend_existing": True}

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    subscribed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user_models: Mapped["UserModel"] = relationship("UserModel", back_populates="subscription_models")
    post_models: Mapped["PostModel"] = relationship("PostModel", back_populates="subscription_models")

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id