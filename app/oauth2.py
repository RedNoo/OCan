import jwt
from datetime import datetime, timedelta
from app.schemas import auth_schema

SECRET_KEY = "3d1bbcbd6ecdc220178199ef4a7deb8273a5c4b782cbe18d343d31df61990ddc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_endode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_endode.update({"exp": expire})

    token = jwt.encode(to_endode, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

        id: str = payload.get("user_id")

        if id is None:
            raise credential_exception

        token_data = auth_schema.TokenData(id)
    except jwt.ExpiredSignatureError:
        raise credential_exception
    except jwt.InvalidTokenError:
        raise credential_exception
    #7:20
