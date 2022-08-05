# azure-cosmos-db-sql-python-flask-webapp

This sample shows a Python web application (Flask) using Azure Cosmos DB SQL API and the Azure Cosmos DB Python SDK.

## Prerequisites

Before you can run this sample, you must have the following prerequisites:

- [Azure Cosmos DB SQL API Account](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/create-sql-api-python)
- [Azure Cosmos DB Python SDK](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cosmos/azure-cosmos)
- Python 3.8+ installed

## Running this sample

1. Clone this repository using:
    ```git clone https://github.com/Azure-Samples/azure-cosmos-db-python-getting-started.git```

1. Open the ```config.py``` file and replace the ENDPOINT and the KEY values with the values from your Cosmos DB Account.

1. Open a terminal and run ```python cosmos_client.py```.

## Request Examples

### Item

- Read an item:

```bash
curl -X GET  "localhost:5000/item?id=Smith_143fe975-5634-4743-bed8-b378a8c69d01&container=FamilyContainer&database=AzureSampleFamilyDatabase&partition_key=Smith"
```

- Upsert an item:

```bash
curl -X POST "localhost:5000/item?container=FamilyContainer&database=AzureSampleFamilyDatabase" -d "{\"id\": \"bar\", \"lastName\": \"bar\"}" -H "Content-Type: application/json"
```

- Delete an item:

 ```bash
curl -X DELETE  "localhost:5000/item?id=Smith_143fe975-5634-4743-bed8-b378a8c69d01&container=FamilyContainer&database=AzureSampleFamilyDatabase&partition_key=Smith"
```

- Replace an item:

```bash
curl -X PUT "localhost:5000/item?container=FamilyContainer&database=AzureSampleFamilyDatabase&id=bar" -d "{\"ola\": \"bar\", \"ole\": \"bareeee\"}" -H "Content-Type: application/json"
```

### Container

- List all databases:

```bash
curl -X GET  "localhost:5000/container?database=AzureSampleFamilyDatabase"
```

- Create container:

```bash
curl -X POST "localhost:5000/container?container=LocationContainer&database=AzureSampleFamilyDatabase&partition_key=location"
```

- Delete an item:

 ```bash
curl -X DELETE  "localhost:5000/container?container=LocationContainer&database=AzureSampleFamilyDatabase"
```

### Database

- List all databases:

```bash
curl -X GET  "localhost:5000/database?max_item_count=20"
```

- Create Database:

```bash
curl -X POST "localhost:5000/database?database=NewDatabase"
```

- Delete Database:

 ```bash
curl -X DELETE  "localhost:5000/database?database=NewDatabase
```
