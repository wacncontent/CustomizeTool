<!-- not suitable for Mooncake -->

<properties
	pageTitle="Provision HBase clusters on a Virtual Network | Azure"
	description="Get started using HBase in Azure HDInsight. Learn how to create HDInsight HBase clusters on Azure Virtual Network."
	keywords=""
	services="hdinsight,virtual-network"
	documentationCenter=""
	authors="mumian"
	manager="paulettm"
	editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="11/18/2015"
	wacn.date=""/>

# Provision HBase clusters on Azure Virtual Network 

Learn how to create Azure HDInsight HBase clusters on an [Azure Virtual Network][1].

[AZURE.INCLUDE [hdinsight-azure-preview-portal](../includes/hdinsight-azure-preview-portal.md)]

* [Provision HBase clusters on Azure Virtual Network](/documentation/articles/hdinsight-hbase-provision-vnet-v1)

With virtual network integration, HBase clusters can be deployed to the same virtual network as your applications so that applications can communicate with HBase directly. The benefits include:

- Direct connectivity of the web application to the nodes of the HBase cluster, which enables communication via HBase Java remote procedure call (RPC) APIs.
- Improved performance by not having your traffic go over multiple gateways and load-balancers.
- The ability to process sensitive information in a more secure manner without exposing a public endpoint.

##Prerequisites
Before you begin this tutorial, you must have the following:

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).

- **A workstation with Azure PowerShell**. See [Install and use Azure PowerShell](/documentation/articles/powershell-install-configure). For instructions, see [Install and configure Azure PowerShell](/documentation/articles/powershell-install-configure). To execute Azure PowerShell scripts, you must run Azure PowerShell as administrator and set the execution policy to *RemoteSigned*. See [Using the Set-ExecutionPolicy cmdlet][2].

	Before running Azure PowerShell scripts, make sure you are connected to your Azure subscription by using the following cmdlet:

		Add-AzureAccount

	If you have multiple Azure subscriptions, use the following cmdlet to set the current subscription:

		Select-AzureSubscription <AzureSubscriptionName>


## Provision an HBase cluster into a virtual network

Applications are typically made up of many components. In this tutorial, you will have:

- an Azure virtual network
- an Azure Storage Account
- an Azure HDInsight HBase Cluster
- (optional) an Azure virtual machine serving as a DNS server

Azure Resource Manager enables you to work with the resources in your application as a group. You can deploy, update or delete all of the resources for your application in a single, coordinated operation. You use a template for deployment and that template can work for different environments such as testing, staging and production. You can clarify billing for your organization by viewing the rolled-up costs for the entire group.

**To create a resource group**

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn).
2. Click **NEW**, click **Management**, and then click **Resource group**.
3. Type or select the following values:

	- **Resource group name**: Enter a name for the resource group.
	- **Subscription**: Select the Azure subscription used for this resource group.
	- **Resource group location**: Select an Azure data center.  This location doesn't have to match the HDInsight cluster location.

4. Click **Create**.

Before provisioning an HBase cluster, you need to have an Azure virtual network.

**To create a virtual network by using the Azure Management Portal**

