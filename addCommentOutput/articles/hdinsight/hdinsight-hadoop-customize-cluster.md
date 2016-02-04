<properties
	pageTitle="Customize HDInsight Clusters using script actions | Windows Azure"
	description="Learn how to customize HDInsight clusters using Script Action."
	services="hdinsight"
	documentationCenter=""
	authors="nitinme"
	manager="paulettm"
	editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="11/13/2015"
	wacn.date=""/>

# Customize HDInsight clusters using Script Action (Windows)

[AZURE.INCLUDE [usescriptaction-selector](../includes/hdinsight-selector-use-script-action.md)]

**Script Action** can be used to invoke [custom scripts](/documentation/articles/hdinsight-hadoop-script-actions) 
during the cluster creation process for installing additional software on a cluster.
<!-- deleted by customization

The information in this article is specific to Windows-based HDInsight clusters. Use the tab 
select above to switch to a version of this article that is specific to Linux-based clusters.
-->

HDInsight clusters can be customized in a variety of other ways as well, such as including 
additional Azure Storage accounts, changing the Hadoop configuration files (core-site.xml, 
hive-site.xml, etc.), or adding shared libraries (e.g., Hive, Oozie) into common locations 
in the cluster. These customizations can be done through Azure PowerShell, the Azure 
HDInsight .NET SDK, or the Azure Management Portal. For more information, see 
[Create Hadoop clusters in HDInsight][hdinsight-provision-cluster].

## Script Action in the cluster creation process

Script Action is only used while a clusters is in the process of being created. The following 
diagram illustrates when Script Action is executed during the creation process:

![HDInsight cluster customization and stages during cluster creation][img-hdi-cluster-states]

When the script is running, the cluster enters the **ClusterCustomization** stage. At this 
stage, the script is run under the system admin account, in parallel on all the specified 
nodes in the cluster, and provides full admin privileges on the nodes.

> [AZURE.NOTE] Because you have admin privileges on the cluster nodes during the 
**ClusterCustomization** stage, you can use the script to perform operations like stopping 
and starting services, including Hadoop-related services. So, as part of the script, you must 
ensure that the Ambari services and other Hadoop-related services are up and running before 
the script finishes running. These services are required to successfully ascertain the health 
and state of the cluster while it is being created. If you change any configuration on the 
cluster that affects these services, you must use the helper functions that are provided. For 
more information about helper functions, see [Develop Script Action scripts for HDInsight][hdinsight-write-script].

The output and the error logs for the script are stored in the default Storage account you 
specified for the cluster. The logs are stored in a table with the name 
**u<\cluster-name-fragment><\time-stamp>setuplog**. These are aggregate logs from the script 
run on all the nodes (head node and worker nodes) in the cluster.

Each cluster can accept multiple script actions that are invoked in the order in which they 
are specified. A script can be ran on the head node, the worker nodes, or both.

HDInsight provides several scripts to install the following components on HDInsight clusters:

Name | Script
----- | -----
<!-- deleted by customization
**Install Spark** | https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1. See [Install and use Spark on HDInsight clusters][hdinsight-install-spark].
-->
**Install R** | https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps1. See [Install and use R on HDInsight clusters][hdinsight-install-r].
**Install Solr** | https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1. See [Install and use Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install-v1).
- **Install Giraph** | https://hdiconfigactions.blob.core.windows.net/giraphconfigactionv01/giraph-installer-v01.ps1. See [Install and use Giraph on HDInsight clusters](/documentation/articles/hdinsight-hadoop-giraph-install).



## Call scripts using the Azure Management Portal

**From the Azure Management Portal**

