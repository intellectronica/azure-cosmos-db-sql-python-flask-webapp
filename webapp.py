from flask import Flask, request
from cosmos_client import Cosmos

cosmosdb_client = Cosmos()

app = Flask(__name__)

@app.route("/item", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def item():
    args = request.args
    id = args.get('id')
    database = args.get('database')
    container = args.get('container')
    partition_key = args.get('partition_key')
    if request.method == 'GET':
        print(f'Request document with the id {id} from {container} container.')
        item = cosmosdb_client.read_item(id=id, partition_key=partition_key, database_name=database, container_name=container)
        return item
    if request.method == 'POST':
        return "POST!"
    if request.method == 'PUT':
        return "PUT!"
    if request.method == 'DELETE':
        return "DELETE!"

@app.route("/container", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def container():
    if request.method == 'GET':
        return "GET!"
    if request.method == 'POST':
        return "POST!"
    if request.method == 'PUT':
        return "PUT!"
    if request.method == 'DELETE':
        return "DELETE!"

@app.route("/database", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def database():
    if request.method == 'GET':
        return "GET!"
    if request.method == 'POST':
        return "POST!"
    if request.method == 'PUT':
        return "PUT!"
    if request.method == 'DELETE':
        return "DELETE!"

@app.route("/item")
def members():
    return "Members"

if __name__ == "__main__":
    app.run()