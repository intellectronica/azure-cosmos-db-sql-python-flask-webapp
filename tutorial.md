# Tutorial: Build a Python (Flask) web application using Azure Cosmos DB and the SQL API

This Python web application tutorial shows you how to use the Microsoft Azure Cosmos DB service to store and access data using a Flask application hosted on Azure App Service Web Apps.

>Note: Set up a free [Try Azure Cosmos DB account](https://cosmos.azure.com/try/).

In this article, you will learn:

- How to build a Flask application.
- How to work with the Azure Cosmos DB service using the Azure Cosmos DB Python SDK.

TODO: Add image of the webapp

## Prerequisites

Before you begin this application development tutorial, you must have the following:

- If you do not have an Azure subscription, you can set up a free [Try Azure Cosmos DB account](https://aka.ms/trycosmosdb).

- [Azure Cosmos DB SQL API Account](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/create-sql-api-python)

- [Azure Cosmos DB Python SDK](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cosmos/azure-cosmos)

- Python 3.8+ installed

## Create an Azure Cosmos DB account

Let's start by creating an Azure Cosmos DB account. If you already have an account or if you are using the Azure Cosmos DB Emulator for this tutorial, you can skip to [Step 2: Create the Flask application](#CreateFlaskApp).

## Deploy the application

Now that you have the complete application working correctly with Azure Cosmos DB we are going to deploy this web app to Azure App Service.

To publish this application, right-click the project in Solution Explorer and select Publish.

In Pick a publish target, select App Service.

To use an existing App Service profile, choose Select Existing, then select Publish.

In App Service, select a Subscription. Use the View filter to sort by resource group or resource type.

Find your profile, and then select OK. Next search the required Azure App Service and select OK.
