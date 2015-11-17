replacement:

deleted:

		## Using Azure CLI
		
		The following steps help you use Azure CLI easily with the most recent version and the proper subscription. If you need to install Azure CLI and connect it to your account first, see the [Azure Command-Line Interface (Azure CLI)](/documentation/articles/xplat-cli-install).
		
		### Step 1: Update Azure CLI version
		
		To use Azure CLI for imperative commands with service management mode, you should have a recent version if possible. To verify your version, type `azure --version`. You should see something like:

replaced by:

		## Using the xplat-cli
		
		The following steps help you use the xplat-cli easily with the most recent version and the proper subscription. If you need to install the xplat-cli and connect it to your account first, see the [Azure Command-Line Interface (xplat-cli)](/documentation/articles/xplat-cli).
		
		## Step 1: Update the xplat-cli version
		
		To use the xplat-cli for imperative commands and ARM templates, you should have a recent version if possible. To verify your version, type `azure --version`. You should see something like:

reason: ()

deleted:

		If you want to update your version of Azure CLI, see [Azure CLI](https://github.com/Azure/azure-xplat-cli).
		
		### Step 2: Set the Azure account and subscription
		
		Once you have connected your Azure CLI with the account you want to use, you may have more than one subscription. If you do, you should review the subscriptions available for your account by typing `azure account list`, and then select the subscription you want to use by typing `azure account set <subscription id or name> true` where _subscription id or name_ is either the subscription id or the subscription name that you would like to work with in the current session. You should see something like the following:
		
		    $ azure account set "Visual Studio Ultimate with MSDN" true
		    info:    Executing command account set
		    info:    Setting subscription to "Visual Studio Ultimate with MSDN" with id "0e220bf6-5caa-4e9f-8383-51f16b6c109f".
		    info:    Changes saved
		    info:    account set command OK
		
		> [AZURE.NOTE] If you don't already have an Azure account but you do have a subscription to MSDN subscription, you can get free Azure credits by activating your [MSDN subscriber benefits here](/pricing/member-offers/msdn-benefits-details/) -- or you can use the free account. Either will work for Azure access.

replaced by:

		If you want to update your version of the xplat-cli, see [xplat-cli](https://github.com/Azure/azure-xplat-cli).
		
		## Step 2: Set the Azure account and subscription
		
		Once you have connected your xplat-cli with the account you want to use, you may have more than one subscription. If you do, you need to select the subscription you want to use by typing
		
		    azure set <subscription id or name> true
		    
		where _subscription id or name_ is either the subscription id or the subscription name that you would like to work with in the current session.
		
		
		Before you can use the xplat-cli with Resource Manager templates and deploy Azure resources and workloads using resource groups, you will need an account with Azure (of course). If you do not have an account, you can get a [free Azure trial here](/pricing/1rmb-trial/).
		
		If you don't already have an Azure account but you do have a subscription to MSDN subscription, you can get free Azure credits by activating your [MSDN subscriber benefits here](/pricing/member-offers/msdn-benefits-details/) -- or you can use the free account. Either will work for Azure access.

reason: ()

