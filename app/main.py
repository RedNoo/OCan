from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel, ConfigDict
from random import randrange
import time
from app.crud import UserCrud
from sqlalchemy.ext.asyncio import async_sessionmaker
from .db import engine, Base
from app.models import User
from app.routes import auth_routes, user_routes
from fastapi.security import OAuth2PasswordBearer


# uvicorn app.main:app --reload
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(user_routes.router)
app.include_router(auth_routes.router)

# 7:42
