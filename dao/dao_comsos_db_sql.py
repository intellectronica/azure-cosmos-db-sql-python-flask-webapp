'''
Python client-side logical representation of an Azure Cosmos DB SQL API.
'''

import json
from typing import Iterable
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import config

# The name of our database.
DATABASE_ID = "TestDB"
# The name of our container.
CONTAINER_ID = "TestCollection"
# The partition key of your containers
PARTITION_KEY = "id"
# TEMP
MAX_ITEM_COUNT = 20

class CosmosSQL():
    '''Class to interact with Cosmos DB'''
    def __init__(self) -> None:
        '''Creates a cosmos client instance'''
        self.client = self.get_client()

    def create_item(self, body: dict):
        '''Insert or update the specified item.'''

        container = self.get_container_client(DATABASE_ID, CONTAINER_ID)

        try:
            container.upsert_item(body)
        except exceptions.CosmosHttpResponseError:
            print('Error inserting TODO item.')
        return json.load(body)


    def read_item(self, item_id: int):
        '''Get the item identified by the provided doc_id.'''

        container = self.get_container_client(DATABASE_ID, CONTAINER_ID)

        try:
            item = container.read_item(item=item_id, partition_key=item_id)
        except exceptions.CosmosHttpResponseError:
            print('Error reading TODO item.')
            return None
        return item


    def read_items(self) -> Iterable[dict]:
        container = self.get_container_client(DATABASE_ID, CONTAINER_ID)

        try:
            items = container.read_all_items(max_item_count=MAX_ITEM_COUNT)
        except exceptions.CosmosHttpResponseError:
            print('Error reading TODO item.')
            return None
        return items


    def update_item(self, item_id: str, body: str):
        '''Replaces the specified item if it exists in the container.'''

        container = self.get_container_client(DATABASE_ID, CONTAINER_ID)

        try:
            read_item = container.read_item(item=item_id, partition_key=item_id)
            for sub in body:
                read_item[sub]  = body[sub]
            container.replace_item(item=read_item, body=read_item)
        except exceptions.CosmosHttpResponseError:
            print('The replace failed or the item with given id does not exist.')
            return None
        return 'Item replaced successfully.'


    def delete_item(self, item_id: str) -> None:
        '''Delete the item identified by the provided doc_id.'''

        container = self.get_container_client(DATABASE_ID, CONTAINER_ID)

        try:
            container.delete_item(item=item_id, partition_key=item_id)
        except exceptions.CosmosResourceNotFoundError:
            print(f'Item {id} does not exist.')
        except exceptions.CosmosHttpResponseError:
            print(f'Item {id} was not deleted successfully.')


    def get_client(self)-> CosmosClient:
        '''Create a client-side logical representation of an Azure Cosmos DB account.'''
        return self.client if self.client else CosmosClient(config.ENDPOINT, config.KEY)


    def get_container_client(self, database_name: str, container_name: str):
        '''Get a container client given a database and container name.'''
        database = self.get_database_client(database_name)
        container = database.get_container_client(container_name)
        if not container:
            self.create_container(database_name, container_name, PARTITION_KEY)
        return container


    def get_database_client(self, database_name: str):
        '''Get a database client based on a database name.'''
        database = self.client.get_database_client(database_name)
        if not database:
            self.create_database(database_name)
        return database


    def create_database(self, database_name: str)-> None:
        '''Create a database if it does not already exist on the service.'''
        try:
            self.client.create_database_if_not_exists(id=database_name)
        except exceptions.CosmosResourceExistsError:
            print(f"{database_name} database already exists.")
        print(f"{database_name} database created.")


    def create_container(self, database_name: str, container_name: str, partition_key: str)-> None:
        '''Create a container if it does not already exist on the service.'''
        database = self.get_database_client(database_name)
        try:
            database.create_container_if_not_exists(
                id=container_name,
                partition_key=f"/{PartitionKey(path=partition_key)}"
            )
        except exceptions.CosmosHttpResponseError:
            print("The container creation failed.")
        print(f"{container_name} container created.")
