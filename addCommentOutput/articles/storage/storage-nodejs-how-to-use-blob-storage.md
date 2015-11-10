<properties
	pageTitle="How to use Blob storage from Node.js | Windows Azure"
	description="Learn how to use the Azure Blob service to upload, download, list, and delete blob content. Samples are written in Node.js."
	services="storage"
	documentationCenter="nodejs"
	authors="MikeWasson"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="storage"
	ms.date="09/01/2015"
	wacn.date=""/>



# How to <!-- deleted by customization use --><!-- keep by customization: begin --> Use <!-- keep by customization: end --> Blob storage from Node.js

[AZURE.INCLUDE [storage-selector-blob-include](../includes/storage-selector-blob-include.md)]

## Overview

<!-- deleted by customization
This article shows you how to perform common scenarios using the Azure Blob service. The samples are written via the Node.js API. The scenarios covered include how to upload, list, download, and delete blobs.
-->
<!-- keep by customization: begin -->
This guide will show you how to perform common scenarios using the
Azure Blob service. The samples are written using the
Node.js API. The scenarios covered include **uploading**, **listing**,
**downloading**, and **deleting** blobs.
<!-- keep by customization: end -->

[AZURE.INCLUDE [storage-blob-concepts-include](../includes/storage-blob-concepts-include.md)]

[AZURE.INCLUDE [storage-create-account-include](../includes/storage-create-account-include.md)]

## Create a Node.js application

<!-- keep by customization: begin --> Create a blank Node.js application. <!-- keep by customization: end --> For instructions <!-- deleted by customization on how to create --><!-- keep by customization: begin --> creating <!-- keep by customization: end --> a Node.js application, see [Create and deploy a Node.js application to an Azure <!-- deleted by customization website] --><!-- keep by customization: begin --> Web Site] <!-- keep by customization: end -->, [Node.js Cloud Service][Node.js Cloud Service] (using Windows PowerShell), or [Web <!-- deleted by customization app --><!-- keep by customization: begin --> Site <!-- keep by customization: end --> with WebMatrix].

## Configure your application to access storage

To use Azure storage, you need the Azure Storage SDK for Node.js, which includes a set of convenience libraries that <!-- deleted by customization communicate with the storage REST services. -->
<!-- keep by customization: begin -->
communicate with the storage REST services.
<!-- keep by customization: end -->

### Use Node Package Manager (NPM) to obtain the package

1.  Use a command-line interface such as **PowerShell** <!-- deleted by customization (Windows), --><!-- keep by customization: begin --> (Windows,) <!-- keep by customization: end --> **Terminal** <!-- deleted by customization (Mac), --><!-- keep by customization: begin --> (Mac,) <!-- keep by customization: end --> or **Bash** (Unix), <!-- deleted by customization to --> navigate to the folder where you created your sample application.

<!-- deleted by customization
2.  Type **npm install azure-storage** in the command window. Output from the command is similar to the following code example.

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

3.  You can manually run the **ls** command to verify that a **node_modules** folder was created. Inside that folder, find the **azure-storage** package, which contains the libraries that you need to access storage.
-->
<!-- keep by customization: begin -->
2.  Type **npm install azure-storage** in the command window, which should
    result in the following output:

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
    **node_modules** folder was created. Inside that folder find the
    **azure-storage** package, which contains the libraries you need to access
    storage.
<!-- keep by customization: end -->

### Import the package

<!-- deleted by customization
Using Notepad or another text editor, add the following to the top of the **server.js** file of the application where you intend to use storage:
-->
<!-- keep by customization: begin -->
Using Notepad or another text editor, add the following to the top the
**server.js** file of the application where you intend to use storage:
<!-- keep by customization: end -->

    var azure = require('azure-storage');

<!-- deleted by customization
## Set up an Azure Storage connection

The Azure module will read the environment variables `AZURE_STORAGE_ACCOUNT` and `AZURE_STORAGE_ACCESS_KEY`, or `AZURE_STORAGE_CONNECTION_STRING` <!-- deleted by customization, --> for information required to connect to your Azure storage account. If these environment variables are not set, you must specify the account information when calling **createBlobService**.

For an example of setting the environment variables in the Azure Management Portal for an Azure web app, see [Node.js Web Application with Storage]

## Create a container

The **BlobService** object lets you work with containers and blobs. The following code creates a **BlobService** object. Add the following near the top of **server.js**:
-->
<!-- keep by customization: begin -->
## Setup an Azure storage connection

