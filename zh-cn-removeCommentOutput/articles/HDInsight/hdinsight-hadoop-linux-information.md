<properties
   pageTitle="有关在基于 Linux 的 HDInsight 上使用 Hadoop 的提示 | Azure"
   description="获取有关在 Azure 云中运行的你所熟悉的 Linux 环境中使用基于 Linux 的 HDInsight (Hadoop) 群集的实施提示。"
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="paulettm"
   editor="cgronlun"
   tags="azure-portal"/>

<tags
   ms.service="hdinsight"
   ms.date="08/12/2015"
   wacn.date=""/>

# 有关在 Linux 上使用 HDInsight 的信息

基于 Linux 的 Azure HDInsight 群集提供基于熟悉的 Linux 环境并在 Azure 云中运行的 Hadoop。在大多数情况下，它的工作方式应该与其他任何 Hadoop-on-Linux 安装完全相同。本文档指出了你应该注意的具体差异。

## 域名

连接到群集时要使用的完全限定域名 (FQDN) 是 **&lt;clustername>.azurehdinsight.cn** 或（仅限 SSH）**&lt;clustername-ssh>.azurehdinsight.cn**。


## 对服务的远程访问

* **Ambari (web)** - https://&lt;clustername>.azurehdinsight.cn

	使用群集管理员用户和密码进行身份验证，然后登录到 Ambari。这也使用群集管理员用户和密码。

	身份验证是纯文本身份验证 - 始终使用 HTTPS 来帮助确保连接是安全的。

	> [AZURE.IMPORTANT]虽然可以直接通过 Internet 访问群集的 Ambari，但若要使用某些功能，则需要根据访问群集所用的内部域名的节点来达到目的。由于这是内部域名且未公开，因此，在尝试通过 Internet 访问某些功能时，你将会收到“找不到服务器”的错误。
	>
	> 若要使用 Ambari web UI 的全部功能，请使用 SSH 隧道通过代理将 Web 流量传送到群集头节点。请参阅[使用 SSH 隧道访问 Ambari Web UI、ResourceManager、JobHistory、NameNode、Oozie 和其他 Web UI](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel)

* **Ambari (REST)** - https://&lt;clustername>.azurehdinsight.cn/ambari

	> [AZURE.NOTE]通过使用群集管理员用户和密码进行身份验证。
	> 
	> 身份验证是纯文本身份验证 - 始终使用 HTTPS 来帮助确保连接是安全的。

* **WebHCat (Templeton)** - https://&lt;clustername>.azurehdinsight.cn/templeton

	> [AZURE.NOTE]通过使用群集管理员用户和密码进行身份验证。
	>
	> 身份验证是纯文本身份验证 - 始终使用 HTTPS 来帮助确保连接是安全的。

* **SSH** - &lt;clustername>-ssh.azurehdinsight.cn，使用端口 22 或 23。端口 22 用于连接 headnode0，而端口 23 用于连接 headnode1。有关头节点的详细信息，请参阅 [HDInsight 中的 Hadoop 群集的可用性和可靠性](/documentation/articles/hdinsight-high-availability-linux)。

	> [AZURE.NOTE]你只能通过 SSH 从客户端计算机访问群集头节点。在连接后，你可以通过使用 SSH 从头节点访问从节点。

## 文件位置

Hadoop 相关文件可在群集节点上的 `/usr/hdp` 中找到。此目录包含以下子目录：

* __2.2.4.9-1__：此目录是根据 HDInsight 使用的 Hortonworks 数据平台版本命名的，因此你的群集上的编号可能不同于此处列出的编号。
* __current__：此目录包含 __2.2.4.9-1__ 目录下的目录的链接，有了此目录，你每次访问某个文件时，便不需要键入版本号（可能会变化）。

示例数据和 JAR 文件可以在 Hadoop 分布式文件系统 (HDFS) 或 Azure Blob 存储上的“/example”或“wasb:///example”处找到。

## HDFS、Azure Blob 存储和存储最佳做法

在大部分的 Hadoop 分发中，HDFS 受群集中计算机上的本地存储的支持。尽管这种方式很有效率，但用于基于云的解决方案时可能费用高昂，因为计算资源以小时为单位来计费。

