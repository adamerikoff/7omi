from motor.motor_asyncio import AsyncIOMotorClient

from beanie import init_beanie

from back.config import MONGO_URI, DB_NAME

from back.models.user import UserDocument
document_models = [
  UserDocument
]
async def init():
  try:
    # Create Motor client
    client = AsyncIOMotorClient(MONGO_URI)
    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client[DB_NAME], document_models=document_models)
  except Exception as e:
    print(f"Error initializing database: {e}")