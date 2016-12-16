<properties
    pageTitle="How to delete an HDInsight cluster | Azure"
    description="Information on the various ways that you can delete an HDInsight cluster."
    services="hdinsight"
    documentationcenter=""
    author="Blackmist"
    manager="jhubbard"
    editor="cgronlun" />
<tags
    ms.assetid="55f7838b-9786-47ff-96db-1b64437bd0bb"
    ms.service="hdinsight"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="big-data"
    ms.date="10/28/2016"
    wacn.date=""
    ms.author="larryfr" />

# How to delete an HDInsight cluster
HDInsight cluster billing starts once a cluster is created and stops when the cluster is deleted and is pro-rated per minute, so you should always delete your cluster when it is no longer in use. In this document, you will learn how to delete a cluster using the Azure Classic Management Portal, Azure PowerShell, and the Azure CLI.

> [AZURE.IMPORTANT]
> Deleting an HDInsight cluster does not delete the Azure Storage account(s) associated with the cluster. This allows you to preserve and reuse any data stored by the cluster.
> 
> 

##Azure Classic Management Portal
1. Login to the [Azure Classic Management Portal](https://manage.windowsazure.cn), click **HDInsight**, and select the cluster you want to delete.

2. Click the __Delete__ at the bottom. When prompted, select __Yes__ to delete the cluster.

## Azure PowerShell
From a PowerShell prompt, use the following command to delete the cluster:

    Remove-AzureHDInsightCluster -Name CLUSTERNAME

Replace **CLUSTERNAME** with the name of your HDInsight cluster.

## Azure CLI
From a prompt, use the following to delete the cluster:

    azure hdinsight cluster delete CLUSTERNAME

Replace **CLUSTERNAME** with the name of your HDInsight cluster.

