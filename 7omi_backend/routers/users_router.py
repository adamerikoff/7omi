from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.orm import Session

from models import models

from db import get_db


router = APIRouter(
  prefix="/users",
  tags=["users"],
  # dependencies=[Depends(get_db)],
  #responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_users(db: Session = Depends(get_db)):
  users = db.query(models.User).all()
  return users

@router.get("/me")
async def read_user_me(db: Session = Depends(get_db)):
  return {"username": "fakecurrentuser"}

@router.post("/")
async def create_new_user(db: Session = Depends(get_db)):
  return f"created user"

@router.get("/{user_id}")
async def read_user(user_id: str, db: Session = Depends(get_db)):
  user = db.query(models.User).filter_by(user_id=user_id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  return user

@router.put("/{user_id}")
async def update_chat(user_id: int, db: Session = Depends(get_db)):
  return f"updated user{user_id}"

@router.delete("/{user_id}")
async def delete_chat(user_id: int, db: Session = Depends(get_db)):
  return f"deleted user {user_id}"