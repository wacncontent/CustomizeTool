deletion:

deleted:

		Ambari,

reason: ()

deleted:

		#### Example customization scripts
		
		Script Actions are scripts that are ran during cluster provisioning, and can be used to install additional components on the cluster. For Windows-based HDInsight clusters, these are PowerShell scripts. For Linux-based clusters, these are Bash scripts.
		
		The following are example scripts provided by the HDInsight team:
		
		* [Hue](/documentation/articles/hdinsight-hadoop-hue-linux)
		
			> [AZURE.NOTE] The Hue script is available only for Linux-based clusters.
		
		* [Giraph](/documentation/articles/hdinsight-hadoop-giraph-install-linux)
		
		* [R](/documentation/articles/hdinsight-hadoop-r-scripts-linux)
		
		* [Solr](/documentation/articles/hdinsight-hadoop-solr-install-linux)
		
		* [Spark](/documentation/articles/hdinsight-hadoop-spark-install-linux)
		
		For information on developing your own Script Actions, see [Script Action development with HDInsight](/documentation/articles/hdinsight-hadoop-script-actions-linux).

reason: ()

deleted:

		* **[Ambari](#ambari)**: Cluster provisioning, management, and monitoring.
		
			> [AZURE.NOTE] Only a subset of the Ambari REST API is provided for Windows-based HDInsight clusters.

reason: ()

deleted:

		###<a name="ambari"></a>Ambari
		
		Apache Ambari is for provisioning, managing and monitoring Apache Hadoop clusters. It includes an intuitive collection of operator tools and a robust set of APIs that hide the complexity of Hadoop, simplifying the operation of clusters. Linux-based HDInsight clusters provide both the Ambari web UI and the Ambari REST API, while Windows-based clusters provide a subset of the REST API.
		
		See [Manage HDInsight clusters using Ambari](/documentation/articles/hdinsight-hadoop-manage-ambari) (Linux only), [Monitor Hadoop clusters in HDInsight using the Ambari API](/documentation/articles/hdinsight-monitor-use-ambari-api), and <a target="_blank" href="https://github.com/apache/ambari/blob/trunk/ambari-server/docs/api/v1/index.md">Apache Ambari API reference</a>.

reason: ()

deleted:

		* [Get started with HDInsight on Linux](/documentation/articles/hdinsight-hadoop-linux-tutorial-get-started): A quick-start tutorial for provisioning HDInsight Hadoop clusters on Linux and running sample Hive queries.
		
		* [Get started with Linux-based Storm on HDInsight](/documentation/articles/hdinsight-apache-storm-tutorial-get-started): A quick-start tutorial for provisioning a Storm on HDInsight cluster and running sample Storm topologies.
		
		* [Provision HDInsight on Linux](/documentation/articles/hdinsight-provision-clusters): Learn how to provision an HDInsight Hadoop cluster on Linux through the Azure Management Portal, Azure CLI, or Azure PowerShell.
		
		* [Working with HDInsight on Linux](/documentation/articles/hdinsight-hadoop-linux-information): Get some quick tips on working with Hadoop Linux clusters provisioned on Azure.
		
		* [Manage HDInsight clusters using Ambari](/documentation/articles/hdinsight-hadoop-manage-ambari): Learn how to monitor and manage your Linux-based Hadoop on HDInsight cluster by using Ambari Web, or the Ambari REST API.
		
		
		### HDInsight on Windows
		
		* [HDInsight documentation](/documentation/services/hdinsight/): The documentation page for Azure HDInsight with links to articles, videos, and more resources.

reason: ()

replacement:

deleted:

		### Linux and Windows clusters
		
		Azure HDInsight deploys and provisions Hadoop clusters in the cloud, by using either **Linux** or **Windows** as the underlying OS.
		
		* **HDInsight on Linux** - A Hadoop cluster on Ubuntu. Use this if you are familiar with Linux or Unix, are migrating from an existing Linux-based Hadoop solution, or want easy integration with Hadoop ecosystem components built for Linux.

replaced by:

		### Windows clusters
		
		Azure HDInsight deploys and provisions Hadoop clusters in the cloud, by using  **Windows** as the underlying OS.

reason: ()

deleted:

		Category | Hadoop on Linux | Hadoop on Windows
		---------| -------------------| --------------------
		**Cluster OS** | Ubuntu 12.04 Long Term Support (LTS) | Windows Server 2012 R2
		**Cluster Type** | Hadoop, HBase, Storm | Hadoop, HBase, Storm
		**Deployment** | Azure preview portal, Azure CLI, Azure PowerShell | Azure Management Portal, Azure preview portal, Azure CLI, Azure PowerShell, HDInsight .NET SDK
		**Cluster UI** | Ambari | Cluster Dashboard
		**Remote Access** | Secure Shell (SSH), REST API, ODBC, JDBC | Remote Desktop Protocol (RDP), REST API, ODBC, JDBC
		
		
		
		### Hadoop, HBase, Storm, Spark, and customized clusters

replaced by:

		Category | Hadoop on Windows
		---------|  --------------------
		**Cluster OS** | Windows Server 2012 R2
		**Cluster Type** | Hadoop, HBase, Storm 
		**Deployment** |  Azure CLI, Azure PowerShell | Azure Management Portal, Azure  CLI, Azure PowerShell, HDInsight .NET SDK
		**Cluster UI** |  Cluster Dashboard
		**Remote Access**  | Remote Desktop Protocol (RDP), REST API, ODBC, JDBC
		
		
		
		### Hadoop, HBase, Storm,  and customized clusters

reason: ()

deleted:

		### HDInsight on Linux

replaced by:

		### HDInsight on Windows

reason: ()

deleted:

		SDK](http://msdnstage.redmond.corp.microsoft.com/zh-cn/library/dn479185.aspx)

replaced by:

		SDK](http://msdn.microsoft.com/zh-cn/library/dn479185.aspx)

reason: ()

