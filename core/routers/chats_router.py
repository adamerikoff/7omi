from fastapi import APIRouter, status, HTTPException, Response, Depends

from core.oauth2 import oauth2

from core.documents.user import UserDocument
from core.documents.chat import MessageDocument, ChatDocument

from core.schemas.user import UserDB, UserBase
from core.schemas.chat import Message, Chat, ChatCreate

from core.services.users_service import user_exists
from core.services.chat_services import chat_exists, user_in_chat, add_user_to_chat, add_message_to_chat, get_messages

router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    #dependencies=[Depends(get_token_header)],
    #responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_chat(chat_data: ChatCreate, current_user: UserDB = Depends(oauth2.get_current_user)):
    if await chat_exists(chat_name=chat_data.name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Chat already exist.")
    new_chat = ChatDocument(name=chat_data.name, users=[current_user.username], messages=[])
    await ChatDocument.insert_one(new_chat)
    return Chat(**new_chat.model_dump())

@router.post("/{chat_name}/{username}")
async def chat_add_user(chat_name: str, username: str, current_user: UserDB = Depends(oauth2.get_current_user)):
    if not await user_exists(username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User doesn't exist.")
    if not await chat_exists(chat_name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Chat doesn't exist.")
    if await user_in_chat(chat_name, username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already in chat.")
    users = await add_user_to_chat(chat_name, username)
    return users

@router.post("/{chat_name}")
async def chat_add_message(chat_name: str, content: str,  current_user: UserDB = Depends(oauth2.get_current_user)):
    if not await user_exists(current_user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User doesn't exist.")
    if not await chat_exists(chat_name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Chat doesn't exist.")
    if not await user_in_chat(chat_name, current_user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User is not in the chat.")
    messages = await add_message_to_chat(chat_name, content, current_user.username)
    return messages

@router.get("/{chat_name}")
async def chat_add_message(chat_name: str, current_user: UserDB = Depends(oauth2.get_current_user)):
    if not await user_exists(current_user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User doesn't exist.")
    if not await chat_exists(chat_name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Chat doesn't exist.")
    if not await user_in_chat(chat_name, current_user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User is not in the chat.")
    messages = await get_messages(chat_name)
    return messages