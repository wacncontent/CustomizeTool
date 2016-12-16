<properties
    pageTitle="Customize HDInsight Clusters using bootstrap | Azure"
    description="Learn how to customize HDInsight clusters using bootstrap."
    services="hdinsight"
    documentationcenter=""
    author="mumian"
    manager="jhubbard"
    editor="cgronlun"
    tags="azure-portal" />
<tags
    ms.assetid="ab2ebf0c-e961-4e95-8151-9724ee22d769"
    ms.service="hdinsight"
    ms.workload="big-data"
    ms.tgt_pltfrm="na"
    ms.devlang="na"
    ms.topic="article"
    ms.date="09/02/2016"
    wacn.date=""
    ms.author="jgao" />

# Customize HDInsight clusters using Bootstrap
Sometimes, you want to configure the configuration files which include:

* clusterIdentity.xml
* core-site.xml
* gateway.xml
* hbase-env.xml
* hbase-site.xml
* hdfs-site.xml
* hive-env.xml
* hive-site.xml
* mapred-site
* oozie-site.xml
* oozie-env.xml
* storm-site.xml
* tez-site.xml
* webhcat-site.xml
* yarn-site.xml

The clusters can't retain the changes due to re-imaging. For more information on re-imaging, 
see [Role Instance Restarts Due to OS Upgrades](http://blogs.msdn.com/b/kwill/archive/2012/09/19/role-instance-restarts-due-to-os-upgrades.aspx). 
To keep the changes through the clusters' lifetime, you can use HDInsight cluster customization during the creation process. This is the recommended way to change configurations of a cluster and persist across these Azure reimage reboot restart events. These configuration changes are applied before service start, so services needn't be restarted. 

There are 2 methods to use bootstrap:

* Use Azure PowerShell
  
    [AZURE.INCLUDE [upgrade-powershell](../../includes/hdinsight-use-latest-powershell.md)]
* Use .NET SDK

For information on installing additional components on HDInsight cluster during the creation time, see :

* [Customize HDInsight clusters using Script Action (Windows)](/documentation/articles/hdinsight-hadoop-customize-cluster-v1/)

## <a name="use-azure-powershell"></a> Use Azure PowerShell
The following PowerShell code customizes a Hive configuration:

    # hive-site.xml configuration
    $hiveConfigValues = @{ "hive.metastore.client.socket.timeout"="90" }
    
    $config = New-AzureHDInsightClusterConfig `
        | Set-AzureHDInsightDefaultStorage `
            -StorageAccountName "$defaultStorageAccountName.blob.core.chinacloudapi.cn" `
            -StorageAccountKey $defaultStorageAccountKey `
        | Add-AzureHDInsightConfigValues `
            -Hive $hiveConfigValues 
    
    New-AzureHDInsightCluster `
        -Name $clusterName `
        -Location $location `
        -ClusterSizeInNodes $clusterSizeInNodes `
        -ClusterType Hadoop `
        -Version "3.2" `
        -Credential $httpCredential `
        -Config $config 

A complete working PowerShell script can be found in [Appendix-A](#appx-a:-powershell-sample).

Some more samples on customizing other configuration files:

    # hdfs-site.xml configuration
    $HdfsConfigValues = @{ "dfs.blocksize"="64m" } #default is 128MB in HDI 3.0 and 256MB in HDI 2.1

    # core-site.xml configuration
    $CoreConfigValues = @{ "ipc.client.connect.max.retries"="60" } #default 50

    # mapred-site.xml configuration
    $MapRedConfigValues = @{ "mapreduce.task.timeout"="1200000" } #default 600000

    # oozie-site.xml configuration
    $OozieConfigValues = @{ "oozie.service.coord.normal.default.timeout"="150" }  # default 120

For more information, see Azim Uddin's blog titled [Customizing HDInsight Cluster creation](http://blogs.msdn.com/b/bigdatasupport/archive/2014/04/15/customizing-hdinsight-cluster-provisioning-via-powershell-and-net-sdk.aspx).

## See also
* [Create Hadoop clusters in HDInsight][hdinsight-provision-cluster] provides instructions on how to create an HDInsight cluster by using other custom options.
* [Develop Script Action scripts for HDInsight][hdinsight-write-script]
* [Install and use R on HDInsight clusters][hdinsight-install-r]
* [Install and use Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install-v1/).
* [Install and use Giraph on HDInsight clusters](/documentation/articles/hdinsight-hadoop-giraph-install-v1/).

[hdinsight-install-r]: /documentation/articles/hdinsight-hadoop-r-scripts/
[hdinsight-write-script]: /documentation/articles/hdinsight-hadoop-script-actions/
[hdinsight-provision-cluster]: /documentation/articles/hdinsight-provision-clusters-v1/
[powershell-install-configure]: /documentation/articles/powershell-install-configure/


[img-hdi-cluster-states]: ./media/hdinsight-hadoop-customize-cluster-v1/HDI-Cluster-state.png "Stages during cluster creation"

## <a name="appx-a:-powershell-sample"></a> Appx-A: PowerShell sample
This PowerShell script creates an HDInsight cluster and customizes a Hive setting:

    ####################################
    # Set these variables
    ####################################
    #region - used for creating Azure service names
    $nameToken = "<ENTER AN ALIAS>" 
    #endregion

    #region - cluster user accounts
    $httpUserName = "admin"  #HDInsight cluster username
    $httpPassword = "<ENTER A PASSWORD>" #"<Enter a Password>"

    $sshUserName = "sshuser" #HDInsight ssh user name
    $sshPassword = "<ENTER A PASSWORD>" #"<Enter a Password>"
    #endregion

    ####################################
    # Service names and varialbes
    ####################################
    #region - service names
    $namePrefix = $nameToken.ToLower() + (Get-Date -Format "MMdd")

    $resourceGroupName = $namePrefix + "rg"
    $hdinsightClusterName = $namePrefix + "hdi"
    $defaultStorageAccountName = $namePrefix + "store"
    $defaultBlobContainerName = $hdinsightClusterName

    $location = "China East 2"
    #endregion

    # Treat all errors as terminating
    $ErrorActionPreference = "Stop"

    ####################################
    # Connect to Azure
    ####################################
    #region - Connect to Azure subscription
    Write-Host "`nConnecting to your Azure subscription ..." -ForegroundColor Green
    try{Get-AzureContext}
    catch{
            Clear-AzureProfile
            Import-AzurePublishSettingsFile -PublishSettingsFile path/to/<subscription name>-<date>-credentials.publishsettings
        }
    #endregion

    Write-Host "Creating the default storage account and default blob container ..."  -ForegroundColor Green
    New-AzureStorageAccount `
        -StorageAccountName $defaultStorageAccountName `
        -Location $location `
        -Type Standard_GRS

    $defaultStorageAccountKey = Get-AzureStorageAccountKey `
                                    -StorageAccountName $defaultStorageAccountName |  %{ $_.Primary }
    $defaultStorageContext = New-AzureStorageContext `
                                    -StorageAccountName $defaultStorageAccountName `
                                    -StorageAccountKey $defaultStorageAccountKey
    New-AzureStorageContainer `
        -Name $defaultBlobContainerName `
        -Context $defaultStorageContext #use the cluster name as the container name

    ####################################
    # Create a configuration object
    ####################################
    $hiveConfigValues = @{ "hive.metastore.client.socket.timeout"="90" }

    $config = New-AzureHDInsightClusterConfig `
        | Set-AzureHDInsightDefaultStorage `
            -StorageAccountName "$defaultStorageAccountName.blob.core.chinacloudapi.cn" `
            -StorageAccountKey $defaultStorageAccountKey `
        | Add-AzureHDInsightConfigValues `
            -Hive $hiveConfigValues 

    ####################################
    # Create an HDInsight cluster
    ####################################
    $httpPW = ConvertTo-SecureString -String $httpPassword -AsPlainText -Force
    $httpCredential = New-Object System.Management.Automation.PSCredential($httpUserName,$httpPW)

    $sshPW = ConvertTo-SecureString -String $sshPassword -AsPlainText -Force
    $sshCredential = New-Object System.Management.Automation.PSCredential($sshUserName,$sshPW)

    New-AzureHDInsightCluster `
        -Name $hdinsightClusterName `
        -Location $location `
        -ClusterSizeInNodes 1 `
        -ClusterType Hadoop `
        -Version "3.2" `
        -Credential $httpCredential `
        -Config $config

    ####################################
    # Verify the cluster
    ####################################
    Get-AzureHDInsightCluster -Name $hdinsightClusterName

    #endregion
