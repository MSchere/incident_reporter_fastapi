from typing import Annotated
from auth.auth_service import get_jwt
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from incidents.queries.get_incidents.get_incidents_use_case import GetIncidentsUseCase

getIncidentsUseCase = GetIncidentsUseCase()

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def get_incidents(jwt: Annotated[dict, Depends(get_jwt())]):
    return JSONResponse(getIncidentsUseCase.execute())