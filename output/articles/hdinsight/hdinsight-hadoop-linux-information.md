<properties
   pageTitle="Tips for using Hadoop on Linux-based HDInsight | Windows Azure"
   description="Get implementation tips for using Linux-based HDInsight (Hadoop) clusters on a familiar Linux environment running in the Azure cloud."
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="paulettm"
   editor="cgronlun"
   tags="azure-portal"/>

<tags
   ms.service="hdinsight"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="big-data"
   ms.date="10/09/2015"
   ms.author="larryfr"/>

# Information about using HDInsight on Linux

Linux-based Azure HDInsight clusters provide Hadoop on a familiar Linux environment, running in the Azure cloud. For most things, it should work exactly as any other Hadoop-on-Linux installation. This document calls out specific differences that you should be aware of.

## Domain names

The fully qualified domain name (FQDN) to use when connecting to the cluster is **&lt;clustername>.azurehdinsight.cn** or (for SSH only) **&lt;clustername-ssh>.azurehdinsight.cn**.

## Remote access to services

* **Ambari (web)** - https://&lt;clustername>.azurehdinsight.cn

	Authenticate by using the cluster administrator user and password, and then log in to Ambari. This also uses the cluster administrator user and password.

	Authentication is plaintext - always use HTTPS to help ensure that the connection is secure.

	> [AZURE.IMPORTANT] While Ambari for your cluster is accessible directly over the Internet, some functionality relies on accessing nodes by the internal domain name used by the cluster. Since this is an internal domain name, and not public, you will receive "server not found" errors when trying to access some features over the Internet.
	>
	> To use the full functionality of the Ambari web UI, use an SSH tunnel to proxy web traffic to the cluster head node. See [Use SSH Tunneling to access Ambari web UI, ResourceManager, JobHistory, NameNode, Oozie, and other web UI's](hdinsight-linux-ambari-ssh-tunnel)

* **Ambari (REST)** - https://&lt;clustername>.azurehdinsight.cn/ambari

	> [AZURE.NOTE] Authenticate by using the cluster administrator user and password.
	>
	> Authentication is plaintext - always use HTTPS to help ensure that the connection is secure.

* **WebHCat (Templeton)** - https://&lt;clustername>.azurehdinsight.cn/templeton

	> [AZURE.NOTE] Authenticate by using the cluster administrator user and password.
	>
	> Authentication is plaintext - always use HTTPS to help ensure that the connection is secure.

* **SSH** - &lt;clustername>-ssh.azurehdinsight.cn on port 22 or 23. Port 22 is used to connect to headnode0, while 23 is used to connect to headnode1. For more information on the head nodes, see [Availability and reliability of Hadoop clusters in HDInsight](hdinsight-high-availability-linux).

	> [AZURE.NOTE] You can only access the cluster head nodes through SSH from a client machine. Once connected, you can then access the worker nodes by using SSH from the head node.

## File locations

Hadoop-related files can be found on the cluster nodes at `/usr/hdp`. This directory contains the following subdirectories:

* __2.2.4.9-1__: This directory is named for the version of the Hortonworks Data Platform used by HDInsight, so the number on your cluster may be different than the one listed here.
* __current__: This directory contains links to directories under the __2.2.4.9-1__ directory, and exists so that you don't have to type a version number (that might change,) every time you want to access a file.

Example data and JAR files can be found on Hadoop Distributed File System (HDFS) or Azure Blob storage at '/example' or 'wasb:///example'.

## HDFS, Azure Blob storage, and storage best practices

In most Hadoop distributions, HDFS is backed by local storage on the machines in the cluster. While this is efficient, it can be costly for a cloud-based solution where you are charged hourly for compute resources.

HDInsight uses Azure Blob storage as the default store, which provides the following benefits:

* Cheap long-term storage

* Accessibility from external services such as websites, file upload/download utilities, various language SDKs, and web browsers

Since it is the default store for HDInsight, you normally don't have to do anything to use it. For example, the following command will list files in the **/example/data** folder, which is stored on Azure Blob storage:

	hadoop fs -ls /example/data

Some commands may require you to specify that you are using Blob storage. For these, you can prefix the command with **WASB://**.

HDInsight also allows you to associate multiple Blob storage accounts with a cluster. To access data on a non-default Blob storage account, you can use the format **WASB://&lt;container-name>@&lt;account-name>.blob.core.chinacloudapi.cn/**. For example, the following will list the contents of the **/example/data** directory for the specified container and Blob storage account:

	hadoop fs -ls wasb://mycontainer@mystorage.blob.core.chinacloudapi.cn/example/data

### What Blob storage is the cluster using?

During cluster creation, you selected to either use an existing Azure Storage account and container, or create a new one. Then, you probably forgot about it. You can find the default storage account and container by using the Ambari REST API.

1. Use the following command to retrieve HDFS configuration information:

        curl -u admin:PASSWORD -G "https://CLUSTERNAME.azurehdinsight.cn/api/v1/clusters/CLUSTERNAME/configurations/service_config_versions?service_name=HDFS&service_config_version=1"

2. In the JSON data returned, find the `fs.defaultFS` entry. This will contain default container and storage account name in a format similar to the following:

        wasb://CONTAINTERNAME@STORAGEACCOUNTNAME.blob.core.chinacloudapi.cn

	> [AZURE.TIP] If you have installed [jq](http://stedolan.github.io/jq/), you can use the following to return just the `fs.defaultFS` entry:
	>
	> `curl -u admin:PASSWORD -G "https://CLUSTERNAME.azurehdinsight.cn/api/v1/clusters/CLUSTERNAME/configurations/service_config_versions?service_name=HDFS&service_config_version=1" | jq '.items[].configurations[].properties["fs.defaultFS"] | select(. != null)'`

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

### How do I access Blob storage?

Other than through the Hadoop command from the cluster, there are a variety of ways to access blobs:

* [Azure CLI for Mac, Linux and Windows](xplat-cli-install): Command-Line interface commands for working with Azure. After installing, use the `azure storage` command for help on using storage, or `azure blob` for blob-specific commands.

* [blobxfer.py](https://github.com/Azure/azure-batch-samples/tree/master/Python/Storage): A python script for working with blobs in Azure Storage.

* A variety of SDKs:

	* [Java](https://github.com/Azure/azure-sdk-for-java)

	* [Node.js](https://github.com/Azure/azure-sdk-for-node)

	* [PHP](https://github.com/Azure/azure-sdk-for-php)

	* [Python](https://github.com/Azure/azure-sdk-for-python)

	* [Ruby](https://github.com/Azure/azure-sdk-for-ruby)

	* [.NET](https://github.com/Azure/azure-sdk-for-net)

* [Storage REST API](https://msdn.microsoft.com/zh-cn/library/azure/dd135733.aspx)

##<a name="scaling"></a>Scaling your cluster

The cluster scaling feature allows you to change the number of data nodes used by a cluster that is running in Azure HDInsight without having to delete and re-create the cluster.

You can perform scaling operations while other jobs or processes are running on a cluster.

The different cluster types are affected by scaling as follows:

* __Hadoop__: When scaling down the number of nodes in a cluster, some of the services in the cluster are restarted. This can cause jobs running or pending to fail at the completion of the scaling operation. You can resubmit the jobs once the operation is complete.

* __HBase__: Regional servers are automatically balanced within a few minutes after completion of the scaling operation. To manually balance regional servers,use the following steps:

	1. Connect to the HDInsight cluster using SSH. For more information on using SSH with HDInsight, see one of the following documents:

		* [Use SSH with HDInsight from Linux, Unix, and Mac OS X](hdinsight-hadoop-linux-use-ssh-unix)

		* [Use SSH with HDInsight from Windows](hdinsight-hadoop-linux-use-ssh-windows)

	1. Use the following to start the HBase shell:

			hbase shell

	2. Once the HBase shell has loaded, use the following to manually balance the regional servers:

			balancer

* __Storm__: You should rebalance any running Storm topologies after a scaling operation has been performed. This allows the topology to readjust parallelism settings based on the new number of nodes in the cluster. To rebalance running topologies, use one of the following options:

	* __SSH__: Connect to the server and use the following command to rebalance a topology:

			storm rebalance TOPOLOGYNAME

		You can also specify parameters to override the parallelism hints originally provided by the topology. For example, `storm rebalance mytopology -n 5 -e blue-spout=3 -e yellow-bolt=10` will reconfigure the topology to 5 worker processes, 3 executors for the blue-spout component, and 10 executors for the yellow-bolt component.

	* __Storm UI__: Use the following steps to rebalance a topology using the Storm UI.

		1. [Create an SSH tunnel to the cluster and open the Ambari web UI](hdinsight-linux-ambari-ssh-tunnel).

		2. From the list of services on the left of the page, select __Storm__. Then select __Storm UI__ from __Quick Links__.


			![Storm UI entry in quick links](./media/hdinsight-hadoop-linux-information/ambari-storm.png)

			This will display the Storm UI:

			![the storm ui](./media/hdinsight-hadoop-linux-information/storm-ui.png)

		3. Select the topology you wish to rebalance, then select the __Rebalance__ button. Enter the delay before the rebalance operation is performed.

For specific information on scaling your HDInsight cluster, see:

* [Manage Hadoop clusters in HDInsight by using the Azure preview portal](hdinsight-administer-use-portal-linux#scaling)

* [Manage Hadoop clusters in HDinsight by using Azure PowerShell](hdinsight-administer-use-command-line#scaling)

## How do I install Hue (or other Hadoop component)?

HDInsight is a managed service, which means that nodes in a cluster may be destroyed and reprovisioned automatically by Azure if a problem is detected. Because of this, it is not recommended to manually install things directly on the cluster nodes. Instead, use [HDInsight Script Actions](hdinsight-hadoop-customize-cluster) when you need to install the following:

* A service or web site such as Spark or Hue.
* A component that requires configuration changes on multiple nodes in the cluster. For example, a required environment variable, creating of a logging directory, or creation of a configuration file.

Script Actions are Bash scripts that are ran during cluster provisioning, and can be used to install and configure additional components on the cluster. Example scripts are provided for installing the following components:

* [Hue](hdinsight-hadoop-hue-linux)
* [Giraph](hdinsight-hadoop-giraph-install-linux)
* [R](hdinsight-hadoop-r-scripts-linux)
* [Solr](hdinsight-hadoop-solr-install-linux)
* [Spark](hdinsight-hadoop-spark-install-linux)

For information on developing your own Script Actions, see [Script Action development with HDInsight](hdinsight-hadoop-script-actions-linux).

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

## Next steps

* [Use Hive with HDInsight](hdinsight-use-hive)
* [Use Pig with HDInsight](hdinsight-use-pig)
* [Use MapReduce jobs with HDInsight](hdinsight-use-mapreduce)