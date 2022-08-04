from flask import Flask, request
from cosmos_client import Cosmos

cosmosdb_client = Cosmos()


app = Flask(__name__)

@app.route("/item", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def item():
    id = request.args.get('id')
    database = request.args.get('database')
    container = request.args.get('container')
    partition_key = request.args.get('partition_key')
    
    if request.method == 'GET':
        # Check if necessary values are present in the request
        if not all([id, database, container, partition_key]):
            return f"The following values should be provided."
        return cosmosdb_client.read_item(id=id, partition_key=partition_key, database_name=database, container_name=container)
    
    elif request.method == 'POST':
        if not all([database, container]):
            return f"The following values should be provided."
        body = request.get_json()
        return cosmosdb_client.upsert_item(body=body, database_name=database, container_name=container)
    
    elif request.method == 'PUT':
        if not all([database, container]):
            return f"The following values should be provided."
        new_body = request.get_json()
        return cosmosdb_client.replace_item(id=id, new_body=new_body, database_name=database, container_name=container)
    
    elif request.method == 'DELETE':
        # Check if necessary values are present in the request
        if not all([id, database, container, partition_key]):
            return f"The all following values  should be provided]."
        return cosmosdb_client.delete_item(id=id, partition_key=partition_key, database_name=database, container_name=container)

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