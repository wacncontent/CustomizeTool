deletion:

deleted:

		For information on using Solr with a Linux-based cluster, see [Install and use Solr on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-solr-install-linux).

reason: (Linux Support)

deleted:

		, Spark

reason: (Spark managment)

deleted:

		- [Install Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install): install Solr on HDInsight cluster using the Azure Preview Portal

reason: (the new Ibiza portal)

deleted:

		- [Install and use Solr on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-solr-install-linux)

reason: (Linux Support)

deleted:

		- [Install Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install): install Solr on HDInsight cluster using the Azure Preview Portal

reason: (the new Ibiza portal)

deleted:

		- [Install and use Solr on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-solr-install-linux)

reason: (Linux Support)

deleted:

		- [Install and use Spark on HDInsight clusters][hdinsight-install-spark]: Script Action sample about installing Spark

reason: (Spark managment)

replacement:

deleted:

		## Install Solr using portal
		
		[AZURE.INCLUDE [hdinsight-azure-portal](../includes/hdinsight-azure-portal.md)]

replaced by:

		<a name="install"></a>
		## How do I install Solr?
		
		A sample script to install Solr on an HDInsight cluster is available from a read-only Azure storage blob at [https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1](https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1). This section provides instructions on how to use the sample script while provisioning the cluster by using the Azure Management Portal.

reason: (the new Ibiza portal)

