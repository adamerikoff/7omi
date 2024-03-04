from pydantic import BaseModel

class ResponseSchema(BaseModel):
  status: int
  detail: str




