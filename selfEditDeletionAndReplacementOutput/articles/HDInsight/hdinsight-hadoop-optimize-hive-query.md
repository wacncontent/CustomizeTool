deletion:

deleted:

		[AZURE.INCLUDE [preview-portal](../includes/hdinsight-azure-preview-portal.md)]

reason: (the new Ibiza portal)

deleted:

		> [AZURE.NOTE] Linux-based HDInsight clusters have Tez enabled by default.

reason: (Linux Support)

deleted:

		- [Analyze Twitter data using Hive in HDInsight](/documentation/articles/hdinsight-analyze-twitter-data)

reason: (google facebook twitter)

replacement:

deleted:

		Increasing the number of worker nodes in a cluster can leverage more mappers and reducers to be run in parallel. There are two ways you can increase scale out in HDInsight:
		
		- At the provision time, you can specify the number of worker nodes using the Azure preview portal, Azure PowerShell or Cross-platform command line interface.  For more information, see [Provision HDInsight clusters](/documentation/articles/hdinsight-provision-clusters). The following screen show the worker node configuration on the Azure preview portal:
		
			![scaleout_1][image-hdi-optimize-hive-scaleout_1]
		
		- At the run time, you can also scale out a cluster without recreating one. This is shown below.
		![scaleout_1][image-hdi-optimize-hive-scaleout_2]

replaced by:

		Scale out refers to increasing the number of nodes that you can have in your cluster. Increasing nodes helps because you can run more mappers and reducers because you have more tasks that can be run in parallel. There are two ways you can increase scale out in HDInsight:
		
		1. During cluster creation, you can pick how many nodes you want your query to run in. This is shown in the image below.
		![scaleout_1][image-hdi-optimize-hive-scaleout_1]
		2. If you already have a cluster up and running, you can also increase the scale without deleting and recreating the cluster. This is shown below.
		![scaleout_1][image-hdi-optimize-hive-scaleout_2]

reason: (the new Ibiza portal)

