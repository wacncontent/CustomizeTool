deletion:

deleted:

		(Linux)

reason: ()

replacement:

deleted:

		creation

replaced by:

		provision

reason: ()

deleted:

		creation

replaced by:

		provision

reason: ()

deleted:

		creation

replaced by:

		provision

reason: ()

deleted:

		creation][img-hdi-cluster-states]

replaced by:

		provisioning][img-hdi-cluster-states]

reason: ()

deleted:

		> [AZURE.IMPORTANT] Script actions must complete within 15 minutes, or they will timeout. During node provisioning, the script is ran concurrently with other setup and configuration processes. Competition for resources such as CPU time or network bandwidth may cause the script to take longer to finish than it does in your development environment.
		> 
		> To minimize the time it takes to run the script, avoid tasks such as downloading and compiling applications from source. Instead, pre-compile the application and store the binary in Azure Blob storage so that it can quickly be downloaded to the cluster.

replaced by:

		> [AZURE.IMPORTANT] Script actions must complete within 15 minutes, or they will timeout.

reason: ()

deleted:

		Preview

replaced by:

		Management

reason: ()

deleted:

		https://hdiconfigactions.blob.core.windows.net/linuxsparkconfigactionv02/spark-installer-v02.sh

replaced by:

		https://hdiconfigactions.blob.core.windows.net/linuxsparkconfigactionv01/spark-installer-v01.sh

reason: ()

deleted:

		## Use a Script Action from the Azure Preview portal
		
		1. Start creating a cluster as described at [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters#portal).

replaced by:

		##Use a Script Action from the Azure Management Portal
		
		1. Start provisioning a cluster as described at [Provisioning a cluster using custom options](/documentation/articles/hdinsight-provision-clusters#portal).

reason: ()

deleted:

		creation

replaced by:

		provisioning

reason: ()

deleted:

		## Use

replaced by:

		##Use

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

		### Create clusters using script action

replaced by:

		### Provision cluster using script action

reason: ()

deleted:

		## Use a Script Action from Azure PowerShell
		
		In this section, we use the **<a href = "http://msdn.microsoft.com/zh-cn/library/dn858088.aspx" target="_blank">Add-AzureHDInsightScriptAction</a>** cmdlet to invoke scripts by using Script Action to customize a cluster. Before proceeding, make sure you have installed and configured Azure PowerShell. For information about configuring a workstation to run HDInsight PowerShell cmdlets, see [Install and configure Azure PowerShell](/documentation/articles/powershell-install-configure).

replaced by:

		##Use a Script Action from Azure PowerShell
		
		In this section, we use the **<a href = "http://msdn.microsoft.com/zh-cn/library/dn858088.aspx" target="_blank">Add-AzureHDInsightScriptAction</a>** cmdlet to invoke scripts by using Script Action to customize a cluster. Before proceeding, make sure you have installed and configured Azure PowerShell. For information about configuring a workstation to run HDInsight Powershell cmdlets, see [Install and configure Azure PowerShell](/documentation/articles/powershell-install-configure).

reason: ()

deleted:

		create

replaced by:

		provision

reason: ()

deleted:

		## Use

replaced by:

		##Use

reason: ()

deleted:

		> [AZURE.IMPORTANT] You must first create a self-signed certificate, install it on your workstation, and then upload it to your Azure subscription. For instructions, see [Create a self-signed certificate](/documentation/articles/hdinsight-administer-use-management-portal-v1/#cert).
		
		
		### Create a Visual Studio project
		
		
		1. Create a C# console application in Visual Studio.
		2. From the Nuget **Package Manager Console**, run the following commands:
		
				Install-Package Microsoft.Azure.Common.Authentication -pre
				Install-Package Microsoft.Azure.Management.HDInsight -Pre
		
			These commands add .NET libraries and references to them to the current Visual Studio project.
		
		3. Open **Program.cs**, and add the following using statements:
		
				using System;
				using System.Security;
				using Microsoft.Azure;
				using Microsoft.Azure.Common.Authentication;
				using Microsoft.Azure.Common.Authentication.Factories;
				using Microsoft.Azure.Common.Authentication.Models;
				using Microsoft.Azure.Management.HDInsight;
				using Microsoft.Azure.Management.HDInsight.Models;
		
		4. Replace the code in the class with the following:
		
		        private static HDInsightManagementClient _hdiManagementClient;
		
		        private static Guid SubscriptionId = new Guid("<AZURE SUBSCRIPTION ID>");
		        private const string ResourceGroupName = "<AZURE RESOURCEGROUP NAME>";
		
		        private const string NewClusterName = "<HDINSIGHT CLUSTER NAME>";
		        private const int NewClusterNumNodes = <NUMBER OF NODES>;
		        private const string NewClusterLocation = "<LOCATION>";  // Must match the Azure Storage account location
		        private const string NewClusterVersion = "3.2";
		        private const HDInsightClusterType NewClusterType = HDInsightClusterType.Hadoop;
		        private const OSType NewClusterOSType = OSType.Windows;
		
		        private const string ExistingStorageName = "<STORAGE ACCOUNT NAME>.blob.core.chinacloudapi.cn";
		        private const string ExistingStorageKey = "<STORAGE ACCOUNT KEY>";
		        private const string ExistingContainer = "<DEFAULT CONTAINER NAME>"; 
		
		        private const string NewClusterUsername = "admin";
		        private const string NewClusterPassword = "<HTTP USER PASSWORD>";
		
		        private const string NewClusterSshUserName = "sshuser";
		        private const string NewClusterSshPublicKey = @"---- BEGIN SSH2 PUBLIC KEY ----
					Comment: ""rsa-key-20150731""
					AAAAB3NzaC1yc2EAAAABJQAAAQEA4QiCRLqT7fnmUA5OhYWZNlZo6lLaY1c+IRsp
					gmPCsJVGQLu6O1wqcxRqiKk7keYq8bP5s30v6bIljsLZYTnyReNUa5LtFw7eauGr
					yVt3Pve6ejfWELhbVpi0iq8uJNFA9VvRkz8IP1JmjC5jsdnJhzQZtgkIrdn3w0e6
					WVfu15kKyY8YAiynVbdV51EB0SZaSLdMZkZQ81xi4DDtCZD7qvdtWEFwLa+EHdkd
					pzO36Mtev5XvseLQqzXzZ6aVBdlXoppGHXkoGHAMNOtEWRXpAUtEccjpATsaZhQR
					zZdZlzHduhM10ofS4YOYBADt9JohporbQVHM5w6qUhIgyiPo7w==
					---- END SSH2 PUBLIC KEY ----"; //replace the public key with your own
		
		        private static void Main(string[] args)

replaced by:

		> [AZURE.IMPORTANT] You must first create a self-signed certificate, install it on your workstation, and then upload it to your Azure subscription. For instructions, see [Create a self-signed certificate](/documentation/articles/hdinsight-administer-use-management-portal-v1#cert).
		
		
		###Create a Visual Studio project
		
		1. Open Visual Studio 2013 or 2015.
		
		2. From the **File** menu, click **New**, and then click **Project**.
		
		3. From **New Project**, type or select the following values:
		
			| Property | Value |
			| -------- | ----- |
			| Category | Templates/Visual C#/Windows |
			| Template | Console Application |
			| Name | ScriptActionCluster |
		
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

reason: ()

deleted:

		var tokenCreds = GetTokenCloudCredentials();
		            var subCloudCredentials = GetSubscriptionCloudCredentials(tokenCreds, SubscriptionId);
		
		            _hdiManagementClient = new HDInsightManagementClient(subCloudCredentials);
		
		            CreateCluster();
		        } <!-- keep by customization: begin -->; <!-- keep by customization: end -->
		
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
		                SshUserName = NewClusterSshUserName,
		        		SshPublicKey = NewClusterSshPublicKey
		            };
		
		            ScriptAction rScriptAction = new ScriptAction("Install R",
		                new Uri("https://hdiconfigactions.blob.core.windows.net/linuxrconfigactionv01/r-installer-v01.sh"), "");
		
		            parameters.ScriptActions.Add(ClusterNodeType.HeadNode,new System.Collections.Generic.List<ScriptAction> { rScriptAction});
		            parameters.ScriptActions.Add(ClusterNodeType.WorkerNode, new System.Collections.Generic.List<ScriptAction> { rScriptAction });
		
		            _hdiManagementClient.Clusters.Create(ResourceGroupName, NewClusterName, parameters);
		        }
				
		6. Replace the class member values.
		
		7. Press **F5** to run the application. A console window should open and display the status of the application. You will also be prompted to enter your Azure account credentials. It can take several minutes to create an HDInsight cluster.

replaced by:

		Name = clusterName,
		            Location = location,
		            DefaultStorageAccountName = storageaccountname,
		            DefaultStorageAccountKey = storageaccountkey,
		            DefaultStorageContainer = clusterName,
		            UserName = username,
		            Password = password,
		            ClusterSizeInNodes = clustersize,
		            Version = "3.1"
		        } <!-- keep by customization: begin -->;

