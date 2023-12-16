from typing import Annotated
from auth.service import get_jwt
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from incidents.commands.delete_incident.delete_incident_use_case import DeleteIncidentUseCase

createIncidentUseCase = DeleteIncidentUseCase()

router = APIRouter(
    prefix="/incident",
    tags=["Incidents"],
    responses={404: {"description": "Not found"}},
)


@router.delete("/{id}")
async def delete_incident(id: str, jwt: Annotated[dict, Depends(get_jwt())]):
    success = createIncidentUseCase.execute(id)
    if not success:
        return JSONResponse({"message": "Failed to delete incident"}, status_code=500)
    return JSONResponse({"message": f"Deleted incident with id {id}"}, status_code=200)