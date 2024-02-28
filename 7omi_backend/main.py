
from fastapi import FastAPI

from sqlalchemy.orm import sessionmaker


from routers import users_router, chats_router, messages_router  

from models import user_model
app = FastAPI()


import sqlalchemy as db

db_config = {
  "dialect": "postgresql",
  "engine": "psycopg2",
  "user": "postgres",
  "password": "postgres",
  "host": "localhost",
  "port": "5432",
  "database": "7omi"
}
db_string = f"{db_config['dialect']}+{db_config['engine']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

engine = db.create_engine(db_string, echo=True)

conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


users = session.query(user_model.User).all()
# Print the results
for user in users:
  print(f"ID: {user.user_id}, Name: {user.username}, Email: {user.password}")


app.include_router(users_router.router)
app.include_router(chats_router.router)
app.include_router(messages_router.router)

@app.get("/")
async def root():
  return {"message": "ROOT"}