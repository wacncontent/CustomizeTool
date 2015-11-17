replacement:

deleted:

		> [AZURE.NOTE] The information in this article is primarily for Windows-based HDInsight clusters, which provide a read-only version of the Ambari REST API. For Linux-based clusters, see [Manage Hadoop clusters using Ambari](/documentation/articles/hdinsight-hadoop-manage-ambari).
		
		## What is Ambari?

replaced by:

		## <a id="whatisambari"></a> What is Ambari?

reason: ()

deleted:

		**Prerequisites**

replaced by:

		##<a id="prerequisites"></a>Prerequisites

reason: ()

deleted:

		## Jump start

replaced by:

		##<a id="jumpstart"></a>Jump start

reason: ()

deleted:

		When using the Ambari endpoint, "https://{clusterDns}.azurehdinsight.cn/ambari/api/v1/clusters/{clusterDns}.azurehdinsight.cn/services/{servicename}/components/{componentname}", the *host_name* field returns the fully qualified domain name (FQDN) of the node instead of the host name. Before the 10/8/2014 release, this example returned simply "**headnode0**". After the 10/8/2014 release, you get the FQDN "**headnode0.{ClusterDNS}.azurehdinsight.cn**", as shown in the previous example. This change was required to facilitate scenarios where multiple cluster types (such as HBase and Hadoop) can be deployed in one virtual network (VNET). This happens, for example, when using HBase as a back-end platform for Hadoop.
		
		## Ambari monitoring APIs

replaced by:

		When using the Ambari endpoint, "https://{clusterDns}.azurehdinsight.cn/ambari/api/v1/clusters/{clusterDns}.azurehdinsight.cn/services/{servicename}/components/{componentname}", the *host_name* field returns the fully qualified domain name (FQDN) of the node instead of the host name. Before the 10/8/2014 release, this example returned simply **headnode0**". After the 10/8/2014 release, you get the FQDN "**headnode0.{ClusterDNS}.azurehdinsight.cn**", as shown in the previous example. This change was required to facilitate scenarios where multiple cluster types (such as HBase and Hadoop) can be deployed in one virtual network (VNET). This happens, for example, when using HBase as a back-end platform for Hadoop.
		
		##<a id="monitor"></a>Ambari monitoring APIs

reason: ()

deleted:

		##Next Steps

replaced by:

		##<a id="nextsteps"></a>Next Steps

reason: ()

deleted:

		- [Manage HDInsight clusters using the Azure preview portal][hdinsight-admin-portal]

replaced by:

		- [Manage HDInsight clusters using the Management portal][hdinsight-admin-portal]

reason: ()

deleted:

		[powershell-install]: /documentation/articles/install-configure-powershell
		[powershell-script]: http://technet.microsoft.com/zh-cn/library/ee176949.aspx

replaced by:

		[Powershell-install]: /documentation/articles/install-configure-powershell
		[Powershell-script]: http://technet.microsoft.com/zh-cn/library/ee176949.aspx

reason: ()

