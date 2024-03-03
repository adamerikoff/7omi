from .routers import users_router

from fastapi import FastAPI 

app = FastAPI()


app.include_router(users_router.router)

@app.get("/")
async def root():
  return "Home"