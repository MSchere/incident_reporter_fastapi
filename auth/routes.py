from typing import Annotated
from auth.service import get_jwt
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def greet_user(jwt: Annotated[dict, Depends(get_jwt())]):
    return JSONResponse({"message": f"Welcome back {jwt['name']}. Greetings from FastAPI!"})

@router.post("")
async def get_jwt(jwt: Annotated[dict, Depends(get_jwt())]):
    return jwt