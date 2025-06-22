from fastapi import FastAPI

from business import get_value

app = FastAPI()


@app.get("/")
async def root():
    return {"message": get_value(__name__)}
