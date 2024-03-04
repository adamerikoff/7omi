from pydantic import BaseModel

from beanie import PydanticObjectId

class UserSchema(BaseModel):
  username: str

class UserInDBSchema(UserSchema):
  hashed_password: str

class UserCreateSchema(UserSchema):
  password: str

class UserRetrieveSchema(UserSchema):
  id: PydanticObjectId






