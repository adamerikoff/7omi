from fastapi import APIRouter

from pydantic_schemas import chat_schemas

router = APIRouter(
  prefix="/chats",
  tags=["chats"],
  #dependencies=[Depends(get_token_header)],
  #responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_chats():
  # Replace with logic to fetch chats based on user
  return "all chats"

@router.post("/")
async def create_chat():
  # Replace with logic to create a new chat and associate with user
  return "Post chats"

@router.get("/{chat_id}")
async def get_chat(chat_id: int):
  return f"{chat_id}"

@router.put("/{chat_id}")
async def update_chat(chat_id: int):
  return f"updated chat{chat_id}"

@router.delete("/chats/{chat_id}")
async def delete_chat():
  return "deleted chat"