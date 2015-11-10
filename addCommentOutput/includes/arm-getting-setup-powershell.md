<!-- keep by customization: begin -->
<properties services="virtual-machines" title="Setting up PowerShell for Resource Manager templates" authors="JoeDavies-MSFT" solutions="" manager="timlt" editor="tysonn" />

<tags
	ms.service="virtual-machines"
	ms.date="04/14/2015"
	wacn.date=""/>

<!-- keep by customization: end -->
## Setting up PowerShell for Resource Manager templates

<!-- deleted by customization
Before you can use Azure PowerShell with Resource Manager, you will need to have the right Windows PowerShell and Azure PowerShell versions.

### Verify PowerShell versions

Verify you  have Windows PowerShell version<!-- keep by customization: begin -->, Version <!-- keep by customization: end --> 3.0 or 4.0. To find the version of Windows PowerShell, type this command at a Windows PowerShell command prompt.
-->
<!-- keep by customization: begin -->
Before you can use Azure PowerShell with Resource Manager templates and deploy Azure resources and workloads using resource groups, follow these steps.

### Step 1: Verify PowerShell versions

Before you can use Windows PowerShell with ARM, you must have Windows PowerShell <!-- keep by customization: begin -->, Version <!-- keep by customization: end --> 3.0 or 4.0. To find the version of Windows PowerShell, type this command at a Windows PowerShell command prompt.
<!-- keep by customization: end -->

	$PSVersionTable

<!-- deleted by customization
You will receive the following type of information:
-->
<!-- keep by customization: begin -->
You should see something like this.
<!-- keep by customization: end -->

	Name                           Value
	----                           -----
	PSVersion                      3.0
	WSManStackVersion              3.0
	SerializationVersion           1.1.0.1
	CLRVersion                     4.0.30319.18444
	BuildVersion                   6.2.9200.16481
	PSCompatibleVersions           {1.0, 2.0, 3.0}
	PSRemotingProtocolVersion      2.2

<!-- deleted by customization

Verify that the value of **PSVersion** is 3.0 or 4.0. If not, see [Windows Management Framework 3.0](http://www.microsoft.com/download/details.aspx?id=34595) or [Windows Management Framework 4.0](http://www.microsoft.com/download/details.aspx?id=40855).

[AZURE.INCLUDE [powershell-preview](../includes/powershell-preview-inline-include.md)]

###  Set your Azure account and subscription
-->
<!-- keep by customization: begin -->
Verify that the value of **PSVersion** is 3.0 or 4.0. To install a compatible version, see [Windows Management Framework 3.0](http://www.microsoft.com/download/details.aspx?id=34595) or [Windows Management Framework 4.0](http://www.microsoft.com/download/details.aspx?id=40855).

You must also have Azure PowerShell version 0.8.0 or later. You can check the version of Azure PowerShell that you have installed with this command at the Azure PowerShell command prompt.

	Get-Module azure | format-table version

You should see something like this.

	Version
	-------
	0.8.16.1

For instructions and a link to the latest version, see [How to Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure).


### Step 2: Set your Azure account and subscription
<!-- keep by customization: end -->

If you don't already have an Azure subscription, you can activate your [MSDN subscriber benefits](http://azure.microsoft.com/pricing/member-offers/msdn-benefits-details/) or sign up for a [trial](/pricing/1rmb-trial/).

<!-- deleted by customization
Open an Azure PowerShell command prompt and log on to Azure with this command.

	Login-AzureRmAccount

If you have multiple Azure subscriptions, you can list your Azure subscriptions with this command.

	Get-AzureRmSubscription

You will receive the following type of information:

	SubscriptionId            : fd22919d-eaca-4f2b-841a-e4ac6770g92e
	SubscriptionName          : Visual Studio Ultimate with MSDN
	Environment               : AzureCloud
	SupportedModes            : AzureServiceManagement,AzureResourceManager
	DefaultAccount            : johndoe@contoso.com
	Accounts                  : {johndoe@contoso.com}
	IsDefault                 : True
	IsCurrent                 : True
	CurrentStorageAccountName :
	TenantId                  : 32fa88b4-86f1-419f-93ab-2d7ce016dba7

You can set the current Azure subscription by running these commands at the Azure PowerShell command prompt. Replace everything within the quotes, including the < and > characters, with the correct name.

	$subscr="<SubscriptionName from the display of Get-AzureRmSubscription>"
	Select-AzureRmSubscription -SubscriptionName $subscr -Current
-->
<!-- keep by customization: begin -->
List your Azure subscriptions with this command.

	Get-AzureSubscription

For the subscription into which you want to deploy new resources, note the **Accounts** property. Run this command to login to Azure using an account listed in the **Accounts** property.

	Add-AzureAccount

Specify the email address of the account and its password in the Windows Azure sign-in dialog.

Set your Azure subscription by running these commands at the Azure PowerShell command prompt. Replace everything within the quotes, including the < and > characters, with the correct name.

	$subscr="<subscription name>"
	Select-AzureSubscription -SubscriptionName $subscr –Current
	Set-AzureSubscription -SubscriptionName $subscr

You can get the correct subscription name from the **SubscriptionName** property of the output of the **Get-AzureSubscription** command.
<!-- keep by customization: end -->

For more information about Azure subscriptions and accounts, see [How to: Connect to your subscription](/documentation/articles/powershell-install-configure#Connect).

<!-- keep by customization: begin -->
### Step 3: Switch to the Azure Resource Manager module

Switch to the Azure Resource Manager set of Azure PowerShell commands with this command.

	Switch-AzureMode AzureResourceManager

> [AZURE.NOTE] You can switch back to the Azure module with the **Switch-AzureMode AzureServiceManagement** command.


<!-- keep by customization: end -->