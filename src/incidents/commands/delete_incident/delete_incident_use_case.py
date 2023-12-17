
from src.incidents.database.incident_repository import IncidentRepository


class DeleteIncidentUseCase:
    def __init__(self):
        self.repository = IncidentRepository()

    def execute(self, incident_id: int) -> bool:
        return self.repository.delete_incident(incident_id)
