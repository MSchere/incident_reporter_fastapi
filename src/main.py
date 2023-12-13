from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from auth import get_jwt
from functools import lru_cache
import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@lru_cache
def get_settings():
    return config.Settings()

@app.get("/")
async def return_jwt(jwt: Annotated[dict, Depends(get_jwt())]):
    return {"message": f"Hi {jwt['name']}. Greetings from fastapi!"}

@app.post("/auth")
async def login(jwt: Annotated[dict, Depends(get_jwt())]):
    return jwt