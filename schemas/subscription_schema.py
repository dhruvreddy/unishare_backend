from pydantic import BaseModel, Field

class SubscriptionSchema():
    user_id: int = Field(default=..., description="ID of the User")
    post_id: int = Field(default=..., description="ID of the Post")

    class Config():
        from_attributes = True