The azure module will read the environment variables `AZURE_STORAGE_ACCOUNT` and `AZURE_STORAGE_ACCESS_KEY`, or `AZURE_STORAGE_CONNECTION_STRING` <!-- deleted by customization, --> for information required to connect to your Azure storage account. If these environment variables are not set, you must specify the account information when calling **createBlobService**.

For an example of setting the environment variables in the management portal for an Azure  Website, see [Node.js Web Application with Storage]

## How to: create a container

The **BlobService** object lets you work with containers and blobs. The 
following code creates a **BlobService** object. Add the following near
the top of **server.js**:
<!-- keep by customization: end -->

    var blobSvc = azure.createBlobService();

> [AZURE.NOTE] You can access a blob anonymously by using **createBlobServiceAnonymous** and providing the host address. For example, <!-- deleted by customization use --> `var blobSvc = azure.createBlobServiceAnonymous('https://myblob.blob.core.chinacloudapi.cn/');`.

[AZURE.INCLUDE [storage-container-naming-rules-include](../includes/storage-container-naming-rules-include.md)]

<!-- deleted by customization
To create a new container, use **createContainerIfNotExists**. The following code example creates a new container named 'mycontainer':
-->
<!-- keep by customization: begin -->
To create a new container, use **createContainerIfNotExists**. The following creates a new container named 'mycontainer'
<!-- keep by customization: end -->

	blobSvc.createContainerIfNotExists('mycontainer', function(error, result, response){
      if(!error){
        // Container exists and allows
        // anonymous read access to blob
        // content and metadata within this container
      }
	});

