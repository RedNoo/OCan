import jwt
from datetime import datetime, timedelta
from app.schemas.auth_schema import Token, TokenData
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.crud.user_crud import UserCrud
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.db import engine

oauth_schema = OAuth2PasswordBearer(tokenUrl="login")


SECRET_KEY = "3d1bbcbd6ecdc220178199ef4a7deb8273a5c4b782cbe18d343d31df61990ddc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

        id: int = payload.get("user_id")

        if id is None:
            raise credential_exception

        token_data = TokenData(id=id)
    except jwt.ExpiredSignatureError:
        raise credential_exception
    except jwt.InvalidTokenError:
        raise credential_exception

    return token_data


async def get_current_user(token: str = Depends(oauth_schema)):

    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could nor validate credentials",
        headers={"WWW-Authebticate": "Bearer"},
    )

    token = verify_access_token(token, credential_exception)

    db = UserCrud()
    session = async_sessionmaker(bind=engine, expire_on_commit=False)

    user = await db.get_by_id(session, token.id)

    return user
