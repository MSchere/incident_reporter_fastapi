from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_nextauth_jwt import NextAuthJWT
from functools import lru_cache
import config
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@lru_cache
def get_settings():
    return config.Settings()

JWT = NextAuthJWT()

@app.get("/auth")
async def return_jwt(jwt: Annotated[dict, Depends(JWT)]):
    return {"message": f"Hi {jwt['name']}. Greetings from FastAPI!"}

@app.post("/auth")
async def login(jwt: Annotated[dict, Depends(JWT)]):
    return jwt