from pydantic import BaseModel


class Chat(BaseModel):
  conversation_id: int
  name: str