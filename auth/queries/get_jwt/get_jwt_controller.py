from typing import Annotated
from auth.auth_service import get_jwt
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("")
async def get_jwt(jwt: Annotated[dict, Depends(get_jwt())]):
    return jwt