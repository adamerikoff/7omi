from pydantic import BaseModel


class Token(BaseModel):
  token_data: str
  token_type: str


class TokenData(BaseModel):
  username: str