1. Sign in to the [Portal](https://manage.windowsazure.cn).
2. Click **NEW**, click **Networking**, and then click **Virtual network**.
3. In **Select a deployment model**, select **Classic** if you will be using a Windows-based HDInsight cluster; select **Resource Manager** if you will be using a Linux-based HDInsight cluster. Finally, click **Create**.

    > [AZURE.NOTE] Windows-based clusters require a v1 (Classic) Virtual Network, while Linux-based clusters require a v2 (Azure Resource Manager,) Virtual Network. If you do not have the correct type of network, it will not be usable when you create the cluster.
    >
    > If you have resources on a Virtual Network that is not usable by the cluster you plan on creating, you can create a new Virtual Network that is usable by the cluster, and connect it to the incompatible Virtual Network. You can then create the cluster in the network version that it requires, and it will be able to access resources in the other network since the two are joined. For more information on connecting classic and new Virtual Networks, see [Connecting classic VNets to new VNets](/documentation/articles/virtual-networks-arm-asm-s2s).
    
4. Type or select the following values:

	- **Name**: The name of your virtual network.
	- **Address space**:  Choose an address space for the virtual network that is large enough to provide addresses for all nodes in the cluster. Otherwise the provision will fail. For walking through this tutorial, you can use the default values. Click **OK** to save the changes.
    
        > [AZURE.NOTE] If you will be using this Virtual Network with multiple HDInsight clusters, it is highly recommended to designate a single subnet for each cluster.
         
	- **Resource group**: Select the resource group you created earlier in the tutorial.
	- **Subscription**: Select the Azure subscription you like to use for this virtual network.
	- **Location** - The location must be the same as the HBase cluster that you will create.
    
        > [AZURE.NOTE] > Azure HDInsight supports only location-based virtual networks, and does not currently work with virtual networks based on affinity group.
        
    For information on using HDInsight with a Virtual Network, including specific configuration requirements for the Virtual Network, see [Extend HDInsight capbilities by using an Azure Virtual Network](/documentation/articles/hdinsight-extend-hadoop-virtual-network).

5. Click **Create**.

By default, the virtual network uses an internal Domain Name System (DNS) server provided by Azure. More advanced networking configurations with custom DNS servers are also supported. For detailed guidance, see [Name Resolution (DNS)](/documentation/articles/virtual-networks-name-resolution-for-vms-and-role-instances).

**(Optinoal) To add a DNS server virtual machine to the virtual network**

A DNS server is optional, but necessary in some cases.  The procedure has been documented in [Configure DNS between two Azure virtual networks][hdinsight-hbase-replication-dns]. Basically, you will need to perform these steps:

1. add an Azure virtual machine to the virtual network
2. set a static IP address for the virtual machine
3. add the DNS server role to the virtual machine
4. Assign the DNS server to the virtual network

**To provision an HBase cluster by using the Azure Management Portal**

> [AZURE.NOTE] For information on provisioning a new HBase cluster by using Azure PowerShell, see [Provision an HBase cluster using Azure PowerShell](#powershell).


**To create an HDInsight cluster**

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn).
2. Click **NEW**, Click **Data Analytics**, and then click **HDInsight**.

    ![Creating a new cluster in the Azure Management Portal](./media/hdinsight-provision-clusters-v1/HDI.CreateCluster.1.png "Creating a new cluster in the Azure Management Portal")

3. Type or select the following values:

  - **Cluster Name**: Enter a name for the cluster. A green check will appear beside the cluster name if the name is available.
  - **Cluster Type**: Select **HBase**.
  - **Cluster Operating System**: Select **Windows Server 2012 R2 Datacenter**.
  - **Subscription**: Select the Azure subscription that will be used for provision this cluster.
  - **Resource Group**: Select the resource group you created earlier in the tutorial.
  - **Credentials**: Configure the username and the password for the Hadoop user (HTTP user). If you enable remote desktop for the cluster, you will need to configure the remote desktop user username and password, and an account expiration date. Click **Select** at the bottom to save the changes.
  - **Data Source**: Select an existing or create a new Azure Storage account that will be used as the default file system for the cluster. The default name for the default container is the cluster name.  The location of the storage account also determine the location of the cluster.
  - **Node Pricing Tier**: For learning or evaluation purpose, select 1 region node to minimize the cost.

  	- **Selection Method**: Set this to **From all subscriptions** to enable browsing of storage accounts from all your subscriptions. Set this to **Access Key** if you want to enter the **Storage Name** and **Access Key** of an existing storage account.
  	- **Select storage account / Create New**: Click **Select storage account** to browse and select an existing storage account you want to associate with the cluster. Or, click **Create New** to create a new storage account. Use the field that appears to enter the name of the storage account. A green check will appear if the name is available.
    - **Choose Default Container**: Use this to enter the name of the default container to use for the cluster. While you can enter any name here, we recommend using the same name as the cluster so that you can easily recognize that the container is used for this specific cluster.
  	- **Location**: The geographic region that the storage account is in, or will be created in. This location will determine the cluster location.  The cluster and its default storage account must co-locate in the same Azure data center.

  - **Node Pricing Tiers**: Set the number of worker nodes that you need for the cluster. The estimated cost of the cluster will be shown within the blade.
	- **Optional Configuration**: For this tutorial, you only need to configure **Virtual Network**.  Select the virtual network you created earlier in the tutorial. Make sure you also select a subnet.

4. Click **Create**.


To begin working with your new HBase cluster, you can use the procedures found in [Get started using HBase with Hadoop in HDInsight](/documentation/articles/hdinsight-hbase-tutorial-get-started-v1).

##Connect to the HBase cluster provisioned in the virtual network by using HBase Java RPC APIs

1.	Provision an infrastructure as a service (IaaS) virtual machine into the same Azure virtual network and the same subnet. So both the virtual machine and the HBase cluster use the same internal DNS server to resolve host names. To do so, you must choose the **From Gallery** option, and select the virtual network instead of a data center. For instructions, see [Create a Virtual Machine Running Windows Server](/documentation/articles/virtual-machines-windows-tutorial-classic-portal). A standard Windows Server 2012 image with a small VM size is sufficient.

2.	When using a Java application to connect to HBase remotely, you must use the fully qualified domain name (FQDN). To determine this, you must get the connection-specific DNS suffix of the HBase cluster. To do that, use Curl to query Ambari, or use Remote Desktop to connect to the cluster.

	* **Curl** - Use the following command:

			curl -u <username>:<password> -k https://<clustername>.azurehdinsight.cn/ambari/api/v1/clusters/<clustername>.azurehdinsight.cn/services/hbase/components/hbrest

		In the JavaScript Object Notation (JSON) data returned, find the "host_name" entry. This will contain the FQDN for the nodes in the cluster. For example:

			...
			"host_name": "wordkernode0.<clustername>.b1.chinacloudapp.cn
			...

		The portion of the domain name beginning with the cluster name is the DNS suffix. For example, mycluster.b1.chinacloudapp.cn.

	* **Azure PowerShell** - Use the following Azure PowerShell script to register the **Get-ClusterDetail** function, which can be used to return the DNS suffix:

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
					$Url = "https://" + $ClusterFQDN + "/ambari/api/v1/clusters/" + $ClusterFQDN + "/services/yarn/components/resourcemanager"
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

	> [AZURE.NOTE] You can also use Remote Desktop to connect to the HBase cluster (you will be connected to the head node) and run **ipconfig** from a command prompt to obtain the DNS suffix. For instructions on enabling Remote Desktop Protocol (RDP) and connecting to the cluster by using RDP, see [Manage Hadoop clusters in HDInsight using the Azure Management Portal][hdinsight-admin-portal].
	>
	> ![hdinsight.hbase.dns.surffix][img-dns-surffix]


<!--
3.	Change the primary DNS suffix configuration of the virtual machine. This enables the virtual machine to automatically resolve the host name of the HBase cluster without explicit specification of the suffix. For example, the *workernode0* host name will be correctly resolved to workernode0 of the HBase cluster.

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

To use this information in a Java application, you can follow the steps in [Use Maven to build Java applications that use HBase with HDInsight (Hadoop)](/documentation/articles/hdinsight-hbase-build-java-maven) to create an application. To have the application connect to a remote HBase server, modify the **hbase-site.xml** file in this example to use the FQDN for Zookeeper. For example:

	<property>
    	<name>hbase.zookeeper.quorum</name>
    	<value>zookeeper0.<dns suffix>,zookeeper1.<dns suffix>,zookeeper2.<dns suffix></value>
	</property>

> [AZURE.NOTE] For more information on name resolution in Azure virtual networks, including how to use your own DNS server, see [Name Resolution (DNS)](/documentation/articles/virtual-networks-name-resolution-for-vms-and-role-instances).

##Provision an HBase cluster by using Azure PowerShell

**To provision an HBase cluster by using Azure PowerShell**

1. Open the Azure PowerShell Integrated Scripting Environment (ISE).
2. Copy and paste the following into the script pane:

		$hbaseClusterName = "<HBaseClusterName>"
		$hadoopUserName = "<HBaseClusterUsername>"
		$hadoopUserPassword = "<HBaseClusterUserPassword>"
		$location = "<HBaseClusterLocation>"  #i.e. "China North"
		$clusterSize = <HBaseClusterSize>  
		$resourceGroup = "<AzureResourceGroupName>"
		$vnetID = "<AzureVirtualNetworkID>"
		$subNetName = "<AzureVirtualNetworkSubNetName>"
		$storageAccountName = "<AzureStorageAccountName>" # Do not use the full name here
		$storageAccountKey = "<AzureStorageAccountKey>"
		$storageContainerName = "<AzureBlobStorageContainer>"

		$password = ConvertTo-SecureString $hadoopUserPassword -AsPlainText -Force
		$creds = New-Object System.Management.Automation.PSCredential ($hadoopUserName, $password)

		New-AzureHDInsightCluster -ResourceGroupName $resourceGroup `
		                          -ClusterName $hbaseClusterName `
				                    	-ClusterType HBase `
				                    	-Location $location `
				                    	-ClusterSizeInNodes $clusterSize `
		                          -HttpCredential $creds `
				                    	-VirtualNetworkId $vnetID `
				                    	-SubnetName $subNetName `
				                    	-DefaultStorageAccountName "$storageAccountName.blob.core.chinacloudapi.cn" `
				                    	-DefaultStorageAccountKey $storageAccountKey `
		                          -DefaultStorageContainer $storageContainerName


3. Click **Run Script**, or press **F5**.
4. To validate the cluster, you can either check the cluster from the Azure Management Portal, or run the following Azure PowerShell cmdlet from the bottom pane:

	Get-AzureHDInsightCluster

##Next steps

In this tutorial you learned how to provision an HBase cluster. To learn more, see:

- [Get started with HDInsight](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1)
- [Configure HBase replication in HDInsight](/documentation/articles/hdinsight-hbase-geo-replication)
- [Provision Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters-v1)
- [Get started using HBase with Hadoop in HDInsight](/documentation/articles/hdinsight-hbase-tutorial-get-started-v1)
- [Analyze Twitter sentiment with HBase in HDInsight](/documentation/articles/hdinsight-hbase-twitter-sentiment)
- [Virtual Network Overview][vnet-overview]


[1]: http://azure.microsoft.com/services/networking/
[2]: http://technet.microsoft.com/zh-cn/library/ee176961.aspx
[3]: http://technet.microsoft.com/zh-cn/library/hh847889.aspx

[hbase-get-started]: /documentation/articles/hdinsight-hbase-tutorial-get-started-v1
[hbase-twitter-sentiment]: /documentation/articles/hdinsight-hbase-twitter-sentiment
[vnet-overview]: /documentation/articles/networking/virtual-networks-overview
[vm-create]: /documentation/articles/virtual-machines-windows-tutorial-classic-portal

[azure-portal]: https://manage.windowsazure.cn
[azure-create-storageaccount]: /documentation/articles/storage-create-storage-account
[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: /pricing/member-offers/
[azure-trial]: /pricing/1rmb-trial/

[hdinsight-admin-powershell]: /documentation/articles/hdinsight-administer-use-powershell
[hdinsight-admin-portal]: /documentation/articles/hdinsight-administer-use-management-portal-v1#rdp

[hdinsight-powershell-reference]: https://msdn.microsoft.com/zh-cn/library/dn858087.aspx


[twitter-streaming-api]: https://dev.twitter.com/docs/streaming-apis
[twitter-statuses-filter]: https://dev.twitter.com/docs/api/1.1/post/statuses/filter


[powershell-install]: /documentation/articles/powershell-install-configure


[hdinsight-customize-cluster]: /documentation/articles/hdinsight-hadoop-customize-cluster-v1
[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters-v1
[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1
[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage
[hdinsight-analyze-flight-delay-data]: /documentation/articles/hdinsight-analyze-flight-delay-data
[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage
[hdinsight-use-sqoop]: /documentation/articles/hdinsight-use-sqoop
[hdinsight-power-query]: /documentation/articles/hdinsight-connect-excel-power-query
[hdinsight-hive-odbc]: /documentation/articles/hdinsight-connect-excel-hive-ODBC-driver
[hdinsight-hbase-replication-dns]: /documentation/articles/hdinsight-hbase-geo-replication-configure-DNS

[img-dns-surffix]: ./media/hdinsight-hbase-provision-vnet-v1/DNSSuffix.png
[img-primary-dns-suffix]: ./media/hdinsight-hbase-provision-vnet-v1/PrimaryDNSSuffix.png
[img-provision-cluster-page1]: ./media/hdinsight-hbase-provision-vnet-v1/hbasewizard1.png "Provision details for the new HBase cluster"
[img-provision-cluster-page5]: ./media/hdinsight-hbase-provision-vnet-v1/hbasewizard5.png "Use Script Action to customize an HBase cluster"

[azure-preview-portal]: https://manage.windowsazure.cn
