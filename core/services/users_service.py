from fastapi import HTTPException, status

from core.documents.user import UserDocument

async def get_users():
    result = await UserDocument.find().to_list()
    return result

async def get_user_by_username(username: str):
    result = await UserDocument.find_one(UserDocument.username == username)
    return result

async def user_exists(username: str):
    result = await UserDocument.find_one(UserDocument.username == username)
    if result:
        return True
    return False
