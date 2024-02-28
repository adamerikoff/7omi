
from fastapi import FastAPI, Depends

from routers import users_router, chats_router, messages_router  


app = FastAPI()


app.include_router(users_router.router)
app.include_router(chats_router.router)
app.include_router(messages_router.router)

@app.get("/")
async def root():
  return {"message": "ROOT"}