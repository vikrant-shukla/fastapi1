from typing import Optional
from passlib.context import CryptContext
from pydantic import BaseModel, validator


class InBoundUser(BaseModel):
    username: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    password: str
    dob: Optional[str] = None
    mobileNumber: Optional[int] = None

    @validator('password')
    def generate_password(cls, value):
        pwt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwt_context.hash(value)


class PayloadInbound(BaseModel):
    username: str
    password: str


class OutBoundSerializer(BaseModel):
    username: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    dob: Optional[str] = None
    mobileNumber: Optional[int] = None


class OutBoundUpdate(BaseModel):
    username: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    password: Optional[str] = None
    dob: Optional[str] = None
    mobileNumber: Optional[int] = None
