
from incidents.commands.update_incident.update_incident_dto import UpdateIncidentDto
from incidents.database.incident_repository import IncidentRepository

class UpdateIncidentUseCase:
    def __init__(self):
        self.incident_repo = IncidentRepository()

    def execute(self, incident_id: str, dto: UpdateIncidentDto, updated_by: str) -> bool:
        return self.incident_repo.update_incident(incident_id, dto.title, dto.description, dto.status, updated_by)