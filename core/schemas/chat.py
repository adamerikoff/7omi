from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    content: str = None
    author: str = None
    time: datetime = None

class Chat(BaseModel):
    name: str = None
    users: list[str] = []
    messages: list[Message] = []

class ChatCreate(BaseModel):
    name: str