reason: ()

deleted:

		> [AZURE.WARNING] Components provided with the HDInsight cluster

replaced by:

		Built-in components

reason: ()

deleted:

		>
		> Custom components receive commercially reasonable support to help you to further troubleshoot the issue. This might result in resolving the issue OR asking you to engage available channels for the open source technologies where deep expertise for that technology is found. For example, there are many community sites that can be used, like: [MSDN forum for HDInsight](https://social.msdn.microsoft.com/Forums/azure/zh-cn/home?forum=hdinsight), [http://stackoverflow.com](http://stackoverflow.com). Also Apache projects have project sites on [http://apache.org](http://apache.org), for example: [Hadoop](http://hadoop.apache.org/), [Spark](http://spark.apache.org/).

replaced by:

		Custom components receive commercially reasonable support to help you to further troubleshoot the issue. This might result in resolving the issue or asking you to engage available channels for the open-source technologies where deep expertise for that technology is found. For example, there are many community sites that can be used, like:
		
		* [MSDN forum for HDInsight](https://social.msdn.microsoft.com/Forums/azure/home?forum=hdinsight)
		
		* [Stack Overflow](https://stackoverflow.com)
		
		Also, Apache projects have project sites on [Apache.org](https://apache.org); for example, [Hadoop](http://hadoop.apache.org/) and [Spark](http://spark.apache.org/).

reason: ()

deleted:

		## Troubleshooting
		
		You can use Ambari web UI to view information logged by scripts during cluster creation.

replaced by:

		##Troubleshooting
		
		You can use Ambari web UI to view information logged by scripts during cluster provisioning.

reason: ()

deleted:

		[img-hdi-cluster-states]: ./media/hdinsight-hadoop-customize-cluster/HDI-Cluster-state.png "Stages during cluster creation"

replaced by:

		[img-hdi-cluster-states]: ./media/hdinsight-hadoop-customize-cluster/HDI-Cluster-state.png "Stages during cluster provisioning"

reason: ()