deleted:

		See [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster#call_scripts_using_powershell).  The sample demonstrates how to install Spark using Azure PowerShell. You need to customize the script to use [https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1](https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1).

replaced by:

		In this section we use the **<a href = "http://msdn.microsoft.com/zh-cn/library/dn858088.aspx" target="_blank">Add-AzureHDInsightScriptAction</a>** cmdlet to invoke scripts by using Script Action to customize a cluster. Before proceeding, make sure you have installed and configured Azure PowerShell. For information on configuring a workstation to run HDInsight Windows PowerShell cmdlets, see [Install and configure Azure PowerShell][powershell-install-configure].
		
		Perform the following steps:
		
		1. Open an Azure PowerShell window and declare the following variables:
		
				# PROVIDE VALUES FOR THESE VARIABLES
				$subscriptionName = "<SubscriptionName>"		# Name of the Azure subscription
				$clusterName = "<HDInsightClusterName>"			# HDInsight cluster name
				$storageAccountName = "<StorageAccountName>"	# Azure Storage account that hosts the default container
				$storageAccountKey = "<StorageAccountKey>"      # Key for the Storage account
				$containerName = $clusterName
				$location = "<MicrosoftDataCenter>"				# Location of the HDInsight cluster. It must be in the same data center as the Storage account.
				$clusterNodes = <ClusterSizeInNumbers>			# Number of nodes in the HDInsight cluster
				$version = "<HDInsightClusterVersion>"          # For example, "3.1"
			
		2. Specify the configuration values such as nodes in the cluster and the default storage to be used.
		
				# Specify the configuration options
				Select-AzureSubscription $subscriptionName
				$config = New-AzureHDInsightClusterConfig -ClusterSizeInNodes $clusterNodes
				$config.DefaultStorageAccount.StorageAccountName="$storageAccountName.blob.core.chinacloudapi.cn"
				$config.DefaultStorageAccount.StorageAccountKey=$storageAccountKey
				$config.DefaultStorageAccount.StorageContainerName=$containerName
			
		3. Use the **Add-AzureHDInsightScriptAction** cmdlet to add a script action to the cluster configuration. Later, when the cluster is being created, the script action gets executed. 
		
				# Add the script action to the cluster configuration
				$config = Add-AzureHDInsightScriptAction -Config $config -Name "Install Solr" -ClusterRoleCollection HeadNode,DataNode -Uri https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1
		
			The **Add-AzureHDInsightScriptAction** cmdlet takes the following parameters:
		
			<table style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse;">
			<tr>
			<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:90px; padding-left:5px; padding-right:5px;">Parameter</th>
			<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:550px; padding-left:5px; padding-right:5px;">Definition</th></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Config</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px; padding-right:5px;">Configuration object to which script action information is added.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name of the script action.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">ClusterRoleCollection</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Nodes on which the customization script is run. The valid values are HeadNode (to install on the head node) or DataNode (to install on all the data nodes). You can use either or both values.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Uri</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">URI to the script that is executed.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Parameters</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Parameters required by the script. The sample script used in this topic does not require any parameters, and hence you do not see this parameter in the snippet above.
			</td></tr>
			</table>
			
		4. Finally, start provisioning a customized cluster with Solr installed.  
			
				# Start provisioning a cluster with Solr installed
				New-AzureHDInsightCluster -Config $config -Name $clusterName -Location $location -Version $version 
		
		When prompted, enter the credentials for the cluster. It can take several minutes before the cluster is created.
		
		<a name="usingSDK"></a>

reason: (Spark managment)

deleted:

		See [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster#call_scripts_using_azure_powershell). The sample demonstrates how to install Spark using the .NET SDK. You need to customize the script to use [https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1](https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1).

replaced by:

		The HDInsight .NET SDK provides .NET client libraries that make it easier to work with HDInsight from a .NET Framework application. This section provides instructions on how to use Script Action from the SDK to provision a cluster that has Solr installed. The following procedures must be performed:
		
		- Install the HDInsight .NET SDK
		- Create a self-signed certificate
		- Create a console application
		- Run the application
		
		
		**To install the HDInsight .NET SDK**
		
		You can install the latest published build of the SDK from [NuGet](http://nuget.codeplex.com/wikipage?title=Getting%20Started). The instructions will be shown in the next procedure.
		
		**To create a self-signed certificate**
		
		Create a self-signed certificate, install it on your workstation, and upload it to your Azure subscription. For instructions, see [Create a self-signed certificate](/documentation/articles/hdinsight-administer-use-management-portal-v1). 
		
		
		**To create a Visual Studio application**
		
		1. Open Visual Studio 2013.
		
		2. From the **File** menu, click **New**, and then click **Project**.
		
		3. From **New Project**, type or select the following values:
			
			<table style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse;">
			<tr>
			<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:90px; padding-left:5px; padding-right:5px;">Property</th>
			<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:90px; padding-left:5px; padding-right:5px;">Value</th></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Category</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px; padding-right:5px;">Templates/Visual C#/Windows</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Template</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Console Application</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">CreateSolrCluster</td></tr>
			</table>
		
		4. Click **OK** to create the project.
		
		5. From the **Tools** menu, click **Nuget Package Manager**, and then click **Package Manager Console**.
		
		6. Run the following command in the console to install the package:
		
				Install-Package Microsoft.WindowsAzure.Management.HDInsight
		
			This command adds the .NET libraries and references to them from the current Visual Studio project.
		
			
		7. From Solution Explorer, double-click **Program.cs** to open it.
		
		8. Add the following using statements to the top of the file:
		
				using System.Security.Cryptography.X509Certificates;
				using Microsoft.WindowsAzure.Management.HDInsight;
				using Microsoft.WindowsAzure.Management.HDInsight.ClusterProvisioning;
				using Microsoft.WindowsAzure.Management.HDInsight.Framework.Logging;
			
		9. In the Main() function, copy and paste the following code, and provide values for the variables:
				
		        var clusterName = args[0];
		
		        // Provide values for the variables
		        string thumbprint = "<CertificateThumbprint>";  
		        string subscriptionId = "<AzureSubscriptionID>";
		        string location = "<MicrosoftDataCenterLocation>";
		        string storageaccountname = "<AzureStorageAccountName>.blob.core.chinacloudapi.cn";
		        string storageaccountkey = "<AzureStorageAccountKey>";
		        string username = "<HDInsightUsername>";
		        string password = "<HDInsightUserPassword>";
		        int clustersize = <NumberOfNodesInTheCluster>;
		
		        // Provide the certificate thumbprint to retrieve the certificate from the certificate store 
		        X509Store store = new X509Store();
		        store.Open(OpenFlags.ReadOnly);
		        X509Certificate2 cert = store.Certificates.Cast<X509Certificate2>().First(item => item.Thumbprint == thumbprint);
		
		        // Create an HDInsight client object
		        HDInsightCertificateCredential creds = new HDInsightCertificateCredential(new Guid(subscriptionId), cert);
		        var client = HDInsightClient.Connect(creds);
				client.IgnoreSslErrors = true;
		        
		        // Provide the cluster information
				var clusterInfo = new ClusterCreateParameters()
		        {
		            Name = clusterName,
		            Location = location,
		            DefaultStorageAccountName = storageaccountname,
		            DefaultStorageAccountKey = storageaccountkey,
		            DefaultStorageContainer = clusterName,
		            UserName = username,
		            Password = password,
		            ClusterSizeInNodes = clustersize,
		            Version = "3.1"
		        };        
		
		10. Append the following code to the Main() function to use the [ScriptAction](http://msdn.microsoft.com/zh-cn/library/microsoft.windowsazure.management.hdinsight.clusterprovisioning.data.scriptaction.aspx) class to invoke a custom script to install Solr.
		
				// Add the script action to install Solr
		        clusterInfo.ConfigActions.Add(new ScriptAction(
		          "Install Solr", // Name of the config action
		          new ClusterNodeType[] { ClusterNodeType.HeadNode, ClusterNodeType.DataNode }, // List of nodes to install Solr on
		          new Uri("https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1"), // Location of the script to install Solr
				  null //Because the script used does not require any parameters
		        ));
		
		11. Finally, create the cluster.
		
				client.CreateCluster(clusterInfo);
		
		11. Save changes to the application and build the solution. 
		
		**To run the application**
		
		Open a Windows PowerShell or Azure PowerShell console, navigate to the location where you saved the Visual Studio project, navigate to the \bin\debug directory within the project, and then run the following command:
		
			.\CreateSolrCluster <cluster-name>
		
		Provide a cluster name and press ENTER to provision a cluster with Solr installed.

reason: (Spark managment)

