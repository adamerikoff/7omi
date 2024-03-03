from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreateSchema(BaseModel):
  fullname: str = Field(...)
  email: EmailStr = Field(...)
  password: str = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "fullname": "John Doe",
        "email": "jdoe@x.edu.ng",
        "password": "password9714912",
      }
    }

class UserUpdateSchema(BaseModel):
  fullname: Optional[str] = None  # Make fullname optional
  email: Optional[str] = None  # Make email optional
  password: Optional[str] = None  # Make password optional

