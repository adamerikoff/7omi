from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from typing import Optional
from datetime import timedelta, datetime

from jose import jwt, JWTError

from core.documents.user import UserDocument
from core.config import pwd_context


SECRET_KEY = "7b1696555cddffdf04b50d17d5b7d81ea5212416a6bae20336869e77106b381d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(plain_text: str):
    return pwd_context.hash(plain_text)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_acess_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + timedelta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserDocument:
    credential_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
                headers={"WWW-Authenticate": "Bearer"}
            )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    user: UserDocument = await UserDocument.find_one(UserDocument.username == username)
    if user is None:
        raise credential_exception
    return user