HDInsight 使用 Azure Blob 存储作为默认存储，以提供以下优势：

* 成本低廉的长期存储

* 可从外部服务访问，例如网站、文件上载/下载实用程序、各种语言 SDK 和 Web 浏览器

由于它是 HDInsight 的默认存储，因此你通常不需要进行任何设置就能使用。例如，以下命令将列出 **/example/data** 文件夹中的文件，该文件夹存储在 Azure Blob 存储上：

	hadoop fs -ls /example/data

一些命令可能会要求你指定使用的是 Blob 存储。对于这些命令，你可以在它的前面加上前缀 **WASB://**。

HDInsight 还允许你将多个 Blob 存储帐户与群集相关联。若要访问非默认 Blob 存储帐户上的数据，可以使用以下格式：**WASB://&lt;container-name>@&lt;account-name>.blob.core.chinacloudapi.cn/**。例如，以下命令会列出指定容器和 Blob 存储帐户的 **/example/data** 目录的内容：

	hadoop fs -ls wasb://mycontainer@mystorage.blob.core.chinacloudapi.cn/example/data

### 群集要使用哪种 Blob 存储？

在群集创建期间，你选择了使用现有的 Azure 存储帐户和容器，或创建新的存储帐户和容器。事后，你可能会忘记了该存储帐户和容器。你可以使用 Ambari REST API 查找默认的存储帐户和容器。

1. 使用以下命令可检索 HDFS 配置信息：

        curl -u admin:PASSWORD -G "https://CLUSTERNAME.azurehdinsight.cn/api/v1/clusters/CLUSTERNAME/configurations/service_config_versions?service_name=HDFS&service_config_version=1"

2. 在返回的 JSON 数据中, 找到 `fs.defaultFS` 条目。其中将包含如下格式的默认容器和存储帐户名称：

        wasb://CONTAINTERNAME@STORAGEACCOUNTNAME.blob.core.chinacloudapi.cn

