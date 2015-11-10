<properties
	pageTitle="How to use Azure Table storage from Node.js | Windows Azure"
	description="Learn how to use Azure Table storage. Code samples are written using the Node.js API."
	services="storage"
	documentationCenter="nodejs"
	authors="MikeWasson"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="storage"
	ms.date="09/01/2015"
	wacn.date=""/>


# How to use <!-- deleted by customization Azure --> Table storage from Node.js

[AZURE.INCLUDE [storage-selector-table-include](../includes/storage-selector-table-include.md)]


## Overview

This topic shows how to perform common scenarios using the <!-- deleted by customization Azure Table service in a Node.js application. -->
<!-- deleted by customization

The code examples in this topic assume you already have a Node.js application. For information about how to create a Node.js application in Azure, see any of these topics:

- [Build and deploy a Node.js website to Azure](Create and deploy a Node.js application to an Azure website)
- [Build and deploy a Node.js website to Azure using WebMatrix](Create and deploy a Node.js application with WebMatrix)
- [Build and deploy a Node.js application to an Azure Cloud Service](Node.js Cloud Service) (using Windows PowerShell)
-->
<!-- keep by customization: begin -->
Azure Table service in a Node.js application. 

The code examples in this topic assume you already have a Node.js application. For instructions on creating a Node.js application in Azure, see any of these topics:

- [Build and deploy a Node.js website to Azure][Create and deploy a Node.js application to an Azure Web Site]
- [Build and deploy a Node.js website to Azure using WebMatrix][Web Site with WebMatrix].
- [Build and deploy a Node.js application to an Azure Cloud Service][Node.js Cloud Service] (using Windows PowerShell)
<!-- keep by customization: end -->


[AZURE.INCLUDE [storage-table-concepts-include](../includes/storage-table-concepts-include.md)]

[AZURE.INCLUDE [storage-create-account-include](../includes/storage-create-account-include.md)]


## Configure your application to access Azure Storage

To use Azure <!-- deleted by customization Storage --><!-- keep by customization: begin --> storage <!-- keep by customization: end -->, you need the Azure Storage SDK for Node.js, which includes a set of convenience libraries that
communicate with the storage REST services.

### Use Node Package Manager (NPM) to install the package

1.  Use a command-line interface such as **PowerShell** (Windows) <!-- deleted by customization, --> **Terminal** (Mac) <!-- deleted by customization, --> or **Bash** (Unix), and navigate to the folder where you created your application.

<!-- deleted by customization
2.  Type **npm install azure-storage** in the command window. Output from the command is similar to the following example.

		azure-storage@0.5.0 node_modules\azure-storage
		+-- extend@1.2.1
		+-- xmlbuilder@0.4.3
		+-- mime@1.2.11
		+-- node-uuid@1.4.3
		+-- validator@3.22.2
		+-- underscore@1.4.4
		+-- readable-stream@1.0.33 (string_decoder@0.10.31, isarray@0.0.1, inherits@2.0.1, core-util-is@1.0.1)
		+-- xml2js@0.2.7 (sax@0.5.2)
		+-- request@2.57.0 (caseless@0.10.0, aws-sign2@0.5.0, forever-agent@0.6.1, stringstream@0.0.4, oauth-sign@0.8.0, tunnel-agent@0.4.1, isstream@0.1.2, json-stringify-safe@5.0.1, bl@0.9.4, combined-stream@1.0.5, qs@3.1.0, mime-types@2.0.14, form-data@0.2.0, http-signature@0.11.0, tough-cookie@2.0.0, hawk@2.3.1, har-validator@1.8.0)

3.  You can manually run the **ls** command to verify that a **node_modules** folder was created. Inside that folder you will find the **azure-storage** package, which contains the libraries you need to access storage.
-->
<!-- keep by customization: begin -->
2.  Type **npm install azure-storage** in the command window, which should result in the following output:

        azure-storage@0.1.0 node_modules\azure-storage
		├── extend@1.2.1
		├── xmlbuilder@0.4.3
		├── mime@1.2.11
		├── underscore@1.4.4
		├── validator@3.1.0
		├── node-uuid@1.4.1
		├── xml2js@0.2.7 (sax@0.5.2)
		└── request@2.27.0 (json-stringify-safe@5.0.0, tunnel-agent@0.3.0, aws-sign@0.3.0, forever-agent@0.5.2, qs@0.6.6, oauth-sign@0.3.0, cookie-jar@0.3.0, hawk@1.0.0, form-data@0.1.3, http-signature@0.10.0)

