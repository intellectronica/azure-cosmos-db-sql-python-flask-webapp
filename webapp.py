from flask import Flask, request
from cosmos_client import CosmosClient
app = Flask(__name__)

cosmosdb_client = CosmosClient()

@app.route("/item", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def item():
    id = request.args.get('id')
    if request.method == 'GET':
        print(f'Request document with the id {id}.')
        return "GET!"
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