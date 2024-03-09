from typing import Optional

from beanie import Document, Indexed

from core.config import pwd_context

class UserDocument(Document):
    username: str
    hashed_password: str
    class Settings:
        name = "users"
        
async def get_users():
    result = await UserDocument.find().to_list()
    return result

async def get_user_by_username(username: str):
    result = await UserDocument.find_one(UserDocument.username == username)
    if not result:
        return None
    return result

async def check_uniqueness(username: str):
    result = await UserDocument.find_one(UserDocument.username == username)
    if not result:
        return True
    return False

def hash_password(plain_text: str):
    return pwd_context.hash(plain_text)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

