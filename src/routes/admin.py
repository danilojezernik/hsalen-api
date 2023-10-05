from fastapi import APIRouter,Depends
from src.services.security import get_current_user

router = APIRouter()


# ADMIN
@router.post("/")
async def post(current_user: str = Depends(get_current_user)):
    return {'msg': 'Ste vpisani!'}
