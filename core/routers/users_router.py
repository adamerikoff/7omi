from fastapi import APIRouter, status, HTTPException, Response, Depends

from core.schemas.user import UserBase, UserCreate, UserDB, UserUpdate
from core.documents.user import UserDocument 
from core.documents.user import check_uniqueness, hash_password, verify_password, get_user_by_username, get_users
from core.oauth2 import oauth2

router = APIRouter(
    prefix="/users",
    tags=["users"],
    #dependencies=[Depends(get_token_header)],
    #responses={404: {"description": "Not found"}},
    
)

@router.get("/")
async def retrieve_users(current_user: UserDB = Depends(oauth2.get_current_user)):
    users = await get_users()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found.")
    return [UserBase(**u.model_dump()) for u in users]

@router.get("/me")
async def retrieve_user(current_user: UserDB = Depends(oauth2.get_current_user)):
    user = await current_user
    return UserBase(**user.model_dump())
    

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
    return UserBase(**user_document_representation.model_dump())

@router.put("/me")
async def update_user(user_data: UserUpdate, current_user: UserDB = Depends(oauth2.get_current_user)):
    if user_data.password:
        user_data.hashed_password = hash_password(user_data.password)
    user_representation = UserDB(**user_data.model_dump())
    # Retrieve the user to update
    user_to_update = await current_user
    if user_to_update is None:
        raise HTTPException(status_code=404, detail="User not found.")
    user_to_update.__dict__.update(**user_representation.model_dump(exclude_unset=True))
    await user_to_update.save()
    return UserBase(**user_to_update.model_dump())

@router.delete("/me")
async def delete_user(current_user: UserDB = Depends(oauth2.get_current_user)):
    #check rights
    user = await current_user
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    await user.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)