<!-- deleted by customization
If the container is newly created, `result` is true. If the container already exists, `result` is false. `response` contains information about the operation, including the [ETag](http://en.wikipedia.org/wiki/HTTP_ETag) information for the container.

### Container security

By default, new containers are private and cannot be accessed anonymously. To make the container public so that you can access it anonymously, you can set the container's access level to **blob** or **container**.

* **blob** - allows anonymous read access to blob content and metadata within this container, but not to container metadata such as listing all blobs within a container <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **container** - allows anonymous read access to blob content and metadata as well as container metadata <!-- keep by customization: begin -->. <!-- keep by customization: end -->

The following code example demonstrates setting the access level to **blob**:
-->
<!-- keep by customization: begin -->
If the container is created, `result` will be true. If the container already exists, `result` will be false. `response` will contain information about the operation, including the [ETag](http://en.wikipedia.org/wiki/HTTP_ETag) information for the container.

###Container security

By default, new containers are private and cannot be accessed anonymously. To make the container public so that they can be accessed anonymously, you can set the container's access level to **blob** or **container**.

* **blob** - allows anonymous read access to blob content and metadata within this container, but not to container metadata such as listing all blobs within a container <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **container** - allows anonymous read access to blob content and metadata as well as container metadata <!-- keep by customization: begin -->. <!-- keep by customization: end -->

The following  example demonstrates setting the access level to **blob**:
<!-- keep by customization: end -->

    blobSvc.createContainerIfNotExists('mycontainer', {publicAccessLevel : 'blob'}, function(error, result, response){
      if(!error){
        // Container exists and is private
      }
	});

Alternatively, you can modify the access level of a container by using **setContainerAcl** to specify the access level. The following <!-- deleted by customization code --> example changes the access level to container:

    blobSvc.setContainerAcl('mycontainer', null /* signedIdentifiers */, 'container' /* publicAccessLevel*/, function(error, result, response){
	  if(!error){
		// Container access level set to 'container'
	  }
	});

The result <!-- deleted by customization contains --><!-- keep by customization: begin --> will contain <!-- keep by customization: end --> information about the operation, including the current **ETag** for the container.

### Filters

<!-- deleted by customization You can apply optional --><!-- keep by customization: begin --> Optional <!-- keep by customization: end --> filtering operations <!-- keep by customization: begin --> can be applied <!-- keep by customization: end --> to operations performed using **BlobService**. Filtering operations can include logging, automatically retrying, etc. Filters are objects that implement a method with the signature:

		function handle (requestOptions, next)

After doing its preprocessing on the request options, the method needs to call "next" <!-- deleted by customization, --> passing a callback with the following signature:

		function (returnObject, finalCallback, next)

In this callback, and after processing the returnObject (the response from the request to the server), the callback needs to either invoke next if it exists to continue processing other filters or simply invoke finalCallback to end the service invocation.

Two filters that implement retry logic are included with the Azure SDK for Node.js, **ExponentialRetryPolicyFilter** and **LinearRetryPolicyFilter**. The following creates a **BlobService** object that uses the **ExponentialRetryPolicyFilter**:

	var retryOperations = new azure.ExponentialRetryPolicyFilter();
	var blobSvc = azure.createBlobService().withFilter(retryOperations);

## <!-- keep by customization: begin --> How to: <!-- keep by customization: end --> Upload a blob into a container

A blob can be either <!-- deleted by customization block-based --><!-- keep by customization: begin --> block, <!-- keep by customization: end --> or <!-- deleted by customization page-based --><!-- keep by customization: begin --> page based <!-- keep by customization: end -->. Block blobs allow you to more efficiently upload large data, while page blobs are optimized for read/write operations. For more information, see [Understanding block blobs and page blobs](http://msdn.microsoft.com/zh-cn/library/azure/ee691964.aspx).

### Block blobs

To upload data to a block blob, use the following:

* **createBlockBlobFromLocalFile** - creates a new block blob and uploads the contents of a file <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **createBlockBlobFromStream** - creates a new block blob and uploads the contents of a stream <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **createBlockBlobFromText** - creates a new block blob and uploads the contents of a string <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **createWriteStreamToBlockBlob** - provides a write stream to a block blob <!-- keep by customization: begin -->. <!-- keep by customization: end -->

The following <!-- deleted by customization code --> example uploads the contents of the **test.txt** file into **myblob**.

	blobSvc.createBlockBlobFromLocalFile('mycontainer', 'myblob', 'test.txt', function(error, result, response){
	  if(!error){
	    // file uploaded
	  }
	});

The `result` returned by these methods <!-- deleted by customization contains --><!-- keep by customization: begin --> will contain <!-- keep by customization: end --> information on the operation, such as the **ETag** of the blob.

### Page blobs

To upload data to a page blob, use the following:

* **createPageBlob** - creates a new page blob of a specific length <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **createPageBlobFromLocalFile** - creates a new page blob and uploads the contents of a file <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **createPageBlobFromStream** - creates a new page blob and uploads the contents of a stream <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **createWriteStreamToExistingPageBlob** - provides a write stream to an existing page blob <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **createWriteStreamToNewPageBlob** - creates a new blob and then provides a stream to write to it <!-- keep by customization: begin -->. <!-- keep by customization: end -->

The following <!-- deleted by customization code --> example uploads the contents of the **test.txt** file into **mypageblob**.

	blobSvc.createPageBlobFromLocalFile('mycontainer', 'mypageblob', 'test.txt', function(error, result, response){
	  if(!error){
	    // file uploaded
	  }
	});

> [AZURE.NOTE] Page blobs consist of 512-byte 'pages'. You may receive an error when uploading data with a size that is not a multiple of 512.

## <!-- keep by customization: begin --> How to: <!-- keep by customization: end --> List the blobs in a container

To list the blobs in a container, use the **listBlobsSegmented** method. If <!-- deleted by customization you'd --><!-- keep by customization: begin --> you would <!-- keep by customization: end --> like to return blobs with a specific prefix, use **listBlobsSegmentedWithPrefix**.

    blobSvc.listBlobsSegmented('mycontainer', null, function(error, result, response){
      if(!error){
<!-- deleted by customization
        // result.entries contains the entries
        // If not all blobs were returned, result.continuationToken has the continuation token.
-->
<!-- keep by customization: begin -->
        // result contains the entries
<!-- keep by customization: end -->
	  }
	});

<!-- deleted by customization
The `result` contains an `entries` collection, which is an array of objects that describe each blob. If all blobs cannot be returned, the `result` also provides a `continuationToken`, which you may use as the second parameter to retrieve additional entries.

## Download blobs
-->
<!-- keep by customization: begin -->
The `result` will contain an `entries` collection, which is an array of objects describing each blob. If all blobs cannot be returned, the `result` will also provide a `continuationToken`, which may be used as the second parameter to retrieve additional entries.

## How to: Download blobs
<!-- keep by customization: end -->

To download data from a blob, use the following:

* **getBlobToFile** - writes the blob contents to file

* **getBlobToStream** - writes the blob contents to a stream <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **getBlobToText** - writes the blob contents to a string <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **createReadStream** - provides a stream to read from the blob

The following <!-- deleted by customization code --> example demonstrates using **getBlobToStream** to download the contents of the **myblob** blob and store it to the **output.txt** file <!-- deleted by customization by --> using a stream:

    var fs = require('fs');
	blobSvc.getBlobToStream('mycontainer', 'myblob', fs.createWriteStream('output.txt'), function(error, result, response){
	  if(!error){
	    // blob retrieved
	  }
	});

The `result` <!-- deleted by customization contains --><!-- keep by customization: begin --> will contain <!-- keep by customization: end --> information about the blob, including **ETag** information.

<!-- deleted by customization
## Delete a blob

Finally, to delete a blob, call **deleteBlob**. The following code example deletes the blob named **myblob**.
-->
<!-- keep by customization: begin -->
## How to: Delete a blob

Finally, to delete a blob, call **deleteBlob**. The following  example deletes the blob named **myblob**.
<!-- keep by customization: end -->

    blobSvc.deleteBlob(containerName, 'myblob', function(error, response){
	  if(!error){
		// Blob has been deleted
	  }
	});

<!-- deleted by customization
## Concurrent access
-->
<!-- keep by customization: begin -->
## How to: Concurrent access
<!-- keep by customization: end -->

To support concurrent access to a blob from multiple clients or multiple process instances, you can use **ETags** or **leases**.

* **Etag** - provides a way to detect that the blob or container has been modified by another process <!-- keep by customization: begin -->. <!-- keep by customization: end -->

* **Lease** - provides a way to obtain exclusive, renewable, write or delete access to a blob for a period of time <!-- keep by customization: begin -->. <!-- keep by customization: end -->

### ETag

<!-- deleted by customization Use --> ETags <!-- keep by customization: begin --> should be used <!-- keep by customization: end --> if you need to allow multiple clients or instances to write to the blob simultaneously. The ETag allows you to determine if the container or blob <!-- deleted by customization was --><!-- keep by customization: begin --> has been <!-- keep by customization: end --> modified since you initially read or created it, which allows you to avoid overwriting changes committed by another client or process.

<!-- deleted by customization
You can set ETag conditions by using the optional `options.accessConditions` parameter. The following code example only uploads the **test.txt** file if the blob already exists and has the ETag value contained by `etagToMatch`.
-->
<!-- keep by customization: begin -->
ETag conditions can be set using the optional `options.accessConditions` parameter. The following example will only upload the **test.txt** file if the blob already exists and has the ETag value contained by `etagToMatch`.
<!-- keep by customization: end -->

	blobSvc.createBlockBlobFromLocalFile('mycontainer', 'myblob', 'test.txt', { accessConditions: { 'if-match': etagToMatch} }, function(error, result, response){
      if(!error){
	    // file uploaded
	  }
	});

<!-- deleted by customization
When you're using ETags, the general pattern is:
-->
<!-- keep by customization: begin -->
The general pattern when using ETags is:
<!-- keep by customization: end -->

1. Obtain the ETag as the result of a create, list, or get operation.

2. Perform an action, checking that the ETag value has not been modified.

If the value <!-- deleted by customization was --><!-- keep by customization: begin --> has been <!-- keep by customization: end --> modified, this indicates that another client or instance <!-- keep by customization: begin --> has <!-- keep by customization: end --> modified the blob or container since you obtained the ETag value.

### Lease

<!-- deleted by customization You can acquire a --><!-- keep by customization: begin --> A <!-- keep by customization: end --> new lease <!-- deleted by customization by --><!-- keep by customization: begin --> can be acquired <!-- keep by customization: end --> using the **acquireLease** method, specifying the blob or container that you wish to obtain a lease on. For example, the following <!-- deleted by customization code --> acquires a lease on **myblob**.

	blobSvc.acquireLease('mycontainer', 'myblob', function(error, result, response){
	  if(!error) {
	    console.log('leaseId: ' + result.id);
	  }
	});

Subsequent operations on **myblob** must provide <!-- deleted by customization the --> `options.leaseId` parameter. The lease ID is returned as `result.id` from **acquireLease**.

> [AZURE.NOTE] By default, the lease duration is infinite. You can specify a non-infinite duration (between 15 and 60 <!-- deleted by customization seconds) --><!-- keep by customization: begin --> seconds,) <!-- keep by customization: end --> by providing the `options.leaseDuration` parameter.

To remove a lease, use **releaseLease**. To break a lease, but prevent others from obtaining a new lease until the original duration has expired, use **breakLease**.

## <!-- keep by customization: begin --> How to: <!-- keep by customization: end --> Work with shared access signatures

Shared <!-- deleted by customization access signatures --><!-- keep by customization: begin --> Access Signatures <!-- keep by customization: end --> (SAS) are a secure way to provide granular access to blobs and containers without providing your storage account name or keys. <!-- deleted by customization Shared access signatures --><!-- keep by customization: begin --> SAS <!-- keep by customization: end --> are often used to provide limited access to your data, such as allowing a mobile app to access blobs.

> [AZURE.NOTE] While you can also allow anonymous access to blobs, <!-- deleted by customization shared access signatures allow --><!-- keep by customization: begin --> SAS allows <!-- keep by customization: end --> you to provide more controlled access, as you must generate the SAS.

A trusted application such as a cloud-based service generates <!-- deleted by customization shared access signatures --><!-- keep by customization: begin --> a SAS <!-- keep by customization: end --> using the **generateSharedAccessSignature** of the **BlobService**, and provides it to an untrusted or semi-trusted application <!-- deleted by customization such as --><!-- keep by customization: begin -->. For example, <!-- keep by customization: end --> a mobile app. <!-- deleted by customization Shared access signatures are --><!-- keep by customization: begin --> The SAS is <!-- keep by customization: end --> generated using a policy, which describes the start and end dates during which the <!-- deleted by customization shared access signatures are --><!-- keep by customization: begin --> SAS is <!-- keep by customization: end --> valid, as well as the access level granted to the <!-- deleted by customization shared access signatures --><!-- keep by customization: begin --> SAS <!-- keep by customization: end --> holder.

The following <!-- deleted by customization code --> example generates a new shared access policy that <!-- deleted by customization allows --><!-- keep by customization: begin --> will allow <!-- keep by customization: end --> the <!-- deleted by customization shared access signatures --><!-- keep by customization: begin --> SAS <!-- keep by customization: end --> holder to perform read operations on the **myblob** blob, and expires 100 minutes after the time it is created.

	var startDate = new Date();
	var expiryDate = new Date(startDate);
	expiryDate.setMinutes(startDate.getMinutes() + 100);
	startDate.setMinutes(startDate.getMinutes() - 100);
	var sharedAccessPolicy = {
	  AccessPolicy: {
	    Permissions: azure.BlobUtilities.SharedAccessPermissions.READ,
	    Start: startDate,
	    Expiry: expiryDate
	  },
	};
	var blobSAS = blobSvc.generateSharedAccessSignature('mycontainer', 'myblob', sharedAccessPolicy);
	var host = blobSvc.host;

Note that the host information must be provided also, as it is required when the <!-- deleted by customization shared access signatures --><!-- keep by customization: begin --> SAS <!-- keep by customization: end --> holder attempts to access the container.

The client application then uses <!-- deleted by customization shared access signatures --><!-- keep by customization: begin --> the SAS <!-- keep by customization: end --> with **BlobServiceWithSAS** to perform operations against the blob. The following gets information about **myblob**.

	var sharedBlobSvc = azure.createBlobServiceWithSas(host, blobSAS);
	sharedBlobSvc.getBlobProperties('mycontainer', 'myblob', function (error, result, response) {
	  if(!error) {
	    // retrieved info
	  }
	});

<!-- deleted by customization
Since the shared access signatures were generated with read-only access, if an attempt is made to modify the blob, an error will be returned.
-->
<!-- keep by customization: begin -->
Since the SAS was generated with only read access, if an attempt were made to modify the blob, an error would be returned.
<!-- keep by customization: end -->

### Access control lists

You can also use an <!-- deleted by customization access control list --><!-- keep by customization: begin --> Access Control List <!-- keep by customization: end --> (ACL) to set the access policy for <!-- keep by customization: begin --> a <!-- keep by customization: end --> SAS. This is useful if you wish to allow multiple clients to access a container <!-- keep by customization: begin -->, <!-- keep by customization: end --> but provide different access policies for each client.

An ACL is implemented using an array of access policies, with an ID associated with each policy. Thefollowing <!-- deleted by customization code --> example defines two policies <!-- deleted by customization, --><!-- keep by customization: begin -->; <!-- keep by customization: end --> one for 'user1' and one for 'user2':

	var sharedAccessPolicy = [
	  {
	    AccessPolicy: {
	      Permissions: azure.BlobUtilities.SharedAccessPermissions.READ,
	      Start: startDate,
	      Expiry: expiryDate
	    },
	    Id: 'user1'
	  },
	  {
	    AccessPolicy: {
	      Permissions: azure.BlobUtilities.SharedAccessPermissions.WRITE,
	      Start: startDate,
	      Expiry: expiryDate
	    },
	    Id: 'user2'
	  }
	];

The following <!-- deleted by customization code --> example gets the current ACL for **mycontainer**, <!-- deleted by customization and --> then adds the new policies using **setBlobAcl**. This approach allows:

	blobSvc.getBlobAcl('mycontainer', function(error, result, response) {
      if(!error){
		//push the new policy into signedIdentifiers
		result.signedIdentifiers.push(sharedAccessPolicy);
		blobSvc.setBlobAcl('mycontainer', result, function(error, result, response){
	  	  if(!error){
	    	// ACL set
	  	  }
		});
	  }
	});

<!-- deleted by customization
Once the ACL is set, you can then create shared access signatures based on the ID for a policy. The following code example creates new shared access signatures for 'user2':
-->
<!-- keep by customization: begin -->
Once the ACL has been set, you can then create a SAS based on the ID for a policy. The following example creates a new SAS for 'user2':
<!-- keep by customization: end -->

	blobSAS = blobSvc.generateSharedAccessSignature('mycontainer', { Id: 'user2' });

## Next steps

<!-- deleted by customization
For more information, see the following resources.

-    [Azure Storage SDK for Node API Reference][]
-   MSDN Reference: [Storing and accessing data in Azure][]
-   [Azure Storage Team Blog][]
-    [Azure Storage SDK for Node][] repository on GitHub <!-- keep by customization: begin -->. <!-- keep by customization: end -->
-   [Node.js Developer Center](/develop/nodejs/)
-->
<!-- keep by customization: begin -->
Now that you've learned the basics of blob storage, follow these links
to learn how to do more complex storage tasks.

-   Read the [Azure Storage SDK for Node API Reference][]
-   See the MSDN Reference: [Storing and Accessing Data in Azure][].
-   Visit the [Azure Storage Team Blog][].
-   Visit the [Azure Storage SDK for Node][] repository on GitHub <!-- keep by customization: begin -->. <!-- keep by customization: end -->
<!-- keep by customization: end -->

[Azure Storage SDK for Node]: https://github.com/Azure/azure-storage-node
[Create and deploy a Node.js application to an Azure Web Site]: <!-- deleted by customization /develop/nodejs/tutorials/create-a-website-(mac)/ --><!-- keep by customization: begin --> /documentation/articles/web-sites-nodejs-develop-deploy-mac <!-- keep by customization: end -->
[Node.js Cloud Service with Storage]: /documentation/articles/storage-nodejs-use-table-storage-cloud-service-app
[Node.js Web Application with Storage]: /documentation/articles/storage-nodejs-use-table-storage-web-site
<!-- deleted by customization
[Web app with WebMatrix]: /documentation/articles/web-sites-nodejs-use-webmatrix
[Using the REST API]: http://msdn.microsoft.com/zh-cn/library/azure/hh264518.aspx
-->
<!-- keep by customization: begin -->
[Web Site with WebMatrix]: /documentation/articles/web-sites-nodejs-use-webmatrix
[using the REST API]: http://msdn.microsoft.com/zh-cn/library/azure/hh264518.aspx
<!-- keep by customization: end -->
[Azure Management Portal]: http://manage.windowsazure.cn
[Node.js Cloud Service]: /documentation/articles/cloud-services-nodejs-develop-deploy-app
<!-- deleted by customization
[Storing and accessing data in Azure]: http://msdn.microsoft.com/zh-cn/library/azure/gg433040.aspx
-->
<!-- keep by customization: begin -->
[Storing and Accessing Data in Azure]: http://msdn.microsoft.com/zh-cn/library/azure/gg433040.aspx
<!-- keep by customization: end -->
[Azure Storage Team Blog]: http://blogs.msdn.com/b/windowsazurestorage/
[Azure Storage SDK for Node API Reference]: http://dl.windowsazure.cn/nodestoragedocs/index.html