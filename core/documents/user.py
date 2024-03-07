from typing import Optional

from beanie import Document, Indexed

from core.config import pwd_context

class UserDocument(Document):
    username: str
    hashed_password: str
    class Settings:
        name = "users"
        

async def check_uniqueness(username: str):
    result = await UserDocument.find(UserDocument.username == username).to_list()
    if not result:
        return True
    return False

def hash_password(plain_text: str):
    return pwd_context.hash(plain_text)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)