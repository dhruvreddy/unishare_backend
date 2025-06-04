import uvicorn
from fastapi import FastAPI

from models.base_model import Base
from utils import engine
from routers import post_router, token_router

app = FastAPI()

app.include_router(post_router)
app.include_router(token_router)

@app.get("/")
def home():
    return "Hello"

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)