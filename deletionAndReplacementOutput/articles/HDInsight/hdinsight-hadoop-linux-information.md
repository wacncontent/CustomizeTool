deletion:

deleted:

		Instead, use [HDInsight Script Actions](/documentation/articles/hdinsight-hadoop-customize-cluster) when you need to install the following:

reason: ()

deleted:

		###Jar files
		
		Some Hadoop technologies are provided in self-contained jar files that are contain functions used as part of a MapReduce job, or from inside Pig or Hive. While these can be installed using Script Actions, they often don't require any setup and can just be uploaded to the cluster after provisioning and used directly. If you want to makle sure the component survives reimaging of the cluster, you can store the jar file in WASB.
		
		For example, if you want to use the latest version of [DataFu](http://datafu.incubator.apache.org/), you can download a jar containing the project and upload it to the HDInsight cluster. Then follow the DataFu documentation on how to use it from Pig or Hive.
		
		> [AZURE.IMPORTANT] Some components that are standalone jar files are provided with HDInsight, but are not in the path. If you are looking for a specific component, you can use the follow to search for it on your cluster:
		>
		> ```find / -name *componentname*.jar 2>/dev/null```
		>
		> This will return the path of any matching jar files.
		
		If the cluster already provides a version of a component as a standalone jar file, but you want to use a different version, you can upload a new version of the component to the cluster and try using it in your jobs.
		
		> [AZURE.WARNING] Components provided with the HDInsight cluster are fully supported and Microsoft Support will help to isolate and resolve issues related to these components.
		>
		> Custom components receive commercially reasonable support to help you to further troubleshoot the issue. This might result in resolving the issue OR asking you to engage available channels for the open source technologies where deep expertise for that technology is found. For example, there are many community sites that can be used, like: [MSDN forum for HDInsight](https://social.msdn.microsoft.com/Forums/azure/zh-cn/home?forum=hdinsight), [http://stackoverflow.com](http://stackoverflow.com). Also Apache projects have project sites on [http://apache.org](http://apache.org), for example: [Hadoop](http://hadoop.apache.org/), [Spark](http://spark.apache.org/).

reason: ()

replacement:

deleted:

		nodes

replaced by:

		node

reason: ()

deleted:

		3. To find the key used to authenticate to the storage account, or to find any secondary storage accounts associated with the cluster, use the following:
		
				curl -u admin:PASSWORD -G "https://CLUSTERNAME.azurehdinsight.cn/api/v1/clusters/CLUSTERNAME/configurations/service_config_versions?service_name=HDFS&service_config_version=1"
		
		4. In the JSON data returned, find the entries that begin with `fs.azure.account.key`. The remainder of the entry name is the storage account name. For example, `fs.azure.account.key.mystorage.blob.core.chinacloudapi.cn`. The value stored in this entry is the key used to authenticate to the storage account.
		
			> [AZURE.TIP] If you have installed [jq](http://stedolan.github.io/jq/), you can use the following to return a list of the keys and values:
			>
			> `curl -u admin:PASSWORD -G "https://CLUSTERNAME.azurehdinsight.cn/api/v1/clusters/CLUSTERNAME/configurations/service_config_versions?service_name=HDFS&service_config_version=1" | jq '.items[].configurations[].properties as $in | $in | keys[] | select(. | contains("fs.azure.account.key.")) as $item | $item | ltrimstr("fs.azure.account.key.") | { storage_account: ., storage_account_key: $in[$item] }'`
		
		You can also find the storage information using the Azure preview portal:
		
		1. In the [Azure Preview Portal](https://manage.windowsazure.cn/), select your HDInsight cluster.
		
		2. From the __Essentials__ section, select __All settings__.
		
		3. From __Settings__, select __Azure Storage Keys__.
		
		4. From __Azure Storage Keys__, select one of the storage accounts listed. This will display information about the storage account.
		
		5. Select the key icon. This will display keys for this storage account.

replaced by:

		**Azure Management Portal**
		
		1. In the [Azure Management Portal](https://manage.windowsazure.cn/), select your HDInsight cluster.
		
		2. Select **Dashboard** at the top of the page.
		
		3. The Storage account(s) and container(s) are listed in the **linked resources** section of the page.
		
			![linked resources](./media/hdinsight-hadoop-linux-information/storageportal.png)

reason: ()

deleted:

		Windows](/documentation/articles/xplat-cli-install)

replaced by:

		Windows](/documentation/articles/xplat-cli)

reason: ()

deleted:

		![Storm UI entry in quick links](./media/hdinsight-hadoop-linux-information/ambari-storm.png)

replaced by:

		![Storm UI entry in quick links](./media/hdinsight-hadoop-linux-information/ambari-storm.png)

reason: ()

deleted:

		things directly

replaced by:

		components

reason: ()

deleted:

		* A service or web site such as Spark or Hue.
		* A component that requires configuration changes on multiple nodes in the cluster. For example, a required environment variable, creating of a logging directory, or creation of a configuration file.
		
		Script Actions are Bash scripts that are ran during cluster provisioning, and can be used to install and configure additional components on the cluster. Example scripts are provided for installing the following components:

replaced by:

		Instead, use [HDInsight Script Actions](/documentation/articles/hdinsight-hadoop-customize-cluster).
		
		Script Actions are Bash scripts that are ran during cluster provisioning, and can be used to install  additional components on the cluster. Example scripts are provided for installing the following components:

reason: ()

