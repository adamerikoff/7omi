from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from pydantic import BaseModel

from datetime import timedelta, datetime

from jose import JWTError, jwt

from passlib.context import CryptContext


SECRET_KEY = "1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 30

app = FastAPI()

@app.get("/")
async def test():
  return "hi"