<properties
	pageTitle="Get started with blob storage and Visual Studio connected services (cloud services) | Windows Azure"
	description="How to get started using Azure Blob storage in a cloud service project in Visual Studio after connecting to a storage account using Visual Studio connected services"
	services="storage"
	documentationCenter=""
	authors="patshea123"
	manager="douge"
	editor="tglee"/>

<tags
	ms.service="storage"
	ms.date="09/03/2015"
	wacn.date=""/>

# Get started with Azure Blob Storage and Visual Studio connected services (cloud services projects)

> [AZURE.SELECTOR]
> - [Getting started](/documentation/articles/vs-storage-cloud-services-getting-started-blobs)
> - [What happened](/documentation/articles/vs-storage-cloud-services-what-happened)
<!-- deleted by customization

> [AZURE.SELECTOR]
-->
> - [Blobs](/documentation/articles/vs-storage-cloud-services-getting-started-blobs)
> - [Queues](/documentation/articles/vs-storage-cloud-services-getting-started-queues)
> - [Tables](/documentation/articles/vs-storage-cloud-services-getting-started-tables)

<!-- deleted by customization
## Overview

This article describes how to get started with Azure Blob Storage after you created or referenced an Azure Storage account by using the Visual Studio **Add Connected Services** dialog in a Visual Studio cloud services project. We'll show you how to access and create blob containers, and how to perform common tasks like uploading, listing, and downloading blobs. The samples are written in C\# and use the [Azure Storage Client Library for .NET](https://msdn.microsoft.com/zh-cn/library/azure/dn261237.aspx).

Azure Blob Storage is a service for storing large amounts of unstructured data that can be accessed from anywhere in the world via HTTP or HTTPS. A single blob can be any size. Blobs can be things like images, audio and video files, raw data, and document files.
-->
<!-- keep by customization: begin -->
##Overview

This article describes how to get started with Azure blob storage after you created or referenced an Azure storage account by using the Visual Studio **Add Connected Services** dialog in a Visual Studio cloud services project. We'll show you how to access and create blob containers, and how to perform common tasks like uploading, listing, and downloading blobs. The samples are written in C\# and use the [Azure Storage Client Library for .NET](https://msdn.microsoft.com/zh-cn/library/azure/dn261237.aspx).

Azure Blob storage is a service for storing large amounts of unstructured data that can be accessed from anywhere in the world via HTTP or HTTPS. A single blob can be any size. Blobs can be things like images, audio and video files, raw data, and document files.
<!-- keep by customization: end -->

Just as files live in folders, storage blobs live in containers. After you have created a storage, you create one or more containers in the storage. For example, in a storage called “Scrapbook,” you can create containers in the storage called “images” to store pictures and another called “audio” to store audio files. After you create the containers, you can upload individual blob files to them.

