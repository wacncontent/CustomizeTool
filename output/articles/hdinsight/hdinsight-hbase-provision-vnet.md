<properties
    pageTitle="Create HBase clusters in a Virtual Network | Azure"
    description="Get started using HBase in Azure HDInsight. Learn how to create HDInsight HBase clusters on Azure Virtual Network."
    keywords=""
    services="hdinsight,virtual-network"
    documentationcenter=""
    author="mumian"
    manager="jhubbard"
    editor="cgronlun" />
<tags
    ms.assetid="8de8e446-f818-4e61-8fad-e9d38421e80d"
    ms.service="hdinsight"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="big-data"
    ms.date="11/18/2016"
    wacn.date=""
    ms.author="jgao" />

# Create HBase clusters in Azure Virtual Network
Learn how to create Azure HDInsight HBase clusters in an [Azure Virtual Network][1].

With virtual network integration, HBase clusters can be deployed to the same virtual network as your applications so that applications can communicate with HBase directly. The benefits include:

* Direct connectivity of the web application to the nodes of the HBase cluster, which enables communication via HBase Java remote procedure call (RPC) APIs.
* Improved performance by not having your traffic go over multiple gateways and load-balancers.
* The ability to process sensitive information in a more secure manner without exposing a public endpoint.

### Prerequisites
Before you begin this tutorial, you must have the following:

* **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).
* **A workstation with Azure PowerShell**. See [Install and use Azure PowerShell](/documentation/articles/powershell-install-configure/).

## Create HBase cluster into virtual network
In this section, you create a Linux-based HBase cluster with the dependent Azure Storage account in an Azure virtual network using an [Azure Resource Manager template](/documentation/articles/resource-group-template-deploy/). For other cluster creation methods and understanding the settings, see [Create HDInsight clusters](/documentation/articles/hdinsight-provision-clusters-v1/). For more information about using a template to create Hadoop clusters in HDInsight, see [Create Hadoop clusters in HDInsight using Azure Resource Manager templates](/documentation/articles/hdinsight-hadoop-create-windows-clusters-arm-templates/)

> [AZURE.NOTE]
> Some properties have been hard-coded into the template. For example:
>
> * **Location**: China East 2
> * __Cluster version: 3.4
> * **Cluster worker node count**: 4
> * **Default storage account**: a unique string
> * **Virtual network name**: &lt;Cluster Name>-vnet
> * **Virtual network address space**: 10.0.0.0/16
> * **Subnet name**: subnet1
> * **Subnet address range**: 10.0.0.0/24
>
> &lt;Cluster Name> is replaced with the cluster name you provide when using the template.
>
>

