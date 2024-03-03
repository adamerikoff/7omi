from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
  prefix="/users",
  tags=["users"],
  dependencies=[],
  responses={404: {"description": "Not found"}},
)



@router.get("/")
async def get_user():
    ## Authentication
    ## Authorization
    ## if true 
    ## else 
    return "Main Page Users"

@router.post("/")
async def create_user():
    return "fake_items_db"

@router.delete("/{user_id}")
async def delete_user(user_id: str):
  return f"{user_id}"

