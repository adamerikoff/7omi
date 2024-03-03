from ..database import user_service


from ..schemas.schemas import UserCreateSchema, UserUpdateSchema


from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

router = APIRouter(
  prefix="/users",
  tags=["users"],
  dependencies=[],
  responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_users():
  users = await user_service.retrieve_users()
  return users

@router.post("/")
async def create_user(user: UserCreateSchema):
  user = jsonable_encoder(user)
  new_user = await user_service.add_user(user)
  return new_user

@router.get("/{user_id}")
async def get_user(user_id):
  user = await user_service.retrieve_user(user_id)
  if user:
      return user
  return "NONE"

@router.put("/{id}")
async def update_user(id: str, user: UserUpdateSchema):
  req = user.model_dump(exclude_unset=True)
  try:
    updated_user = await user_service.update_user(id, req)
    if updated_user:
      return f"User with ID: {id} updated successfully"
    else:
      return "An error occurred"
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{user_id}")
async def delete_user(user_id: str):
  deleted_student = await user_service.delete_user(user_id)
  if deleted_student:
    return f"Student with ID: {user_id} removed"
  else:
    return "ERROR"

