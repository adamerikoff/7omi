from fastapi import FastAPI

from routers import users_router, chats_router, messages_router  

app = FastAPI()


from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

db_config = {
  "user": "postgres",
  "password": "postgres",
  "host": "localhost",
  "port": "5432",
  "database": "7om"
}







app.include_router(users_router.router)
app.include_router(chats_router.router)
app.include_router(messages_router.router)

@app.get("/")
async def root():
  return {"message": "ROOT"}