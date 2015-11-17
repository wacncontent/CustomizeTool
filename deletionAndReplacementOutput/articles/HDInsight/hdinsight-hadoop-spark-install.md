deletion:

deleted:

		using Script Action

reason: ()

replacement:

deleted:

		> [AZURE.IMPORTANT] This article is now deprecated. HDInsight now provides Spark as a first-class cluster type for Windows-based clusters, which means you can now directly create a Spark cluster without modifying a Hadoop cluster using Script action. Using the Spark cluster type, you get an HDInsight version 3.2 cluster with Spark version 1.3.1.  To install different versions of Spark, you can use Script action. HDInsight provides a sample Script Action script.
		
		Learn how to install Spark on Windows based HDInsight using Script Action, and how to run Spark queries on HDInsight clusters.
		
		
		**Related articles**
		- [Install Spark on Linux-based HDInsight clusters](/documentation/articles/hdinsight-hadoop-spark-install-linux).
		
		- [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters): general information on creating HDInsight clusters.
		
		- [Get Started with Apache Spark on HDInsight](/documentation/articles/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql): create a Spark type cluster on Windows OS.
		
		- [Customize HDInsight cluster using Script Action][hdinsight-cluster-customize]: general information on customizing HDInsight clusters using Script Action.
		
		- [Develop Script Action scripts for HDInsight](/documentation/articles/hdinsight-hadoop-script-actions).
		
		## What is Spark?

replaced by:

		You can install Spark on any type of cluster in Hadoop on Azure HDInsight by using **Script Action** cluster customization. Script Action lets you run scripts to customize a cluster, only when the cluster is being created. For more information, see [Customize HDInsight cluster using Script Action][hdinsight-cluster-customize].
		
		In this topic, you will learn how to install Spark by using Script Action. Once you have installed Spark, you'll also learn how to run a Spark query on HDInsight clusters.
		
		> [AZURE.NOTE] HDInsight now provides Spark as a first-class cluster type, which means you can now directly provision a Spark cluster without modifying a Hadoop cluster. Using the Spark cluster type, you get an HDInsight version 3.2 cluster with Spark version 1.3.1. For more information, see [Get Started with Apache Spark on HDInsight](/documentation/articles/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql).
		
		
		## <a name="whatis"></a>What is Spark?

reason: ()

deleted:

		## Install Spark using the Azure Preview portal
		
		A sample script to install Spark on an HDInsight cluster is available from a read-only Azure storage blob at [https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1](https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1). This script can install Spark 1.2.0 or Spark 1.0.2 depending on the version of the HDInsight cluster you create.
		
		- If you use the script while creating an **HDInsight 3.2** cluster, it installs **Spark 1.2.0**.
		- If you use the script while creating an **HDInsight 3.1** cluster, it installs **Spark 1.0.2**.

replaced by:

		## <a name="whatis"></a>Which version of Spark can I install?
		
		In this topic, we use a Script Action custom script to install Spark on an HDInsight cluster. This script can install Spark 1.2.0 or Spark 1.0.2 depending on the version of the HDInsight cluster you provision.
		
		- If you use the script while provisioning an **HDInsight 3.2** cluster, it installs **Spark 1.2.0**.
		- If you use the script while provisioning an **HDInsight 3.1** cluster, it installs **Spark 1.0.2**.

reason: ()

deleted:

		creating

replaced by:

		provisioning

reason: ()

