from fastapi import APIRouter, HTTPException, status, Response, Depends

from sqlalchemy.orm import Session

from models import models

from pydantic_schemas import user_schemas

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
async def create_new_user(user_data: user_schemas.CreateUser, db: Session = Depends(get_db)):
  existing_user = db.query(models.User).filter(models.User.username == user_data.username).first()
  if existing_user:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username is already taken")
  hashed_password = models.User.hash_password(user_data.password)
  new_user = models.User(username=user_data.username, password=hashed_password)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@router.get("/{user_id}")
async def read_user(user_id: str, db: Session = Depends(get_db)):
  user = db.query(models.User).filter_by(user_id=user_id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  return user

@router.put("/{user_id}")
async def update_chat(user_id: int, db: Session = Depends(get_db)):
  return f"updated user{user_id}"

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_chat(user_id: int, db: Session = Depends(get_db)):
  user_query = db.query(models.User).filter_by(user_id=user_id)
  if user_query.first() == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  user_query.delete(synchronize_session=False)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)