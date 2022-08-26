import uuid

class Item:
    def __init__(self, name: str, description: str, completed: bool) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.completed = completed

    def get_item_as_dict(self) -> dict:
        return {"name": self.name, "category": self.category, "is_completed": self.is_completed, "id": self.id}
