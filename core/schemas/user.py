from pydantic import BaseModel

class UserUpdate(BaseModel):
    username: str = None
    password: str = None
    hashed_password: str = None

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserDB(UserBase):
    hashed_password: str