from fastapi import FastAPI, Body


app = FastAPI()



@app.get("/")
async def root() -> str:
    return "Hello World Hide"

@app.post("/")
async def response_my_name(payload: dict = Body(...)) -> str:
    return f"Hi! it {payload["name"]}"