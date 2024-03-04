from beanie import Document, Indexed

class UserDocument(Document):
  username: Indexed(str, unique=True)
  hashed_password: str
  
  class Settings:
    name = "users_collection"