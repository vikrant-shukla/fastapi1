
from passlib.context import CryptContext
from crud.hashing import verify
from crud.model import RegistrationModel



def registerdata(payload):
    RegistrationModel.create(**payload.dict(exclude_unset=True))
    return {"message": "saved"}


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    print(hashed_password)
    print(plain_password)
    print(pwd_context.verify(plain_password, hashed_password))
    return pwd_context.verify(plain_password, hashed_password)


def loginUser(payload):
    user = RegistrationModel.get_user(payload.username)

    if not user:
        return False
    if not verify_password(payload.password, user.password):
        return False
    token = verify(payload)
    return token
