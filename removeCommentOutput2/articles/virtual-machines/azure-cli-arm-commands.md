<properties
	pageTitle="Use the Azure CLI with Resource Manager | Azure"
	description="Learn about using the Azure CLI for Mac, Linux, and Windows to manage Azure resources using the CLI in Azure Resource Manager mode."
	services="virtual-machines,virtual-network,mobile-services,cloud-services"
	documentationCenter=""
	authors="dlepow"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="multiple"
	ms.date="11/18/2015"
	wacn.date=""/>

# Using the Azure CLI for Mac, Linux, and Windows with Azure Resource Manager

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-rm-include.md)]

This article describes how to use the Azure Command-Line Interface (Azure CLI) in the Azure Resource Manager mode to create, manage, and delete services on the command line of Mac, Linux, and Windows computers. You can perform many of the same tasks using the various libraries of the Azure SDKs, with Azure PowerShell, and using the Azure Management Portal.

Azure Resource Manager enables you to create a group of resources -- virtual machines, websites, databases, and so on -- as a single deployable unit. You can then deploy, update, or delete all of the resources for your application in a single, coordinated operation. You describe your group resources in a JSON template for deployment and then can use that template for different environments such as testing, staging, and production.

## Scope of article

This article provides syntax and options for commonly used Azure CLI commands for the Resource Manager deployment model. It is not a complete reference, and your CLI version may show some different commands or parameters. For current command syntax and options at the command line in Resource Manager mode, type `azure help` or, to display help for a specific command, `azure help [command]`. You'll also find CLI examples in the documentation for creating and managing specific Azure services.

Optional parameters are shown in square brackets (for example, [parameter]). All other parameters are required.

In addition to command-specific optional parameters documented here, there are three optional parameters that can be used to display detailed output such as request options and status codes. The -v parameter provides verbose output, and the -vv parameter provides even more detailed verbose output. The --json option will output the result in raw json format. Usage with the --json switch is very common, and is an important part of both obtaining and understanding results from Azure CLI operations that return resource information, status, and logs and also using templates. You may want to install JSON parser tools such as **jq** or **jsawk** or use your favorite language library.

## Imperative and declarative approaches

As with the [Azure Service Management mode](/documentation/articles/virtual-machines-command-line-tools), the Resource Manager mode of the Azure CLI gives you commands that create resources imperatively on the command line. For example, if you type `azure group create <groupname> <location>` you are asking Azure to create a resource group, and with `azure group deployment create <resourcegroup> <deploymentname>` you are instructing Azure to create a deployment of any number of items and place them in a group. Because each type of resource has imperative commands, you can chain them together to create fairly complex deployments.

However, using resource group _templates_ that describe a resource group is a declarative approach that is far more powerful, allowing you to automate complex deployments of (almost) any number of resources for (almost) any purpose. When using templates, the only imperative command is to deploy one. For a general overview of templates, resources, and resource groups, see [Azure Resource Group Overview](/documentation/articles/resource-group-overview).  

##Usage requirements

The set-up requirements to use the Resource Manager mode with the Azure CLI are:

- an Azure account ([get a trial here](/pricing/1rmb-trial/))
- [installing the Azure CLI](/documentation/articles/xplat-cli-install)


Once you have an account and have installed the Azure CLI, you must

- [configure the Azure CLI](/documentation/articles/xplat-cli-connect) to use a work or school account or a Microsoft account identity
- switch to the Resource Manager mode by typing `azure config mode arm`


## azure account: Manage your account information
Your Azure subscription information is used by the tool to connect to your account.

**List the imported subscriptions**

	account list [options]

**Set the current subscription**

	account set [options] <subscriptionNameOrId>

**Remove a subscription or environment, or clear all of the stored account and environment info**  

	account clear [options]

**Commands to manage your account environment**  

	account env list [options]
	account env show [options] [environment]
	account env add [options] [environment]
	account env set [options] [environment]
	account env delete [options] [environment]

## azure ad: Commands to display Active Directory objects

**Commands to display active directory applications**

	ad app create [options]
	ad app delete [options] <object-id>

**Commands to display active directory groups**

	ad group list [options]
	ad group show [options]

**Commands to provide an active directory sub group or member info**

	ad group member list [options] [objectId]

**Commands to display active directory service principals**

	ad sp list [options]
	ad sp show [options]
	ad sp create [options] <application-id>
	ad sp delete [options] <object-id>

**Commands to display active directory users**

	ad user list [options]
	ad user show [options]

## azure availset: commands to manage your availability sets

**Creates an availability set within a resource group**

	availset create [options] <resource-group> <name> <location> [tags]

**Lists the availability sets within a resource group**

	availset list [options] <resource-group>

**Gets one availability set within a resource group**

	availset show [options] <resource-group> <name>

**Deletes one availability set within a resource group**

	availset delete [options] <resource-group> <name>

## azure config: commands to manage your local settings

**List Azure CLI configuration settings**

	conconfig list [options]

**Delete a config setting**

	conconfig delete [options] <name>

**Update a config setting**

	conconfig set <name> <value>


**Sets the Azure CLI working mode to either arm or asm**

	conconfig mode [options] <modename>


## azure feature: commands to manage account features

**List all features available for your subscription**

	feature list [options]

**Shows a feature**

	feature show [options] <providerName> <featureName>

**Registers a previewed feature of a resource provider**

	feature register [options] <providerName> <featureName>

## azure group: Commands to manage your resource groups

**Creates a new resource group**

	group create [options] <name> <location>

**Set tags to a resource group**

	group set [options] <name> <tags>

**Deletes a resource group**

	group delete [options] <name>

**Lists the resource groups for your subscription**

	group list [options]

**Shows a resource group for your subscription**

	group show [options] <name>

**Commands to manage resource group logs**

	group log show [options] [name]

**Commands to manage your deployment in a resource group**

	group deployment create [options] [resource-group] [name]
	group deployment list [options] <resource-group> [state]
	group deployment show [options] <resource-group> [deployment-name]
	group deployment stop [options] <resource-group> [deployment-name]

**Commands to manage your local or gallery resource group template**

	group template list [options]
	group template show [options] <name>
	group template download [options] [name] [file]
	group template validate [options] <resource-group>

## azure hdinsight: Commands to manage your HDInsight clusters


In Azure China, HDInsight is not manageable by ARM yet. For Azure CLI ASM commands of HDInsight, read [Create Windows-based Hadoop clusters in HDInsight using Azure CLI](/documentation/articles/hdinsight-hadoop-create-windows-clusters-cli) and [Create Windows-based Hadoop clusters in HDInsight using Azure CLI](/documentation/articles/hdinsight-hadoop-create-windows-clusters-cli)

## azure insights: Commands related to monitoring Insights (events, alert rules, autoscale settings, metrics)

**Retrieve operation logs for a subscription, a correlationId, a resource group, resource, or resource provider**

	insights logs list [options]

## azure location: Commands to get the available locations for all resource types

**List the available locations**

	location list [options]

## azure network: Commands to manage network resources


In Azure China, VNet is not manageable by ARM yet. For Azure CLI ASM commands of VNet, read the following articles:

- [Create a virtual network using Azure CLI](/documentation/articles/virtual-networks-create-vnet-classic-cli)
- [How to create NSGs in classic mode using the Azure CLI](/documentation/articles/virtual-networks-create-nsg-classic-cli)
- [Control routing and use virtual appliances using the Azure CLI in the classic deployment model](/documentation/articles/virtual-network-create-udr-classic-cli)
- [Deploy multi NIC VMs using the Azure CLI in the classic deployment model](/documentation/articles/virtual-network-deploy-multinic-classic-cli)
- [How to set a static private IP in classic mode ausing the CLI](/documentation/articles/virtual-networks-static-private-ip-classic-cli).

## azure provider: Commands to manage resource provider registrations

**List currently registered providers in ARM**

	provider list [options]

**Show details about the requested provider namespace**

	provider show [options] <namespace>

**Register provider with the subscription**

	provider register [options] <namespace>

**Unregister provider with the subscription**

	provider unregister [options] <namespace>

## azure resource: Commands to manage your resources

**Creates a resource in a resource group**

	resource create [options] <resource-group> <name> <resource-type> <location> <api-version>

**Updates a resource in a resource group without any templates or parameters**

	resource set [options] <resource-group> <name> <resource-type> <properties> <api-version>

**Lists the resources**

	resource list [options] [resource-group]

**Gets one resource within a resource group or subscription**

	resource show [options] <resource-group> <name> <resource-type> <api-version>

**Deletes a resource in a resource group**

	resource delete [options] <resource-group> <name> <resource-type> <api-version>

## azure role: Commands to manage your Azure roles

**Get all available role definitions**

	role list [options]

**Get an available role definition**

	role show [options] [name]

**Commands to manage your role assignment**

	role assignment create [options] [objectId] [upn] [mail] [spn] [role] [scope] [resource-group] [resource-type] [resource-name]
	role assignment list [options] [objectId] [upn] [mail] [spn] [role] [scope] [resource-group] [resource-type] [resource-name]
	role assignment delete [options] [objectId] [upn] [mail] [spn] [role] [scope] [resource-group] [resource-type] [resource-name]

## azure storage: Commands to manage your Storage objects


In Azure China, Storage is not manageable by ARM yet. For Azure CLI ASM commands of Storage, read [Using the Azure CLI with Azure Storage](/documentation/articles/storage-azure-cli)

## azure tag: Commands to manage your resource manager tag

**Add a tag**

	tag create [options] <name> <value>

**Remove an entire tag or a tag value**

	tag delete [options] <name> <value>

**Lists the tag information**

	tag list [options]

**Get a tag**

	tag show [options] [name]

## azure vm: Commands to manage your Azure Virtual Machines


In Azure China, Virtual Machines is not manageable by ARM yet. For Azure CLI ASM commands of Virtual Machines, read [Equivalent Azure CLI commands for VM tasks](/documentation/articles/xplat-cli-azure-manage-vm-asm-arm)