deleted:

		[Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters#portal)

replaced by:

		[Provisioning a cluster using custom options](/documentation/articles/hdinsight-provision-clusters#portal)

reason: ()

deleted:

		create

replaced by:

		provision

reason: ()

deleted:

		create

replaced by:

		provision

reason: ()

deleted:

		cluster](./media/hdinsight-hadoop-spark-install/HDI.CustomProvision.Page6.png

replaced by:

		cluster](./media/hdinsight-hadoop-customize-cluster/HDI.CustomProvision.Page6.png

reason: ()

deleted:

		creating

replaced by:

		provisioning

reason: ()

deleted:

		## Use Spark in HDInsight

replaced by:

		## <a name="usespark"></a>How do I use Spark in HDInsight?

reason: ()

deleted:

		[Use

replaced by:

		[Using

reason: ()

deleted:

		[Use

replaced by:

		[Using

reason: ()

deleted:

		- [Use a standalone Scala program](#standalone)
		
		###<a <!-- deleted by customization name="sparkshell"></a>Use --><!-- keep by customization: begin --> name="sparkshell"></a>Using <!-- keep by customization: end --> the Spark shell to run interactive queries

replaced by:

		- [Using a standalone Scala program](#standalone)
		
		###<a <!-- deleted by customization name="sparkshell"></a>Use --><!-- keep by customization: begin --> name="sparkshell"></a>Using

reason: ()

deleted:

		name="sparksql"></a>Use

replaced by:

		name="sparksql"></a>Using

reason: ()

deleted:

		create

replaced by:

		provision

reason: ()

deleted:

		creating

replaced by:

		provisioning

reason: ()

deleted:

		### <a name="standalone"></a>Use a standalone Scala program

replaced by:

		### <a name="standalone"></a>Using a standalone Scala program

reason: ()

deleted:

		## Install Spark using Azure PowerShell

replaced by:

		## <a name="usingPS"></a>Install Spark on HDInsight Hadoop clusters by using Azure PowerShell

reason: ()

deleted:

		head node)

replaced by:

		headnode)

reason: ()

deleted:

		data nodes)

replaced by:

		datanodes)

reason: ()

deleted:

		4. Finally, start creating a customized cluster with Spark installed.
				# Start creating a cluster with Spark installed

replaced by:

		4. Finally, start provisioning a customized cluster with Spark installed.
			
				# Start provisioning a cluster with Spark installed

reason: ()

deleted:

		## Install Spark using PowerShell
		
		See [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster#call_scripts_using_powershell).
		
		## Install Spark using .NET SDK
		
		See [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster#call_scripts_using_azure_powershell).
		
		
		## See also
		
		- [Install Spark on Linux-based HDInsight clusters](/documentation/articles/hdinsight-hadoop-spark-install-linux): install Spark on Linux based HDInsight clusters.
		- [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters): create HDInsight clusters.
		- [Get Started with Apache Spark on HDInsight](/documentation/articles/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql): get started with Spark on HDInsight.
		- [Customize HDInsight cluster using Script Action][hdinsight-cluster-customize]: customize HDInsight clusters using Script Action.
		- [Develop Script Action scripts for HDInsight](/documentation/articles/hdinsight-hadoop-script-actions): develop Script Action scripts.

replaced by:

		## <a name="usingSDK"></a>Install Spark on HDInsight Hadoop clusters by using the .NET SDK
		
		The HDInsight .NET SDK provides .NET client libraries that make it easier to work with HDInsight from a .NET Framework application. This section provides instructions on how to use Script Action from the SDK to provision a cluster that has Spark installed. The following procedures must be performed:
		
		- Install the HDInsight .NET SDK
		- Create a self-signed certificate
		- Create a console application
		- Run the application
		
		
		**To install the HDInsight .NET SDK**
		
		You can install latest published build of the SDK from [NuGet](http://nuget.codeplex.com/wikipage?title=Getting%20Started). The instructions will be shown in the next procedure.
		
		**To create a self-signed certificate**
		
		Create a self-signed certificate, install it on your workstation, and upload it to your Azure subscription. For instructions, see [Create a self-signed certificate](/documentation/articles/hdinsight-administer-use-management-portal-v1#cert). 
		
		
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
			<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">CreateSparkCluster</td></tr>
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
			
		9. In the Main() function, copy and paste the following code, and provide values for the variables :
				
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
		            Version = "3.2"
		        };        
		
		10. Append the following code to the Main() function to use the [ScriptAction](http://msdn.microsoft.com/zh-cn/library/microsoft.windowsazure.management.hdinsight.clusterprovisioning.data.scriptaction.aspx) class to invoke a custom script to install Spark.
		
				// Add the script action to install Spark
		        clusterInfo.ConfigActions.Add(new ScriptAction(
		          "Install Spark", // Name of the config action
		          new ClusterNodeType[] { ClusterNodeType.HeadNode }, // List of nodes to install Spark on
		          new Uri("https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1"), // Location of the script to install Spark.
				  null //Because the script used does not require any parameters
		        ));
		
		11. Finally, create the cluster.
		
				client.CreateCluster(clusterInfo);
		
		11. Save changes to the application and build the solution. 
		
		**To run the application**
		
		Open an Azure PowerShell console, navigate to the location where you saved the Visual Studio project, navigate to the \bin\debug directory within the project, and then run the following command:
		
			.\CreateSparkCluster <cluster-name>
		
		Provide a cluster name and press ENTER to provision a cluster with Spark installed.
		
		
		## See also##

reason: ()

