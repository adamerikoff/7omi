from datetime import datetime

from beanie import Document, Indexed

class MessageDocument(Document):
    content: str
    author: str
    time: datetime

    class Settings:
        name = "messages"

class ChatDocument(Document):
    name: str
    users: list[str] = []
    messages: list[MessageDocument] = []

    class Settings:
        name = "chats"