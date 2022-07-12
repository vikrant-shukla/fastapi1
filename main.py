from fastapi import FastAPI, Request, Depends

from crud.auth import authentication_decorator
from crud.controller import registerData, loginUser, userProfile, userProfileUpdate, userProfiledelete
from crud.serializer import PayloadInbound, InBoundUser, OutBoundUpdate

app = FastAPI()


@app.post("/login")
async def loginRoute(request: Request, payload: PayloadInbound):
    return loginUser(payload)


@app.post("/register")
async def registerUser(request: Request, payload: InBoundUser):
    return registerData(payload)


@app.get("/profile", dependencies=[Depends(authentication_decorator)])
async def profile(username: str):
    return userProfile(username)


@app.patch("/updateprofile", dependencies=[Depends(authentication_decorator)])
async def updateProfile(payload: OutBoundUpdate):
    return userProfileUpdate(payload)


@app.patch("/{delete}", dependencies=[Depends(authentication_decorator)])
async def deleteProfile(payload: str):
    return userProfiledelete(payload)