> [AZURE.TIP]如果你已安装 [jq](http://stedolan.github.io/jq/)，则可以使用以下方式仅返回 `fs.defaultFS` 条目：
>
> `curl -u admin:PASSWORD -G "https://CLUSTERNAME.azurehdinsight.cn/api/v1/clusters/CLUSTERNAME/configurations/service_config_versions?service_name=HDFS&service_config_version=1" | jq '.items[].configurations[].properties["fs.defaultFS"] | select(. != null)'`

**Azure 门户**

1. 在 [Azure 门户](https://manage.windowsazure.cn/)中，选择你的 HDInsight 群集。

2. 选择页面顶部的“仪表板”。

3. 存储帐户和容器在该页的“链接的资源”部分中列出。

	![链接的资源](./media/hdinsight-hadoop-linux-information/storageportal.png)

### 如何访问 Blob 存储？

除了通过群集的 Hadoop 命令，还有各种不同方式可用来访问 Blob：

* [适用于 Mac、Linux 和 Windows 的 Azure CLI](/documentation/articles/xplat-cli)：适用于 Azure 的命令行界面命令。在安装后，使用 `azure storage` 命令获取有关使用存储的帮助，或者使用 `azure blob` 获取特定于 Blob 的命令。

* [blobxfer.py](https://github.com/Azure/azure-batch-samples/tree/master/Python/Storage)：用于 Azure 存储中的 Blob 的 python 脚本。

* 各种 SDK：

	* [Java](https://github.com/Azure/azure-sdk-for-java)

	* [Node.js](https://github.com/Azure/azure-sdk-for-node)

	* [PHP](https://github.com/Azure/azure-sdk-for-php)

	* [Python](https://github.com/Azure/azure-sdk-for-python)

	* [Ruby](https://github.com/Azure/azure-sdk-for-ruby)

	* [.NET](https://github.com/Azure/azure-sdk-for-net)

* [存储 REST API](https://msdn.microsoft.com/zh-cn/library/azure/dd135733.aspx)

##<a name="scaling"></a>缩放你的群集

群集缩放功能可让你更改 Azure HDInsight 中运行的群集使用的数据节点数，而无需删除然后再重新创建群集。

你可以在其他作业或进程正在群集上运行时执行缩放操作。

不同的群集类型会受缩放操作影响，如下所示：

* __Hadoop__：减少群集中的节点数时，群集中的某些服务将重新启动。这会导致正在运行或挂起的作业在缩放操作完成时失败。你可以在操作完成后重新提交这些作业。

* __HBase__：在完成缩放操作后的几分钟内，区域服务器会自动进行平衡。若要手动平衡区域服务器，请使用以下步骤：

	1. 使用 SSH 连接到 HDInsight 群集。有关如何将 SSH 与 HDInsight 配合使用的详细信息，请参阅以下文档之一：

		* [在 Linux、Unix 和 Mac OS X 上将 SSH 与 HDInsight 配合使用](/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix)

		* [在 Windows 上将 SSH 与 HDInsight 配合使用](/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows)

	1. 使用以下命令来启动 HBase shell：

			hbase shell

	2. 加载 HBase shell 后，使用以下方法来手动平衡区域服务器：

			balancer

* __Storm__：你应在执行缩放操作后重新平衡任何正在运行的 Storm 拓扑。这允许拓扑根据群集中的新节点数重新调整并行度设置。若要重新平衡正在运行的拓扑，请使用下列选项之一：

	* __SSH__：连接到服务器并使用以下命令来重新平衡拓扑：

			storm rebalance TOPOLOGYNAME

		你还可以指定参数来替代拓扑原来提供的并行度提示。例如，`storm rebalance mytopology -n 5 -e blue-spout=3 -e yellow-bolt=10` 会将拓扑重新配置为 5 个工作进程，蓝色的 BlueSpout 组件有 3 个 executor，黄色 YellowBolt 组件有 10 个 executor。

	* __Storm UI__：使用以下步骤来重新平衡使用 Storm UI 的拓扑。

		1. [创建到群集的 SSH 隧道并打开 Ambari Web UI](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel)。

		2. 从页面左侧的服务列表中选择 __Storm__。然后从“快速链接”中选择 __Storm UI__。

			![快速链接中的 Storm UI 条目](./media/hdinsight-hadoop-linux-information/ambari-storm.png)

			这将会显示 Storm UI：

			![Storm UI](./media/hdinsight-hadoop-linux-information/storm-ui.png)

		3. 选择要重新平衡的拓扑，然后选择“重新平衡”按钮。输入执行重新平衡操作前的延迟。

有关缩放 HDInsight 群集的特定信息，请参阅：

* [使用 Azure 预览门户管理 HDInsight 中的 Hadoop 群集](/documentation/articles/hdinsight-administer-use-portal-linux#scaling)

* [使用 Azure PowerShell 管理 HDInsight 中的 Hadoop 群集](/documentation/articles/hdinsight-administer-use-command-line#scaling)

## 如何安装 Hue（或其他 Hadoop 组件）？

HDInsight 是一项托管服务，这意味着如果检测到问题，Azure 可能会自动破坏并重新预配群集中的节点。因此，不建议在群集节点上手动安装组件。

请改用 [HDInsight 脚本操作](/documentation/articles/hdinsight-hadoop-customize-cluster)。

脚本操作是在群集预配期间运行的 Bash 脚本，可用于在群集上安装其他组件。提供了用于安装以下组件的示例脚本：

* [Hue](/documentation/articles/hdinsight-hadoop-hue-linux)
* [Giraph](/documentation/articles/hdinsight-hadoop-giraph-install-linux)
* [R](/documentation/articles/hdinsight-hadoop-r-scripts-linux)
* [Solr](/documentation/articles/hdinsight-hadoop-solr-install-linux)
* [Spark](/documentation/articles/hdinsight-hadoop-spark-install-linux)

有关开发你自己的脚本操作的信息，请参阅[使用 HDInsight 进行脚本操作开发](/documentation/articles/hdinsight-hadoop-script-actions-linux)。

## 后续步骤

* [将 Hive 与 HDInsight 配合使用](/documentation/articles/hdinsight-use-hive/)
* [将 Pig 与 HDInsight 配合使用](/documentation/articles/hdinsight-use-pig/)
* [将 MapReduce 作业与 HDInsight 配合使用](/documentation/articles/hdinsight-use-mapreduce)

<!---HONumber=74-->