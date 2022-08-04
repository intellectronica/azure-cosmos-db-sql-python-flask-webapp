import json
from azure.cosmos import exceptions, CosmosClient, PartitionKey, DatabaseProxy, ContainerProxy
from requests import delete
import config

class Cosmos():
    def __init__(self) -> None:
        self.client = self.create_cosmos_client()

    def create_cosmos_client(self)-> None:
        '''Create a client-side logical representation of an Azure Cosmos DB account.'''
        return CosmosClient(config.ENDPOINT, config.KEY)

    def create_database(self, database_name: str)-> DatabaseProxy:
        '''Create a database if it does not already exist on the service.'''
        # TODO: Add ThroughputProperties
        return self.client.create_database_if_not_exists(id=database_name)
    
    def create_container(self, database: str, container_details: dict)-> ContainerProxy:
        '''Create a container if it does not already exist on the service.'''
        return database.create_container_if_not_exists(
            id=container_details['container_name'], 
            partition_key=PartitionKey(path=container_details['/partitionKey']),
            offer_throughput=container_details['throughput']
        )

    def read_container_items(self, container) -> list[dict]:
        '''Get the item identified by item.'''
        items = container.read_item()
        request_units = container.client_connection.last_response_headers['x-ms-request-charge']
        print(f'Read item with id {id}. Operation consumed {request_units} request units')
        return items
    
    def read_item(self, database_name: str, container_name: str, id: str, partition_key: str) -> dict:
        '''Get the item identified by the provided id.'''
        
        container = self.get_container_client(database_name, container_name)
        
        try:
            item = container.read_item(item=id, partition_key=partition_key)
        except exceptions.CosmosHttpResponseError:
            return f'Item with id {id} does not exist in the {container_name} container of {database_name} database.'
        return item

    def delete_item(self, database_name: str, container_name: str, id: str, partition_key: str) -> dict:
        '''Delete the item identified by the provided id.'''

        container = self.get_container_client(database_name, container_name)

        try:
            container.delete_item(item=id, partition_key=partition_key)
        except exceptions.CosmosHttpResponseError:
            return (f'Item with id {id} was not deleted successfully from the {container} container of {database_name} database.')
        except exceptions.CosmosResourceNotFoundError:
            return f'Item with id {id} does not exist in the {container_name} container of {database_name} database.'
        return f'Item with id {id} deleted successfully from the {container_name} container of {database_name} database.'

    def upsert_item(self, database_name: str, container_name: str, body: dict):
        '''Insert or update the specified item.'''
        container = self.get_container_client(database_name, container_name)

        try:
            container.upsert_item(body)
        except exceptions.CosmosHttpResponseError:
            return (f'The given item could not be upserted into the {container} container of {database_name} database.')
        return f'Item upserted successfully into the {container_name} container of {database_name} database.'

    def replace_item(self, database_name: str, container_name: str, id: str, new_body: dict):
        '''Replaces the specified item if it exists in the container.
        id: The id or dict representing item to be replaced.
        new_body: A dict-like object representing the item to replace.'''

        container = self.get_container_client(database_name, container_name)

        try:
            read_item = container.read_item(item=id, partition_key=id)
            for sub in new_body:
                read_item[sub]  = new_body[sub]
            container.replace_item(item=read_item, body=read_item)
        except exceptions.CosmosHttpResponseError:
            return 'The replace failed or the item with given id does not exist.'
        return 'Item replaced successfully.'


    def get_container_client(self, database_name: str, container_name: str):
        ''''''
        # TODO: handle possible errors 
        database = self.client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        return container
    
    def read_item_SQL_query(self, container, sql_query):
        items = list(container.query_items(query=sql_query, enable_cross_partition_query=True))

    def check_if_item_exist(self, container, id: str, partition_key: str):
        # TODO
        pass
