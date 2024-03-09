from fastapi import APIRouter, status, HTTPException, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm

from core.oauth2 import oauth2
from core.schemas.user import UserDB
from core.documents.user import UserDocument 
from core.documents.user import check_uniqueness, hash_password, verify_password, get_user_by_username, get_users


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    #dependencies=[Depends(get_token_header)],
    #responses={404: {"description": "Not found"}},
    
)

@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_by_username(request.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials")
    user = UserDB(**user.model_dump())
    if not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials")
    access_token = oauth2.create_acess_token(data={"username": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }