<properties
	pageTitle="Manage Hadoop clusters using Azure CLI | Microsoft Azure"
	description="How to use the Azure CLI to manage Hadoop clusters in HDIsight"
	services="hdinsight"
	editor="cgronlun"
	manager="paulettm"
	authors="mumian"
	tags="azure-portal"
	documentationCenter=""/>

<tags
	ms.service="hdinsight"
	ms.date="05/24/2016"
	wacn.date=""/>

# Manage Hadoop clusters in HDInsight using the Azure CLI

[AZURE.INCLUDE [selector](../includes/hdinsight-portal-management-selector.md)]

Learn how to use the [Azure Command-line Interface](/documentation/articles/xplat-cli-install/) to manage Hadoop clusters in Azure HDInsight. The Azure CLI is implemented in Node.js. It can be used on any platform that supports Node.js, including Windows, Mac, and Linux.

This article covers only using the Azure CLI with HDInsight. For a general guide on how to use Azure CLI, see [Install and configure Azure CLI][azure-command-line-tools].

[AZURE.INCLUDE [use-latest-version](../includes/hdinsight-use-latest-cli.md)]

##Prerequisites

Before you begin this article, you must have the following:

- **An Azure subscription**. See [Get Azure  free  trial](/pricing/1rmb-trial/).
- **Azure CLI** - See [Install and configure the Azure CLI](/documentation/articles/xplat-cli-install/) for installation and configuration information.
- **Connect to Azure**, using the following command:

		azure login  -e AzureChinaCloud -u <your account> 

	For more information on authenticating using a work or school account, see [Connect to an Azure subscription from the Azure CLI](/documentation/articles/xplat-cli-connect/).
	

- **Switch to the Azure Resource Manager mode**, using the following command:

		azure config mode arm


To get help, use the **-h** switch.  For example:

	azure hdinsight cluster create -h
	
##Create clusters


See [Create Linux-based clusters in HDInsight using the Azure CLI](/documentation/articles/hdinsight-hadoop-create-linux-clusters-azure-cli/).


See [Create Windows-based Hadoop clusters in HDInsight using Azure CLI](/documentation/articles/hdinsight-hadoop-create-windows-clusters-cli/).


##List and show cluster details
Use the following commands to list and show cluster details:

	azure hdinsight cluster list
	azure hdinsight cluster show <Cluster Name>

![HDI.CLIListCluster][image-cli-clusterlisting]


##Delete clusters

Use the following command to delete a cluster:

	azure hdinsight cluster delete <Cluster Name>


You can also delete a cluster by deleting the resource group that contains the cluster. Please note, this will delete all the resources in the group including the default storage account.

	azure group delete <Resource Group Name>

##Scale clusters

To change the Hadoop cluster size:

	azure hdinsight cluster resize [options] <clusterName> <Target Instance Count>


## Enable/disable HTTP access for a cluster

	azure hdinsight cluster enable-http-access [options] <Cluster Name> <userName> <password>
	azure hdinsight cluster disable-http-access [options] <Cluster Name>


## Enable/disable RDP access for a cluster

  	azure hdinsight cluster enable-rdp-access [options] <Cluster Name> <rdpUserName> <rdpPassword> <rdpExpiryDate>
  	azure hdinsight cluster disable-rdp-access [options] <Cluster Name>


##Next steps
In this article, you have learned how to perform different HDInsight cluster administrative tasks. To learn more, see the following articles:

* [Administer HDInsight by using the  Azure  Classic Management  Portal] [hdinsight-admin-portal]
* [Administer HDInsight by using Azure PowerShell] [hdinsight-admin-powershell]
* [Get started with Azure HDInsight] [hdinsight-get-started]
* [How to use the Azure CLI] [azure-command-line-tools]


[azure-command-line-tools]: /documentation/articles/xplat-cli-install/
[azure-create-storageaccount]: /documentation/articles/storage-create-storage-account/
[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: /pricing/member-offers/

[azure-free-trial]: /pricing/1rmb-trial/


[hdinsight-admin-portal]: /documentation/articles/hdinsight-administer-use-management-portal/


[azure-trial]: /pricing/1rmb-trial/


[hdinsight-admin-portal]: /documentation/articles/hdinsight-administer-use-management-portal-v1/

[hdinsight-admin-powershell]: /documentation/articles/hdinsight-administer-use-powershell/

[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-linux-tutorial-get-started/


[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1/


[image-cli-account-download-import]: ./media/hdinsight-administer-use-command-line/HDI.CLIAccountDownloadImport.png
[image-cli-clustercreation]: ./media/hdinsight-administer-use-command-line/HDI.CLIClusterCreation.png
[image-cli-clustercreation-config]: ./media/hdinsight-administer-use-command-line/HDI.CLIClusterCreationConfig.png
[image-cli-clusterlisting]: ./media/hdinsight-administer-use-command-line/HDI.CLIListClusters.png "List and show clusters"
