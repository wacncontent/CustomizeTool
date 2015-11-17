deletion:

deleted:

		AND INPUT__FILE__NAME LIKE '%.log'

reason: ()

deleted:

		* **INPUT__FILE__NAME LIKE '%.log'** - Tells Hive that we should only return data from files ending in .log. This restricts the search to the sample.log file that contains the data, and keeps it from returning data from other example data files that do not match the schema we defined.

reason: ()

deleted:

		AND INPUT__FILE__NAME LIKE '%.log'

reason: ()

replacement:

deleted:

		> [AZURE.IMPORTANT] While the Hive command is available on Linux-based HDInsight clusters, you should consider using Beeline. Beeline is a newer client for working with Hive, and is included with your HDInsight cluster. For more information on using this, see [Use Hive with Hadoop in HDInsight with Beeline](/documentation/articles/hdinsight-hadoop-use-hive-beeline).

replaced by:

		> [AZURE.NOTE] If you are already familiar with using Linux-based Hadoop servers, but are new to HDInsight, see [What you need to know about Hadoop on Linux-based HDInsight](/documentation/articles/hdinsight-hadoop-linux-information).

reason: ()

deleted:

		[hdinsight-sdk-documentation]: http://msdnstage.redmond.corp.microsoft.com/zh-cn/library/dn479185.aspx
		
		[azure-purchase-options]: /pricing/overview/
		[azure-member-offers]: /pricing/member-offers/
		[azure-trial]: /pricing/1rmb-trial/

replaced by:

		[hdinsight-sdk-documentation]: http://msdn.microsoft.com/zh-cn/library/dn479185.aspx

reason: ()

deleted:

		/documentation/articles/hdinsight-connect-excel-power-query/

replaced by:

		/documentation/articles/hdinsight-connect-excel-power-query

reason: ()

