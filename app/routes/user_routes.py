from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List
from app.models.user import User
from app.schemas.user import CreateUser,User
from app.crud.user_crud import UserCrud
from app.db import engine
from sqlalchemy.ext.asyncio import async_sessionmaker

router = APIRouter()
session = async_sessionmaker(bind=engine, expire_on_commit=False)
db = UserCrud()


@router.get("/users")
async def get_user():
    print(session)
    users = await db.get_all(session)
    return users


@router.post("/users", status_code=status.HTTP_201_CREATED,response_model=User)
async def create_user(user: CreateUser):
    new_user = user.model_dump
    new_user = await db.add(session, new_user)
    return {"data": new_user}


@router.get("/users/{id}")
async def get_user(id: int):
    print("idid",id)
    user = await db.get_by_id(session, id)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with following id : {id} ",
        )
    return ("user", user)


@router.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
    user = await db.get_by_id(session,id)
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with following id : {id} ",
        )
    await db.delete(session,user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/users/{id}")
async def update_user(id: int, user: CreateUser):
    update_user = await  db.update(session, id, user)
    return {"data": update_user}


