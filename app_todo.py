"""
Flask API

"""

import json
from flask import Flask, request
from controller.controller import Controller


app = Flask(__name__)


@app.route("/api", methods=['GET', 'POST'])
def todo():
    # API Keys
    API_METHOD = "method"

    # API Methods
    CREATE_TODO_ITEM = "createTodoItem"
    GET_TODO_ITEMS = "getTodoItems"
    UPDATE_TODO_ITEM = "updateTodoItem"
    DELETE_TODO_ITEM = "deleteTodoItem"

    # API Parameters
    TODO_ITEM_ID = "todoItemId"
    TODO_ITEM_NAME = "todoItemName"
    TODO_ITEM_CATEGORY = "todoItemCategory"
    TODO_ITEM_COMPLETE = "todoItemComplete"

    MESSAGE_ERROR_INVALID_METHOD = "{'error': 'Invalid method'}"

    response = MESSAGE_ERROR_INVALID_METHOD

    todo_item_controller = Controller()

    item_id = request.args.get(TODO_ITEM_ID)
    name = request.args.get(TODO_ITEM_NAME)
    category = request.args.get(TODO_ITEM_CATEGORY)
    item_complete = request.args.get(TODO_ITEM_COMPLETE)
    is_completed = (item_complete is not None) and (item_complete.lower() == "true")

    api_method = request.get(API_METHOD)
    
    if api_method == CREATE_TODO_ITEM:
        response = todo_item_controller.create_todo_item(name, category, is_completed)

    elif api_method == GET_TODO_ITEMS:
        response = todo_item_controller.get_todo_items()

    elif api_method == UPDATE_TODO_ITEM:
        response = todo_item_controller.update_todo_item(item_id, is_completed)
    
    elif api_method == DELETE_TODO_ITEM:
        response = todo_item_controller.delete_todo_item(item_id, is_completed)

    return json.loads(response)

if __name__ == "__main__":
    app.run()

