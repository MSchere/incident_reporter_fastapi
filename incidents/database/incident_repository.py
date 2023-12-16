
from core.redis import get_redis
from incidents.database.incident_model import Incident, IncidentStatus
from datetime import datetime
import json

class IncidentRepository:
    def __init__(self):
        self.redis = get_redis()
    
    def create_incident(self, title: str, description: str, created_by: str) -> Incident or None:
        try:
            incident = Incident(title, description, created_by)
            self.redis.set(incident.id, incident.json())
            return incident
        except Exception as e:
            print(f"Error creating incident: {e}")
            return None

    def update_incident(self, id: str, title: str, description: str, status: IncidentStatus, updated_by: str) -> bool:
        try:
            incident_to_update = self.redis.get(id)
            if incident_to_update is None:
                return False
            incident = Incident(
                title,
                description,
                incident_to_update['createdBy'],
                incident_to_update['id'],
                status,
                updated_by,
                incident_to_update['createdAt'],
                updated_at=datetime.now()
            )
            self.redis.set(incident.id, incident.json())
            return True
        except Exception as e:
            print(f"Error updating incident: {e}")
            return False

    def delete_incident(self, id: str) -> bool:
        try:
            return self.redis.delete(id) == 1
        except Exception as e:
            print(e)
            return False

    def get_incident(self, id: str) -> Incident or None:
        try:
            incident = self.redis.get(id)
            if incident is None:
                return None
            return Incident(
                incident["title"],
                incident["description"],
                incident["createdBy"],
                incident["id"],
                IncidentStatus[incident["status"]],
                incident["updatedBy"],
                datetime.strptime(incident["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ"),
                datetime.strptime(incident["updatedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
            )
        except Exception as e:
            print(f"Error getting incident: {e}")
            return None

    def get_incidents(self) -> list:
        try:
            incidents = []
            for key in self.redis.keys("*"):
                incident = json.loads(self.redis.get(key))
                incidents.append(Incident(
                    incident["title"],
                    incident["description"],
                    incident["createdBy"],
                    incident["id"],
                    IncidentStatus[incident["status"]],
                    incident["updatedBy"],
                    datetime.strptime(incident["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ"),
                    datetime.strptime(incident["updatedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
                ).json())
            return incidents
        except Exception as e:
            print(f"Error getting incidents: {e}")
            return []


