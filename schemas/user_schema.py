from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    full_name: str = Field(default=..., description="Name of the user")
    email: str = Field(default=..., description="Email of the user")
    password:str = Field(default=...,)

    class Config:
        from_attributes = True