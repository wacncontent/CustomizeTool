<properties
   pageTitle="Create Hadoop clusters in HDInsight | Windows Azure"
   	description="Learn how to create clusters for Azure HDInsight by using the Azure Preview Portal, Azure PowerShell, a command line, or a .NET SDK."
   services="hdinsight"
   documentationCenter=""
   tags="azure-portal"
   authors="mumian"
   manager="paulettm"
   editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="09/29/2015"
	wacn.date=""/>

# Create Hadoop clusters in HDInsight

Learn how to plan for creating HDInsight clusters.

[AZURE.INCLUDE [selector](../includes/hdinsight-portal-management-selector.md)]

* [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters-v1)

* [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters-v1)

**Prerequisites:**

Before you begin the instructions in this article, you must have the following:

- An Azure subscription. See [Get Azure trial](/pricing/1rmb-trial/).


## Basic configuration options


- **Cluster name**

	Cluster name is used to identify a cluster. Cluster name must follow the following guidelines:

	- The field must be a string that contains between 3 and 63 characters
	- The field can contain only letters, numbers, and hyphens.

- **Subscription name**

	An HDInsight cluster is tied to one Azure subscription.

- **Resource group name**

	Applications are typically made up of many components, for example a web app, database, database server, storage, and 3rd party services. Azure Resource Manager (ARM) enables you to work with the resources in your application as a group, referred to as an Azure Resource Group. You can deploy, update, monitor or delete all of the resources for your application in a single, coordinated operation. You use a template for deployment and that template can work for different environments such as testing, staging and production. You can clarify billing for your organization by viewing the rolled-up costs for the entire group. For more information, see [Azure Resource Manager Overview](/documentation/articles/resource-group-overview).	
- **Operating system**

	You can create HDInsight clusters on one of the following two operating systems:
	- **HDInsight on Windows (Windows Server 2012 R2 Datacenter)**:


- **HDInsight version**

	It is used to determine the version of HDInsight to use for this cluster. For more information, see [Hadoop cluster versions and components in HDInsight](/documentation/articles/hdinsight-component-versioning/)

