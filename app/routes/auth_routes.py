from fastapi import APIRouter, Depends, status, HTTPException, Response
from app.db import engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.schemas.auth_schema import UserLogin
from app.models.user import User
from app.crud import AuthCrud
from app.util import verify
from app.oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

session = async_sessionmaker(bind=engine, expire_on_commit=False)
db = AuthCrud()


@router.post("/login")
async def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    user = await db.get_by_email(session, user_credentials.username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Invalid Credintials ",
        )

    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Invalid Credintials ",
        )

    access_token = create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
