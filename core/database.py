from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import MONGO_URI, MONGO_DB_NAME

from core.documents.user import UserDocument

document_model = [UserDocument]

async def init_database():
    # Create Motor client
    client = AsyncIOMotorClient(MONGO_URI)

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client[MONGO_DB_NAME], document_models=document_model)


