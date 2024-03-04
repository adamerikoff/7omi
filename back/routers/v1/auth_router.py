from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from beanie import PydanticObjectId

import jwt

import time

from back.schemas.user import UserSchema, UserInDBSchema, UserRetrieveSchema
from back.schemas.token import Token, TokenData

from back.models.user import UserDocument

from back.config import pwd_context, ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

def signJWT(username: str, id: PydanticObjectId) -> Token:
  payload = {
    "username": username,
    "username": str(id),
    "expires": time.time() + ACCESS_TOKEN_EXPIRE_MINUTES*60
  }
  token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
  return Token(access_token=token, token_type="Bearer")


def decodeJWT(token: str) -> dict:
  try:
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_token if decoded_token["expires"] >= time.time() else None
  except:
    return {}
    
router = APIRouter(
  prefix="/auth",
  tags=["auth"],
  # dependencies=[],
  # responses={404: {"description": "Not found"}},
)

@router.post('/login', response_model=Token)
async def auth_issue_token(user: OAuth2PasswordRequestForm = Depends()):
  user_doc = await UserDocument.find_one(UserDocument.username == user.username)
  # Check if the user exists and if the password is correct
  if not user_doc or not pwd_context.verify(user.password, user_doc.hashed_password):
    raise HTTPException(status_code=401, detail="Incorrect username or password")
  token = signJWT(user_doc.username, user_doc.id)
  # Generate and return the authentication token
  return token
