deletion:

deleted:

		[AZURE.INCLUDE [hdinsight-azure-preview-portal](../includes/hdinsight-azure-preview-portal.md)]

reason: ()

deleted:

		> [AZURE.NOTE] The information in this article is specific to Windows-based HDInsight clusters. For a version of this article that is specific to Linux-based clusters, see [Customize HDInsight clusters using Script Action (Linux)](/documentation/articles/hdinsight-hadoop-customize-cluster)

reason: ()

deleted:

		**Install Spark** | https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1. See [Install and use Spark on HDInsight clusters][hdinsight-install-spark].

reason: ()

deleted:

		, [Spark](http://spark.apache.org/)

reason: ()

deleted:

		- [Install and use Spark on HDInsight clusters][hdinsight-install-spark]

reason: ()

deleted:

		[hdinsight-install-spark]: /documentation/articles/hdinsight-hadoop-spark-install

reason: ()

replacement:

deleted:

		Preview portal

replaced by:

		Management Portal

reason: ()

deleted:

		## Call scripts using the Azure Preview Portal
		
		**From the Azure Preview portal**
		
		1. Start creating a cluster as described at [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters#portal).
		2. Under Optional Configuration, for the **Script Actions** blade, click **add script action** to provide details about the script action, as shown below:
		
			![Use Script Action to customize a cluster](./media/hdinsight-hadoop-customize-cluster/HDI.CreateCluster.8.png "Use Script Action to customize a cluster")

replaced by:

		## Call scripts using the Azure Management Portal
		
		**From the Azure Management Portal**
		1. Start provisioning a cluster using the **CUSTOM CREATE** option, as described at [Provisioning a cluster using custom options](/documentation/articles/hdinsight-provision-clusters#portal). 
		2. On the **Script Actions** page of the wizard, click **add script action** to provide details about the script action, as shown below:
		
			![Use Script Action to customize a cluster](./media/hdinsight-hadoop-customize-cluster/HDI.CustomProvision.Page6.png "Use Script Action to customize a cluster")

reason: ()

deleted:

		## Call scripts using Azure PowerShell
		
		This following PowerShell script demonstrates how to install Spark on Windows based HDInsight cluster.  To install other software, you will need to replace the script file in the script:
		
		In this section, we use the **<a href = "http://msdn.microsoft.com/zh-cn/library/dn858088.aspx" target="_blank">Add-AzureHDInsightScriptAction</a>** cmdlet to invoke scripts by using Script Action to customize a cluster. Before proceeding, make sure you have installed and configured Azure PowerShell. For information on configuring a workstation to run Azure PowerShell cmdlets for HDInsight, see [Install and configure Azure PowerShell][powershell-install-configure].
		
		Perform the following steps:
		
		1. Open an Azure PowerShell window and declare the following variables:
		
				# Provide values for these variables
				$subscriptionName = "<SubscriptionName>"		# Name of the Azure subscription
				$clusterName = "<HDInsightClusterName>"			# HDInsight cluster name
				$storageAccountName = "<StorageAccountName>"	# Azure Storage account that hosts the default container
				$storageAccountKey = "<StorageAccountKey>"      # Key for the Storage account
				$containerName = $clusterName
				$location = "<MicrosoftDataCenter>"				# Location of the HDInsight cluster. It must be in the same data center as the Storage account.
				$clusterNodes = <ClusterSizeInNumbers>			# Number of nodes in the HDInsight cluster
				$version = "<HDInsightClusterVersion>"          # For example, "3.2"
		
		2. Specify the configuration values such as nodes in the cluster and the default storage to be used.
		
				# Specify the configuration options
				Select-AzureSubscription $subscriptionName
				$config = New-AzureHDInsightClusterConfig -ClusterSizeInNodes $clusterNodes
				$config.DefaultStorageAccount.StorageAccountName="$storageAccountName.blob.core.chinacloudapi.cn"
				$config.DefaultStorageAccount.StorageAccountKey=$storageAccountKey
				$config.DefaultStorageAccount.StorageContainerName=$containerName
		
		3. Use the **Add-AzureHDInsightScriptAction** cmdlet to add a script action to cluster configuration. Later, when the cluster is being created, the script action gets executed.
		
				# Add a script action to the cluster configuration
				$config = Add-AzureHDInsightScriptAction -Config $config -Name "Install Spark" -ClusterRoleCollection HeadNode -Uri https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1
		
			**Add-AzureHDInsightScriptAction** cmdlet takes the following parameters:
		
			<table style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse;">
			<tr>
			<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:90px; padding-left:5px; padding-right:5px;">Parameter</th>
			<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:550px; padding-left:5px; padding-right:5px;">Definition</th></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Config</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px; padding-right:5px;">The configuration object to which script action information is added.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name of the script action.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">ClusterRoleCollection</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Specifies the nodes on which the customization script is run. The valid values are HeadNode (to install on the head node) or DataNode (to install on all the data nodes). You can use either or both values.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Uri</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Specifies the URI to the script that is executed.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Parameters</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Parameters required by the script. The sample script used in this topic does not require any parameters, and hence you do not see this parameter in the snippet above.
			</td></tr>
			</table>
		
		4. Finally, start creating a customized cluster with Spark installed.  
		
				# Start creating a cluster with Spark installed
				New-AzureHDInsightCluster -Config $config -Name $clusterName -Location $location -Version $version
		
		When prompted, enter the credentials for the cluster. It can take several minutes before the cluster is created.
		
		## Call scripts using .NET SDK 
		
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
		
		4. Press **F5** to run the application.

replaced by:

		**From Azure PowerShell cmdlets**
		
		Use Azure PowerShell commands for HDInsight to run a single script action or multiple script actions. You can use the **<a href = "http://msdn.microsoft.com/zh-cn/library/dn858088.aspx" target="_blank">Add-AzureHDInsightScriptAction</a>** cmdlet to invoke custom scripts. To use these cmdlets, you must have Azure PowerShell installed and configured. For information on configuring a workstation to run Azure PowerShell cmdlets for HDInsight, see [Install and configure Azure PowerShell][powershell-install-configure].
		
		Use the following Azure PowerShell commands to run a single script action when deploying an HDInsight cluster:
		
			$config = New-AzureHDInsightClusterConfig –ClusterSizeInNodes 4
		
			$config = Add-AzureHDInsightScriptAction -Config $config –Name MyScriptActionName –Uri http://uri.to/scriptaction.ps1 –Parameters MyScriptActionParameter -ClusterRoleCollection HeadNode,DataNode
		
			New-AzureHDInsightCluster -Config $config
		
		Use the following Azure PowerShell commands to run multiple script actions when deploying an HDInsight cluster:
		
			$config = New-AzureHDInsightClusterConfig –ClusterSizeInNodes 4
		
			$config = Add-AzureHDInsightScriptAction -Config $config –Name MyScriptActionName1 –Uri http://uri.to/scriptaction1.ps1 –Parameters MyScriptAction1Parameters -ClusterRoleCollection HeadNode,DataNode | Add-AzureHDInsightScriptAction -Config $config –Name MyScriptActionName2 –Uri http://uri.to/scriptaction2.ps1 -Parameters MyScriptAction2Parameters -ClusterRoleCollection HeadNode
		
			New-AzureHDInsightCluster -Config $config
		
		**From the HDInsight .NET SDK**
		
		The HDInsight .NET SDK provides a <a href="http://msdn.microsoft.com/zh-cn/library/microsoft.windowsazure.management.hdinsight.clusterprovisioning.data.scriptaction.aspx" target="_blank">ScriptAction</a> class to invoke custom scripts. To use the HDInsight .NET SDK:
		
		1. Create a Visual Studio application, and then install the SDK from NuGet. From the **Tools** menu, click **Nuget Package Manager**, and then click **Package Manager Console**. Run the following command in the console to install the package:
		
				Install-Package Microsoft.WindowsAzure.Management.HDInsight
		
		2. Create a cluster by using the SDK. For instructions, see [Provision HDInsight cluster using .NET SDK](/documentation/articles/hdinsight-provision-clusters#sdk).
		
		3. Use the **ScriptAction** class to invoke a custom script as shown below:
		
				
				var clusterInfo = new ClusterCreateParameters()
				{
					// Provide the cluster information, like
					// name, Storage account, credentials,
					// cluster size, and version		    
					...
					...
				};

reason: ()