- **Cluster type** and **cluster size (a.k.a. data nodes)**

	HDInsight allows customers to deploy a variety of cluster types, for different data analytics workloads. Cluster types offered today are:

	- Hadoop clusters: for query and analysis workloads
	- HBase clusters:  for NoSQL workloads
	- Storm clusters: for real time event processing workloads

	![HDInsight clusters](./media/hdinsight-provision-clusters/hdinsight.clusters.png)

	> [AZURE.NOTE] *Azure HDInsight cluster* is also called *Hadoop clusters in HDInsight*, or *HDInsight cluster*. Sometimes, it is used interchangeably with *Hadoop cluster*. They all refer to the Hadoop clusters hosted in the Windows Azure environment.

	Within a given cluster type, there are different roles for the various nodes, which allow a customer to size those nodes in a given role appropriate to the details of their workload. For example, a Hadoop cluster can have its worker nodes created with a large amount of memory if the type of analytics being performed are memory intensive.

	![HDInsight Hadoop cluster roles](./media/hdinsight-provision-clusters/HDInsight.Hadoop.roles.png)

	Hadoop clusters for HDInsight are deployed with two roles:

	- Head node (2 nodes)
	- Data node (at least 1 node)

	![HDInsight Hadoop cluster roles](./media/hdinsight-provision-clusters/HDInsight.HBase.roles.png)

	HBase clusters for HDInsight are deployed with three roles:
	- Head servers (2 nodes)
	- Region servers (at least 1 node)
	- Master/Zookeeper nodes (3 nodes)

	![HDInsight Hadoop cluster roles](./media/hdinsight-provision-clusters/HDInsight.Storm.roles.png)

	Storm clusters for HDInsight are deployed with three roles:
	- Nimbus nodes (2 nodes)
	- Supervisor servers (at least 1 node)
	- Zookeeper nodes (3 nodes)


	Customers are billed for the usage of those nodes for the duration of the cluster’s life. Billing starts once a cluster is created and stops when the cluster is deleted (clusters can’t be de-allocated or put on hold). The cluster size affects the cluster price. For learning purposes, it is recommended to use 1 data node. For more information about HDInsight pricing, see [HDInsight pricing](/home/features/hdinsight/#price).


	>[AZURE.NOTE] The cluster size limit varies among Azure subscriptions. Contact billing support to increase the limit.

- **Region/virtual network (a.k.a. location)**

	![Azure regions](./media/hdinsight-provision-clusters/Azure.regions.png)

	For a list of supported regions, click the **Region** drop-down list on [HDInsight pricing](/home/features/hdinsight/#price).

- **Node size**

	![hdinsight vm node sizes](./media/hdinsight-provision-clusters/hdinsight.node.sizes.png)

	Select the VM size for the nodes. For more information, see [Sizes for Cloud Services](/documentation/articles/cloud-services-sizes-specs)

	Based on the choice of VMs, your cost might vary. HDInsight uses all standard-tier VMs for cluster nodes. For information on how VM sizes affect your prices, see <a href="/home/features/hdinsight/#price" target="_blank">HDInsight Pricing</a>.


- **HDInsight users**

	The HDInsight clusters allow you to configure two user accounts during provisioning:

	- HTTP user. The default user name is admin using the basic configuration on the Azure Management Portal.
	- RDP user (Windows clusters): It is used to connect to the cluster using RDP. When you create the account, you must set an expiration date that is within 90 days from today.



- **Azure storage account**

	The original HDFS uses of many local disks on the cluster. HDInsight uses Azure Blob storage instead for data storage. Azure Blob storage is a robust, general-purpose storage solution that integrates seamlessly with HDInsight. Through a Hadoop distributed file system (HDFS) interface, the full set of components in HDInsight can operate directly on structured or unstructured data in Blob storage. Storing data in Blob storage enables you to safely delete the HDInsight clusters that are used for computation without losing user data.

	During configuration, you must specify an Azure storage account and an Azure Blob storage container on the Azure storage account. Some creation process requires the Azure storage account and the Blob storage container created beforehand.  The Blob storage container is used as the default storage location by the cluster. Optionally, you can specify additional Azure Storage accounts (linked storage) that will be accessible by the cluster. In addition, the cluster can also access any Blob containers that are configured with full public read access or pulic read access for blobs only.  For more information on the restrict access, see [Manage Access to Azure Storage Resources](/documentation/articles/storage-manage-access-to-resources).

	![HDInsight storage](./media/hdinsight-provision-clusters/HDInsight.storage.png)

	>[AZURE.NOTE] A Blob storage container provides a grouping of a set of blobs as shown in the image:

	![Azure blob storage](./media/hdinsight-provision-clusters/Azure.blob.storage.jpg)


	>[AZURE.WARNING] Don't share one Blob storage container for multiple clusters. This is not supported.

	For more information on using secondary Blob stores, see [Using Azure Blob Storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage).

- **Hive/Oozie metastore**

	The metastore contains Hive and Oozie metadata, such as Hive tables, partitions, schemas, and columns. Using the metastore helps you to retain your Hive and Oozie metadata, so that you don't need to re-create Hive tables or Oozie jobs when you create a new cluster. By default, Hive uses an embedded Azure SQL database to store this information. The embedded database can't preserve the metadata when the cluster is deleted. For example, you have a cluster created with a Hive metastore. You created some Hive tables. After you delete the cluster, and recreat the cluster using the same Hive metastore, you will be able to see the Hive tables you created in the original cluster.

## Advanced configuration options

>[AZURE.NOTE] This section currently only apply to Windows base HDInsight clusters.

### Customize clusters using HDInsight cluster customization

Sometimes, you want to configure the configuration files.  Here are some of them.

- core-site.xml
- hdfs-site.xml
- mapred-site.xml
- yarn-site.xml
- hive-site.xml
- oozie-site.xml

The clusters can't retain the changes due to re-image.  For more information, see [Role Instance Restarts Due to OS Upgrades](http://blogs.msdn.com/b/kwill/archive/2012/09/19/role-instance-restarts-due-to-os-upgrades.aspx). To keep the changes through the clusters' lifetime, you can use HDInsight cluster customization during the creation process.

The following is an Azure PowerShell script example of customizing a Hive configuration:

	# hive-site.xml configuration
	$hiveConfigValues = new-object 'Microsoft.WindowsAzure.Management.HDInsight.Cmdlet.DataObjects.AzureHDInsightHiveConfiguration'
	$hiveConfigValues.Configuration = @{ "hive.metastore.client.socket.timeout"="90" } #default 60

	$config = New-AzureHDInsightClusterConfig `
	            -ClusterSizeInNodes $clusterSizeInNodes `
	            -ClusterType $clusterType `
	          | Set-AzureHDInsightDefaultStorage `
	            -StorageAccountName $defaultStorageAccount `
	            -StorageAccountKey $defaultStorageAccountKey `
	            -StorageContainerName $defaultBlobContainer `
	          | Add-AzureHDInsightConfigValues `
	            -Hive $hiveConfigValues

	New-AzureHDInsightCluster -Name $clusterName -Location $location -Credential $credential -OSType Windows -Config $config

Some more samples on customizing other configuration files:

	# hdfs-site.xml configuration
	$HdfsConfigValues = @{ "dfs.blocksize"="64m" } #default is 128MB in HDI 3.0 and 256MB in HDI 2.1

	# core-site.xml configuration
	$CoreConfigValues = @{ "ipc.client.connect.max.retries"="60" } #default 50

	# mapred-site.xml configuration
	$MapRedConfigValues = new-object 'Microsoft.WindowsAzure.Management.HDInsight.Cmdlet.DataObjects.AzureHDInsightMapReduceConfiguration'
	$MapRedConfigValues.Configuration = @{ "mapreduce.task.timeout"="1200000" } #default 600000

	# oozie-site.xml configuration
	$OozieConfigValues = new-object 'Microsoft.WindowsAzure.Management.HDInsight.Cmdlet.DataObjects.AzureHDInsightOozieConfiguration'
	$OozieConfigValues.Configuration = @{ "oozie.service.coord.normal.default.timeout"="150" }  # default 120

For more information, see Azim Uddin's blog titled [Customizing HDInsight Cluster creationg](http://blogs.msdn.com/b/bigdatasupport/archive/2014/04/15/customizing-hdinsight-cluster-provisioning-via-powershell-and-net-sdk.aspx).




### Customize clusters using Script action

You can install additional components or customize cluster configuration by using scripts during creation. Such scripts are invoked via **Script Action**, which is a configuration option that can be used from the preview portal, HDInsight Windows PowerShell cmdlets, or the HDInsight .NET SDK. For more information, see [Customize HDInsight cluster using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster).


### Use Azure virtual networks

[Azure Virtual Network](/documentation/services/networking/) allows you to create a secure, persistent network containing the resources you need for your solution. A virtual network allows you to:

* Connect cloud resources together in a private network (cloud-only).

	![diagram of cloud-only configuration](./media/hdinsight-provision-clusters/hdinsight-vnet-cloud-only.png)

* Connect your cloud resources to your local data-center network (site-to-site or point-to-site) by using a virtual private network (VPN).

	Site-to-site configuration allows you to connect multiple resources from your data center to the Azure virtual network by using a hardware VPN or the Routing and Remote Access Service.

	![diagram of site-to-site configuration](./media/hdinsight-provision-clusters/hdinsight-vnet-site-to-site.png)

	Point-to-site configuration allows you to connect a specific resource to the Azure virtual network by using a software VPN.

	![diagram of point-to-site configuration](./media/hdinsight-provision-clusters/hdinsight-vnet-point-to-site.png)

For more information on Virtual Network features, benefits, and capabilities, see the [Azure Virtual Network overview](/documentation/articles/virtual-networks-overview).

> [AZURE.NOTE] You must create the Azure virtual network before provisioning an HDInsight cluster. For more information, see [Create a Hadoop cluster into a virtual network](/documentation/articles/hdinsight-hbase-provision-vnet#provision-an-hbase-cluster-into-a-virtual-network).
>
> Azure HDInsight only supports location-based Virtual Networks, and does not currently work with Affinity Group-based Virtual Networks. Use Azure PowerShell cmdlet Get-AzureVNetConfig to check whether an existing Azure virtual network is location-based. If your virtual network is not location-based, you have the following options:
>
> - Export the existing Virtual Network configuration and then create a new Virtual Network. All new Virtual Networks are location based  by default.
> - Migrate to a location-based Virtual Network.  See [Migrate existing services to regional scope](http://azure.microsoft.com/blog/2014/11/26/migrating-existing-services-to-regional-scope/).
>
> It is highly recommended to designate a single subnet for one cluster.

<a id="portal"></a>
## Create using the Management Portal

HDInsight clusters use an Azure Blob storage container as the default file system. An Azure Storage account located on the same data center is required before you can create an HDInsight cluster. For more information, see [Use Azure Blob Storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage). For details on creating an Azure Storage account, see [How to Create a Storage Account](/documentation/articles/storage-create-storage-account).


> [AZURE.NOTE] Currently, only the **China North**, and **China East** regions can host HDInsight clusters.

**To create an HDInsight cluster**

1. Sign in to the [Azure Management Portal][azure-management-portal].
2. Click **+ NEW** on the bottom of the page, click **DATA SERVICES**, click **HDINSIGHT**, and then click **CUSTOM CREATE**.
3. On the **Cluster Details** page, type or choose the following values:

	![Provide Hadoop HDInsight cluster details][image-customprovision-page1]

    <table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>Cluster Name</td>
			<td><p>Name the cluster. </p>
				<ul>
				<li>The Domain Name System (DNS) name must start and end with an alphanumeric character and may contain dashes.</li>
				<li>The field must be a string from 3 to 63 characters.</li>
				</ul></td></tr>
		<tr><td>Cluster Type</td>
			<td>For cluster type, select <strong>Hadoop</strong>.</td></tr>
		<tr><td>HDInsight Version</td>
			<td>Choose the version. For Hadoop, the default is HDInsight version 3.1, which uses Hadoop 2.4.</td></tr>
		</table>

	Enter or select the values as shown in the table and then click the right arrow.

4. On the **Configure Cluster** page, enter or select the following values:

	![Provide Hadoop HDInsight cluster details](./media/hdinsight-provision-clusters/HDI.CustomProvision.Page2.png)

	<table border="1">
	<tr><th>Name</th><th>Value</th></tr>
	<tr><td>Data Nodes</td><td>Number of data nodes you want to deploy. For testing purposes, create a single-node cluster. <br />The cluster size limit varies for Azure subscriptions. Contact Azure billing support to increase the limit.</td></tr>
	<tr><td>Region/Virtual Network</td><td><p>Choose the same region as the Storage account you created in the last procedure. HDInsight requires the Storage account to be located in the same region. Later in the configuration, you can choose only a Storage account that is in the same region that you specified here.</p><p> The available regions are: <strong>China East</strong>, <strong>China North</strong>. <br/>If you have created an Azure Virtual Network, you can select the network that the HDInsight cluster will be configured to use.</p><p>For more information on creating an Azure Virtual Network, see [Virtual Network configuration tasks](http://msdn.microsoft.com/zh-cn/library/azure/jj156206.aspx).</p></td></tr>
	<tr><td>Head Node Size</td><td><p>Select a virtual machine (VM) size for the head node.</p></td></tr>
	<tr><td>Data Node Size</td><td><p>Select a VM size for the data nodes.</p></td></tr>
	</table>

	>[AZURE.NOTE] Based on the choice of VMs, your cost might vary. HDInsight uses all standard-tier VMs for cluster nodes. For information on how VM sizes affect your prices, see <a href="/home/features/hdinsight/#price" target="_blank">HDInsight Pricing</a>.	


5. On the **Configure Cluster User** page, provide the following values:

    ![Provide Hadoop HDInsight cluster user and metastore details](./media/hdinsight-provision-clusters/HDI.CustomProvision.Page3.png)

    <table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>HTTP User Name</td>
			<td>Specify the HDInsight cluster user name.</td></tr>
		<tr><td>HTTP Password/Confirm Password</td>
			<td>Specify the HDInsight cluster user password.</td></tr>
		<tr><td>Enable remote desktop for cluster</td>
			<td>Select this check box to specify a username, password, and expiry date for a remote desktop user that can remote into the cluster nodes, once it is provisioned. You can also enable remote desktop later, after the cluster is provisioned. For instructions, see <a href="/documentation/articles/hdinsight-administer-use-management-portal-v1/#rdp" target="_blank">Connect to HDInsight clusters using RDP</a>.</td></tr>
		<tr><td>Enter the Hive/Oozie Metastore</td>
			<td>Select this check box to specify a SQL database on the same data center as the cluster, to be used as the Hive/Oozie metastore. If you select this checkbox, you must spcecify details about the Azure SQL database in the subsequent pages of the wizard. This is useful if you want to retain the metadata about Hive/Oozie jobs even after a cluster has been deleted.</td></tr>
		</td></tr>		
	</table>

	Click the right arrow.

6. On the **Configure Hive/Oozie Metastore** page, provide the following values:

    ![Provide Hadoop HDInsight cluster user](./media/hdinsight-provision-clusters/HDI.CustomProvision.Page4.png)

	Specify an Azure SQL database that will be used as the Hive/Oozie metastore. You can specify the same database for both Hive and Oozie metastores. This SQL database must be in the same data center as the HDInsight cluster. The list box lists only the SQL databases in the same data center that you specified on the <strong>Cluster Details</strong> page. Also specify the username and password to connect to the Azure SQL database you selected.

    >[AZURE.NOTE] The Azure SQL database used for the metastore must allow connectivity to other Azure services, including Azure HDInsight. On the Azure SQL database dashboard, on the right side, click the server name. This is the server on which the SQL database instance is running. Once you are on the server view, click **Configure**, and then for **Azure Services**, click **Yes**, and then click **Save**.

    Click the right arrow.


7. On the **Storage Account** page, provide the following values:

    ![Provide storage account for Hadoop HDInsight cluster](./media/hdinsight-provision-clusters/HDI.CustomProvision.Page5.png)

	<table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>Storage Account</td>
			<td>Specify the Azure Storage account that will be used as the default file system for the HDInsight cluster. You can choose one of the three options:
			<ul>
				<li><strong>Use Existing Storage</strong></li>
				<li><strong>Create New Storage</strong></li>
				<li><strong>Use Storage from Another Subscription</strong></li>
			</ul>
			</td></tr>
		<tr><td>Account Name</td>
			<td><ul>
				<li>If you chose to use existing storage, for <strong>Account Name</strong>, select an existing Storage account. The drop-down lists only the Storage accounts located in the same data center where you chose to provision the cluster.</li>
				<li>If you chose the <strong>Create New Storage</strong> or <strong>Use Storage from Another Subscription</strong> option, you must provide the Storage account name.</li>
			</ul></td></tr>
		<tr><td>Account Key</td>
			<td>If you chose the <strong>Use Storage from Another Subscription</strong> option, specify the account key for that Storage account.</td></tr>
		<tr><td>Default Container</td>
			<td><p>Specify the default container on the Storage account that is used as the default file system for the HDInsight cluster. If you chose <strong>Use Existing Storage</strong> for the <strong>Storage Account</strong> field, and there are no existing containers in that account, the container is created by default with the same name as the cluster name. If a container with the name of the cluster already exists, a sequence number will be appended to the container name. For example, mycontainer1, mycontainer2, and so on. However, if the existing Storage account has a container with a name different from the cluster name you specified, you can use that container as well.</p>
            <p>If you chose to create new storage or use storage from another Azure subscription, you must specify the default container name.</p>
        </td></tr>
		<tr><td>Additional Storage Accounts</td>
			<td>HDInsight supports multiple Storage accounts. There is no limit on the additional Storage accounts that can be used by a cluster. However, if you create a cluster by using the Azure Management Portal, you have a limit of seven due to the UI constraints. Each additional Storage account you specify adds an extra **Storage Account** page to the wizard where you can specify the account information. For example, in the screenshot above, one additional Storage account is selected, and hence page 5 is added to the dialog.</td></tr>
	</table>

	Click the right arrow.

7. If you chose to configure additional storage for the cluster, on the **Storage Account** page, enter the account information for the additional Storage account:

	![Provide additional storage details for HDInsight cluster](./media/hdinsight-provision-clusters/HDI.CustomProvision.Page6.png)

    Here again, you have the option to choose from existing storage, create new storage, or use storage from another Azure subscription. The procedure to provide the values is similar to the previous step.

    > [AZURE.NOTE] Once an Azure Storage account is chosen for your HDInsight cluster, you can neither delete the account nor change the account to a different account.

8. On the **Script Actions** page, click **add script action** to provide details about the custom script that you want to run to customize a cluster, as the cluster is being created. For more information, see [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster). 
	
	![Configure Script Action to customize an HDInsight cluster](./media/hdinsight-provision-clusters/HDI.CustomProvision.Page7.png)

	<table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>Name</td>
			<td>Specify a name for the script action.</td></tr>
		<tr><td>Script URI</td>
			<td>Specify the Uniform Resource Identifier (URI) to the script that is invoked to customize the cluster.</td></tr>
		<tr><td>Node Type</td>
			<td>Specify the nodes on which the customization script is run. You can choose <b>All Nodes</b>, <b>Head nodes only</b>, or <b>Data nodes only</b>.
		<tr><td>Parameters</td>
			<td>Specify the parameters, if required by the script.</td></tr>
	</table>

	You can add more than one script action to install multiple components on the cluster. After you have added the scripts, click the check mark to start provisioning the cluster.


## Create using Azure PowerShell
Azure PowerShell is a powerful scripting environment that you can use to control and automate the deployment and management of your workloads in Azure. This section provides instructions on how to provision an HDInsight cluster by using Azure PowerShell. For information on configuring a workstation to run HDInsight Windows PowerShell cmdlets, see [Install and configure Azure PowerShell](/documentation/articles/install-configure-powershell). For more information on using Azure PowerShell with HDInsight, see [Administer HDInsight using PowerShell](/documentation/articles/hdinsight-administer-use-powershell). For the list of the HDInsight Windows PowerShell cmdlets, see [HDInsight cmdlet reference](https://msdn.microsoft.com/zh-cn/library/azure/dn858087.aspx).


The following procedures are needed to create an HDInsight cluster by using Azure PowerShell:

- Create an Azure resource group
- Create an Azure Storage account
- Create an Azure Blob container
- Create an HDInsight cluster


		# Sign in
		Add-AzureAccount

		###########################################
		# Create required items, if none exist
		###########################################

		# Select the subscription to use
		$subscriptionName = "<SubscriptionName>"        # Provide your Subscription Name
		Select-AzureSubscription -SubscriptionName $subscriptionName

		# Create an Azure Resource Group
		$resourceGroupName = "<ResourceGroupName>"      # Provide a Resource Group name
		$location = "<Location>"                        # For example, "China North"
		New-AzureResourceGroup -Name $resourceGroupName -Location $location

		# Create an Azure Storage account
		$storageAccountName = "<StorageAcccountName>"   # Provide a Storage account name
		New-AzureStorageAccount -ResourceGroupName $resourceGroupName -StorageAccountName $storageAccountName -Location $location -Type Standard_GRS

		# Create an Azure Blob Storage container
		$containerName = "<ContainerName>"              # Provide a container name
		$storageAccountKey = Get-AzureStorageAccountKey -ResourceGroupName $resourceGroupName -Name $storageAccountName | %{ $_.Key1 }
		$destContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey
		New-AzureStorageContainer -Name $containerName -Context $destContext

		###########################################
		# Create an HDInsight Cluster
		###########################################

		# Skip these variables if you just created them
		$resourceGroupName = "<ResourceGroupName>"      # Provide the Resource Group name
		$storageAccountName = "<StorageAcccountName>"   # Provide the Storage account name
		$containerName = "<ContainerName>"              # Provide the container name
		$storageAccountKey = Get-AzureStorageAccountKey -Name $storageAccountName -ResourceGroupName $resourceGroupName | %{ $_.Key1 }

		# Set these variables
		$clusterName = $containerName           		# As a best practice, have the same name for the cluster and container
		$clusterNodes = <ClusterSizeInNodes>    		# The number of nodes in the HDInsight cluster
		$credentials = Get-Credential

		# The location of the HDInsight cluster. It must be in the same data center as the Storage account.
		$location = Get-AzureStorageAccount -ResourceGroupName $resourceGroupName -StorageAccountName $storageAccountName | %{$_.Location}

		# Create a new HDInsight cluster
		New-AzureHDInsightCluster -ResourceGroupName $resourceGroupName `
									-ClusterName $clusterName `
									-Location $location `
									-ClusterSizeInNodes $clusterNodes `
									-ClusterType Hadoop `
									-OSType Windows `
									-HttpCredential $credentials `
									-DefaultStorageAccountName "$storageAccountName.blob.core.chinacloudapi.cn" `
									-DefaultStorageAccountKey $storageAccountKey `
									-DefaultStorageContainer $containerName  

	![HDI.CLI.Provision](./media/hdinsight-provision-clusters/HDI.ps.provision.png)

## Create using the HDInsight .NET SDK
The HDInsight .NET SDK provides .NET client libraries that make it easier to work with HDInsight from a .NET Framework application. Follow the instructions below to create a Visual Studio console application and paste the code for creating a cluster.

**To create a Visual Studio console application**

1. Create a new C# console application in Visual Studio.
2. Run the following Nuget command in the Nuget Package Management console.

		Install-Package Microsoft.Azure.Management.HDInsight -Pre

6. From Solution Explorer, double-click **Program.cs** to open it, paste the following code, and provide values for the variables:


        using System;
		using System.Collections.Generic;
		using System.Diagnostics;
		using System.Linq;
		using System.Security;
		using System.Text;
		using System.Threading.Tasks;
		using Hyak.Common;
		using Microsoft.Azure;
		using Microsoft.Azure.Common.Authentication;
		using Microsoft.Azure.Common.Authentication.Models;
		using Microsoft.Azure.Management.HDInsight;
		using Microsoft.Azure.Management.HDInsight.Job;
		using Microsoft.Azure.Management.HDInsight.Job.Models;
		using Microsoft.Azure.Management.HDInsight.Models;
		using Newtonsoft.Json;

		namespace CreateHDICluster
		{
		    internal class Program
		    {
		        private static ProfileClient _profileClient;
		        private static SubscriptionCloudCredentials _cloudCredentials;
		        private static HDInsightManagementClient _hdiManagementClient;

		        private static Guid SubscriptionId = new Guid("<SubscriptionID>");
		        private const string ResourceGroupName = "<ResourceGroupName>";
		        private const string ExistingStorageName = "<storageaccountname>.blob.core.chinacloudapi.cn";
		        private const string ExistingStorageKey = "<account key>";
		        private const string ExistingContainer = "<container name>";
		        private const string NewClusterName = "<cluster name>";
		        private const int NewClusterNumNodes = <number of nodes>;
		        private const string NewClusterLocation = "<location>";		//must be same as the storage account
		        private const OSType NewClusterOsType = OSType.Windows;
		        private const HDInsightClusterType NewClusterType = HDInsightClusterType.Hadoop;
		        private const string NewClusterVersion = "3.2";
		        private const string NewClusterUsername = "admin";
		        private const string NewClusterPassword = "<password>";

		        private static void Main(string[] args)
		        {
		            System.Console.WriteLine("Start cluster creation");

		            _profileClient = GetProfile();
		            _cloudCredentials = GetCloudCredentials();
		            _hdiManagementClient = new HDInsightManagementClient(_cloudCredentials);

		            System.Console.WriteLine(String.Format("Creating the cluster {0}...", NewClusterName));
		            CreateCluster();
		            System.Console.WriteLine("Done. Press any key to continue.");
		            System.Console.ReadKey(true);
		        }

		        private static void CreateCluster()
		        {
		            var parameters = new ClusterCreateParameters
		            {
		                ClusterSizeInNodes = NewClusterNumNodes,
		                UserName = NewClusterUsername,
		                Password = NewClusterPassword,
		                Location = NewClusterLocation,
		                DefaultStorageAccountName = ExistingStorageName,
		                DefaultStorageAccountKey = ExistingStorageKey,
		                DefaultStorageContainer = ExistingContainer,
		                ClusterType = NewClusterType,
		                OSType = NewClusterOsType
		            };

		            _hdiManagementClient.Clusters.Create(ResourceGroupName, NewClusterName, parameters);
		        }

		        private static ProfileClient GetProfile(string username = null, SecureString password = null)
		        {
		            var profileClient = new ProfileClient(new AzureProfile());
		            var env = profileClient.GetEnvironmentOrDefault(EnvironmentName.AzureCloud);
		            var acct = new AzureAccount { Type = AzureAccount.AccountType.User };

		            if (username != null && password != null)
		                acct.Id = username;

		            profileClient.AddAccountAndLoadSubscriptions(acct, env, password);

		            return profileClient;
		        }

		        private static SubscriptionCloudCredentials GetCloudCredentials()
		        {
		            var sub = _profileClient.Profile.Subscriptions.Values.FirstOrDefault(s => s.Id.Equals(SubscriptionId));

		            Debug.Assert(sub != null, "subscription != null");
		            _profileClient.SetSubscriptionAsDefault(sub.Id, sub.Account);

		            return AzureSession.AuthenticationFactory.GetSubscriptionCloudCredentials(_profileClient.Profile.Context);
		        }

		    }
		}

7. Press **F5** to run the application. A console window should open and display the status of the application. You will also be prompted to enter your Azure account credentials. It can take several minutes to create an HDInsight cluster.


## Creating HDInsight cluster using on-premises SQL Server Integration Services

You can also use SQL Server Integration Services (SSIS) to create or delete an HDInsight cluster. The Azure Feature Pack for SSIS provides the following components that work with HDInsight clusters.


- [Azure HDInsight Create Cluster Task][ssisclustercreate]
- [Azure HDInsight Delete Cluster Task][ssisclusterdelete]
- [Azure Subscription Connection Manager][connectionmanager]

Learn more about the Azure Feature Pack for SSIS [here][ssispack].


##<a id="nextsteps"></a> Next steps
In this article, you have learned several ways to create an HDInsight cluster. To learn more, see the following articles:

* [Get started with Azure HDInsight](/documentation/articles/hdinsight-get-started) - Learn how to start working with your HDInsight cluster
* [Use Sqoop with HDInsight](/documentation/articles/hdinsight-use-sqoop) - Learn how to copy data between HDInsight and SQL Database or SQL Server
* [Administer HDInsight using PowerShell](/documentation/articles/hdinsight-administer-use-powershell) - Learn how to work with HDInsight by using Azure PowerShell
* [Submit Hadoop jobs programmatically](/documentation/articles/hdinsight-submit-hadoop-jobs-programmatically) - Learn how to programmatically submit jobs to HDInsight
* [Azure HDInsight SDK documentation] [hdinsight-sdk-documentation] - Discover the HDInsight SDK



##Appendix A - ARM template

The following Azure Resource Manger template creates a Hadoop cluster with the dependent Azure storage account.

	{
	  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
	  "contentVersion": "1.0.0.0",
	  "parameters": {
	    "location": {
	      "type": "string",
	      "defaultValue": "China North",
	      "allowedValues": [
	        "China North"
	      ],
	      "metadata": {
	        "description": "The location where all azure resources will be deployed."
	      }
	    },
	    "clusterName": {
	      "type": "string",
	      "metadata": {
	        "description": "The name of the HDInsight cluster to create."
	      }
	    },
	    "clusterLoginUserName": {
	      "type": "string",
	      "defaultValue": "admin",
	      "metadata": {
	        "description": "These credentials can be used to submit jobs to the cluster and to log into cluster dashboards."
	      }
	    },
	    "clusterLoginPassword": {
	      "type": "securestring",
	      "metadata": {
	        "description": "The password for the cluster login."
	      }
	    },
	    "sshUserName": {
	      "type": "string",
	      "defaultValue": "hdiuser",
	      "metadata": {
	        "description": "These credentials can be used to remotely access the cluster and the edge node virtual machine."
	      }
	    },
	    "sshPassword": {
	      "type": "securestring",
	      "metadata": {
	        "description": "The password for the ssh user."
	      }
	    },
	    "clusterStorageAccountName": {
	      "type": "string",
	      "metadata": {
	        "description": "The name of the storage account to be created and be used as the cluster's storage."
	      }
	    },
	    "clusterStorageType": {
	      "type": "string",
	      "defaultValue": "Standard_LRS",
	      "allowedValues": [
	        "Standard_LRS",
	        "Standard_GRS",
	        "Standard_ZRS"
	      ]
	    },
	    "clusterWorkerNodeCount": {
	      "type": "int",
	      "defaultValue": 4,
	      "metadata": {
	        "description": "The number of nodes in the HDInsight cluster."
	      }
	    }
	  },
	  "variables": {},
	  "resources": [
	    {
	      "name": "[parameters('clusterStorageAccountName')]",
	      "type": "Microsoft.Storage/storageAccounts",
	      "location": "[parameters('location')]",
	      "apiVersion": "2015-05-01-preview",
	      "dependsOn": [],
	      "tags": {},
	      "properties": {
	        "accountType": "[parameters('clusterStorageType')]"
	      }
	    }
	  ],
	  "outputs": {
	    "cluster": {
	      "type": "object",
	      "value": "[reference(resourceId('Microsoft.HDInsight/clusters',parameters('clusterName')))]"
	    }
	  }
	}


[hdinsight-sdk-documentation]: http://msdn.microsoft.com/zh-cn/library/dn479185.aspx
[azure-preview-portal]: https://manage.windowsazure.cn
[connectionmanager]: http://msdn.microsoft.com/zh-cn/library/mt146773(v=sql.120).aspx
[ssispack]: http://msdn.microsoft.com/zh-cn/library/mt146770(v=sql.120).aspx
[ssisclustercreate]: http://msdn.microsoft.com/zh-cn/library/mt146774(v=sql.120).aspx
[ssisclusterdelete]: http://msdn.microsoft.com/zh-cn/library/mt146778(v=sql.120).aspx
