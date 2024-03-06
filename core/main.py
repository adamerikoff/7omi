from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.database import init_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    await init_database()  
    print("Startup complete")
    yield
    print("Shutdown complete")


app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return "Hello world!"