3.  You can manually run the **ls** command to verify that a 
    **node_modules** folder was created. Inside that folder you will
    find the **azure-storage** package, which contains the libraries you need to
    access storage.
<!-- keep by customization: end -->

### Import the package

Add the following code to the top of the **server.js** file in your application:

    var azure = require('azure-storage');

<!-- deleted by customization
## Set up an Azure Storage connection
-->
<!-- keep by customization: begin -->
## Setup an Azure Storage Connection
<!-- keep by customization: end -->

The azure module will read the environment variables AZURE_STORAGE_ACCOUNT and AZURE_STORAGE_ACCESS_KEY, or AZURE_STORAGE_CONNECTION_STRING for information required to connect to your Azure storage account. If these environment variables are not set, you must specify the account information when calling **TableService**.

For an example of setting the environment variables in the <!-- deleted by customization Azure Management Portal --><!-- keep by customization: begin --> management portal <!-- keep by customization: end --> for an Azure Website, see [Node.js <!-- deleted by customization web application --><!-- keep by customization: begin --> Web Application <!-- keep by customization: end --> with Storage]

## Create a table

The following code creates a **TableService** object and uses it to <!-- deleted by customization create a new table. Add the following near the top of **server.js**. -->
<!-- keep by customization: begin -->
create a new table. Add the following near the top of **server.js**.
<!-- keep by customization: end -->

    var tableSvc = azure.createTableService();

The call to **createTableIfNotExists** will create a new table with the specified name if it does <!-- deleted by customization not already exist. The following example creates a new table named 'mytable' if it does not already exist: -->
<!-- keep by customization: begin -->
not already exist. The following example creates a new table named 'mytable' if it does not already exist:
<!-- keep by customization: end -->

    tableSvc.createTableIfNotExists('mytable', function(error, result, response){
		if(!error){
			// Table exists or created
		}
	});

The `result` will be `true` if a new table is created, and `false` if the table already exists. <!-- deleted by customization The --> `response` will contain information about the request.

### Filters

Optional filtering operations can be applied to operations performed using **TableService**. Filtering operations can include logging, automatically retrying, etc. Filters are objects that implement a method with the signature:

		function handle (requestOptions, next)

After doing its preprocessing on the request options, the method needs to call "next" <!-- deleted by customization, --> passing a callback with the following signature:

		function (returnObject, finalCallback, next)

In this callback, and after processing the returnObject (the response from the request to the server), the callback needs to either invoke next if it exists to continue processing other filters or simply invoke finalCallback otherwise to end <!-- keep by customization: begin --> up <!-- keep by customization: end --> the service invocation.

Two filters that implement retry logic are included with the Azure SDK for Node.js, **ExponentialRetryPolicyFilter** and **LinearRetryPolicyFilter**. The following creates a **TableService** object that uses the **ExponentialRetryPolicyFilter**:

	var retryOperations = new azure.ExponentialRetryPolicyFilter();
	var tableSvc = azure.createTableService().withFilter(retryOperations);

## Add an entity to a table

<!-- deleted by customization
To add an entity, first create an object that defines your entity properties. All entities must contain a **PartitionKey** and **RowKey**, which are unique identifiers for the entity.

* **PartitionKey** - determines the partition that the entity is stored in <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **RowKey** - uniquely identifies the entity within the partition

