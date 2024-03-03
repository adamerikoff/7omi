from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/token")
async def login():
    
    return "access token"

@router.post("/refresh_token")
async def read_items():
    return "refreshed"


