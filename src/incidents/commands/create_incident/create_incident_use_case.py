

from src.incidents.commands.create_incident.create_incident_dto import CreateIncidentDto
from src.incidents.database.incident_model import Incident
from src.incidents.database.incident_repository import IncidentRepository


class CreateIncidentUseCase:

    def __init__(self):
        self.repository = IncidentRepository()

    def execute(self, dto: CreateIncidentDto, created_by: str) -> Incident or None:
        return self.repository.create_incident(dto.title, dto.description, created_by)
