import os
from jose import jwt, JWTError
from datetime import datetime, timedelta

JWT_SECRET_KET = os.environ.get("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_token(data: dict):
    try:
        exp = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        data["exp"] = exp
        token = jwt.encode(data, JWT_SECRET_KET, algorithm=ALGORITHM)
    except JWTError:
        raise

    return token

def verify_token(token: str):
    try:
        data = jwt.decode(token, JWT_SECRET_KET, algorithms=[ALGORITHM])
        if data:
            return data , False
        return None, True
    except JWTError as err:
        return None, True
        