Both **PartitionKey** and **RowKey** must be string values. For more information, see [Understanding the Table service data model](http://msdn.microsoft.com/zh-cn/library/azure/dd179338.aspx).
-->
<!-- keep by customization: begin -->
To add an entity, first create an object that defines your entity
 properties. All entities must contain a **PartitionKey** and **RowKey**, which are unique identifiers for the entity.

* **PartitionKey** - Determines the partition that the entity is stored in <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **RowKey** - Uniquely identifies the entity within the partition.

Both **PartitionKey** and **RowKey** must be string values. For more information, see [Understanding the Table Service data model](http://msdn.microsoft.com/zh-cn/library/azure/dd179338.aspx).
<!-- keep by customization: end -->

The following is an example of defining an entity. Note that **dueDate** is defined as a type of **Edm.DateTime**. Specifying the type is optional, and types will be inferred if not specified.

	var task = {
	  PartitionKey: {'_':'hometasks'},
	  RowKey: {'_': '1'},
	  description: {'_':'take out the trash'},
	  dueDate: {'_':new Date(2015, 6, 20), '$':'Edm.DateTime'}
	};

> [AZURE.NOTE] There is also a **Timestamp** field for each record, which is set by Azure when an entity is inserted or updated.

You can also use the **entityGenerator** to create entities. The following example creates the same task entity using the **entityGenerator**.

	var entGen = azure.TableUtilities.entityGenerator;
    var task = {
	  PartitionKey: entGen.String('hometasks'),
      RowKey: entGen.String('1'),
      description: entGen.String('take out the trash'),
      dueDate: entGen.DateTime(new Date(Date.UTC(2015, 6, 20))),
    };

To add an entity to your table, pass the entity object to <!-- deleted by customization the **insertEntity** method. -->
<!-- keep by customization: begin -->
the **insertEntity** method.
<!-- keep by customization: end -->

	tableSvc.insertEntity('mytable',task, function (error, result, response) {
		if(!error){
			// Entity inserted
		}
	});

If the operation is successful, `result` will contain the [ETag](http://en.wikipedia.org/wiki/HTTP_ETag) of the inserted record and `response` will contain information about the operation.

Example response:

	{ '.metadata': { etag: 'W/"datetime\'2015-02-25T01%3A22%3A22.5Z\'"' } }

> [AZURE.NOTE] By default, **insertEntity** does not return the inserted entity as part of the `response` information. If you plan on performing other operations on this entity, or wish to cache the information, it can be useful to have it returned as part of the `result`. You can do this by enabling **echoContent** as follows:
>
> `tableSvc.insertEntity('mytable', task, {echoContent: true}, function (error, result, response) {...}`

## Update an entity

There are multiple methods available to update an existing entity:

<!-- deleted by customization
* **updateEntity** - updates an existing entity by replacing it

* **mergeEntity** - updates an existing entity by merging new property values into the existing entity <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **insertOrReplaceEntity** - updates an existing entity by replacing it. If no entity exists, a new one will be inserted <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **insertOrMergeEntity** - updates an existing entity by merging new property values into the existing. If no entity exists, a new one will be inserted <!-- keep by customization: begin -->. <!-- keep by customization: end -->
-->
<!-- keep by customization: begin -->
* **updateEntity** - Updates an existing entity by replacing it.

* **mergeEntity** - Updates an existing entity by merging new property values into the existing entity <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **insertOrReplaceEntity** - Updates an existing entity by replacing it. If no entity exists, a new one will be inserted <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **insertOrMergeEntity** - Updates an existing entity by merging new property values into the existing. If no entity exists, a new one will be inserted <!-- keep by customization: begin -->. <!-- keep by customization: end -->
<!-- keep by customization: end -->

The following example demonstrates updating an entity using **updateEntity**:

	tableSvc.updateEntity('mytable', updatedTask, function(error, result, response){
      if(!error) {
        // Entity updated
      }
    });

> [AZURE.NOTE] By default, updating an entity does not check to see if the data being updated has previously been modified by another process. To support concurrent updates:
>
> 1. Get the ETag of the object being updated. This is returned as part of the `response` for any entity related operation and can be retrieved through `response['.metadata'].etag`.
>
> 2. When performing an update operation on an entity, add the ETag information previously retrieved to the new entity. For example:
>
>     `entity2['.metadata'].etag = currentEtag;`
>    
> 3. Perform the update operation. If the entity has been modified since you retrieved the ETag value, such as another instance of your application, an `error` will be returned stating that the update condition specified in the request was not satisfied.
<!-- deleted by customization

With **updateEntity** and **mergeEntity**, if the entity that is being updated doesn't exist, then the update operation will fail. Therefore if you wish to store an entity regardless of whether it already exists, use **insertOrReplaceEntity** or **insertOrMergeEntity**.
-->
<!-- keep by customization: begin -->
    
With **updateEntity** and **mergeEntity**, if the entity that is being updated doesn't exist then the update operation will fail. Therefore if you wish to store an entity regardless of whether it already exists, you should instead use **insertOrReplaceEntity** or **insertOrMergeEntity**.
<!-- keep by customization: end -->

The `result` for successful update operations will contain the **Etag** of the updated entity.

## Work with groups of entities

<!-- deleted by customization
Sometimes it makes sense to submit multiple operations together in a batch to ensure atomic processing by the server. To accomplish that, use the **TableBatch** class to create a batch, and then use the **executeBatch** method of **TableService** to perform the batched operations.
-->
<!-- keep by customization: begin -->
Sometimes it makes sense to submit multiple operations together in a
 batch to ensure atomic processing by the server. To accomplish that, use the **TableBatch** class to create a batch, and then use the **executeBatch** method of **TableService** to perform the batched operations.
<!-- keep by customization: end -->

 The following example demonstrates submitting two entities in a batch:

    var task1 = {
	  PartitionKey: {'_':'hometasks'},
	  RowKey: {'_': '1'},
	  description: {'_':'Take out the trash'},
	  dueDate: {'_':new Date(2015, 6, 20)}
	};
	var task2 = {
	  PartitionKey: {'_':'hometasks'},
	  RowKey: {'_': '2'},
	  description: {'_':'Wash the dishes'},
	  dueDate: {'_':new Date(2015, 6, 20)}
	};

	var batch = new azure.TableBatch();
	batch.insertEntity(task1, {echoContent: true});
	batch.insertEntity(task2, {echoContent: true});

	tableSvc.executeBatch('mytable', batch, function (error, result, response) {
	  if(!error) {
	    // Batch completed
	  }
	});

For successful batch operations, `result` will contain information for each operation in the batch.

<!-- deleted by customization
### Work with batched operations

Operations added to a batch can be inspected by viewing the `operations` property. You can also use the following methods to work with operations <!-- deleted by customization: --><!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **clear** - clears all operations from a batch <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **getOperations** - gets an operation from the batch <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **hasOperations** - returns true if the batch contains operations <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **removeOperations** - removes an operation <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **size** - returns the number of operations in the batch <!-- keep by customization: begin -->. <!-- keep by customization: end -->
-->
<!-- keep by customization: begin -->
### Working with batched operations

Operations added to a batch can be inspected by viewing the `operations` property. You can also use the following methods to work with operations <!-- deleted by customization: --><!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **clear** - clears all operations from a batch <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **getOperations** - gets an operation from the batch <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **hasOperations** - returns true if the batch contains operations <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **removeOperations** - removes an operation <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **size** - returns the number of operations in the batch <!-- keep by customization: begin -->. <!-- keep by customization: end -->
<!-- keep by customization: end -->

## Retrieve an entity by key

To return a specific entity based on the **PartitionKey** and **RowKey**, use the **retrieveEntity** method.

    tableSvc.retrieveEntity('mytable', 'hometasks', '1', function(error, result, response){
	  if(!error){
	    // result contains the entity
	  }
    });

Once this operation <!-- deleted by customization is complete --><!-- keep by customization: begin --> completes <!-- keep by customization: end -->, `result` will contain the entity.

<!-- deleted by customization
## Query a set of entities

To query a table, use the **TableQuery** object to build up a query expression using the following clauses:

* **select** - the fields to be returned from the query <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **where** - the where clause

	* **and** - an `and` where condition

	* **or** - an `or` where condition

* **top** - the number of items to fetch


The following example builds a query that will return the top five items with a PartitionKey of 'hometasks'.
-->
<!-- keep by customization: begin -->
## Query a set of Entities

To query a table, use the **TableQuery** object to build up a query 
expression using the following clauses:

* **select** - The fields to be returned from the query <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **where** - The where clause.

	* **and** - An `and` where condition.

	* **or** - An `or` where condition.

* **top** - The number of items to fetch.


The following example builds a query that will return the top 5 items with a PartitionKey of 'hometasks'.
<!-- keep by customization: end -->

	var query = new azure.TableQuery()
	  .top(5)
	  .where('PartitionKey eq ?', 'hometasks');

Since **select** is not used, all fields will be returned. To perform the query against a table, use **queryEntities**. The following example uses this query to return entities from 'mytable'.

	tableSvc.queryEntities('mytable',query, null, function(error, result, response) {
	  if(!error) {
	    // query was successful
	  }
	});

If successful, `result.entries` will contain an array of entities that match the query. If the query was unable to return all entities, `result.continuationToken` will be non-*null* and can be used as the third parameter of **queryEntities** to retrieve more results. For the initial query, <!-- deleted by customization use *null* for --> the third parameter <!-- keep by customization: begin --> should be *null* <!-- keep by customization: end -->.

<!-- deleted by customization
### Query a subset of entity properties
-->
<!-- keep by customization: begin -->
### How to Query a Subset of Entity Properties
<!-- keep by customization: end -->

A query to a table can retrieve just a few fields from an entity.
This reduces bandwidth and can improve query performance, especially for large entities. Use the **select** clause and pass the names of the fields to be returned. For example, the following query will <!-- keep by customization: begin --> only <!-- keep by customization: end --> return <!-- deleted by customization only --> the **description** and **dueDate** fields.

	var query = new azure.TableQuery()
	  .select(['description', 'dueDate'])
	  .top(5)
	  .where('PartitionKey eq ?', 'hometasks');

<!-- deleted by customization
## Delete an entity

You can delete an entity using its partition and row keys. In this example, the **task1** object contains the **RowKey** and **PartitionKey** values of the entity to be deleted. Then the object is passed to the **deleteEntity** method.
-->
<!-- keep by customization: begin -->
## How to Delete an Entity

You can delete an entity using its partition and row keys. In this 
example, the **task1** object contains the **RowKey** and
**PartitionKey** values of the entity to be deleted. Then the object is
passed to the **deleteEntity** method.
<!-- keep by customization: end -->

	var task = {
	  PartitionKey: {'_':'hometasks'},
	  RowKey: {'_': '1'}
	};

    tableSvc.deleteEntity('mytable', task, function(error, response){
	  if(!error) {
		// Entity deleted
	  }
	});

<!-- deleted by customization
> [AZURE.NOTE] Consider using ETags when deleting items, to ensure that the item hasn't been modified by another process. See [Update an entity](#update-an-entity) for information on using ETags.

## Delete a table
-->
<!-- keep by customization: begin -->
> [AZURE.NOTE] You should consider using ETags when deleting items, to ensure that the item hasn't been modified by another process. See [How To: Update an Entity][] for information in using ETags.

## How to Delete a Table
<!-- keep by customization: end -->

The following code deletes a table from a storage account.

    tableSvc.deleteTable('mytable', function(error, response){
		if(!error){
			// Table deleted
		}
	});

If you are uncertain whether the table exists, use **deleteTableIfExists**.

<!-- deleted by customization
## Use continuation tokens

When you are querying tables for large amounts of results, look for continuation tokens. There may be large amounts of data available for your query that you might not realize if you do not build to recognize when a
-->
<!-- keep by customization: begin -->
## How to: Use continuation tokens

When you are querying tables for large amounts of results, you should look for 
continuation tokens. There may be large amounts of data available for your 
query that you might not realize if you do not build to recognize when a 
<!-- keep by customization: end -->
continuation token is present.

<!-- deleted by customization
The results object returned during querying entities sets a `continuationToken` property when such a token is present. You can then use this when performing a query to continue to move across the partition and table entities.

When querying, a continuationToken parameter may be provided between the query object instance and the callback function:
-->
<!-- keep by customization: begin -->
The results object returned when querying entities sets a `continuationToken` 
property when such a token is present. You can then use this when performing 
a query to continue to move across the partition and table entities.

When querying, a continuationToken parameter may be provided between the 
query object instance and the callback function:
<!-- keep by customization: end -->

```
var nextContinuationToken = null;
dc.table.queryEntities(tableName,
    query,
    nextContinuationToken,
    function (error, results) {
        if (error) throw error;

        // iterate through results.entries with results

        if (results.continuationToken) {
            nextContinuationToken = results.continuationToken;
        }

    });
```

If you inspect the `continuationToken` object, you will find properties such as <!-- deleted by customization `nextPartitionKey`, `nextRowKey` and `targetLocation`, which can be used to iterate through all the results. -->
<!-- deleted by customization

There is also a continuation sample within the Azure Storage Node.js repo on GitHub. Look for `examples/samples/continuationsample.js`.

## Work with shared access signatures

Shared access signatures (SAS) are a secure way to provide granular access to tables without providing your storage account name or keys. SAS are often used to provide limited access to your data, such as allowing a mobile app to query records.

A trusted application such as a cloud-based service generates a SAS using the **generateSharedAccessSignature** of the **TableService**, and provides it to an untrusted or semi-trusted application such as<!-- keep by customization: begin -->. For example, <!-- keep by customization: end --> a mobile app. The SAS is generated using a policy, which describes the start and end dates during which the SAS is valid, as well as the access level granted to the SAS holder.
-->
<!-- keep by customization: begin -->
`nextPartitionKey`, `nextRowKey` and `targetLocation` which can be used to 
iterate through all the results.

There is also a continuation sample within the Azure Storage Node.js repo on 
GitHub, look for `examples/samples/continuationsample.js`.

## How to: Work with Shared Access Signatures

Shared Access Signatures (SAS) are a secure way to provide granular access to tables without providing your storage account name or keys. SAS are often used to provide limited access to your data, such as allowing a mobile app to query records.

A trusted application such as a cloud-based service generates a SAS using the **generateSharedAccessSignature** of the **TableService**, and provides it to an untrusted or semi-trusted application <!-- keep by customization: begin -->. For example, <!-- keep by customization: end --> a mobile app. The SAS is generated using a policy, which describes the start and end dates during which the SAS is valid, as well as the access level granted to the SAS holder.
<!-- keep by customization: end -->

The following example generates a new shared access policy that will allow the SAS holder to query ('r') the table, and expires 100 minutes after the time it is created.

	var startDate = new Date();
	var expiryDate = new Date(startDate);
	expiryDate.setMinutes(startDate.getMinutes() + 100);
	startDate.setMinutes(startDate.getMinutes() - 100);
	var sharedAccessPolicy = {
	  AccessPolicy: {
	    Permissions: azure.TableUtilities.SharedAccessPermissions.QUERY,
	    Start: startDate,
	    Expiry: expiryDate
	  },
	};

	var tableSAS = tableSvc.generateSharedAccessSignature('mytable', sharedAccessPolicy);
	var host = tableSvc.host;

Note that the host information must be provided also, as it is required when the SAS holder attempts to access the table.

The client application then uses the SAS with **TableServiceWithSAS** to perform operations against the table. The following example connects to the table and performs a query.

	var sharedTableService = azure.createTableServiceWithSas(host, tableSAS);
	var query = azure.TableQuery()
	  .where('PartitionKey eq ?', 'hometasks');
	sharedTableService.queryEntities(query, null, function(error, result, response) {
	  if(!error) {
		// result contains the entities
	  }
	});

Since the SAS was generated with only query access, if an attempt were made to insert, update, or delete entities, an error would be returned.

<!-- deleted by customization
### Access Control Lists
-->
<!-- keep by customization: begin -->
### Access control lists
<!-- keep by customization: end -->

You can also use an Access Control List (ACL) to set the access policy for a SAS. This is useful if you wish to allow multiple clients to access the table, but provide different access policies for each client.

An ACL is implemented using an array of access policies, with an ID associated with each policy. Thefollowing example defines two policies <!-- deleted by customization, --><!-- keep by customization: begin -->; <!-- keep by customization: end --> one for 'user1' and one for 'user2':

	var sharedAccessPolicy = [
	  {
	    AccessPolicy: {
	      Permissions: azure.TableUtilities.SharedAccessPermissions.QUERY,
	      Start: startDate,
	      Expiry: expiryDate
	    },
	    Id: 'user1'
	  },
	  {
	    AccessPolicy: {
	      Permissions: azure.TableUtilities.SharedAccessPermissions.ADD,
	      Start: startDate,
	      Expiry: expiryDate
	    },
	    Id: 'user2'
	  }
	];

The following example gets the current ACL for the **hometasks** table, <!-- deleted by customization and --> then adds the new policies using **setTableAcl**. This approach allows:

	tableSvc.getTableAcl('hometasks', function(error, result, response) {
      if(!error){
		//push the new policy into signedIdentifiers
		result.signedIdentifiers.push(sharedAccessPolicy);
		tableSvc.setTableAcl('hometasks', result, function(error, result, response){
	  	  if(!error){
	    	// ACL set
	  	  }
		});
	  }
	});

Once the ACL has been set, you can then create a SAS based on the ID for a policy. The following example creates a new SAS for 'user2':

	tableSAS = tableSvc.generateSharedAccessSignature('hometasks', { Id: 'user2' });

<!-- deleted by customization
## Next steps

For more information, see the following resources.

-   MSDN Reference: [Storing and accessing data in Azure][].
-   [Azure Storage Team Blog][].
-    [Azure Storage SDK for Node][] repository on GitHub.
-   [Node.js Developer Center](/develop/nodejs/)
-->
<!-- keep by customization: begin -->
## Next Steps

Now that you've learned the basics of table storage, follow these links
to learn how to do more complex storage tasks.

-   See the MSDN Reference: [Storing and Accessing Data in Azure][].
-   [Visit the Azure Storage Team Blog][].
-   Visit the [Azure Storage SDK for Node][] repository on GitHub.
<!-- keep by customization: end -->

  [Azure Storage SDK for Node]: https://github.com/Azure/azure-storage-node
  [OData.org]: http://www.odata.org/
<!-- deleted by customization
  [Using the REST API]: http://msdn.microsoft.com/zh-cn/library/azure/hh264518.aspx
-->
<!-- keep by customization: begin -->
  [using the REST API]: http://msdn.microsoft.com/zh-cn/library/azure/hh264518.aspx
<!-- keep by customization: end -->
  [Azure Management Portal]: http://manage.windowsazure.cn

  [Node.js Cloud Service]: /documentation/articles/cloud-services-nodejs-develop-deploy-app
<!-- deleted by customization
  [Storing and accessing data in Azure]: http://msdn.microsoft.com/zh-cn/library/azure/gg433040.aspx
  [Azure Storage Team Blog]: http://blogs.msdn.com/b/windowsazurestorage/
  [Website with WebMatrix]: /documentation/articles/web-sites-nodejs-use-webmatrix
-->
<!-- keep by customization: begin -->
  [Storing and Accessing Data in Azure]: http://msdn.microsoft.com/zh-cn/library/azure/gg433040.aspx
  [Visit the Azure Storage Team Blog]: http://blogs.msdn.com/b/windowsazurestorage/
  [ Website with WebMatrix]: /documentation/articles/web-sites-nodejs-use-webmatrix
<!-- keep by customization: end -->
  [Node.js Cloud Service with Storage]: /documentation/articles/storage-nodejs-use-table-storage-cloud-service-app
<!-- deleted by customization
  [Node.js web application with Storage]: /documentation/articles/storage-nodejs-use-table-storage-web-site
  [Create and deploy a Node.js application to an Azure website]: /documentation/articles/web-sites-nodejs-develop-deploy-mac
-->
<!-- keep by customization: begin -->
  [Node.js Web Application with Storage]: /documentation/articles/storage-nodejs-use-table-storage-web-site
  [Create and deploy a Node.js application to an Azure  Website]: /documentation/articles/web-sites-nodejs-develop-deploy-mac

<!-- keep by customization: end -->