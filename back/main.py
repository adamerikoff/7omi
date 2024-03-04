from contextlib import asynccontextmanager

from fastapi import FastAPI

from back.database import init

from back.routers.v1 import users_router, auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    await init()
    print("Startup complete")
    yield
    print("Shutdown complete")

app = FastAPI(lifespan=lifespan)

app.include_router(users_router.router)
app.include_router(auth_router.router)

@app.get("/", tags=["Root"])
async def index() -> dict:
    return {"message": "Welcome to your books app!"}