<properties
   	pageTitle="Linux tutorial: Get started with Hadoop and Hive | Windows Azure"
   	description="Follow this Linux tutorial to get started using Hadoop in HDInsight. Learn how to provision Linux clusters, and query data with Hive."
   	services="hdinsight"
   	documentationCenter=""
   	authors="nitinme"
   	manager="paulettm"
   	editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="10/05/2015"
	wacn.date=""/>

# Hadoop tutorial: Get started using Hadoop with Hive in HDInsight on Linux <!-- keep by customization: begin --> (preview) <!-- keep by customization: end -->

> [AZURE.SELECTOR]
- [Windows](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows)
- [Linux](/documentation/articles/hdinsight-hadoop-linux-tutorial-get-started)

<!-- deleted by customization
This docuent gets you started quickly with Azure HDInsight on Linux by showing you how to create a Linux-based Hadoop cluster, connect to the cluster using a Secure Shell (SSH,) and then run a Hive query against example data that is included with the cluster.

> [AZURE.NOTE] If you are new to Hadoop and big data, you can read more about the terms [Apache Hadoop](http://hadoop.apache.org/), [MapReduce](http://wiki.apache.org/hadoop/MapReduce), [Hadoop Distributed File System (HDFS)](http://hadoop.apache.org/docs/r1.0.4/hdfs_design.html), and [Hive](https://cwiki.apache.org/confluence/display/Hive/Home%3bjsessionid=AF5B37E667D7DBA633313BB2280C9072). To understand how HDInsight enables Hadoop in Azure, see [Introduction to Hadoop in HDInsight](/documentation/articles/hdinsight-hadoop-introduction).
-->
<!-- keep by customization: begin -->
This Hadoop tutorial gets you started quickly with Azure HDInsight on Linux by showing you how to provision an Hadoop cluster on Linux and run a Hive query.


> [AZURE.NOTE] If you are new to Hadoop and big data, you can read more about the terms <a href="http://hadoop.apache.org/" target="_blank">Apache Hadoop</a>, <a href="http://wiki.apache.org/hadoop/MapReduce" target="_blank">MapReduce</a>, <a href="http://hadoop.apache.org/docs/r1.0.4/hdfs_design.html" target="_blank">Hadoop Distributed File System (HDFS)</a>, and <a href="https://cwiki.apache.org/confluence/display/Hive/Home%3bjsessionid=AF5B37E667D7DBA633313BB2280C9072" target="_blank">Hive</a>. To understand how HDInsight enables Hadoop in Azure, see [Introduction to Hadoop in HDInsight](/documentation/articles/hdinsight-hadoop-introduction).


## What does this tutorial accomplish?

Assume you have a large unstructured data set and you want to run queries on it to extract some meaningful information. Here's how you achieve this:

   ![Hadoop tutorial steps: Create a Storage account; provision a Hadoop cluster; query data with Hive.](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.Linux.GetStartedFlow.png)

<!-- keep by customization: end -->

## Prerequisites

Before you begin this Linux tutorial for Hadoop, you must have the following:

<!-- deleted by customization
- **An Azure subscription**: See [Get Azure trial](/pricing/1rmb-trial/).

- **A Secure Shell (SSH) client**: Linux, Unix, and OS X systems provied an SSH client through the `ssh` command. For Windows systems, we recommend [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

    > [AZURE.NOTE] The steps in this document use SSH to connect to the HDInsight cluster, as SSH is available for all client operating systems. For other methods of connecting to the HDInsight cluster, such as using the HDInsight Tools for Visual Studio or REST APIs, see the Hive, Pig, and MapReduce links in the [Next Steps](#nextsteps) section of this document.
    
- **Secure Shell (SSH) keys (optional)**: You can secure the SSH account used to connect to the cluster using either a password or a public key. Using a password gets you started quickly, and you should use this option if you want to quickly provision a cluster and run some test jobs. Using a key is more secure, however it requires additional setup. You might want to use this approach when provisioning a production cluster. In this article, we use the password approach. For instructions on how to create and use SSH keys with HDInsight, refer to the following articles:

-->
<!-- keep by customization: begin -->

- An Azure subscription. For more information about obtaining a subscription, see <a href="/pricing/overview/" target="_blank">Purchase Options</a>, <a href="/pricing/1rmb-trial/" target="_blank">Trial</a>.
- **Secure Shell (SSH) keys**. If you want to remote into a Linux cluster by using SSH with a key instead of a password. Using a key is the recommended method as it is more secure. For instructions on how to generate SSH keys, refer to the following articles:
<!-- keep by customization: end -->
	-  From a Linux computer - [Use SSH with Linux-based HDInsight (Hadoop) from Linux, Unix, or OS X](/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix).
	-  From a Windows computer - [Use SSH with Linux-based HDInsight (Hadoop) from Windows](/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows).

<!-- keep by customization: begin -->
**Estimated time to complete:** 30 minutes

## In this tutorial

* [Create an Azure Storage account](#storage)
* [Provision an HDInsight Linux cluster](#provision)
* [Submit a Hive job on the cluster](#hivequery)
* [Next steps](#nextsteps)

## <a name="storage"></a>Create an Azure Storage account

HDInsight uses Azure Blob storage for storing data. For more information, see [Use Azure Blob storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage).

When you provision an HDInsight cluster, you specify an Azure Storage account. A specific Blob storage container from that account is designated as the default file system, just like in HDFS. The HDInsight cluster is, by default, provisioned in the same datacenter as the Storage account you specify.

In addition to this Storage account, you can add other Storage accounts when you custom-configure an HDInsight cluster. These additional Storage accounts can be from either the same Azure subscription or different Azure subscriptions. For instructions, see [Provision HDInsight Linux clusters using custom options](/documentation/articles/hdinsight-provision-clusters).

To simplify this tutorial, only the default Blob container and the default Storage account are used. In practice, the data files are usually stored in a designated Storage account.

**To create an Azure Storage account**

1. Sign in to the <a href="https://manage.windowsazure.cn/" target="_blank">Azure Management Portal</a>.
2. Click **NEW** in the lower-left corner, point to **DATA SERVICES**, point to **STORAGE**, and then click **QUICK CREATE**.

	![Azure Management Portal where you can use Quick Create to set up a new Storage account.](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.StorageAccount.QuickCreate.png)

3. Enter information for **URL**, **LOCATION** and **REPLICATION**, and then click **CREATE STORAGE ACCOUNT**. Affinity groups are not supported. You will see the new Storage account in the storage list.

	>[AZURE.NOTE]  The Quick Create option to provision an HDInsight Linux cluster, like the one we use in this tutorial, does not ask for a location while provisioning the cluster. By default, it co-locates the cluster in the same datacenter as the Storage account. So, make sure you create your Storage account in the locations supported for the cluster, which are: **China East**, **China North**.

4. Wait until **STATUS** for the new Storage account is changed to **Online**.
5. Select the new Storage account from the list and click **MANAGE ACCESS KEYS** from the bottom of the page.
7. Make a note of the information for **STORAGE ACCOUNT NAME** and **PRIMARY ACCESS KEY** (or **SECONDARY ACCESS KEY**; either of the keys works). You will need them later in the tutorial.


For more information, see
[How to Create a Storage Account](/documentation/articles/storage-create-storage-account) and [Use Azure Blob Storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage).

<!-- keep by customization: end -->
## <a name="provision"></a>Provision an HDInsight cluster on Linux

<!-- deleted by customization
When you provision a cluster, you create the Azure compute resources that contain Hadoop services and resources. In this section, you provision an HDInsight version 3.2 cluster, which contains Hadoop version 2.2. For information about HDInsight versions and their SLAs, see [HDInsight component versioning](/documentation/articles/hdinsight-component-versioning). For more detailed information on creating an HDInsight cluster, see [Provision HDInsight clusters using custom options][hdinsight-provision].

>[AZURE.NOTE]  You can also create Hadoop clusters running the Windows Server operating system. For instructions, see [Get Started with HDInsight on Windows](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows).

Use the following steps to create a new cluster:

1. Sign in to the [Azure Preview Portal](https://ms.portal.azure.com/).
2. Click **NEW**, Click **Data Analytics**, and then click **HDInsight**.

    ![Creating a new cluster in the Azure Preview Portal](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.CreateCluster.1.png "Creating a new cluster in the Azure Preview Portal")

3. Enter a **Cluster Name**, select **Hadoop** for the **Cluster Type**, and from the **Cluster Operating System** drop-down, select **Ubuntu**. A green check will appear beside the cluster name if it is available.

	![Enter cluster name and type](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.CreateCluster.2.png "Enter cluster name and type")

4. If you have more than one subscription, click the **Subscription** entry to select the Azure subscription that will be used for the cluster.

5. Click **Resource Group** to see a list of existing resource groups and then select the one to create the cluster in. Or, you can click **Create New** and then enter the name of the new resource group. A green check will appear to indicate if the new group name is available.

	> [AZURE.NOTE] This entry will default to one of your existing resource groups, if any are available.

6. Click **Credentials** and then enter a password for the admin user. You must also enter an **SSH Username**. For **SSH Authentication Type**, click **PASSWORD** and specify a password for the SSH user. Click **Select** at the bottom to save the credentials configuration.

	![Provide cluster credentials](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.CreateCluster.3.png "Provide cluster credentials")

    > [AZURE.NOTE] SSH is used to remotely access the HDInsight cluster using a command-line. The user name and password you use here is used when connecting to the cluster through SSH. Also, the SSH user name must be unique, as it creates a user account on all the HDInsight cluster nodes. The following are some of the account names reserved for use by services on the cluster, and cannot be used as the SSH user name:
    >
    > root, hdiuser, storm, hbase, ubuntu, zookeeper, hdfs, yarn, mapred, hbase, hive, oozie, falcon, sqoop, admin, tez, hcat, hdinsight-zookeeper.

	For more information on using SSH with HDInsight, see one of the following documents:

	* [Use SSH with Linux-based Hadoop on HDInsight from Linux, Unix, or OS X](/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix)
	* [Use SSH with Linux-based Hadoop on HDInsight from Windows](/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows)


7. Click **Data Source** to choose an existing data source for the cluster, or create a new one. When you provision a Hadoop cluster in HDInsight, you specify an Azure Storage account. A specific Blob storage container from that account is designated as the default file system, like in the Hadoop distributed file system (HDFS). By default, the HDInsight cluster is provisioned in the same data center as the storage account you specify. For more information, see [Use Azure Blob storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage)

	![Data source blade](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.CreateCluster.4.png "Provide data source configuration")

	Currently you can select an Azure Storage Account as the data source for an HDInsight cluster. Use the following to understand the entries on the **Data Source** blade.

	- **Selection Method**: Set this to **From all subscriptions** to enable browsing of storage accounts from all your subscriptions. Set this to **Access Key** if you want to enter the **Storage Name** and **Access Key** of an existing storage account.

	- **Select storage account / Create New**: Click **Select storage account** to browse and select an existing storage account you want to associate with the cluster. Or, click **Create New** to create a new storage account. Use the field that appears to enter the name of the storage account. A green check will appear if the name is available.

	- **Choose Default Container**: Use this to enter the name of the default container to use for the cluster. While you can enter any name here, we recommend using the same name as the cluster so that you can easily recognize that the container is used for this specific cluster.

	- **Location**: The geographic region that the storage account is in, or will be created in.

		> [AZURE.IMPORTANT] Selecting the location for the default data source will also set the location of the HDInsight cluster. The cluster and default data source must be located in the same region.

	Click **Select** to save the data source configuration.

8. Click **Node Pricing Tiers** to display information about the nodes that will be created for this cluster. Set the number of worker nodes that you need for the cluster. The estimated cost of the cluster will be shown within the blade.

	![Node pricing tiers blade](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.CreateCluster.5.png "Specify number of cluster nodes")

	Click **Select** to save the node pricing configuration.

9. On the **New HDInsight Cluster** blade, ensure that **Pin to Startboard** is selected, and then click **Create**. This will create the cluster and add a tile for it to the Startboard of your Azure Management Portal. The icon will indicate that the cluster is provisioning, and will change to display the HDInsight icon once provisioning has completed.

While provisioning|Provisioning complete
------------------|---------------------
	![Provisioning indicator on startboard](./media/hdinsight-hadoop-linux-tutorial-get-started/provisioning.png)|![Provisioned cluster tile](./media/hdinsight-hadoop-linux-tutorial-get-started/provisioned.png)

> [AZURE.NOTE] It will take some time for the cluster to be created, usually around 15 minutes. Use the tile on the Startboard, or the **Notifications** entry on the left of the page to check on the provisioning process.

Once the provisioning is completed, click the tile for the cluster from the Startboard to launch the cluster blade.

## <a name="connect"></a> To connect to the cluster
-->
<!-- keep by customization: begin -->
When you provision an HDInsight cluster, you provision Azure compute resources that contain Hadoop and related applications. In this section, you provision an HDInsight cluster on Linux by using the Quick Create option. This option uses default user names and Azure Storage containers, and configures a cluster with HDInsight version 3.2 (Hadoop version 2.6, Hortonworks Data Platform version 2.2) running on Ubuntu 12.04 long-term support (LTS). For information about different HDInsight versions and their service level agreements, see the [HDInsight component versioning](/documentation/articles/hdinsight-component-versioning) page.

>[AZURE.NOTE]  You can also create Hadoop clusters running the Windows Server operating system. For instructions, see [Get Started with HDInsight](/documentation/articles/hdinsight-get-started).


**To provision an HDInsight cluster**

1. Sign in to the <a href="https://manage.windowsazure.cn/" target="_blank">Azure Management Portal</a>.

2. Click **NEW** on the lower-left side, click **DATA SERVICES**, click **HDINSIGHT**, and then click **HADOOP ON LINUX**.

	![Creation of a Hadoop cluster in HDInsight.](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.QuickCreateCluster.png)

4. Enter or select the following values:

	<table border="1">
	<tr><th>Name</th><th>Value</th></tr>
	<tr><td>Cluster Name</td><td>Name of the cluster.</td></tr>
	<tr><td>Cluster Size</td><td>Number of data nodes you want to deploy. The default value is 4. But the option to use 1 or 2 data nodes is also available from the drop-down. Any number of cluster nodes can be specified by using the <strong>Custom Create</strong> option. Pricing details on the billing rates for various cluster sizes are available. Click the <strong>?</strong> symbol just above the drop-down box and follow the link on the pop-up.</td></tr>
	<tr><td>Password</td><td>The password for the <i>HTTP</i> account (default user name: admin) and <i>SSH</i> account (default user name: hdiuser). Note that these are NOT the administrator accounts for the virtual machines on which the clusters are provisioned. </td></tr>

	<tr><td>Storage Account</td><td>Select the Storage account you created from the drop-down box. <br/>

	Once a Storage account is chosen, it cannot be changed. If the Storage account is removed, the cluster will no longer be available for use.

	The HDInsight cluster is co-located in the same datacenter as the Storage account.
	</td></tr>
	</table>

	Keep a copy of the cluster name. You will need it later in the tutorial.


5. Click **CREATE HDINSIGHT CLUSTER**. When the provisioning finishes, the status column shows **Running**.

	>[AZURE.NOTE] The procedure above creates a Linux cluster with the Quick Create option that uses the default SSH user name and Azure Storage containers. To create a cluster with custom options, such as using an SSH key for authentication or using additional Storage accounts, see [Provision HDInsight Linux clusters using custom options](/documentation/articles/hdinsight-provision-clusters).


## <a name="hivequery"></a>Submit a Hive job on the cluster
Now that you have an HDInsight Linux cluster provisioned, the next step is to run a sample Hive job to query sample data (sample.log) that comes with HDInsight clusters. The sample data contains log information, including trace, warnings, info, and errors. We query this data to retrieve all the error logs with a specific severity. You must perform the following steps to run a Hive query on an HDInsight Linux cluster:

- Connect to a Linux cluster
- Run a Hive job



### To connect to a cluster
<!-- keep by customization: end -->

You can connect to an HDInsight cluster on Linux from a Linux computer or a Windows-based computer by using SSH.

<!-- deleted by customization
###To connect from a Linux computer
-->
<!-- keep by customization: begin -->
**To connect from a Linux computer**
<!-- keep by customization: end -->

1. Open a terminal and enter the following command:

		ssh <username>@<clustername>-ssh.azurehdinsight.cn

	Because you provisioned a cluster with the Quick Create option, the default SSH user name is **hdiuser**. So, the command must be:

		ssh hdiuser@myhdinsightcluster-ssh.azurehdinsight.cn

2. When prompted, enter the password that you provided while provisioning the cluster. After you are successfully connected, the prompt will change to the following:

		hdiuser@headnode-0:~$


<!-- deleted by customization
###To connect from a Windows-based computer

1. Download [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) for Windows-based clients.
-->
<!-- keep by customization: begin -->
**To connect from a Windows-based computer**

1. Download <a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html" target="_blank">PuTTY</a> for Windows-based clients.
<!-- keep by customization: end -->

2. Open PuTTY. In **Category**, click **Session**. From the **Basic options for your PuTTY session** screen, enter the SSH address of your HDInsight server in the **Host Name (or IP address)** field. The SSH address is your cluster name, followed by**-ssh.azurehdinsight.cn**. For example, **myhdinsightcluster-ssh.azurehdinsight.cn**.

	![Connect to an HDInsight cluster on Linux using PuTTY](./media/hdinsight-hadoop-linux-tutorial-get-started/HDI.linux.connect.putty.png)

3. To save the connection information for future use, enter a name for this connection under **Saved Sessions**, and then click **Save**. The connection will be added to the list of saved sessions.

4. Click **Open** to connect to the cluster. When prompted for the user name, enter **hdiuser**. For the password, enter the password you specified while provisioning the cluster. After you are successfully connected, the prompt will change to the following:

		hdiuser@headnode-0:~$

<!-- deleted by customization
##<a name="hivequery"></a>Run a Hive query

Once you are connected to the cluster via SSH, use the following commands to run a Hive query <!-- deleted by customization: --><!-- keep by customization: begin -->. <!-- keep by customization: end -->
-->
<!-- keep by customization: begin -->
### To run a Hive job

Once you are connected to the cluster via SSH, use the following commands to run a Hive query <!-- deleted by customization: --><!-- keep by customization: begin -->. <!-- keep by customization: end -->
<!-- keep by customization: end -->

1. Start the Hive command-line interface (CLI) by using the following command at the prompt:

		hive

2. Using the CLI, enter the following statements to create a new table named **log4jLogs** by using the sample data already available on the cluster:

		DROP TABLE log4jLogs;
		CREATE EXTERNAL TABLE log4jLogs(t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string)
		ROW FORMAT DELIMITED FIELDS TERMINATED BY ' '
		STORED AS TEXTFILE LOCATION 'wasb:///example/data/';
		SELECT t4 AS sev, COUNT(*) AS cnt FROM log4jLogs WHERE t4 = '[ERROR]' GROUP BY t4;

	These statements perform the following actions:

	- **DROP TABLE** - Deletes the table and the data file, in case the table already exists.
	- **CREATE EXTERNAL TABLE** - Creates a new "external" table in Hive. External tables store only the table definition in Hive; the data is left in the original location.
	- **ROW FORMAT** - Tells Hive how the data is formatted. In this case, the fields in each log are separated by a space.
	- **STORED AS TEXTFILE LOCATION** - Tells Hive where the data is stored (the example/data directory), and that it is stored as text.
	- **SELECT** - Selects a count of all rows where column t4 contains the value [ERROR].

	>[AZURE.NOTE] External tables should be used when you expect the underlying data to be updated by an external source, such as an automated data upload process, or by another MapReduce operation, but you always want Hive queries to use the latest data. Dropping an external table does *not* delete the data, only the table definition.

	This returns the following output:

		Query ID = hdiuser_20150116000202_cceb9c6b-4356-4931-b9a7-2c373ebba493
		Total jobs = 1
		Launching Job 1 out of 1
		Number of reduce tasks not specified. Estimated from input data size: 1
		In order to change the average load for a reducer (in bytes):
		  set hive.exec.reducers.bytes.per.reducer=<number>
		In order to limit the maximum number of reducers:
		  set hive.exec.reducers.max=<number>
		In order to set a constant number of reducers:
		  set mapreduce.job.reduces=<number>
		Starting Job = job_1421200049012_0006, Tracking URL = <URL>:8088/proxy/application_1421200049012_0006/
		Kill Command = /usr/hdp/2.2.1.0-2165/hadoop/bin/hadoop job  -kill job_1421200049012_0006
		Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
		2015-01-16 00:02:40,823 Stage-1 map = 0%,  reduce = 0%
		2015-01-16 00:02:55,488 Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 3.32 sec
		2015-01-16 00:03:05,298 Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 5.62 sec
		MapReduce Total cumulative CPU time: 5 seconds 620 msec
		Ended Job = job_1421200049012_0006
		MapReduce Jobs Launched:
		Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 5.62 sec   HDFS Read: 0 HDFS Write: 0 SUCCESS
		Total MapReduce CPU Time Spent: 5 seconds 620 msec
		OK
		[ERROR]    3
		Time taken: 60.991 seconds, Fetched: 1 row(s)

	Note that the output contains **[ERROR]  3**, as there are three rows that contain this value.

3. Use the following statements to create a new "internal" table named **errorLogs**:

		CREATE TABLE IF NOT EXISTS errorLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) STORED AS ORC;
		INSERT OVERWRITE TABLE errorLogs SELECT t1, t2, t3, t4, t5, t6, t7 FROM log4jLogs WHERE t4 = '[ERROR]';


	These statements perform the following actions:

	- **CREATE TABLE IF NOT EXISTS** - Creates a table, if it does not already exist. Since the **EXTERNAL** keyword is not used, this is an internal table, which is stored in the Hive data warehouse and is managed completely by Hive. Unlike external tables, dropping an internal table will delete the underlying data as well.
	- **STORED AS ORC** - Stores the data in Optimized Row Columnar (ORC) format. This is a highly optimized and efficient format for storing Hive data.
	- **INSERT OVERWRITE ... SELECT** - Selects rows from the **log4jLogs** table that contain [ERROR], and then inserts the data into the **errorLogs** table.

4. To verify that only rows containing [ERROR] in column t4 were stored to the **errorLogs** table, use the following statement to return all the rows from **errorLogs**:

		SELECT * from errorLogs;

	The following output should be displayed on the console:

		2012-02-03	18:35:34	SampleClass0	[ERROR]	 incorrect		id
		2012-02-03	18:55:54	SampleClass1	[ERROR]	 incorrect		id
		2012-02-03	19:25:27	SampleClass4	[ERROR]	 incorrect		id
		Time taken: 0.987 seconds, Fetched: 3 row(s)

	The returned data should all correspond to [ERROR] logs.

## <a name="nextsteps"></a>Next steps
<!-- deleted by customization

In this document, you have learned how to create a Linux-based HDInsight cluster using the Azure preview portal, connect to the cluster using SSH, and how to perform basic Hive queries.

To learn more about analyzing data with HDinsight, see the following:

- To learn more about using Hive with HDInsight, including how to perform Hive queries from Visual Studio, see [Use Hive with HDInsight][hdinsight-use-hive].

- To learn about Pig, a language used to transform data, see [Use Pig with HDInsight][hdinsight-use-pig].

- To learn about MapReduce, a way to write programs that process data on Hadoop, see [Use MapReduce with HDInsight][hdinsight-use-mapreduce].

- To learn about using the HDInsight Tools for Visual Studio to analyze data on HDInsight, see [Get started using Visual Studio Hadoop tools for HDInsight](/documentation/articles/hdinsight-hadoop-visual-studio-tools-get-started).

If you're ready to start working with your own data and need to know more about how HDInsight stores data or how to get data into HDInsight, see the following:

- For information on how HDInsight uses Azure blob storage, see [Use Azure Blob storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage).

- For information on how to upload data to HDInsight, see [Upload data to HDInsight][hdinsight-upload-data].

If you'd like to learn more about creating or managing an HDInsight cluster, see the following:

- To learn about managing your Linux-based HDInsight cluster, see [Manage HDInsight clusters using Ambari](/documentation/articles/hdinsight-hadoop-manage-ambari).

- To learn more about the options you can select when creating an HDInsight cluster, see [Provision HDInsight on Linux using custom options](/documentation/articles/hdinsight-provision-clusters).

- If you are familiar with Linux, and Hadoop, but want to know specifics about Hadoop on the HDInsight, see [Working with HDInsight on Linux](/documentation/articles/hdinsight-hadoop-linux-information). This provides information such as:
-->
<!-- keep by customization: begin -->
In this Linux tutorial, you have learned how to provision a Hadoop cluster on Linux with HDInsight and run a Hive query on it by using SSH. To learn more, see the following articles:

- [Manage HDInsight clusters using Ambari](/documentation/articles/hdinsight-hadoop-manage-ambari): Linux-based HDInsight clusters use Ambari for management and monitoring of Hadoop services. The Ambari web UI is available on each cluster at https://CLUSTERNAME.azurehdinsight.cn

	> [AZURE.IMPORTANT] While many sections of the Ambari web are directly accessible through the Internet, the web UI for Hadoop services such as Resource Manager or Job History require the use of an SSH tunnel. For more information on using an SSH tunnel with HDInsight, see the following articles:
	>
	> * [Use SSH with Linux-based Hadoop on HDInsight from Linux, Unix, or OS X](/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix#tunnel)
	> * [Use SSH with Linux-based Hadoop on HDInsight from Windows](/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows#tunnel)

- [Provision HDInsight on Linux using custom options](/documentation/articles/hdinsight-provision-clusters): Learn more details about how to provision HDInsight clusters.

- [Working with HDInsight on Linux](/documentation/articles/hdinsight-hadoop-linux-information): If you are already familiar with Hadoop on Linux platforms, this document provides guidance on Azure specific information, such as:
<!-- keep by customization: end -->

	* URLs for services hosted on the cluster, such as Ambari and WebHCat
	* The location of Hadoop files and examples on the local file system
	* The use of Azure Storage (WASB) instead of HDFS as the default data store
<!-- keep by customization: begin -->

- For more information on Hive, or to learn about Pig and MapReduce, see the following:

	- [Use MapReduce with HDInsight][hdinsight-use-mapreduce]
	- [Use Hive with HDInsight][hdinsight-use-hive]
	- [Use Pig with HDInsight][hdinsight-use-pig]

- For more information on how to work with the Azure Storage used by your HDInsight cluster, see the following:
- [Use Azure Blob storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage)
- [Upload data to HDInsight][hdinsight-upload-data]
<!-- keep by customization: end -->


[1]: /documentation/articles/hdinsight-hadoop-visual-studio-tools-get-started
[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters
[hdinsight-admin-powershell]: /documentation/articles/hdinsight-administer-use-powershell
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data
[hdinsight-use-mapreduce]: /documentation/articles/hdinsight-use-mapreduce
[hdinsight-use-hive]: /documentation/articles/hdinsight-use-hive
[hdinsight-use-pig]: /documentation/articles/hdinsight-use-pig
[powershell-download]: http://go.microsoft.com/fwlink/p/?linkid=320376&clcid=0x409
[powershell-install-configure]: /documentation/articles/install-configure-powershell
[powershell-open]: /documentation/articles/install-configure-powershell#Install

<!-- deleted by customization
[img-hdi-dashboard]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.png
-->
<!-- keep by customization: begin -->
[img-hdi-dashboard]: .
media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.png
<!-- keep by customization: end -->
[img-hdi-dashboard-query-select]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.query.select.png
[img-hdi-dashboard-query-select-result]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.query.select.result.png
[img-hdi-dashboard-query-select-result-output]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.query.select.result.output.png
[img-hdi-dashboard-query-browse-output]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.query.browse.output.png
[image-hdi-clusterstatus]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.ClusterStatus.png
[image-hdi-gettingstarted-powerquery-importdata]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.GettingStarted.PowerQuery.ImportData.png
[image-hdi-gettingstarted-powerquery-importdata2]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.GettingStarted.PowerQuery.ImportData2.png
