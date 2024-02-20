from fastapi import APIRouter

router = APIRouter()

@router.post("/ping")
async def ping():
    return {"ping": "pong"}

@router.post("/submit")
async def submit():
    ...