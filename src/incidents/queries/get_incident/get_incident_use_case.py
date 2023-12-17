
from src.incidents.database.incident_repository import IncidentRepository
from src.incidents.database.incident_model import Incident


class GetIncidentUseCase():

    def __init__(self):
        self.repository = IncidentRepository()

    def execute(self, id: str) -> Incident or None:
        return self.repository.get_incident(id)
