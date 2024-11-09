from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session
from typing import List
from app.models.user import User
from app.schemas.user_schema import CreateUser, UserResponse, UpdateUser
from app.crud.user_crud import UserCrud
from app.db import engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.util import hash
from app.oauth2 import get_current_user


router = APIRouter(prefix="/users", tags=["Users"])
session = async_sessionmaker(bind=engine, expire_on_commit=False)
db = UserCrud()


@router.get("/")
async def get_user():
    print(session)
    users = await db.get_all(session)
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
    request: Request,
    user: CreateUser #, current_user: int = Depends(get_current_user)
):
    #   print(current_user.email)
    hashed_password = hash(user.password)
    user.password = hashed_password
    new_user = User(created_ip_address= request.client.host, **user.model_dump())
    new_user = await db.add(session, new_user)
    return new_user


@router.get("/{id}", response_model=UserResponse)
async def get_user(id: int):
    print("idid", id)
    user = await db.get_by_id(session, id)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with following id : {id} ",
        )
    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
    user = await db.get_by_id(session, id)
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with following id : {id} ",
        )
    await db.delete(session, user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=UserResponse)
async def update_user(id: int, user: UpdateUser):
    update_user = await db.update(session, id, user)
    return update_user
