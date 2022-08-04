''''''
from flask import Flask, request
from cosmos_client import Cosmos

cosmosdb_client = Cosmos()
app = Flask(__name__)


@app.route("/item", methods=['GET', 'POST', 'PUT', 'DELETE'])
def item():
    '''Interact with items'''
    doc_id = request.args.get('id')
    database_name = request.args.get('database')
    container_name = request.args.get('container')
    partition_key = request.args.get('partition_key')

    if request.method == 'GET':
        # Check if necessary values are present in the request
        return cosmosdb_client.read_item(database_name, container_name, doc_id, partition_key)

    if request.method == 'POST':
        body = request.get_json()
        return cosmosdb_client.upsert_item(database_name, container_name, body)

    if request.method == 'PUT':
        new_body = request.get_json()
        return cosmosdb_client.replace_item(database_name, container_name, doc_id, new_body)

    if request.method == 'DELETE':
        # Check if necessary values are present in the request
        return cosmosdb_client.delete_item(database_name, container_name, doc_id, partition_key)


@app.route("/container", methods=['GET', 'POST', 'PUT', 'DELETE'])
def container():
    '''Interact with container'''
    database_name = request.args.get('database')
    container_name = request.args.get('container')
    partition_key = request.args.get('partition_key')

    if request.method == 'GET':
        max_item_count = request.args.get('database')
        return cosmosdb_client.list_containers(max_item_count)
    if request.method == 'POST':
        return cosmosdb_client.create_container(database_name, container_name, partition_key)
    if request.method == 'DELETE':
        return cosmosdb_client.delete_container(database_name, container_name)


@app.route("/database", methods=['GET', 'POST', 'DELETE'])
def database():
    '''Interact with database'''
    if request.method == 'GET':
        max_item_count = request.args.get('database')
        return cosmosdb_client.list_databases(max_item_count)

    if request.method == 'POST':
        database_name = request.args.get('database')
        return cosmosdb_client.create_database(database_name)

    if request.method == 'DELETE':
        database_name = request.args.get('database')
        return cosmosdb_client.delete_database(database_name)


if __name__ == "__main__":
    app.run()
