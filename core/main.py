from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.database import init_database

from core.routers import users_router, chats_router, auth_router

origins = [
    "http://localhost:8000",
    "localhost:8000",
    "http://localhost:5173",
    "localhost:5173"
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    await init_database()  
    print("Startup complete")
    yield
    print("Shutdown complete")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users_router.router)
app.include_router(auth_router.router)
app.include_router(chats_router.router)

@app.get("/")
def root():
    return "server root"