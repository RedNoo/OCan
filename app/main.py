from typing import Optional,List
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel, ConfigDict
from random import randrange
import time
from app.crud import UserCrud
from sqlalchemy.ext.asyncio import async_sessionmaker
from .db import engine
from app.models import User
from app.routes import auth_routes, user_routes

#uvicorn app.main:app --reload
app = FastAPI()

app.include_router(user_routes.router)
app.include_router(auth_routes.router)