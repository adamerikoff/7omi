from fastapi import APIRouter

router = APIRouter(
  prefix="/chats",
  tags=["messages"],
  #dependencies=[Depends(get_token_header)],
  #responses={404: {"description": "Not found"}},
)

@router.get("/{chat_id}/messages")
async def get_chats(chat_id: int):
  # Replace with logic to fetch chats based on user
  return f"all messages for {chat_id}"

@router.post("/{chat_id}/messages")
async def create_chat():
  # Replace with logic to create a new chat and associate with user
  return "Post message"

@router.get("/{chat_id}/messages/{message_id}")
async def get_chat(message_id: int):
  return f"{message_id}"

@router.put("/{chat_id}/messages/{message_id}")
async def update_chat(message_id: int):
  return f"updated chat{message_id}"

@router.delete("/{chat_id}/messages/{message_id}")
async def delete_chat(message_id: int):
  return f"deleted chat {message_id}"