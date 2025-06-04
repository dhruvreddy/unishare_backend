from pydantic import BaseModel, Field

class PostSchema(BaseModel):
    user_id: int = Field(default=..., description="ID of the User")
    title: str = Field(default=..., description="Title of the post")
    description: str = Field(default=..., description="Description of the post")

    class Config():
        from_attributes = True