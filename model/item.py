from unicodedata import category
import uuid

class Item:
    def __init__(self, name: str, category: str, description: str, completed: bool, new_item: bool = True) -> None:
        self.id = str(uuid.uuid4()) if new_item else ""
        self.name = name if name else ""
        self.category = category if category else ""
        self.description = description if description else ""
        self.is_completed = completed

    def get_item_as_dict(self) -> dict:
        return {"name": self.name, "category": self.category, "description": self.description, "is_completed": self.is_completed, "id": self.id}
