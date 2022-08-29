
from dao.dao_comsos_db_sql import CosmosSQL
from model.item import Item

class Controller:
    def __init__(self) -> None:
        self.todo_dao = CosmosSQL()

    def create_todo_item(self, name: str, category: str, description: str, is_completed: bool) -> None: 
        todo_item = Item(name, category, description, is_completed).get_item_as_dict()
        return self.todo_dao.create_item(todo_item)


    def delete_todo_item(self, item_id: str) -> bool:
        return self.todo_dao.delete_item(item_id)


    def get_todo_item_by_id(self, item_id: str) -> Item:
        return self.todo_dao.read_item(item_id)


    def get_todo_items(self) -> list[Item]:
        return self.todo_dao.read_items()


    def update_todo_item(self, item_id: str, name: str, category: str, description: str, is_completed: bool) -> Item:

        item_body = Item(name, category, description, is_completed, new_item=False).get_item_as_dict()
        # identify and discard properties without a value to update
        items_to_discard = []
        for property, value in item_body.items():
            if not value:
                items_to_discard.append(property)
        for item in items_to_discard:
            del item_body[item]


        return self.todo_dao.update_item(item_id, item_body)
