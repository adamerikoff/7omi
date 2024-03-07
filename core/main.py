from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.database import init_database
from core.routers import users_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    await init_database()  
    print("Startup complete")
    yield
    print("Shutdown complete")


app = FastAPI(lifespan=lifespan)

app.include_router(users_router.router)

@app.get("/")
def root():
    return "Hello world!"