<properties
	pageTitle="Create an Azure Batch account | Windows Azure"
	description="Learn how to create an Azure Batch account in the Azure Management Portal to run large-scale parallel workloads in the cloud"
	services="batch"
	documentationCenter=""
	authors="dlepow"
	manager="timlt"
	editor=""/>

<tags
	ms.service="batch"
	ms.date="11/10/2015"
	wacn.date=""/>



# Create and manage an Azure Batch account in the Azure Management Portal

> [AZURE.SELECTOR]
- [Azure Management Portal](/documentation/articles/batch-account-create-portal)
- [Batch Management .NET](/documentation/articles/batch-management-dotnet)

This article shows you how to use the [Azure Management Portal](https://manage.windowsazure.cn) to create and manage an Azure Batch account and settings such as account keys. You need a Batch account URL and an associated access key to authenticate all Batch API requests. And you associate all the Batch resources (such as pools, jobs, and tasks) for your Batch workload with a specific Batch account.  

>[AZURE.NOTE] Currently the preview portal supports features for Batch account management and viewing some account resources. The full Batch features are available to developers through the Batch APIs.

## Create a Batch account

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn).

2. Click **New** > **Compute** > **Batch Service**.

	![Batch in the Marketplace][marketplace_portal]

3. Review the information and then click **Create**.

4. In the **New Batch Account** blade, enter the following information:

	a. In **Account Name**, enter a unique name to use in the Batch account URL.

	>[AZURE.NOTE] The Batch account name must be unique to Azure, contain between 3 and 24 characters, and use only lowercase letters and numbers.

	b. If you have more than one subscription, click **Subscription** to select an available subscription where the account will be created.

	c. Click **Resource group** to select an existing resource group for the account, or create a new one.

	d. In **Location**, select an Azure region in which Batch is available.

	![Create a Batch account][account_portal]

5. Click **Create** to complete the account creation.

## Manage access keys and account settings
After the account is created, you can find it in the portal to manage access keys, authorized users, and other settings.

The Batch account URL appears in **Essentials**. It's a URL of the form <!-- deleted by customization `https://<account_name>.<region>.batch.azure.com` --><!-- keep by customization: begin --> `https://<account_name>.<region>.batch.chinacloudapi.cn` <!-- keep by customization: end -->.

To see and manage the access keys, click the key icon.

![Batch account keys][account_keys]

## Additional things to know about the Batch account

* Other ways to create and manage Batch accounts include the [Batch PowerShell cmdlets](/documentation/articles/batch-powershell-cmdlets-get-started) and the [Batch Management .NET library](http://www.nuget.org/packages/Microsoft.Azure.Management.Batch/).


* Azure doesn't charge you to have a Batch account. You only get charged for your use of Azure compute resources and other services when your workloads run (see [Batch pricing](/home/features/batch/#price)).

* You can run multiple Batch workloads in a single Batch account, or distribute your workloads among Batch accounts in different Azure regions.

* If you're running several large-scale Batch workloads, be aware of certain [Batch service quotas and limits](/documentation/articles/batch-quota-limit) that apply to your Azure subscription and each Batch account. Current quotas on a Batch account appear in the preview portal in the account properties.

## Next steps

* See [Azure Batch feature overview](/documentation/articles/batch-api-basics) to learn more about the Batch concepts.

* Get started developing your first application with the [Batch .NET client library](/documentation/articles/batch-dotnet-get-started).

[marketplace_portal]: ./media/batch-account-create-portal/marketplace_batch.PNG
[account_portal]: ./media/batch-account-create-portal/batch_acct_portal.png
[account_keys]: ./media/batch-account-create-portal/account_keys.PNG
