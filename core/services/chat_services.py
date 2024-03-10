from datetime import datetime

from core.documents.chat import ChatDocument, MessageDocument

async def get_chat(chat_name: str) -> ChatDocument:
    result = await ChatDocument.find_one(ChatDocument.name == chat_name)
    return result

async def chat_exists(chat_name: str) -> bool:
    result = await ChatDocument.find_one(ChatDocument.name == chat_name)
    if result:
        return True
    return False

async def get_messages(chat_name: str) -> list[MessageDocument]:
    result = await ChatDocument.find_one(ChatDocument.name == chat_name)
    return result.messages

async def add_message_to_chat(chat_name: str, message: str, author: str) -> list[MessageDocument]:
    chat = await ChatDocument.find_one(ChatDocument.name == chat_name)
    new_message = MessageDocument(author=author, content=message, time=datetime.utcnow())
    chat.messages.append(new_message)
    await chat.save()
    return await get_messages(chat_name)

async def get_chat_users(chat_name: str) -> list:
    chat = await ChatDocument.find_one(ChatDocument.name == chat_name)
    return chat.users
    
async def add_user_to_chat(chat_name: str, user: str):
    chat = await ChatDocument.find_one(ChatDocument.name == chat_name)
    chat.users.append(user)
    await chat.save()
    return await get_chat_users(chat_name)

async def user_in_chat(chat_name: str, username: str) -> bool:
    chat = await ChatDocument.find_one(ChatDocument.name == chat_name)
    if username in chat.users:
        return True
    return False



