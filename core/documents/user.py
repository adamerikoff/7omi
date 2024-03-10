from typing import Optional

from beanie import Document

class UserDocument(Document):
    username: str
    hashed_password: str
    class Settings:
        name = "users"