<!-- deleted by customization
- For more information on programmatically manipulating blobs, see [How to use blob storage from .NET](/documentation/articles/storage-dotnet-how-to-use-blobs).
- For general information about Azure Storage,see [Storage documentation](/documentation/services/storage/).
- For general information about Azure Cloud Services, see [Cloud Services documentation](/documentation/services/cloud-services/).
- For more information about programming ASP.NET applications, see [ASP.NET](http://www.asp.net).

## Access blob containers in code

To programmatically access blobs in cloud service projects, you need to add the following items, if they're not already present.
-->
<!-- keep by customization: begin -->
- See [How to use Blob Storage from .NET](/documentation/articles/storage-dotnet-how-to-use-blobs) for more information on programmatically manipulating blobs.
- See [Storage documentation](http://www.windowsazure.cn/documentation/services/storage/) for general information about Azure Storage.
- See [Cloud Services documentation](http://www.windowsazure.cn/documentation/services/cloud-services/) for general information about Azure cloud services.
- See [ASP.NET](http://www.asp.net) for more information about programming ASP.NET applications.

##Access blob containers in code

To programmatically access blobs in Cloud Service projects, you need to add the following items, if they're not already present.
<!-- keep by customization: end -->

1. Add the following code namespace declarations to the top of any C# file in which you wish to programmatically access Azure Storage.

        using Microsoft.Framework.Configuration;
        using Microsoft.WindowsAzure.Storage;
        using Microsoft.WindowsAzure.Storage.Blob;
        using System.Threading.Tasks;
        using LogLevel = Microsoft.Framework.Logging.LogLevel;

2. Get a <!-- deleted by customization **CloudStorageAccount** --><!-- keep by customization: begin --> `CloudStorageAccount` <!-- keep by customization: end --> object that <!-- deleted by customization represents --><!-- keep by customization: begin --> represent <!-- keep by customization: end --> your storage account information. Use the following code to get the your storage connection string and storage account information from the Azure service configuration.

        CloudStorageAccount storageAccount = CloudStorageAccount.Parse(
        CloudConfigurationManager.GetSetting("<storage account name>_AzureStorageConnectionString"));

<!-- deleted by customization
3. Get a **CloudBlobClient** object to reference an existing container in your storage account.
-->
<!-- keep by customization: begin -->

3. Get a `CloudBlobClient` object to reference an existing container in your storage account.
<!-- keep by customization: end -->

		// Create a blob client.
		CloudBlobClient blobClient = storageAccount.CreateCloudBlobClient();

4. Get a <!-- deleted by customization **CloudBlobContainer** --><!-- keep by customization: begin --> `CloudBlobContainer` <!-- keep by customization: end --> object to reference a specific blob container.

        // Get a reference to a container named “mycontainer.”
        CloudBlobContainer container = blobClient.GetContainerReference("mycontainer");

> [AZURE.NOTE] Use all of the code shown in the previous procedure in front of the code shown in the following sections.

<!-- deleted by customization
## Create a container in code

> [AZURE.NOTE] Some APIs that perform calls out to Azure Storage in ASP.NET are asynchronous. See [Asynchronous programming with Async and Await](http://msdn.microsoft.com/zh-cn/library/hh191443.aspx) for more information. The code in the following example assumes that you are using async programming methods.

To create a container in your storage account, all you need to do is add a call to **CreateIfNotExistsAsync** as in the following code:
-->
<!-- keep by customization: begin -->
##Create a container in code

**NOTE:** Some APIs that perform calls out to Azure storage in ASP.NET are asynchronous. See [Asynchronous Programming with Async and Await](http://msdn.microsoft.com/zh-cn/library/hh191443.aspx) for more information. The code below assumes that your are using async programming methods.

To create a container in your storage account, all you need to do is add a call to `CreateIfNotExistsAsync` as in the following code:
<!-- keep by customization: end -->

	// Get a reference to a CloudBlobContainer with the variable name 'container'
    // as described in the "Access blob containers in code" section.

    // If “mycontainer” doesn’t exist, create it.
    await container.CreateIfNotExistsAsync();


To make the files within the container available to everyone, you can set the container to be public by using the following code.

	await container.SetPermissionsAsync(new BlobContainerPermissions
    {
        PublicAccess = BlobContainerPublicAccessType.Blob
    });


Anyone on the Internet can see blobs in a public container, but you can
modify or delete them only if you have the appropriate access key.

## Upload a blob into a container

Azure Storage supports block blobs and page blobs. In the majority of cases, block blob is the recommended type to use.

To upload a file to a block blob, get a container reference and use it to get a block blob reference. Once you have a blob reference, you can upload any stream of data to it by calling the **UploadFromStream** method. This operation creates the blob if it didn't previously exist, or overwrites it if it does exist. The following example shows how to upload a blob into a container and assumes that the container was already created.

	// Get a reference to a CloudBlobContainer with the variable name 'container' as described in
    // the "Access blob containers in code" section.

    // Retrieve a reference to a blob named "myblob".
    CloudBlockBlob blockBlob = container.GetBlockBlobReference("myblob");

    // Create or overwrite the "myblob" blob with contents from a local file.
    using (var fileStream = System.IO.File.OpenRead(@"path\myfile"))
    {
        blockBlob.UploadFromStream(fileStream);
    }

## List the blobs in a container

To list the blobs in a container, first get a container reference. You can then use the container's **ListBlobs** method to retrieve the blobs and/or directories within it. To access the rich set of properties and methods for a  returned **IListBlobItem**, you must cast it to a **CloudBlockBlob**, **CloudPageBlob**, or **CloudBlobDirectory** object. If the type is unknown, you can use a type check to determine which to cast it to. The following code demonstrates how to retrieve and output the URI of each item in the **photos** container:

	// Get a reference to a CloudBlobContainer with the variable name 'container' as described in
    // the "Access blob containers in code" section.
	// Loop over items within the container and output the length and URI.
	foreach (IListBlobItem item in container.ListBlobs(null, false))
	{
		if (item.GetType() == typeof(CloudBlockBlob))
		{
			CloudBlockBlob blob = (CloudBlockBlob)item;

			Console.WriteLine("Block blob of length {0}: {1}", blob.Properties.Length, blob.Uri);
		}
		else if (item.GetType() == typeof(CloudPageBlob))
		{
			CloudPageBlob pageBlob = (CloudPageBlob)item;

			Console.WriteLine("Page blob of length {0}: {1}", pageBlob.Properties.Length, pageBlob.Uri);

		}
		else if (item.GetType() == typeof(CloudBlobDirectory))
		{
			CloudBlobDirectory directory = (CloudBlobDirectory)item;
			Console.WriteLine("Directory: {0}", directory.Uri);
		}
	}

As shown in the previous code sample, the blob service has the concept of directories within containers, as well. This is so that you can organize your blobs in a more folder-like structure. For example, consider the following set of block blobs in a container named **photos**:

	photo1.jpg
	2010/architecture/description.txt
	2010/architecture/photo3.jpg
	2010/architecture/photo4.jpg
	2011/architecture/photo5.jpg
	2011/architecture/photo6.jpg
	2011/architecture/description.txt
	2011/photo7.jpg

When you call **ListBlobs** on the container (as in the previous sample), the collection returned
contains **CloudBlobDirectory** and **CloudBlockBlob** objects representing the directories and blobs contained at the top level. Here is the resulting output:

	Directory: https://<accountname>.blob.core.chinacloudapi.cn/photos/2010/
	Directory: https://<accountname>.blob.core.chinacloudapi.cn/photos/2011/
	Block blob of length 505623: https://<accountname>.blob.core.chinacloudapi.cn/photos/photo1.jpg


<!-- deleted by customization
Optionally, you can set the **UseFlatBlobListing** parameter of of the **ListBlobs** method to
**true**. This results in every blob being returned as a **CloudBlockBlob**, regardless of directory. Here is the call to **ListBlobs**:
-->
<!-- keep by customization: begin -->
Optionally, you can set the `UseFlatBlobListing` parameter of of the `ListBlobs` method to 
`true`. This would result in every blob being returned as a `CloudBlockBlob`, regardless of directory.  Here would be the call to `ListBlobs`:
<!-- keep by customization: end -->

    // Loop over items within the container and output the length and URI.
	foreach (IListBlobItem item in container.ListBlobs(null, true))
	{
	   ...
	}

and here are the results:

	Block blob of length 4: https://<accountname>.blob.core.chinacloudapi.cn/photos/2010/architecture/description.txt
	Block blob of length 314618: https://<accountname>.blob.core.chinacloudapi.cn/photos/2010/architecture/photo3.jpg
	Block blob of length 522713: https://<accountname>.blob.core.chinacloudapi.cn/photos/2010/architecture/photo4.jpg
	Block blob of length 4: https://<accountname>.blob.core.chinacloudapi.cn/photos/2011/architecture/description.txt
	Block blob of length 419048: https://<accountname>.blob.core.chinacloudapi.cn/photos/2011/architecture/photo5.jpg
	Block blob of length 506388: https://<accountname>.blob.core.chinacloudapi.cn/photos/2011/architecture/photo6.jpg
	Block blob of length 399751: https://<accountname>.blob.core.chinacloudapi.cn/photos/2011/photo7.jpg
	Block blob of length 505623: https://<accountname>.blob.core.chinacloudapi.cn/photos/photo1.jpg

For more information, see [CloudBlobContainer.ListBlobs][].

## Download blobs

To download blobs, first retrieve a blob reference and then call the <!-- deleted by customization **DownloadToStream** --><!-- keep by customization: begin --> `DownloadToStream` <!-- keep by customization: end --> method. The following
example uses the <!-- deleted by customization **DownloadToStream** --><!-- keep by customization: begin --> `DownloadToStream` <!-- keep by customization: end --> method to transfer the blob
contents to a stream object that you can then persist to a local file.

	// Get a reference to a CloudBlobContainer with the variable name 'container' as described in
    // the "Access blob containers in code" section.

    // Get a reference to a blob named "photo1.jpg".
    CloudBlockBlob blockBlob = container.GetBlockBlobReference("photo1.jpg");

    // Save blob contents to a file.
    using (var fileStream = System.IO.File.OpenWrite(@"path\myfile"))
    {
        blockBlob.DownloadToStream(fileStream);
    }

You can also use the <!-- deleted by customization **DownloadToStream** --><!-- keep by customization: begin --> `DownloadToStream` <!-- keep by customization: end --> method to download the contents of a blob as a text string.

	// Get a reference to a CloudBlobContainer with the variable name 'container' as described in
    // the "Access blob containers in code" section.

	// Get a reference to a blob named "myblob.txt"
	CloudBlockBlob blockBlob2 = container.GetBlockBlobReference("myblob.txt");

	string text;
	using (var memoryStream = new MemoryStream())
	{
		blockBlob2.DownloadToStream(memoryStream);
		text = System.Text.Encoding.UTF8.GetString(memoryStream.ToArray());
	}

## Delete blobs

To delete a blob, first get a blob reference and then call the
<!-- deleted by customization
**Delete** method.
-->
<!-- keep by customization: begin -->
`Delete` method.
<!-- keep by customization: end -->

	// Get a reference to a CloudBlobContainer with the variable name 'container' as described in
    // the "Access blob containers in code" section.

    // Get a reference to a blob named "myblob.txt".
    CloudBlockBlob blockBlob = container.GetBlockBlobReference("myblob.txt");

    // Delete the blob.
    blockBlob.Delete();


## List blobs in pages asynchronously

If you are listing a large number of blobs, or you want to control the number of results you return in one listing operation, you can list blobs in pages of results. This example shows how to return results in pages asynchronously, so that execution is not blocked while waiting to return a large set of results.

<!-- deleted by customization
This example shows a flat blob listing, but you can also perform a hierarchical listing, by setting the **useFlatBlobListing** parameter of the **ListBlobsSegmentedAsync** method to **false**.

Because the sample method calls an asynchronous method, it must be prefaced with the **async** keyword, and it must return a **Task** object. The await keyword specified for the **ListBlobsSegmentedAsync** method suspends execution of the sample method until the listing task completes.
-->
<!-- keep by customization: begin -->
This example shows a flat blob listing, but you can also perform a hierarchical listing, by setting the `useFlatBlobListing` parameter of the `ListBlobsSegmentedAsync` method to `false`.

Because the sample method calls an asynchronous method, it must be prefaced with the `async` keyword, and it must return a `Task` object. The await keyword specified for the `ListBlobsSegmentedAsync` method suspends execution of the sample method until the listing task completes.
<!-- keep by customization: end -->

    async public static Task ListBlobsSegmentedInFlatListing(CloudBlobContainer container)
    {
        <!-- deleted by customization // List --><!-- keep by customization: begin --> //List <!-- keep by customization: end --> blobs to the console window, with paging.
        Console.WriteLine("List blobs in pages:");

        int i = 0;
        BlobContinuationToken continuationToken = null;
        BlobResultSegment resultSegment = null;

        <!-- deleted by customization // Call --><!-- keep by customization: begin --> //Call <!-- keep by customization: end --> ListBlobsSegmentedAsync and enumerate the result segment returned, while the continuation token is non-null.
        <!-- deleted by customization // When --><!-- keep by customization: begin --> //When <!-- keep by customization: end --> the continuation token is null, the last page has been returned and execution can exit the loop.
        do
        {
            <!-- deleted by customization // This --><!-- keep by customization: begin --> //This <!-- keep by customization: end --> overload allows control of the page size. You can return all remaining results by passing null for the maxResults parameter,
<!-- deleted by customization
            // or by calling a different overload.
-->
<!-- keep by customization: begin -->
            //or by calling a different overload.
<!-- keep by customization: end -->
            resultSegment = await container.ListBlobsSegmentedAsync("", true, BlobListingDetails.All, 10, continuationToken, null, null);
            if (resultSegment.Results.Count<IListBlobItem>() > 0) { Console.WriteLine("Page {0}:", ++i); }
            foreach (var blobItem in resultSegment.Results)
            {
                Console.WriteLine("\t{0}", blobItem.StorageUri.PrimaryUri);
            }
            Console.WriteLine();

            //Get the continuation token.
            continuationToken = resultSegment.ContinuationToken;
        }
        while (continuationToken != null);
    }

## Next steps

[AZURE.INCLUDE [vs-storage-dotnet-blobs-next-steps](../includes/vs-storage-dotnet-blobs-next-steps.md)]
