from typing import List

from fastapi import APIRouter, status, HTTPException

from beanie import PydanticObjectId

from back.schemas.user import UserCreateSchema, UserSchema, UserInDBSchema, UserRetrieveSchema

from back.models.user import UserDocument

from back.config import pwd_context

router = APIRouter(
  prefix="/users",
  tags=["users"],
  # dependencies=[],
  # responses={404: {"description": "Not found"}},
)

# Create operation
@router.post("/", response_model=UserRetrieveSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreateSchema):
  if await UserDocument.find_one(UserDocument.username == user_data.username):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
  new_user = UserDocument(username=user_data.username, hashed_password=pwd_context.hash(user_data.password))
  await new_user.insert()
  return UserRetrieveSchema(**new_user.model_dump())

# Read operation (Get all items)
@router.get("/", status_code=status.HTTP_200_OK)
async def retrieve_users() -> List[UserRetrieveSchema]:
  users = await UserDocument.find().to_list()
  return [UserRetrieveSchema(**i.model_dump()) for i in users]


# Read operation (Get user by ID)
@router.get("/{user_id}", response_model=UserRetrieveSchema, status_code=status.HTTP_200_OK)
async def retrieve_user(user_id: PydanticObjectId):
  user = await UserDocument.find_one(UserDocument.id == user_id)
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  return UserRetrieveSchema(**user.model_dump())