<!-- deleted by customization
1. Start creating a cluster as described at [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters-v1#portal).
2. Under Optional Configuration, for the **Script Actions** blade, click **add script action** to provide details about the script action, as shown below:

	![Use Script Action to customize a cluster](./media/hdinsight-hadoop-customize-cluster-v1/HDI.CreateCluster.8.png "Use Script Action to customize a cluster")
-->
<!-- keep by customization: begin -->
1. Start provisioning a cluster using the **CUSTOM CREATE** option, as described at [Provisioning a cluster using custom options](/documentation/articles/hdinsight-provision-clusters-v1#portal). 
2. On the **Script Actions** page of the wizard, click **add script action** to provide details about the script action, as shown below:

	![Use Script Action to customize a cluster](./media/hdinsight-hadoop-customize-cluster-v1/HDI.CustomProvision.Page6.png "Use Script Action to customize a cluster")
<!-- keep by customization: end -->

	<table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>Name</td>
			<td>Specify a name for the script action.</td></tr>
		<tr><td>Script URI</td>
			<td>Specify the URI to the script that is invoked to customize the cluster. s</td></tr>
		<tr><td>Head/Worker</td>
			<td>Specify the nodes (**Head** or **Worker**) on which the customization script is run.</b>.
		<tr><td>Parameters</td>
			<td>Specify the parameters, if required by the script.</td></tr>
	</table>

	Press ENTER to add more than one script action to install multiple components on the cluster.

3. Click **Select** to save the script action configuration and continue with cluster creation.

<!-- deleted by customization
## Call scripts using Azure PowerShell

This following PowerShell script demonstrates how to install Spark on Windows based HDInsight cluster.  

	# Provide values for these variables
	$subscriptionID = "<Azure Suscription ID>" # After "Login-AzureRmAccount", use "Get-AzureRmSubscription" to list IDs.

	$nameToken = "<Enter A Name Token>"  # The token is use to create Azure service names.
	$namePrefix = $nameToken.ToLower() + (Get-Date -Format "MMdd")
	
	$resourceGroupName = $namePrefix + "rg"
	$location = "EAST US 2" # used for creating resource group, storage account, and HDInsight cluster.
	
	$hdinsightClusterName = $namePrefix + "spark"
	$httpUserName = "admin"
	$httpPassword = "Pass@word111"
	
	$defaultStorageAccountName = "$namePrefix" + "store"
	$defaultBlobContainerName = $hdinsightClusterName
	
	#############################################################
	# Connect to Azure
	#############################################################
	
	Try{
		Get-AzureRmSubscription
	}
	Catch{
		Login-AzureRmAccount
	}
	Select-AzureRmSubscription -SubscriptionId $subscriptionID
	
	#############################################################
	# Prepare the dependent components
	#############################################################
	
	# Create resource group
	New-AzureRmResourceGroup -Name $resourceGroupName -Location $location
	
	# Create storage account
	New-AzureRmStorageAccount -ResourceGroupName $resourceGroupName -Name $defaultStorageAccountName -Location $location -Type Standard_LRS
	$defaultStorageAccountKey = Get-AzureRmStorageAccountKey -ResourceGroupName $resourceGroupName -Name $defaultStorageAccountName |  %{ $_.Key1 }
	$defaultStorageAccountContext = New-AzureStorageContext -StorageAccountName $defaultStorageAccountName -StorageAccountKey $storageAccountKey  
	New-AzureStorageContainer -Name $defaultBlobContainerName -Context $defaultStorageAccountContext
	
	#############################################################
	# Create cluster with Spark
	#############################################################
	
	# Specify the configuration options
	$config = New-AzureRmHDInsightClusterConfig `
				-DefaultStorageAccountName "$defaultStorageAccountName.blob.core.chinacloudapi.cn" `
				-DefaultStorageAccountKey $defaultStorageAccountKey 
				
	
	# Add a script action to the cluster configuration
	$config = Add-AzureRmHDInsightScriptAction `
				-Config $config `
				-Name "Install Spark" `
				-NodeType HeadNode `
				-Uri https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1 `
	
	# Start creating a cluster with Spark installed
	New-AzureRmHDInsightCluster `
			-ResourceGroupName $resourceGroupName `
			-ClusterName $hdinsightClusterName `
			-Location $location `
			-ClusterSizeInNodes 2 `
			-ClusterType Hadoop `
			-OSType Windows `
			-DefaultStorageContainer $defaultBlobContainerName `
			-Config $config


To install other software, you will need to replace the script file in the script:


When prompted, enter the credentials for the cluster. It can take several minutes before the cluster is created.
-->
<!-- keep by customization: begin -->
##<a name="call_scripts_using_powershell"></a> Call scripts using Azure PowerShell

Use Azure PowerShell commands for HDInsight to run a single script action or multiple script actions. You can use the **<a href = "http://msdn.microsoft.com/zh-cn/library/dn858088.aspx" target="_blank">Add-AzureHDInsightScriptAction</a>** cmdlet to invoke custom scripts. To use these cmdlets, you must have Azure PowerShell installed and configured. For information on configuring a workstation to run Azure PowerShell cmdlets for HDInsight, see [Install and configure Azure PowerShell][powershell-install-configure].

Use the following Azure PowerShell commands to run a single script action when deploying an HDInsight cluster:

	$config = New-AzureHDInsightClusterConfig -ClusterSizeInNodes 4

	$config = Add-AzureHDInsightScriptAction -Config $config -Name MyScriptActionName -Uri http://uri.to/scriptaction.ps1 -Parameters MyScriptActionParameter -ClusterRoleCollection HeadNode,DataNode

	New-AzureHDInsightCluster -Config $config

Use the following Azure PowerShell commands to run multiple script actions when deploying an HDInsight cluster:

	$config = New-AzureHDInsightClusterConfig -ClusterSizeInNodes 4

	$config = Add-AzureHDInsightScriptAction -Config $config -Name MyScriptActionName1 -Uri http://uri.to/scriptaction1.ps1 -Parameters MyScriptAction1Parameters -ClusterRoleCollection HeadNode,DataNode | Add-AzureHDInsightScriptAction -Config $config -Name MyScriptActionName2 -Uri http://uri.to/scriptaction2.ps1 -Parameters MyScriptAction2Parameters -ClusterRoleCollection HeadNode

	New-AzureHDInsightCluster -Config $config
<!-- keep by customization: end -->

## Call scripts using .NET SDK 

<!-- deleted by customization
The following sample demonstrates how to install Spark on Windows based HDInsight cluster. To install other software, you will need to replace the script file in the code.

**To create a HDInsight cluster with Spark** 

1. Create a C# console application in Visual Studio.
2. From the Nuget Package Manager Console, run the following command.

		Install-Package Microsoft.Azure.Management.HDInsight -Pre
		Install-Package Microsoft.Azure.Common.Authentication -Pre

2. Use the following using statements in the Program.cs file:

		using System;
		using System.Security;
		using Microsoft.Azure.Management.HDInsight;
		using Microsoft.Azure.Management.HDInsight.Models;
		
		using Microsoft.Azure;
		using Microsoft.Azure.Common.Authentication;
		using Microsoft.Azure.Common.Authentication.Factories;
		using Microsoft.Azure.Common.Authentication.Models;

3. Place the code in the class with the following:

        private static HDInsightManagementClient _hdiManagementClient;

        private static Guid SubscriptionId = new Guid("<YourAzureSubscriptionID>");
        private const string ResourceGroupName = "<ExistingAzureResourceGroupName>";
        private const string NewClusterName = "<NewAzureHDInsightClusterName>";
        private const int NewClusterNumNodes = <NumberOfClusterNodes>;
        private const string NewClusterLocation = "China East";
        private const string NewClusterVersion = "3.2";
        private const string ExistingStorageName = "<ExistingAzureStorageAccountName>";
        private const string ExistingStorageKey = "<ExistingAzureStorageAccountKey>";
        private const string ExistingContainer = "<ExistingAzureBlobStorageContainer>";
        private const HDInsightClusterType NewClusterType = HDInsightClusterType.Hadoop;
        private const OSType NewClusterOSType = OSType.Windows;
        private const string NewClusterUsername = "<HttpUserName>";
        private const string NewClusterPassword = "<HttpUserPassword>";

        static void Main(string[] args)
        {
            System.Console.WriteLine("Running");

            var tokenCreds = GetTokenCloudCredentials();
            var subCloudCredentials = GetSubscriptionCloudCredentials(tokenCreds, SubscriptionId);

            _hdiManagementClient = new HDInsightManagementClient(subCloudCredentials);

            CreateCluster();

        }

        private static void CreateCluster()
        {
            var parameters = new ClusterCreateParameters
            {
                ClusterSizeInNodes = NewClusterNumNodes,
                Location = NewClusterLocation,
                ClusterType = NewClusterType,
                OSType = NewClusterOSType,
                Version = NewClusterVersion,

                DefaultStorageAccountName = ExistingStorageName,
                DefaultStorageAccountKey = ExistingStorageKey,
                DefaultStorageContainer = ExistingContainer,

                UserName = NewClusterUsername,
                Password = NewClusterPassword,
            };

            ScriptAction sparkScriptAction = new ScriptAction("Install Spark",
                new Uri("https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1"), "");

            parameters.ScriptActions.Add(ClusterNodeType.HeadNode, new System.Collections.Generic.List<ScriptAction> { sparkScriptAction });
            parameters.ScriptActions.Add(ClusterNodeType.WorkerNode, new System.Collections.Generic.List<ScriptAction> { sparkScriptAction });

            _hdiManagementClient.Clusters.Create(ResourceGroupName, NewClusterName, parameters);
        }


        public static SubscriptionCloudCredentials GetTokenCloudCredentials(string username = null, SecureString password = null)
        {
            var authFactory = new AuthenticationFactory();

            var account = new AzureAccount { Type = AzureAccount.AccountType.User };

            if (username != null && password != null)
                account.Id = username;

            var env = AzureEnvironment.PublicEnvironments[EnvironmentName.AzureCloud];

            var accessToken =
                authFactory.Authenticate(account, env, AuthenticationFactory.CommonAdTenant, password, ShowDialog.Auto)
                    .AccessToken;

            return new TokenCloudCredentials(accessToken);
        }

        public static SubscriptionCloudCredentials GetSubscriptionCloudCredentials(SubscriptionCloudCredentials creds, Guid subId)
        {
            return new TokenCloudCredentials(subId.ToString(), ((TokenCloudCredentials)creds).Token);
        }
-->
<!-- keep by customization: begin -->
The HDInsight .NET SDK provides a <a href="http://msdn.microsoft.com/zh-cn/library/microsoft.windowsazure.management.hdinsight.clusterprovisioning.data.scriptaction.aspx" target="_blank">ScriptAction</a> class to invoke custom scripts. To use the HDInsight .NET SDK:

1. Create a Visual Studio application, and then install the SDK from NuGet. From the **Tools** menu, click **Nuget Package Manager**, and then click **Package Manager Console**. Run the following command in the console to install the package:

		Install-Package Microsoft.WindowsAzure.Management.HDInsight

2. Create a cluster by using the SDK. For instructions, see [Provision HDInsight cluster using .NET SDK](/documentation/articles/hdinsight-provision-clusters-v1#sdk).

3. Use the **ScriptAction** class to invoke a custom script as shown below:

		
		var clusterInfo = new ClusterCreateParameters()
		{
			// Provide the cluster information, like
			// name, Storage account, credentials,
			// cluster size, and version		    
			...
			...
		};

		// Add the script action to install Spark
		clusterInfo.ConfigActions.Add(new ScriptAction(
	  		"MyScriptActionName", // Name of the config action
	  		new ClusterNodeType[] { ClusterNodeType.HeadNode }, // List of nodes to install the component on
	  		new Uri("http://uri.to/scriptaction.ps1"), // Location of the script to install the component
	  		"MyScriptActionParameter" //Parameters, if any, required by the script
		));
<!-- keep by customization: end -->

4. Press **F5** to run the application.


## Support for open-source software used on HDInsight clusters
The Windows Azure HDInsight service is a flexible platform that enables you to build big-data applications in the cloud by using an ecosystem of open-source technologies formed around Hadoop. Windows Azure provides a general level of support for open-source technologies, as discussed in the **Support Scope** section of the <a href="/support/faq/" target="_blank">Azure Support FAQ website</a>. The HDInsight service provides an additional level of support for some of the components, as described below.

There are two types of open-source components that are available in the HDInsight service:

- **Built-in components** - These components are pre-installed on HDInsight clusters and provide core functionality of the cluster. For example, YARN ResourceManager, the Hive query language (HiveQL), and the Mahout library belong to this category. A full list of cluster components is available in [What's new in the Hadoop cluster versions provided by HDInsight?](/documentation/articles/hdinsight-component-versioning)</a>.
- **Custom components** - You, as a user of the cluster, can install or use in your workload any component available in the community or created by you.

Built-in components are fully supported, and Microsoft Support will help to isolate and resolve issues related to these components.

> [AZURE.WARNING] Components provided with the HDInsight cluster are fully supported and Microsoft Support will help to isolate and resolve issues related to these components.
>
> Custom components receive commercially reasonable support to help you to further troubleshoot the issue. This might result in resolving the issue OR asking you to engage available channels for the open source technologies where deep expertise for that technology is found. For example, there are many community sites that can be used, like: [MSDN forum for HDInsight](https://social.msdn.microsoft.com/Forums/azure/zh-cn/home?forum=hdinsight), [http://stackoverflow.com](http://stackoverflow.com). Also Apache projects have project sites on [http://apache.org](http://apache.org), for example: [Hadoop](http://hadoop.apache.org/) <!-- deleted by customization, [Spark](http://spark.apache.org/) -->.

The HDInsight service provides several ways to use custom components. Regardless of how a component is used or installed on the cluster, the same level of support applies. Below is a list of the most common ways that custom components can be used on HDInsight clusters:

1. Job submission - Hadoop or other types of jobs that execute or use custom components can be submitted to the cluster.
2. Cluster customization - During cluster creation, you can specify additional settings and custom components that will be installed on the cluster nodes.
3. Samples - For popular custom components, Microsoft and others may provide samples of how these components can be used on the HDInsight clusters. These samples are provided without support.

## Develop Script Action scripts

See [Develop Script Action scripts for HDInsight][hdinsight-write-script].


## See also

- [Create Hadoop clusters in HDInsight][hdinsight-provision-cluster] provides instructions on how to create an HDInsight cluster by using other custom options.
- [Develop Script Action scripts for HDInsight][hdinsight-write-script]
<!-- deleted by customization
- [Install and use Spark on HDInsight clusters][hdinsight-install-spark]
-->
- [Install and use R on HDInsight clusters][hdinsight-install-r]
- [Install and use Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install-v1).
- [Install and use Giraph on HDInsight clusters](/documentation/articles/hdinsight-hadoop-giraph-install).

<!-- deleted by customization
[hdinsight-install-spark]: hdinsight-hadoop-spark-install.md
[hdinsight-install-r]: hdinsight-hadoop-r-scripts.md
[hdinsight-write-script]: hdinsight-hadoop-script-actions.md
[hdinsight-provision-cluster]: hdinsight-provision-clusters-v1.md
[powershell-install-configure]: ../install-configure-powershell.md
-->
<!-- keep by customization: begin -->
[hdinsight-install-r]: /documentation/articles/hdinsight-hadoop-r-scripts
[hdinsight-write-script]: /documentation/articles/hdinsight-hadoop-script-actions
[hdinsight-provision-cluster]: /documentation/articles/hdinsight-provision-clusters-v1
[powershell-install-configure]: /documentation/articles/powershell-install-configure
<!-- keep by customization: end -->


[img-hdi-cluster-states]: ./media/hdinsight-hadoop-customize-cluster-v1/HDI-Cluster-state.png "Stages during cluster creation"
