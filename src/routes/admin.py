from fastapi import APIRouter

router = APIRouter()


# ADMIN
@router.post("/")
async def post():
    return {'msg': 'Ste vpisani!'}
