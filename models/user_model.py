from datetime import datetime
from typing import List

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base
# from .post_model import PostModel
# from .subscription_model import SubscriptionModel


# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     full_name VARCHAR(150) NOT NULL,
#     email VARCHAR(150) NOT NULL UNIQUE,
#     password VARCHAR(255) NOT NULL, -- Store hashed passwords
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );


class UserModel(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    post_models: Mapped[List["PostModel"]] = relationship("PostModel", back_populates="user_models")
    subscription_models: Mapped[List["SubscriptionModel"]] = relationship("SubscriptionModel", back_populates="user_models")

    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password