import jwt
from fastapi import Header, HTTPException
from passlib.context import CryptContext
from crud.hashing import JWT_SECRET, JWT_ALGO
from crud.model import RegistrationModel


def authentication_decorator(token: str = Header("Authorization")):
    try:
        decode = jwt.decode(token, key=JWT_SECRET, algorithms=JWT_ALGO)
        obj = RegistrationModel.get_user(decode["username"])
        if obj and obj.username:
            return {"status": "authorised"}
        raise HTTPException(status_code=401, detail="Unauthorized token.")
    except:
        raise HTTPException(status_code=401, detail="Unauthorized token.")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
