from fastapi import APIRouter

router = APIRouter(
  prefix="/users",
  tags=["users"],
  #dependencies=[Depends(get_token_header)],
  #responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_users():
  return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me")
async def read_user_me():
  return {"username": "fakecurrentuser"}


@router.get("/{user_id}")
async def read_user(user_id: str):
  return {"username": user_id}

@router.put("/{user_id}")
async def update_chat(user_id: int):
  return f"updated user{user_id}"

@router.delete("/{user_id}")
async def delete_chat(user_id: int):
  return f"deleted user {user_id}"