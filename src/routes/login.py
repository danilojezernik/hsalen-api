import os

from typing import Annotated
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from flask import request

router = APIRouter()

db_username = os.getenv('UPORABNIK')
db_geslo = os.getenv('GESLO')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Setting up FastAPI security
@router.get("/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


# LOGIN
@router.post("/")
async def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return {"msg": "Missing username or password"}, 400

    if username != db_username or password != db_geslo:
        return {"msg": "Bad username or password"}, 401

    return {'access_token': 'access_token'}
