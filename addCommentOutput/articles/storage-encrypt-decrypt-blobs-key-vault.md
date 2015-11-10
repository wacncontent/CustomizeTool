<properties
   pageTitle="Encrypt and decrypt blobs in Windows Azure Storage using Azure Key Vault | Windows Azure"
   description="This tutorial walks you through how to encrypt and decrypt a blob using client-side encryption for Windows Azure Storage with Azure Key Vault."
   services="storage"
   documentationCenter=""
   authors="adhurwit"
   manager=""
   editor=""/>

<tags
	ms.service="storage"
	ms.date="06/17/2015"
	wacn.date=""/>

# Encrypt and decrypt blobs in Windows Azure Storage using Azure Key Vault

## Introduction
 
This tutorial covers how to make use of client-side storage encryption <!-- keep by customization: begin --> - currently in preview - <!-- keep by customization: end --> with Azure Key Vault <!-- keep by customization: begin --> - also currently in preview <!-- keep by customization: end -->. It walks you through how to encrypt and decrypt a blob in a console application using these technologies.

**Estimated time to complete:** 20 minutes

For overview information about Azure Key Vault, see [What is Azure Key Vault?](/documentation/articles/key-vault-whatis)

<!-- deleted by customization
For overview information about client-side encryption for Azure Storage, see [Get Started with Client-Side Encryption for Windows Azure Storage](/documentation/articles/storage-client-side-encryption)
-->
<!-- keep by customization: begin -->
For overview information about client-side encryption for Azure Storage, see [Client-Side Encryption for Windows Azure Storage – Preview](http://blogs.msdn.com/b/windowsazurestorage/archive/2015/04/28/client-side-encryption-for-microsoft-azure-storage-preview.aspx)
<!-- keep by customization: end -->


## Prerequisites

To complete this tutorial, you must have the following:

- An Azure Storage account
- Visual Studio 2013 or later
- Azure PowerShell 


<!-- deleted by customization
## Overview of client-side encryption

For an overview of client-side encryption for Azure Storage, see [Get Started with Client-Side Encryption for Windows Azure Storage](/documentation/articles/storage-client-side-encryption)

Here is a brief description of how client side encryption works:

1. The Azure Storage client SDK generates a content encryption key (CEK) <!-- deleted by customization, --> which is a one-time-use symmetric key.
2. Customer data is encrypted using this CEK.
3. The CEK is then wrapped (encrypted) using the key encryption key (KEK). The KEK is identified by a key identifier and can be an asymmetric key pair or a symmetric key and can be managed locally or stored in Azure Key Vault. The Storage client itself never has access to the KEK. It just invokes the key wrapping algorithm that is provided by Key Vault. Customers can choose to use custom providers for key wrapping/unwrapping if they want.
-->
<!-- keep by customization: begin -->
## Overview of the Client-Side Encryption process

For an overview of Client-Side Encryption for Windows Azure Storage, see [http://blogs.msdn.com/b/windowsazurestorage/archive/2015/04/29/getting-started-with-client-side-encryption-for-microsoft-azure-storage.aspx](http://blogs.msdn.com/b/windowsazurestorage/archive/2015/04/29/getting-started-with-client-side-encryption-for-microsoft-azure-storage.aspx "Getting Started with Client-Side Encryption for Windows Azure Storage")

Here is the process as described in that blog post:

1. The Azure Storage client SDK will generate a content encryption key (CEK) <!-- deleted by customization, --> which is a one-time-use symmetric key.
2. User data is encrypted using this CEK.
3. The CEK is then wrapped (encrypted) using the key encryption key KEK. The KEK is identified by a key identifier and can be an asymmetric key pair or a symmetric key and can be managed locally or stored in Azure Key Vaults. The Storage client itself never has access to  KEK. It just invokes the key wrapping algorithm that is provided by Key Vault. Users can choose to use custom providers for key wrapping/unwrapping if desired.
<!-- keep by customization: end -->
4. The encrypted data is then uploaded to the Azure Storage service.


<!-- deleted by customization
## Set up your Azure Key Vault
In order to proceed with this tutorial, you need to do the following steps, which are outlined in the tutorial  [Get started with Azure Key Vault](/documentation/articles/key-vault-get-started):

- Create a key vault <!-- deleted by customization. -->
- Add a key or secret to the key vault <!-- deleted by customization. -->
- Register an application with Azure Active Directory <!-- deleted by customization. -->
- Authorize the application to use the key or secret <!-- deleted by customization. -->
-->
<!-- keep by customization: begin -->
## Set-up your Azure Key Vault
In order to proceed with this tutorial, you need to do the following which are outlined in the tutorial:  [Get Started with Azure Key Vault](/documentation/articles/key-vault-get-started) 

- Create a key vault <!-- deleted by customization. -->
- Add a key or secret to the key vault <!-- deleted by customization. -->
- Register an application with Azure Active Directory <!-- deleted by customization. -->
- Authorize the application to use the key or secret <!-- deleted by customization. -->
<!-- keep by customization: end -->

Make note of the ClientID and ClientSecret that were generated when registering an application with Azure Active Directory. 

Create both <!-- deleted by customization keys --><!-- keep by customization: begin --> a key <!-- keep by customization: end --> in the key vault. We <!-- keep by customization: begin --> will <!-- keep by customization: end --> assume for the rest of the tutorial that you have used the following names: ContosoKeyVault and TestRSAKey1.


## Create a console application with packages and AppSettings

<!-- deleted by customization
In Visual Studio, create a new console application.

Add necessary nuget packages in the Package Manager Console <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->

	Install-Package WindowsAzure.Storage 

	// This is the latest stable release for ADAL <!-- deleted by customization. -->
-->
<!-- keep by customization: begin -->
In Visual Studio, create a new Console Application.

Add necessary nuget packages in the Package Manager Console <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->

	// Note that this is the preview version for Azure Storage
	Install-Package WindowsAzure.Storage -Pre

	// This is the latest stable release for ADAL <!-- deleted by customization. -->
<!-- keep by customization: end -->
	Install-Package Microsoft.IdentityModel.Clients.ActiveDirectory -Version 2.16.204221202

<!-- deleted by customization
	Install-Package Microsoft.Azure.KeyVault 
	Install-Package Microsoft.Azure.KeyVault.Extensions 
-->
<!-- keep by customization: begin -->
	// These are currently only available in preview
	Install-Package Microsoft.Azure.KeyVault -Pre
	Install-Package Microsoft.Azure.KeyVault.Extensions -Pre
<!-- keep by customization: end -->


Add AppSettings to the App.Config. 

	<appSettings>
	    <add key="accountName" value="myaccount"/>
	    <add key="accountKey" value="theaccountkey"/>
	    <add key="clientId" value="theclientid"/>
	    <add key="clientSecret" value="theclientsecret"/>
    	<add key="container" value="stuff"/>
	</appSettings>

Add the following <!-- deleted by customization `using` --><!-- keep by customization: begin --> using <!-- keep by customization: end --> statements and make sure to add a reference to System.Configuration to the project.

	using Microsoft.IdentityModel.Clients.ActiveDirectory;
	using System.Configuration;
	using Microsoft.WindowsAzure.Storage.Auth;
	using Microsoft.WindowsAzure.Storage;
	using Microsoft.WindowsAzure.Storage.Blob;
	using Microsoft.Azure.KeyVault;
	using System.Threading;		
	using System.IO;


<!-- deleted by customization
## Add a method to get a token to your console application

The following method is used by Key Vault classes that need to authenticate for access to your key vault.
-->
<!-- keep by customization: begin -->
## Add method to get token to your console application

The following method is used by Key Vault classes that need to authenticate for access to your Key Vault.
<!-- keep by customization: end -->

	private async static Task<string> GetToken(string authority, string resource, string scope)
	{
	    var authContext = new AuthenticationContext(authority);
	    ClientCredential clientCred = new ClientCredential(
	        ConfigurationManager.AppSettings["clientId"], 
	        ConfigurationManager.AppSettings["clientSecret"]);
		AuthenticationResult result = await authContext.AcquireTokenAsync(resource, clientCred);
	
	    if (result == null)
	        throw new InvalidOperationException("Failed to obtain the JWT token");
	
	    return result.AccessToken;
	}

## Access <!-- deleted by customization Storage --><!-- keep by customization: begin --> storage <!-- keep by customization: end --> and Key Vault in your program

In the Main function, add the following code <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->

	// This is standard code to interact with Blob <!-- deleted by customization storage. --><!-- keep by customization: begin --> Storage <!-- keep by customization: end -->
	StorageCredentials creds = new StorageCredentials(
		ConfigurationManager.AppSettings["accountName"],
       	ConfigurationManager.AppSettings["accountKey"]);
	CloudStorageAccount account = new CloudStorageAccount(creds, useHttps: true);
	CloudBlobClient client = account.CreateCloudBlobClient();
	CloudBlobContainer contain = client.GetContainerReference(ConfigurationManager.AppSettings["container"]);
	contain.CreateIfNotExists();

	// The Resolver object is used to interact with Key Vault for Azure Storage <!-- deleted by customization. -->
	// This is where the GetToken method from above is used <!-- deleted by customization. -->
	KeyVaultKeyResolver cloudResolver = new KeyVaultKeyResolver(GetToken);


> [AZURE.NOTE] Key Vault Object Models
>
>It is important to understand that there are actually two Key Vault object models to be aware of: one is based on the REST API (KeyVault namespace) and the other is an extension for client-side encryption.

> The Key Vault Client interacts with the REST API and understands JSON Web Keys and <!-- deleted by customization secrets --><!-- keep by customization: begin --> Secrets <!-- keep by customization: end --> for the two kinds of things that are contained in <!-- keep by customization: begin --> the <!-- keep by customization: end --> Key Vault.

> The Key Vault Extensions are classes that seem specifically created for client-side encryption in Azure Storage. They contain an interface for keys <!-- deleted by customization (IKey) --><!-- keep by customization: begin --> - IKey - <!-- keep by customization: end --> and classes based on the concept of a Key Resolver. There are two implementations of IKey that you need to know: RSAKey and SymmetricKey. Now they happen to coincide with the things that are contained in a Key Vault, but at this point they are independent classes (so the Key and Secret retrieved by the Key Vault Client do not implement IKey).


## Encrypt blob and upload
<!-- deleted by customization
Add the following code to encrypt a blob and upload it to your Azure storage account. The **ResolveKeyAsync** method that is used returns an IKey.

	
	// Retrieve the key that you created previously <!-- deleted by customization. -->
	// The IKey that is returned here is an RsaKey <!-- deleted by customization. -->
	// Remember that we used the names contosokeyvault and testrsakey1 <!-- deleted by customization. -->
-->
<!-- keep by customization: begin -->
Add the following code to encrypt a Blob and upload it to your Azure Storage account. The ResolveKeyAsync method that is used returns an IKey. 

	
	// Retrieve the key that you created previously <!-- deleted by customization. -->
	// The IKey that is returned here is an RsaKey <!-- deleted by customization. -->
	// Remember that we used the names contosokeyvault and testrsakey1 <!-- deleted by customization. -->
<!-- keep by customization: end -->
    var rsa = cloudResolver.ResolveKeyAsync("https://contosokeyvault.vault.azure.net/keys/TestRSAKey1", CancellationToken.None).GetAwaiter().GetResult();


	// Now you simply use the RSA key to encrypt by setting it in the BlobEncryptionPolicy. 
	BlobEncryptionPolicy policy = new BlobEncryptionPolicy(rsa, null);
	BlobRequestOptions options = new BlobRequestOptions() { EncryptionPolicy = policy };

	// Reference a block blob <!-- deleted by customization. -->
	CloudBlockBlob blob = contain.GetBlockBlobReference("MyFile.txt");

	// Upload using the UploadFromStream method <!-- deleted by customization. -->
	using (var stream = System.IO.File.OpenRead(@"C:\data\MyFile.txt"))
		blob.UploadFromStream(stream, stream.Length, null, options, null);


<!-- deleted by customization
Following is a screenshot from the current Azure Management Portal for a blob that has been encrypted by using client-side encryption with a key stored in Key Vault. The **KeyId** property is the URI for the key in Key Vault that acts as the KEK. The **EncryptedKey** property contains the encrypted version of the CEK.

![Screenshot showing Blob metadata that includes encryption metadata][1]
-->
<!-- keep by customization: begin -->
Following is a screenshot from the current Azure Management portal for a blob that has been encrypted using client-side encryption with a key stored in Key Vault. The KeyId property is the URI for the key in Key Vault that acts as the key encryption key (KEK). The EncryptedKey property contains the encrypted version of the content encryption key (CEK). 

![Screenshot showing Blob metadata that includes encryption metadata][1]
<!-- keep by customization: end -->

> [AZURE.NOTE] If you look at the BlobEncryptionPolicy constructor, you will see that it can accept a key and/or a resolver. Be aware that right now you cannot use a resolver for encryption because it does not currently support a default key.



## Decrypt blob and download
Decryption is really when <!-- deleted by customization using --> the Resolver classes make sense. The ID of the key used for encryption is associated with the <!-- deleted by customization blob --><!-- keep by customization: begin --> Blob <!-- keep by customization: end --> in its metadata, so there is no reason for you to retrieve the key and remember the association between key and blob. You just have to make sure that the key remains in <!-- keep by customization: begin --> the <!-- keep by customization: end --> Key Vault.

The private key of an RSA Key remains in Key Vault, so for decryption to occur <!-- deleted by customization, --> the Encrypted Key from the blob metadata <!-- deleted by customization that --><!-- keep by customization: begin --> which <!-- keep by customization: end --> contains the <!-- deleted by customization CEK --><!-- keep by customization: begin --> CEC (content encryption key) <!-- keep by customization: end --> is sent to Key Vault for decryption.

Add the following to decrypt the blob that you just uploaded. 

	// In this case <!-- deleted by customization, --> we will not pass a key and only pass the resolver because
	// this policy will only be used for downloading / decrypting <!-- deleted by customization. -->
	BlobEncryptionPolicy policy = new BlobEncryptionPolicy(null, cloudResolver);
	BlobRequestOptions options = new BlobRequestOptions() { EncryptionPolicy = policy };

    using (var np = File.Open(@"C:\data\MyFileDecrypted.txt", FileMode.Create))
	    blob.DownloadToStream(np, null, options, null);


> [AZURE.NOTE] There are a couple of other kinds of <!-- deleted by customization resolvers --><!-- keep by customization: begin --> Resolvers <!-- keep by customization: end --> to make key management easier, including: AggregateKeyResolver and CachingKeyResolver.


<!-- deleted by customization
## Use Key Vault secrets
The way to use a secret with client-side encryption is via the SymmetricKey class because a secret is essentially a symmetric key. But, as noted above, a secret in Key Vault does not map exactly to a SymmetricKey. There are a few things to understand:


- The key in a SymmetricKey has to be a fixed length: 128, 192, 256, 384, or 512 bits <!-- deleted by customization. -->
- The key in a SymmetricKey should be Base64 encoded <!-- deleted by customization. -->
- A Key Vault secret that will be used as a SymmetricKey needs to have a Content Type of "application/octet-stream" in Key Vault <!-- deleted by customization. -->

Here is an example in PowerShell of creating a secret in Key Vault that can be used as a SymmetricKey <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->
-->
<!-- keep by customization: begin -->
## Using Key Vault Secrets
The way to use a Secret with client-side encryption is via the SymmetricKey class because a Secret is essentially a symmetric key. But, as noted above, a Secret in Key Vault does not map exactly to a SymmetricKey. There are a few things to understand:


- The key in a SymmetricKey has to be a fixed length: 128, 192, 256, 384, or 512 bits <!-- deleted by customization. -->
- The key in a SymmetricKey should be Base64 encoded <!-- deleted by customization. -->
- A Key Vault Secret that will be used as a SymmetricKey needs to have a Content Type of "application/octet-stream" in Key Vault <!-- deleted by customization. -->

Here is an example in PowerShell of creating a Secret in Key Vault that can be used as a SymmetricKey <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->
<!-- keep by customization: end -->

	// Here we are making a 128-bit key so we have 16 characters. 
	// 	The characters are in the ASCII range of UTF8 so they are
	//	each 1 byte. 16 x 8 = 128 <!-- deleted by customization. -->
	$key = "qwertyuiopasdfgh"
	$b = [System.Text.Encoding]::UTF8.GetBytes($key)
	$enc = [System.Convert]::ToBase64String($b)
	$secretvalue = ConvertTo-SecureString $enc -AsPlainText -Force

<!-- deleted by customization
	// Substitute the VaultName and Name in this command.
-->
<!-- keep by customization: begin -->
	// substitute the VaultName and Name in this command
<!-- keep by customization: end -->
	$secret = Set-AzureKeyVaultSecret -VaultName 'ContoseKeyVault' -Name 'TestSecret2' -SecretValue $secretvalue -ContentType "application/octet-stream"

In your console application, you can use the same call as before to retrieve this <!-- deleted by customization secret --><!-- keep by customization: begin --> Secret <!-- keep by customization: end --> as a SymmetricKey.

	SymmetricKey sec = (SymmetricKey) cloudResolver.ResolveKeyAsync(
    	"https://contosokeyvault.vault.azure.net/secrets/TestSecret2/", 
        CancellationToken.None).GetAwaiter().GetResult();

That's it. Enjoy!

## Next steps

For more information about using Windows Azure Storage with C#, see [Windows Azure Storage Client Library for .NET](https://msdn.microsoft.com/zh-cn/library/azure/dn261237.aspx) <!-- deleted by customization. -->

For more information about the Blob REST API, see [Blob Service REST API](https://msdn.microsoft.com/zh-cn/library/azure/dd135733.aspx) <!-- deleted by customization. -->

For the latest information on Windows Azure Storage, go to the [Windows Azure Storage Team Blog](http://blogs.msdn.com/b/windowsazurestorage/) <!-- deleted by customization. -->


<!--Image references-->
[1]: ./media/storage-encrypt-decrypt-blobs-key-vault/blobmetadata.png
