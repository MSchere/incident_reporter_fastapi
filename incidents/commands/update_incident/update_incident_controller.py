from typing import Annotated
from auth.service import get_jwt
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from incidents.commands.update_incident.update_incident_dto import UpdateIncidentDto
from incidents.commands.update_incident.update_incident_use_case import UpdateIncidentUseCase

updateIncidentUseCase = UpdateIncidentUseCase()

router = APIRouter(
    prefix="/incident",
    tags=["Incidents"],
    responses={404: {"description": "Not found"}},
)


@router.put("/{id}")
async def update_incident(id: str, dto: UpdateIncidentDto, jwt: Annotated[dict, Depends(get_jwt())]):
    success = updateIncidentUseCase.execute(id, dto, jwt['name'])
    if not success:
        return JSONResponse({"message": "Failed to update incident"}, status_code=500)
    return JSONResponse({"message": f"Updated incident with id {id}"}, status_code=200)