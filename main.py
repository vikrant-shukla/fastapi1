from fastapi import FastAPI, Request

from crud.controller import registerdata, loginUser
from crud.serializer import PayloadInbound, InBoundUser

app = FastAPI()


@app.post("/login")
async def loginRoute(request: Request, payload: PayloadInbound):
    return loginUser(payload)


@app.post("/register")
async def registerUser(request: Request, payload: InBoundUser):
    return registerdata(payload)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
