from datetime import datetime

from pydantic import BaseModel, Field

class PostReturnFull(BaseModel):
    id: int = Field(default=...)
    user_id: int = Field(default=...)
    title: str = Field(default=...)
    description: str = Field(...)
    created_at: datetime

    class Config():
        from_attributes = True

class PostReturnFullWithUser(BaseModel):
    id: int = Field(default=...)
    user_id: int = Field(default=...)
    title: str = Field(default=...)
    description: str = Field(...)
    created_at: datetime

    full_name: str = Field(...)
    email: str = Field(...)

    class Config():
        from_attributes = True
