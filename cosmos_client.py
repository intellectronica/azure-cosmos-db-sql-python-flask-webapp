'''
Python client-side logical representation of an Azure Cosmos DB.
This sample demonstrates the basic CRUD operations on a document in the Azure Cosmos DB API for SQL.
'''

from typing import Iterable
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import config

class Cosmos():
    '''Class to interact with Cosmos DB'''
    def __init__(self) -> None:
        '''Creates a cosmos client instance'''
        self.client = self.create_cosmos_client()

    def create_cosmos_client(self)-> None:
        '''Create a client-side logical representation of an Azure Cosmos DB account.'''
        return CosmosClient(config.ENDPOINT, config.KEY)

    def get_container_client(self, database_name: str, container_name: str):
        '''Get a container client given a database and container name.'''
        database = self.get_database_client(database_name)
        container = database.get_container_client(container_name)
        return container

    def get_database_client(self, database_name: str):
        '''Get a database client based on a database name.'''
        return self.client.get_database_client(database_name)

    # Database Operations
    def create_database(self, database_name: str)-> None:
        '''Create a database if it does not already exist on the service.'''
        try:
            self.client.create_database_if_not_exists(id=database_name)
        except exceptions.CosmosResourceExistsError:
            return f"{database_name} database already exists."
        return f"{database_name} database created."

    def delete_database(self, database_name: str)-> str:
        '''Delete a database.'''
        try:
            self.client.delete_database(database_name)
        except exceptions.CosmosHttpResponseError:
            return f"{database_name} database couldn't be deleted."
        return f"{database_name} database deleted."

    def list_databases(self, max_item_count: int = 10)-> list:
        '''List all databases.'''
        return list(self.client.list_databases(max_item_count))

    # Container Operations
    def create_container(self, database_name: str, container_name: str, partition_key: str)-> None:
        '''Create a container if it does not already exist on the service.'''
        database = self.get_database_client(database_name)
        try:
            database.create_container_if_not_exists(
                id=container_name,
                partition_key=f"/{PartitionKey(path=partition_key)}"
            )
        except exceptions.CosmosHttpResponseError:
            return f"The container creation failed."
        return f"{container_name} container created into {database_name} database."

    def delete_container(self, database_name: str, container_name: str)-> str:
        '''Delete a container.'''
        database = self.get_database_client(database_name)
        try:
            database.delete_container(container_name)
        except exceptions.CosmosHttpResponseError:
            return f"{container_name} container of {database_name} database couldn't be deleted."
        return f"{container_name} container of {database_name} database was deleted."

    def list_containers(self, database_name: str, max_item_count: int = 10)-> Iterable:
        '''List containers of a database.'''
        database = self.get_database_client(database_name)
        return list(database.list_containers(max_item_count))

    # Item Operations
    def read_item(self, database_name: str, container_name: str, doc_id: str, partition_key: str) -> dict:
        '''Get the item identified by the provided doc_id.'''

        container = self.get_container_client(database_name, container_name)

        try:
            item = container.read_item(item=doc_id, partition_key=partition_key)
        except exceptions.CosmosHttpResponseError:
            return f'Item with id {doc_id} does not exist in the {container_name} container of {database_name} database.'
        return item

    def delete_item(self, database_name: str, container_name: str, doc_id: str, partition_key: str) -> dict:
        '''Delete the item identified by the provided doc_id.'''

        container = self.get_container_client(database_name, container_name)

        try:
            container.delete_item(item=id, partition_key=partition_key)
        except exceptions.CosmosResourceNotFoundError:
            return f'Item with id {doc_id} does not exist in the {container_name} container of {database_name} database.'
        except exceptions.CosmosHttpResponseError:
            return f'Item with id {doc_id} was not deleted successfully from the {container} container of {database_name} database.'
        return f'Item with id {doc_id} deleted successfully from the {container_name} container of {database_name} database.'

    def upsert_item(self, database_name: str, container_name: str, body: dict):
        '''Insert or update the specified item.'''
        container = self.get_container_client(database_name, container_name)

        try:
            container.upsert_item(body)
        except exceptions.CosmosHttpResponseError:
            return f'The given item could not be upserted into the {container} container of {database_name} database.'
        return f'Item upserted successfully into the {container_name} container of {database_name} database.'

    def replace_item(self, database_name: str, container_name: str, item: str, new_body: dict):
        '''Replaces the specified item if it exists in the container.'''

        container = self.get_container_client(database_name, container_name)

        try:
            read_item = container.read_item(item=item, partition_key=item)
            for sub in new_body:
                read_item[sub]  = new_body[sub]
            container.replace_item(item=read_item, body=read_item)
        except exceptions.CosmosHttpResponseError:
            return 'The replace failed or the item with given id does not exist.'
        return 'Item replaced successfully.'
