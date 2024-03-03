from pydantic import BaseModel, EmailStr, Field

class StudentSchema(BaseModel):
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