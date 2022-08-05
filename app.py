'''
Flask Application
'''
from flask import Flask, request
from cosmos_client import Cosmos

cosmosdb_client = Cosmos()
app = Flask(__name__)


@app.route("/item", methods=['GET', 'POST', 'PUT', 'DELETE'])
def item():
    '''Interact with items of a container.'''

    args = request.args

    if request.method == 'GET':
        response = cosmosdb_client.read_item(args.get('database'), args.get('container'), args.get('id'), args.get('partition_key'))
    elif request.method == 'POST':
        body = request.get_json()
        response = cosmosdb_client.upsert_item(args.get('database'), args.get('container'), body)
    elif request.method == 'PUT':
        new_body = request.get_json()
        response = cosmosdb_client.replace_item(args.get('database'), args.get('container'), args.get('id'), new_body)
    elif request.method == 'DELETE':
        response = cosmosdb_client.delete_item(args.get('database'), args.get('container'), args.get('id'), args.get('partition_key'))

    return response


@app.route("/container", methods=['GET', 'POST', 'DELETE'])
def container():
    '''Interact with container'''

    args = request.args

    if request.method == 'GET':
        response = cosmosdb_client.list_containers(args.get('max_item_count'))
    elif request.method == 'POST':
        response = cosmosdb_client.create_container(args.get('database'), request.args.get('container'), request.args.get('partition_key'))
    elif request.method == 'DELETE':
        response = cosmosdb_client.delete_container(args.get('database'), request.args.get('container'))

    return response

@app.route("/database", methods=['GET', 'POST', 'DELETE'])
def database():
    '''Interact with database'''
    
    args = request.args

    if request.method == 'GET':
        response =  cosmosdb_client.list_databases(args.get('database'))
    elif request.method == 'POST':
        response =  cosmosdb_client.create_database(args.get('database'))
    elif request.method == 'DELETE':
        response =  cosmosdb_client.delete_database(args.get('database'))
    
    return response

if __name__ == "__main__":
    app.run()
