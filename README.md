---
page_type: sample
languages:
- python
products:
- azure
- azure-cosmos-db
description: "How to use the Azure Cosmos DB with the SQL API with a Flask WebApp"
urlFragment: azure-cosmos-db-sql-python-flask-webapp
---

# Build a Python web application using Azure Cosmos DB and the SQL API

This sample shows a Python web application (Flask) using Azure Cosmos DB SQL API and the Azure Cosmos DB Python SDK.

## Prerequisites

Before you can run this sample, you must have the following prerequisites:

- [Azure Cosmos DB SQL API Account](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/create-sql-api-python)
- [Azure Cosmos DB Python SDK](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cosmos/azure-cosmos)
- Python 3.8+ installed

## Running this sample locally

1. Clone this repository using:

    ```git clone https://github.com/Azure-Samples/azure-cosmos-db-python-getting-started.git```

1. Open the ```config.py``` file and replace the **ENDPOINT** and the **KEY** values with the values of your Cosmos DB Account.

1. Open a command line and run: ```python app.py```.

1. If a browser doesn't open automatically, start the browser of your choice and navigate to localhost:5000. Alternatively, open a new command line and make requests. [See bellow some examples.](#Request-Examples)

## Request Examples

### Item

- Read an item:

```curl -X GET  "localhost:5000/item?id=<doc_id>&container=<container_name>&database=<database_name>&partition_key=<partition_key>"```

- Upsert an item:

```curl -X POST "localhost:5000/item?container=<container_name>&database=<database_name>" -d "{\"id\": \"1234\", \"property\": \"abcd\"}" -H "Content-Type: application/json"```

- Delete an item:

 ```curl -X DELETE  "localhost:5000/item?id=<doc_id>&container=<container_name>&database=<database_name>&partition_key=<partition_key>"```

- Replace an item:

```curl -X PUT "localhost:5000/item?container=<container_name>&database=<database_name>&id=<doc_id>" -d "{\"property\": \"abc\"}" -H "Content-Type: application/json"```

### Container

- List all containers:

```curl -X GET  "localhost:5000/container?database=<database_name>"```

- Create container:

```curl -X POST "localhost:5000/container?container=<container_name>&database=<database_name>&partition_key=<partition_key>"```

- Delete a container:

 ```curl -X DELETE  "localhost:5000/container?container=<container_name>&database=<database_name>"```

### Database

- List all databases:

```curl -X GET  "localhost:5000/database?max_item_count=20"```

- Create Database:

```curl -X POST "localhost:5000/database?database=<database_name>"```

- Delete Database:

 ```curl -X DELETE  "localhost:5000/database?database=<database_name>```

## Deploy the web app to Azure App Service

Follow the steps described in this [quickstart](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli#3---deploy-your-application-code-to-azure) to deploy the web application to Azure App Service.