import datetime

class Task:
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = datetime.datetime.now().isoformat()
        self.updatedAt = datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
