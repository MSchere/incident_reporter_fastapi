from typing import Annotated
from auth.auth_service import get_jwt
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from incidents.queries.get_incident.get_incident_use_case import GetIncidentUseCase

getIncidentUseCase = GetIncidentUseCase()

router = APIRouter(
    prefix="/incident",
    tags=["Incidents"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}")
async def get_incident(jwt: Annotated[dict, Depends(get_jwt())]):
    incident = JSONResponse(getIncidentUseCase.execute(id))
    if incident is None:
        return JSONResponse(status_code=404, content={"message": "Incident not found"})
    return incident.json()