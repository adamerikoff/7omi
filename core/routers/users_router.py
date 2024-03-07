from fastapi import APIRouter, status, HTTPException

from core.schemas.user import UserBase, UserCreate, UserDB
from core.documents.user import UserDocument, check_uniqueness, hash_password, verify_password

router = APIRouter(
    prefix="/users",
    tags=["users"],
    #dependencies=[Depends(get_token_header)],
    #responses={404: {"description": "Not found"}},
    
)

@router.get("/")
async def retrieve_users():
    users = []
    return users

@router.get("/{user_id}")
async def retrieve_user(user_id: str):
    user: UserBase = None
    return f"{user_id}"

@router.post("/")
async def create_user(new_user: UserCreate):
    if not await check_uniqueness(new_user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exist.")
    hashed_password = hash_password(new_user.password)
    user_document_representation = UserDocument(
        username=new_user.username,
        hashed_password=hashed_password
        )
    await UserDocument.insert(user_document_representation)
    return user_document_representation

@router.put("/")
async def update_user():
    update_user = None
    return update_user

@router.delete("/{user_id}")
async def delete_user(user_id: str):

    return f"deleted {user_id}"