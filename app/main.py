from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr


app = FastAPI()


class User(BaseModel):
    username: str
    mail: EmailStr
    rating: int





@app.get("/")
async def root() -> str:
    return "Hello World Hide"

@app.post("/")
async def response_my_name(payload: User) -> str:
    return f"Hi! it {payload.username} and your eamil is {payload.mail} you rated {payload.rating} star to the Course"


@app.post("/Hi")
async def user_comment(payload: dict = Body(...)) -> str:
    return f"Hi! it {payload["name"]}."