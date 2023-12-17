from typing import Annotated
from src.auth.auth_service import get_jwt
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from src.incidents.commands.create_incident.create_incident_dto import CreateIncidentDto
from src.incidents.commands.create_incident.create_incident_use_case import CreateIncidentUseCase

createIncidentUseCase = CreateIncidentUseCase()

router = APIRouter(
    prefix="/incident",
    tags=["Incidents"],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def create_incident(dto: CreateIncidentDto, jwt: Annotated[dict, Depends(get_jwt())]):
    incident = createIncidentUseCase.execute(dto, jwt['name'])
    if incident is None:
        return JSONResponse({"message": "Failed to create incident"}, status_code=500)

    return JSONResponse({"message": f"Created incident with id {incident.id}"}, status_code=200)
