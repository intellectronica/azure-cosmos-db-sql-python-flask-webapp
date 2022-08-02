from azure.cosmos import exceptions, CosmosClient, PartitionKey
import config

class CosmosClient():

    def create_cosmos_client(self)-> None:
        '''Create a client-side logical representation of an Azure Cosmos DB account.'''
        self.client = CosmosClient(config.ENDPOINT, config.KEY)

    def create_database(self, database_name: str)-> None:
        '''Create a database if it does not already exist on the service.'''
        #TODO: Add ThroughputProperties
        database = self.client.create_database_if_not_exists(id=database_name)

    def create_databases(self, databases_list: list)-> None:
        '''Create a database per element sent in the databases_list'''
        for database_name in databases_list:
            self.create_database(database_name)
    
    def create_container(self, database: str, container_details: dict)-> None:
        '''Create a container if it does not already exist on the service.'''
        container = database.create_container_if_not_exists(
            id=container_details['container_name'], 
            partition_key=PartitionKey(path=container_details['/partitionKey']),
            offer_throughput=container_details['throughput']
        )
    def create_containers(self, database_name: str, containers_list: list[dict])-> None:
        '''Create a container per element sent in the containers_list'''
        for container_details in containers_list:
            self.create_container(database_name, container_details)
    
    def create_items(self, container, items: list[dict]):
        '''Create a item per element in the items list'''
        for item in items:
            container.create_item(body=item)

    def read_container_items(self, container) -> list[dict]:
        '''Get the item identified by item.'''
        items = container.read_item()
        request_units = container.client_connection.last_response_headers['x-ms-request-charge']
        print(f'Read item with id {id}. Operation consumed {request_units} request units')
        return items
    
    def read_item(self, container, id: str, partition_key: str) -> dict:
        '''Get the item identified by item.'''
        try:
            item = container.read_item(item=id, partition_key=partition_key)
            request_units = container.client_connection.last_response_headers['x-ms-request-charge']
            print(f'Read item with id {id}. Operation consumed {request_units} request units')
        except exceptions.CosmosHttpResponseError:
            item = {}
            print(f'Item with id {id} does not exist in the {container} container.')
        
        return item
    
    def read_item_SQL_query(self, container, sql_query):
        items = list(container.query_items(query=sql_query, enable_cross_partition_query=True))

    def check_if_item_exist(self, container, id: str, partition_key: str):
        #TODO
        pass

    def replace_item(self, container, id: str, new_body: dict, ):
        '''Replaces the specified item if it exists in the container.
        id: The id or dict representing item to be replaced.
        new_body: A dict-like object representing the item to replace.'''
        try:
            new_item = container.replace_item(item=id, body=new_body)
        except exceptions.CosmosHttpResponseError:
            print(f'Item with id {id} does not exist in the {container} container.')