1. Click the following image to open the template in the Azure portal. The template is located in [Azure QuickStart Templates](https://azure.microsoft.com/resources/templates/101-hdinsight-hbase-linux-vnet/).

    <a href="https://portal.azure.cn/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F101-hdinsight-hbase-linux-vnet%2Fazuredeploy.json" target="_blank"><img src="https://acom.azurecomcdn.net/80C57D/cdn/mediahandler/docarticles/dpsmedia-prod/azure.microsoft.com/documentation/articles/hdinsight-hbase-tutorial-get-started-v1/20160201111850/deploy-to-azure.png" alt="Deploy to Azure"></a>
2. From the **Custom deployment** blade, enter the following:

   * **Subscription**: Select an Azure subscription used to create the HDInsight cluster, the dependent Storage account and the Azure virtual network.
   * **Resource group**: Select **Create new**, and specify a new resource group name.
   * **Location**: Select a location for the resource group.
   * **ClusterName**: Enter a name for the Hadoop cluster to be created.
   * **Cluster login name and password**: The default login name is **admin**.
   * **SSH username and password**: The default username is **sshuser**.  You can rename it.
   * **I agree to the terms and the conditions stated above**: (Select)
3. Click **Purchase**. It takes about around 20 minutes to create a cluster. Once the cluster is created, you can click the cluster blade in the portal to open it.

After you complete the tutorial, you might want to delete the cluster. With HDInsight, your data is stored in Azure Storage, so you can safely delete a cluster when it is not in use. You are also charged for an HDInsight cluster, even when it is not in use. Since the charges for the cluster are many times more than the charges for storage, it makes economic sense to delete clusters when they are not in use. For the instructions of deleting a cluster, see [Manage Hadoop clusters in HDInsight by using the Azure portal](/documentation/articles/hdinsight-administer-use-management-portal-v1/#delete-clusters).

To begin working with your new HBase cluster, you can use the procedures found in [Get started using HBase with Hadoop in HDInsight](/documentation/articles/hdinsight-hbase-tutorial-get-started-v1/).

## Connect to the HBase cluster using HBase Java RPC APIs
1. Create an infrastructure as a service (IaaS) virtual machine into the same Azure virtual network and the same subnet. For instructions on creating a new IaaS virtual machine, see [Create a Virtual Machine Running Windows Server](/documentation/articles/virtual-machines-windows-hero-tutorial/). When following the steps in this document, you must use the following for the Network configuration:

   * **Virtual network**: &lt;Cluster name>-vnet
   * **Subnet**: subnet1

   > [AZURE.IMPORTANT]
   > Replace &lt;Cluster name> with the name you used when creating the HDInsight cluster in previous steps.
   >
   >

   Using these values, the virtual machine is placed in the same virtual network and subnet as the HDInsight cluster. This configuration allows them to directly communicate with each other. There is a way to create an HDInsight cluster with an empty edge node. The edge node can be used to manage the cluster.  For more information, see [Use empty edge nodes in HDInsight](/documentation/articles/hdinsight-apps-use-edge-node/).

2. When using a Java application to connect to HBase remotely, you must use the fully qualified domain name (FQDN). To determine this, you must get the connection-specific DNS suffix of the HBase cluster. To do that, you can use one of the following methods:

   * Use a Web browser to make an Ambari call:

     Browse to https://&lt;ClusterName>.azurehdinsight.cn/api/v1/clusters/&lt;ClusterName>/hosts?minimal_response=true. It turns a JSON file with the DNS suffixes.
   * Use the Ambari website:

     1. Browse to  https://&lt;ClusterName>.azurehdinsight.cn.
     2. Click **Hosts** from the top menu.
   * Use Curl to make REST calls:

         curl -u <username>:<password> -k https://<clustername>.azurehdinsight.cn/ambari/api/v1/clusters/<clustername>.azurehdinsight.cn/services/hbase/components/hbrest

     In the JavaScript Object Notation (JSON) data returned, find the "host_name" entry. This contains the FQDN for the nodes in the cluster. For example:

         ...
         "host_name": "wordkernode0.<clustername>.b1.chinacloudapp.cn
         ...

     The portion of the domain name beginning with the cluster name is the DNS suffix. For example, mycluster.b1.chinacloudapp.cn.
   * Use Azure PowerShell

     Use the following Azure PowerShell script to register the **Get-ClusterDetail** function, which can be used to return the DNS suffix:

         function Get-ClusterDetail(
             [String]
             [Parameter( Position=0, Mandatory=$true )]
             $ClusterDnsName,
             [String]
             [Parameter( Position=1, Mandatory=$true )]
             $Username,
             [String]
             [Parameter( Position=2, Mandatory=$true )]
             $Password,
             [String]
             [Parameter( Position=3, Mandatory=$true )]
             $PropertyName
             )
         {
         <#
             .SYNOPSIS
              Displays information to facilitate an HDInsight cluster-to-cluster scenario within the same virtual network.
             .Description
              This command shows the following 4 properties of an HDInsight cluster:
              1. ZookeeperQuorum (supports only HBase type cluster)
                 Shows the value of HBase property "hbase.zookeeper.quorum".
              2. ZookeeperClientPort (supports only HBase type cluster)
                 Shows the value of HBase property "hbase.zookeeper.property.clientPort".
              3. HBaseRestServers (supports only HBase type cluster)
                 Shows a list of host FQDNs that run the HBase REST server.
              4. FQDNSuffix (supports all cluster types)
                 Shows the FQDN suffix of hosts in the cluster.
             .EXAMPLE
              Get-ClusterDetail -ClusterDnsName {clusterDnsName} -Username {username} -Password {password} -PropertyName ZookeeperQuorum
              This command shows the value of HBase property "hbase.zookeeper.quorum".
             .EXAMPLE
              Get-ClusterDetail -ClusterDnsName {clusterDnsName} -Username {username} -Password {password} -PropertyName ZookeeperClientPort
              This command shows the value of HBase property "hbase.zookeeper.property.clientPort".
             .EXAMPLE
              Get-ClusterDetail -ClusterDnsName {clusterDnsName} -Username {username} -Password {password} -PropertyName HBaseRestServers
              This command shows a list of host FQDNs that run the HBase REST server.
             .EXAMPLE
              Get-ClusterDetail -ClusterDnsName {clusterDnsName} -Username {username} -Password {password} -PropertyName FQDNSuffix
              This command shows the FQDN suffix of hosts in the cluster.
         #>

             $DnsSuffix = ".azurehdinsight.cn"

             $ClusterFQDN = $ClusterDnsName + $DnsSuffix
             $webclient = new-object System.Net.WebClient
             $webclient.Credentials = new-object System.Net.NetworkCredential($Username, $Password)

             if($PropertyName -eq "ZookeeperQuorum")
             {
                 $Url = "https://" + $ClusterFQDN + "/ambari/api/v1/clusters/" + $ClusterFQDN + "/configurations?type=hbase-site&tag=default&fields=items/properties/hbase.zookeeper.quorum"
                 $Response = $webclient.DownloadString($Url)
                 $JsonObject = $Response | ConvertFrom-Json
                 Write-host $JsonObject.items[0].properties.'hbase.zookeeper.quorum'
             }
             if($PropertyName -eq "ZookeeperClientPort")
             {
                 $Url = "https://" + $ClusterFQDN + "/ambari/api/v1/clusters/" + $ClusterFQDN + "/configurations?type=hbase-site&tag=default&fields=items/properties/hbase.zookeeper.property.clientPort"
                 $Response = $webclient.DownloadString($Url)
                 $JsonObject = $Response | ConvertFrom-Json
                 Write-host $JsonObject.items[0].properties.'hbase.zookeeper.property.clientPort'
             }
             if($PropertyName -eq "HBaseRestServers")
             {
                 $Url1 = "https://" + $ClusterFQDN + "/ambari/api/v1/clusters/" + $ClusterFQDN + "/configurations?type=hbase-site&tag=default&fields=items/properties/hbase.rest.port"
                 $Response1 = $webclient.DownloadString($Url1)
                 $JsonObject1 = $Response1 | ConvertFrom-Json
                 $PortNumber = $JsonObject1.items[0].properties.'hbase.rest.port'

                 $Url2 = "https://" + $ClusterFQDN + "/ambari/api/v1/clusters/" + $ClusterFQDN + "/services/hbase/components/hbrest"
                 $Response2 = $webclient.DownloadString($Url2)
                 $JsonObject2 = $Response2 | ConvertFrom-Json
                 foreach ($host_component in $JsonObject2.host_components)
                 {
                     $ConnectionString = $host_component.HostRoles.host_name + ":" + $PortNumber
                     Write-host $ConnectionString
                 }
             }
             if($PropertyName -eq "FQDNSuffix")
             {
                 $Url = "https://" + $ClusterFQDN + "/ambari/api/v1/clusters/" + $ClusterFQDN + "/home/features/YARN/components/RESOURCEMANAGER"
                 $Response = $webclient.DownloadString($Url)
                 $JsonObject = $Response | ConvertFrom-Json
                 $FQDN = $JsonObject.host_components[0].HostRoles.host_name
                 $pos = $FQDN.IndexOf(".")
                 $Suffix = $FQDN.Substring($pos + 1)
                 Write-host $Suffix
             }
         }

     After running the Azure PowerShell script, use the following command to return the DNS suffix by using the **Get-ClusterDetail** function. Specify your HDInsight HBase cluster name, admin name, and admin password when using this command.

         Get-ClusterDetail -ClusterDnsName <yourclustername> -PropertyName FQDNSuffix -Username <clusteradmin> -Password <clusteradminpassword>

     This will return the DNS suffix. For example, **yourclustername.b4.internal.chinacloudapp.cn**.
   * Use RDP

     You can also use Remote Desktop to connect to the HBase cluster (you will be connected to the head node) and run **ipconfig** from a command prompt to obtain the DNS suffix. For instructions on enabling Remote Desktop Protocol (RDP) and connecting to the cluster by using RDP, see [Manage Hadoop clusters in HDInsight using the Azure portal][hdinsight-admin-portal].

     ![hdinsight.hbase.dns.surffix][img-dns-surffix]

<!--
3.    Change the primary DNS suffix configuration of the virtual machine. This enables the virtual machine to automatically resolve the host name of the HBase cluster without explicit specification of the suffix. For example, the *workernode0* host name will be correctly resolved to workernode0 of the HBase cluster.

    To make the configuration change:

    1. RDP into the virtual machine.
    2. Open **Local Group Policy Editor**. The executable is gpedit.msc.
    3. Expand **Computer Configuration**, expand **Administrative Templates**, expand **Network**, and then click **DNS Client**.
    - Set **Primary DNS Suffix** to the value obtained in step 2:

        ![hdinsight.hbase.primary.dns.suffix][img-primary-dns-suffix]
    4. Click **OK**.
    5. Reboot the virtual machine.
-->

To verify that the virtual machine can communicate with the HBase cluster, use the command `ping headnode0.<dns suffix>` from the virtual machine. For example, ping headnode0.mycluster.b1.chinacloudapp.cn.

To use this information in a Java application, you can follow the steps in [Use Maven to build Java applications that use HBase with HDInsight (Hadoop)](/documentation/articles/hdinsight-hbase-build-java-maven/) to create an application. To have the application connect to a remote HBase server, modify the **hbase-site.xml** file in this example to use the FQDN for Zookeeper. For example:

    <property>
        <name>hbase.zookeeper.quorum</name>
        <value>zookeeper0.<dns suffix>,zookeeper1.<dns suffix>,zookeeper2.<dns suffix></value>
    </property>

> [AZURE.NOTE]
> For more information on name resolution in Azure virtual networks, including how to use your own DNS server, see [Name Resolution (DNS)](/documentation/articles/virtual-networks-name-resolution-for-vms-and-role-instances/).
>
>

## Next steps
In this tutorial you learned how to create an HBase cluster. To learn more, see:

* [Get started with HDInsight](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1/)
* [Use empty edge nodes in HDInsight](/documentation/articles/hdinsight-apps-use-edge-node/)
* [Configure HBase replication in HDInsight](/documentation/articles/hdinsight-hbase-geo-replication/)
* [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters-v1/)
* [Get started using HBase with Hadoop in HDInsight](/documentation/articles/hdinsight-hbase-tutorial-get-started-v1/)
* [Analyze Twitter sentiment with HBase in HDInsight](/documentation/articles/hdinsight-hbase-analyze-twitter-sentiment/)
* [Virtual Network Overview][vnet-overview]

[1]: http://azure.microsoft.com/services/networking/
[2]: http://technet.microsoft.com/zh-cn/library/ee176961.aspx
[3]: http://technet.microsoft.com/zh-cn/library/hh847889.aspx

[hbase-get-started]: /documentation/articles/hdinsight-hbase-tutorial-get-started-v1/
[hbase-twitter-sentiment]: /documentation/articles/hdinsight-hbase-analyze-twitter-sentiment/
[vnet-overview]: /documentation/articles/virtual-networks-overview/
[vm-create]: /documentation/articles/virtual-machines-windows-hero-tutorial/

[azure-portal]: https://portal.azure.cn
[azure-create-storageaccount]: /documentation/articles/storage-create-storage-account/
[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: /pricing/member-offers/
[azure-trial]: /pricing/1rmb-trial/

[hdinsight-admin-powershell]: /documentation/articles/hdinsight-administer-use-powershell/
[hdinsight-admin-portal]: /documentation/articles/hdinsight-administer-use-management-portal-v1/#connect-to-clusters-using-rdp

[hdinsight-powershell-reference]: https://msdn.microsoft.com/zh-cn/library/dn858087.aspx


[twitter-streaming-api]: https://dev.twitter.com/docs/streaming-apis
[twitter-statuses-filter]: https://dev.twitter.com/docs/api/1.1/post/statuses/filter


[powershell-install]: /documentation/articles/powershell-install-configure/


[hdinsight-customize-cluster]: /documentation/articles/hdinsight-hadoop-customize-cluster-v1/
[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters-v1/
[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1/
[hdinsight-storage-powershell]: /documentation/articles/hdinsight-hadoop-use-blob-storage/#powershell
[hdinsight-analyze-flight-delay-data]: /documentation/articles/hdinsight-analyze-flight-delay-data/
[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage/
[hdinsight-use-sqoop]: /documentation/articles/hdinsight-use-sqoop/
[hdinsight-power-query]: /documentation/articles/hdinsight-connect-excel-power-query/
[hdinsight-hive-odbc]: /documentation/articles/hdinsight-connect-excel-hive-ODBC-driver/
[hdinsight-hbase-replication-dns]: /documentation/articles/hdinsight-hbase-geo-replication-configure-DNS/

[img-dns-surffix]: ./media/hdinsight-hbase-provision-vnet-v1/DNSSuffix.png
[img-primary-dns-suffix]: ./media/hdinsight-hbase-provision-vnet-v1/PrimaryDNSSuffix.png
[img-provision-cluster-page1]: ./media/hdinsight-hbase-provision-vnet-v1/hbasewizard1.png "Provision details for the new HBase cluster"
[img-provision-cluster-page5]: ./media/hdinsight-hbase-provision-vnet-v1/hbasewizard5.png "Use Script Action to customize an HBase cluster"

[azure-preview-portal]: https://portal.azure.cn
