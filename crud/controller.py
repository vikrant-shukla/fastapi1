from fastapi import HTTPException
from crud.auth import verify_password
from crud.hashing import verify
from crud.model import RegistrationModel
from crud.serializer import OutBoundSerializer, OutBoundUpdate


def registerData(payload):
    RegistrationModel.create(**payload.dict(exclude_unset=True))
    return {"message": "saved"}


def loginUser(payload):
    user = RegistrationModel.get_user(payload.username)
    if not user:
        return False
    if not verify_password(payload.password, user.password):
        return False
    token = verify(payload)
    return token


def userProfile(username):
    obj = RegistrationModel.get_user(username)
    data = OutBoundSerializer(
        username=obj.username,
        firstname=obj.firstname,
        lastname=obj.lastname,
        password=obj.password,
        dob=obj.dob,
        mobileNumber=obj.mobileNumber
    )
    return data


def userProfileUpdate(payload):
    obj = RegistrationModel.get_user(payload.username)
    if not obj:
        return HTTPException(status_code=404, detail="User Not Found")

    RegistrationModel.update_user(obj.id, **payload.dict(exclude_unset=True))
    return {"status": " successfully updated"}


def userProfiledelete(payload):
    obj = RegistrationModel.get_user(payload)
    data = RegistrationModel.delete_user(obj.id)
    return {"status": "success"}
