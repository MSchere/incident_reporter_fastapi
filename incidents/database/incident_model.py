from enum import Enum
from datetime import datetime

class IncidentStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"

class Incident():
    id: str
    title: str
    description: str
    status: IncidentStatus
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, title, description, created_by, 
                id=None, status=None, 
                updated_by=None, created_at=None, updated_at=None):
        
        self.id = id or f"{created_by}_{int(datetime.now().timestamp())}"  
        self.title = title
        self.description = description
        self.status = status or IncidentStatus.OPEN
        self.created_by = created_by
        self.updated_by = updated_by or created_by
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def print(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Status: {self.status}, Created By: {self.created_by}, Updated By: {self.updated_by}, Created At: {self.created_at}, Updated At: {self.updated_at}"

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "createdBy": self.created_by,
            "updatedBy": self.updated_by,
            "createdAt": datetime.strftime(self.created_at, "%Y-%m-%dT%H:%M:%S.%fZ"),
            "updatedAt": datetime.strftime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        }