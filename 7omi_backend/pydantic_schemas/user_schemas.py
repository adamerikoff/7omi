from pydantic import BaseModel

class BaseUser(BaseModel):
  username: str
  password: str

class CreateUser(BaseUser):
  pass

