from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()


# Models
class User(BaseModel):
    username: str
    comment: str



# Routers
@app.get("/")
async def root() -> str:
    return "Hello World Hide"

@app.post("/")
async def response_my_name(payload: dict = Body(...)) -> str:
    return f"Hi! it {payload["name"]}"

@app.post("/user_comment")
async def user_comment(UserData: User):
    return{
        "Your Name": UserData.username,
        "Your Comment": UserData.comment
    }