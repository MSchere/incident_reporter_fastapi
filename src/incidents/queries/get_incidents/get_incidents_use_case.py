
from src.incidents.database.incident_repository import IncidentRepository
from src.incidents.database.incident_model import Incident


class GetIncidentsUseCase:

    def __init__(self):
        self.repository = IncidentRepository()

    def execute(self) -> list:
        return self.repository.get_incidents()
