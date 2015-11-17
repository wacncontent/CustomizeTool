deletion:

deleted:

		> [AZURE.WARNING] You may discover that some Spark 1.3.1 binaries are installed by default on your HDInsight cluster. These should not be used, and will be removed from the HDInsight cluster image in a future update.

reason: ()

deleted:

		> [AZURE.NOTE] The example Spark script only installs components on the head nodes, so the other node types can be unchecked.

reason: ()

replacement:

deleted:

		1.5.1

replaced by:

		1.3.1

reason: ()

deleted:

		1.5.1

replaced by:

		1.3.1

reason: ()

deleted:

		[https://hdiconfigactions.blob.core.windows.net/linuxsparkconfigactionv02/spark-installer-v02.sh](https://hdiconfigactions.blob.core.windows.net/linuxsparkconfigactionv02/spark-installer-v02.sh)

replaced by:

		[https://hdiconfigactions.blob.core.windows.net/linuxsparkconfigactionv01/spark-installer-v01.sh](https://hdiconfigactions.blob.core.windows.net/linuxsparkconfigactionv01/spark-installer-v01.sh)

reason: ()

deleted:

		creating

replaced by:

		provisioning

reason: ()

deleted:

		1. Start creating a cluster by using the steps in [Create Linux-based HDInsight clusters](/documentation/articles/hdinsight-provision-linux-clusters#portal), but do not complete creation.

replaced by:

		1. Start provisioning a cluster by using the steps in [Provision Linux-based HDInsight clusters](/documentation/articles/hdinsight-provision-linux-clusters#portal), but do not complete provisioning.

reason: ()

deleted:

		* __SCRIPT URI__: https://hdiconfigactions.blob.core.windows.net/linuxsparkconfigactionv02/spark-installer-v02.sh

replaced by:

		* __SCRIPT URI__: https://hdiconfigactions.blob.core.windows.net/linuxsparkconfigactionv01/spark-installer-v01.sh

reason: ()

deleted:

		* __WORKER__: Uncheck this option
			* __ZOOKEEPER__: Uncheck this option

replaced by:

		* __WORKER__: Check this option
			* __ZOOKEEPER__: Check this option to install on the Zookeeper node.

reason: ()

deleted:

		[Create

replaced by:

		[Provision

reason: ()

deleted:

		creation

replaced by:

		provisioning

reason: ()

deleted:

		create

replaced by:

		provision

reason: ()

deleted:

		/usr/hdp/current/spark/bin/spark-submit --class "SimpleApp" --master yarn target/scala-2.10/simpleapp_2.10-1.0.jar

replaced by:

		/usr/hdp/current/spark/bin/spark-submit --class "SimpleApp" --master local target/scala-2.10/simpleapp_2.10-1.0.jar

reason: ()

