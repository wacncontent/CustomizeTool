deletion:

deleted:

		## uniqueString
		
		**uniqueString (stringForCreatingUniqueString, ...)**
		
		Performs a 64-bit hash of the provided strings to create a unique string. This function is helpful when you need to create a unique name for a resource. You provide parameter values that represent the level of uniqueness for the result. You can specify whether the name is unique for your subscription, resource group, or deployment. 
		
		| Parameter                          | Required | Description
		| :--------------------------------: | :------: | :----------
		| stringForCreatingUniqueString      |   Yes    | The base string used in the hash function to create a unique string.
		| additional parameters as needed    | No       | You can add as many strings as needed to create the value that specifies the level for uniqueness.
		
		The returned value is not a completely random string, but rather the result of a hash function. The returned value is 13 characters long. It is not guaranteed to be globally unique. You may want to combine the value with a prefix from your naming convention to create a more friendly name.
		
		The following examples show how to use uniqueString to create a unique value for a different commonly-used levels.
		
		Unique based on subscription
		
		    "[uniqueString(subscription().subscriptionId)]"
		
		Unique based on resource group
		
		    "[uniqueString(resourceGroup().id)]"
		
		Unique based on deployment for a resource group
		
		    "[uniqueString(resourceGroup().id, deployment().name)]"
		    
		The following example shows how to create a unique name for a storage account based on your resource group.
		
		    "resources": [{ 
		        "name": "[concat('ContosoStorage', uniqueString(resourceGroup().id))]", 
		        "type": "Microsoft.Storage/storageAccounts", 
		        ...

reason: ()

