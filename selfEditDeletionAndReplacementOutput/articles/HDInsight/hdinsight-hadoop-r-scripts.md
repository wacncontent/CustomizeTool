deletion:

deleted:

		For information on using R with a Linux-based cluster, see [Install and use R on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-r-scripts-linux).

reason: ()

deleted:

		, Spark

reason: ()

deleted:

		- [Install and use R on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-r-scripts-linux)

reason: ()

deleted:

		- [Install and use R on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-r-scripts-linux)

reason: ()

deleted:

		- [Install and use Spark on HDInsight clusters][hdinsight-install-spark]: Script Action sample about installing Spark

reason: ()

deleted:

		- [Install Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install-linux): Script Action sample about installing Solr.

reason: ()

deleted:

		[hdinsight-install-spark]: /documentation/articles/hdinsight-hadoop-spark-install-linux

reason: ()

replacement:

deleted:

		preview portal

replaced by:

		Management Portal

reason: ()

deleted:

		1. When you create an HDInsight cluster from the preview portal, click **Optional Configuration**, and then click **Script Actions**.
		2. On the **Script Actions** page, enter the following values:

replaced by:

		1. Start provisioning a cluster by using the **CUSTOM CREATE** option, as described at [Provisioning a cluster using custom options](/documentation/articles/hdinsight-provision-clusters#portal). 
		2. On the **Script Actions** page of the wizard, click **Add script action** to provide details about the script actions, as follows:

reason: ()

deleted:

		preview portal

replaced by:

		Management Portal

reason: ()

deleted:

		See [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster#call_scripts_using_powershell).  The sample demonstrates how to install Spark using Azure PowerShell. You need to customize the script to use [https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps1](https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps1).

replaced by:

		In this section, we use the **<a href = "http://msdn.microsoft.com/zh-cn/library/dn858088.aspx" target="_blank">Add-AzureHDInsightScriptAction</a>** cmdlet to invoke scripts by using Script Action to customize a cluster. Before proceeding, make sure you have installed and configured Azure PowerShell. For information about configuring a workstation to run HDInsight Powershell cmdlets, see [Install and configure Azure PowerShell][powershell-install-configure].
		
		Perform the following steps:
		
		1. Open the Azure PowerShell console and declare the following variables:
		
				# PROVIDE VALUES FOR THESE VARIABLES
				$subscriptionName = "<SubscriptionName>"		# Name of the Azure subscription
				$clusterName = "<HDInsightClusterName>"			# HDInsight cluster name
				$storageAccountName = "<StorageAccountName>"	# Azure storage account that hosts the default container
				$storageAccountKey = "<StorageAccountKey>"      # Key for the storage account
				$containerName = $clusterName
				$location = "<MicrosoftDataCenter>"				# Location of the HDInsight cluster. It must be in the same data center as the storage account.
				$clusterNodes = <ClusterSizeInNumbers>			# The number of nodes in the HDInsight cluster.
				$version = "<HDInsightClusterVersion>"          # HDInsight version, for example "3.1"
		
		2. Specify the configuration values (such as nodes in the cluster) and the default storage to be used.
		
				# SPECIFY THE CONFIGURATION OPTIONS
				Select-AzureSubscription $subscriptionName
				$config = New-AzureHDInsightClusterConfig -ClusterSizeInNodes $clusterNodes
				$config.DefaultStorageAccount.StorageAccountName="$storageAccountName.blob.core.chinacloudapi.cn"
				$config.DefaultStorageAccount.StorageAccountKey=$storageAccountKey
				$config.DefaultStorageAccount.StorageContainerName=$containerName
		
		3. Use **Add-AzureHDInsightScriptAction** cmdlet to invoke the sample script to install R, for example:
		
				# INVOKE THE SCRIPT USING THE SCRIPT ACTION
				$config = Add-AzureHDInsightScriptAction -Config $config -Name "Install R"  -ClusterRoleCollection HeadNode,DataNode -Uri https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps1
		
		
			**Add-AzureHDInsightScriptAction** cmdlet takes the following parameters:
		
			<table style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse;">
			<tr>
			<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:90px; padding-left:5px; padding-right:5px;">Parameter</th>
			<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:550px; padding-left:5px; padding-right:5px;">Definition</th></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Config</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px; padding-right:5px;">Configuration object to which script action information is added</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name of the script action</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">ClusterRoleCollection</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Specifies the nodes on which the customization script is run. The valid values are **HeadNode** (to install on the head node) or **DataNode** (to install on all the data nodes). You can use either or both values.</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Parameters</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Parameters required by the script
			</td></tr>
			<tr>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Uri</td>
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Specifies the URI to the script that is executed</td></tr>
			</table>
		
		4. Finally, provision the cluster that you customized to have R installed.  
		
				# PROVISION A CLUSTER WITH R INSTALLED
				New-AzureHDInsightCluster -Config $config -Name $clusterName -Location $location -Version $version
		
		When prompted, enter the credentials for the cluster. It can take several minutes before the cluster is created.

reason: ()

deleted:

		See [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster#call_scripts_using_azure_powershell). The sample demonstrates how to install Spark using the .NET SDK. You need to customize the script to use [https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps1](https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps11).

replaced by:

		The HDInsight .NET SDK provides .NET client libraries that makes it easier to work with HDInsight from a .NET application.
		
		Perform the following procedures to provision an HDInsight cluster using the SDK:
		
		- [Install the HDInsight .NET SDK](#installSDK)
		- [Create a self-signed certificate](#createCert)
		- [Create a .NET application in Visual Studio](#createApp)
		- [Run the application](#runApp)
		
		The following sections show how to perform these procedures.
		
		**To install the HDInsight .NET SDK**
		
		You can install latest published build of the SDK from [NuGet](http://nuget.codeplex.com/wikipage?title=Getting%20Started). The instructions will be shown in the next procedure.
		
		**To create a self-signed certificate**
		
		Create a self-signed certificate, install it on your workstation, and upload it to your Azure subscription. For instructions, see [Create a self-signed certificate](/documentation/articles/hdinsight-administer-use-management-portal-v1#cert). 
		
		
		**To create a .NET application in Visual Studio**
		
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
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">CreateRCluster</td></tr>
			</table>
		
		4. Click **OK** to create the project.
		
		5. From the **Tools** menu, click **Nuget Package Manager**, and then click **Package Manager Console**.
		
		6. Run the following command in the console to install the package.
		
				Install-Package Microsoft.WindowsAzure.Management.HDInsight
		
			This command adds the .NET libraries and references to them from the current Visual Studio project.
		
		7. From **Solution Explorer**, double-click **Program.cs** to open it.
		
		8. Add the following **using** statements to the top of the file:
		
				using System.Security.Cryptography.X509Certificates;
				using Microsoft.WindowsAzure.Management.HDInsight;
				using Microsoft.WindowsAzure.Management.HDInsight.ClusterProvisioning;
				using Microsoft.WindowsAzure.Management.HDInsight.Framework.Logging;
		
		9. In the **Main()** function, paste the following code, and provide values for the variables :
		
		        var clusterName = args[0];
		
		        // PROVIDE VALUES FOR THE VARIABLES
		        string thumbprint = "<CertificateThumbprint>";  
		        string subscriptionId = "<AzureSubscriptionID>";
		        string location = "<MicrosoftDataCenterLocation>";
		        string storageaccountname = "<AzureStorageAccountName>.blob.core.chinacloudapi.cn";
		        string storageaccountkey = "<AzureStorageAccountKey>";
		        string username = "<HDInsightUsername>";
		        string password = "<HDInsightUserPassword>";
		        int clustersize = <NumberOfNodesInTheCluster>;
		
		        // PROVIDE THE CERTIFICATE THUMBPRINT TO RETRIEVE THE CERTIFICATE FROM THE CERTIFICATE STORE
		        X509Store store = new X509Store();
		        store.Open(OpenFlags.ReadOnly);
		        X509Certificate2 cert = store.Certificates.Cast<X509Certificate2>().First(item => item.Thumbprint == thumbprint);
		
		        // CREATE AN HDINSIGHT CLIENT OBJECT
		        HDInsightCertificateCredential creds = new HDInsightCertificateCredential(new Guid(subscriptionId), cert);
		        var client = HDInsightClient.Connect(creds);
				client.IgnoreSslErrors = true;
		
		        // PROVIDE THE CLUSTER INFORMATION
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
		
		10. Append the following code to the **Main()** function to use the [ScriptAction](http://msdn.microsoft.com/zh-cn/library/microsoft.windowsazure.management.hdinsight.clusterprovisioning.data.scriptaction.aspx) class to invoke a custom script to install R.
		
				// ADD THE SCRIPT ACTION TO INSTALL R
		
		        clusterInfo.ConfigActions.Add(new ScriptAction(
		            "Install R",
		            new ClusterNodeType[] { ClusterNodeType.HeadNode, ClusterNodeType.DataNode },
		            new Uri("https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps1"), null
		            ));
		
		11. Finally, create the cluster:
		
				client.CreateCluster(clusterInfo);
		
		11. Save changes to the application and build the solution.
		
		**To run the application**
		
		Open the Azure PowerShell console, navigate to the location where you saved the project, navigate to the \bin\debug directory within the project, and then run the following command:
		
			.\CreateRCluster <cluster-name>
		
		Provide a cluster name and press ENTER to provision a cluster with R installed.

reason: ()

