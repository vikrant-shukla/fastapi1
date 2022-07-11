import jwt
import os

JWT_SECRET = f"{os.getenv('SECRET_URL')}"
JWT_ALGO = 'HS256'


def verify(payload):
    payload = payload.dict(exclude_unset=True)
    token = jwt.encode(payload, key=JWT_SECRET, algorithm=JWT_ALGO)
    return token
