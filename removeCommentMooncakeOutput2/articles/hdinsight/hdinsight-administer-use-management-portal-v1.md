<properties
	pageTitle="Manage Hadoop clusters in HDInsight using Azure Management Portal | Windows Azure"
	description="Learn how to administer HDInsight Service. Create an HDInsight cluster, open the interactive JavaScript console, and open the Hadoop command console."
	services="hdinsight"
	documentationCenter=""
	authors="mumian"
	manager="paulettm"
	editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="08/11/2015"
	wacn.date=""/>

# Manage Hadoop clusters in HDInsight by using the Azure Management Portal

Using the [Azure Management Portal](https://manage.windowsazure.cn), you can provision Hadoop clusters in Azure HDInsight, change Hadoop user password, and enable Remote Desktop Protocol (RDP) so you can access the Hadoop command console on the cluster.

[AZURE.INCLUDE [hdinsight-azure-portal](../includes/hdinsight-azure-portal.md)]

## Other tools for administering HDInsight
There are also other tools available for administering HDInsight in addition to the Azure Management Portal.

- For more information on administering HDInsight by using Azure PowerShell, see [Administer HDInsight Using Azure PowerShell](/documentation/articles/hdinsight-administer-use-powershell).

- For more information on administering HDInsight by using the Azure CLI, see [Administer HDInsight Using Azure CLI](/documentation/articles/hdinsight-administer-use-command-line).

##Prerequisites

Before you begin this article, you must have the following:

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).
- **Azure Storage account** - An HDInsight cluster uses an Azure Blob storage container as the default file system. For more information about how Azure Blob storage provides a seamless experience with HDInsight clusters, see [Use Azure Blob Storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage). For details on creating an Azure Storage account, see [How to Create a Storage Account](/documentation/articles/storage-create-storage-account).


##Provision HDInsight clusters

You can provision HDInsight clusters from the Azure Management Portal by using the Quick Create or Custom Create option. See the following links for instructions:

- [Provision a cluster by using Quick Create](/documentation/articles/hdinsight-get-started#provision)
- [Provision a cluster by using Custom Create](/documentation/articles/hdinsight-provision-clusters#portal)

[AZURE.INCLUDE [data center list](../includes/hdinsight-pricing-data-centers-clusters.md)]


##Customize HDInsight clusters

HDInsight works with a wide range of Hadoop components. For the list of the components that have been verified and supported, see [What version of Hadoop is in Azure HDInsight](/documentation/articles/hdinsight-component-versioning). You can customize HDInsight by using one of the following options:

- Use Script Action to run custom scripts that can customize a cluster to either change cluster configuration or install custom components such as Giraph or Solr. For more information, see [Customize HDInsight cluster using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster).
- Use the cluster customization parameters in the HDInsight .NET SDK or Azure PowerShell during cluster provisioning. These configuration changes are then preserved through the lifetime of the cluster and are not affected by cluster node reimages that Azure platform periodically performs for maintenance. For more information on using the cluster customization parameters, see [Provision HDInsight clusters](/documentation/articles/hdinsight-provision-clusters).
- Some native Java components, like Mahout and Cascading, can be run on the cluster as JAR files. These JAR files can be distributed to Azure Blob storage, and submitted to HDInsight clusters through Hadoop job submission mechanisms. For more information, see [Submit Hadoop jobs programmatically](/documentation/articles/hdinsight-submit-hadoop-jobs-programmatically).


	>[AZURE.NOTE] If you have issues deploying JAR files to HDInsight clusters or calling JAR files on HDInsight clusters, contact [Microsoft Support](/support/contact/).

	> Cascading is not supported by HDInsight, and is not eligible for Microsoft Support. For lists of supported components, see [What's new in the cluster versions provided by HDInsight?](/documentation/articles/hdinsight-component-versioning).


Installation of custom software on the cluster by using Remote Desktop Connection is not supported. You should avoid storing any files on the drives of the head node, as they will be lost if you need to re-create the clusters. We recommend storing files on Azure Blob storage. Blob storage is persistent.

##Change the HDInsight cluster user name and password
An HDInsight cluster can have two user accounts. The HDInsight cluster user account is created during the provisioning process. You can also create an RDP user account for accessing the cluster via RDP. See [Enable remote desktop](#connect-to-hdinsight-clusters-by-using-rdp).

**To change the HDInsight cluster user name and password**

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn/).
2. Click **HDINSIGHT** on the left pane. You will see a list of deployed HDInsight clusters.
3. Click the HDInsight cluster that you want to reset the user name and password for.
4. From the top of the page, click **CONFIGURATION**.
5. Click **OFF** next to **HADOOP SERVICES**.
6. Click **SAVE** on the bottom of the page, and wait for the disabling to finish.
7. After the service has been disabled, click **ON** next to **HADOOP SERVICES**.
8. For **USER NAME** and **NEW PASSWORD**, enter the new user name and password (respectively) for the cluster.
8. Click **SAVE**.


##Connect to HDInsight clusters by using RDP

The credentials for the cluster that you provided at its creation give access to the services on the cluster, but not to the cluster itself through Remote Desktop. Remote Desktop access is turned off by default, and so direct access to the cluster using it requires some additional, post-creation configuration.

**To enable Remote Desktop**

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn/).
2. Click **HDINSIGHT** on the left pane. You will see a list of deployed HDInsight clusters.
3. Click the HDInsight cluster that you want to connect to.
4. From the top of the page, click **CONFIGURATION**.
5. From the bottom of the page, click **ENABLE REMOTE**.
6. In the **Configure Remote Desktop** wizard, enter a user name and password for the remote desktop. Note that the user name must be different from the one used to create the cluster (**admin** by default with the Quick Create option). Enter an expiration date in the **EXPIRES ON** box. Note that the expiration date must be in the future and up to 90 days from today. The expiration time of day is assumed by default to be midnight of the specified date. Then click the check icon.

	![HDI.CreateRDPUser][image-hdi-create-rpd-user]


> [AZURE.NOTE] You can also use the HDInsight .NET SDK to enable Remote Desktop on a cluster. Use the **EnableRdp** method on the HDInsight client object in the following manner: **client.EnableRdp(clustername, location, "rdpuser", "rdppassword", DateTime.Now.AddDays(6))**. Similarly, to disable Remote Desktop on the cluster, you can use **client.DisableRdp(clustername, location)**. For more information on these methods, see [HDInsight .NET SDK Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn469975.aspx). This is applicable only for HDInsight clusters running on Windows.



> [AZURE.NOTE] Once RDP is enabled for a cluster, you must refresh the page before you can connect to the cluster.

**To connect to a cluster by using RDP**

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn/).
2. Click **HDINSIGHT** on the left pane. You will see a list of deployed HDInsight clusters.
3. Click the HDInsight cluster that you want to connect to.
4. From the top of the page, click **CONFIGURATION**.
5. Click **CONNECT**, and then follow the instructions.

##Create a self-signed certificate

If you want to perform any operations on the cluster by using the .NET SDK, you must create a self-signed certificate on the workstation, and also upload the certificate to your Azure subscription. This is a one-time task. You can install the same certificate on other machines, as long as the certificate is valid.

**To create a self-signed certificate**

1. Create a self-signed certificate that is used to authenticate the requests. You can use Internet Information Services (IIS) or [makecert]( https://msdn.microsoft.com/zh-cn/library/bfsktky3(v=vs.110).aspx) to create the certificate.

2. Browse to the location of the certificate, right-click the certificate, click **Install Certificate**, and install the certificate to the computer's personal store. Edit the certificate properties to assign it a friendly name.

3. Import the certificate into the Azure Management Portal. From the portal, click **SETTINGS** on the bottom left of the page, and then click **MANAGEMENT CERTIFICATES**. From the bottom of the page, click **UPLOAD** and follow the instructions to upload the .cer file you created in the previous step.

	![HDI.ClusterCreate.UploadCert][image-hdiclustercreate-uploadcert]


##Grant/revoke HTTP services access

HDInsight clusters have the following HTTP web services (all of these services have RESTful endpoints):

- ODBC
- JDBC
- Ambari
- Oozie
- Templeton

By default, these services are granted for access. You can revoke/grant the access from the Azure Management Portal.

>[AZURE.NOTE] By granting/revoking the access, you will reset the cluster user name and password.

**To grant/revoke HTTP web services access**

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn/).
2. Click **HDINSIGHT** on the left pane. You will see a list of deployed HDInsight clusters.
3. Click the HDInsight cluster that you want to configure.
4. From the top of the page, click **CONFIGURATION**.
5. Click **ON** or **OFF** next to **HADOOP SERVICES**.
6. For **USER NAME** and **NEW PASSWORD**, enter the new user name and password (respectively) for the cluster.
7. Click **SAVE**.

This can also be done through the Azure PowerShell cmdlets:

- Grant-AzureHDInsightHttpServicesAccess
- Revoke-AzureHDInsightHttpServicesAccess

See [Administer HDInsight using Azure PowerShell](/documentation/articles/hdinsight-administer-use-powershell).

##Open a Hadoop command line

To connect to the cluster by using Remote Desktop and use the Hadoop command line, you must first have enabled Remote Desktop access to the cluster as described in the previous section.

**To open a Hadoop command line**

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn/).
2. Click **HDINSIGHT** on the left pane. You will see a list of deployed Hadoop clusters.
3. Click the HDInsight cluster that you want to connect to.
3. Click **CONFIGURATION** on the top of the page.
4. Click **CONNECT** on the bottom of the page.
5. Click **Open**.
6. Enter your credentials, and then click **OK**. Use the user name and password you configured when you created the cluster.
7. Click **Yes**.
8. From the desktop, double-click **Hadoop Command Line**.

	![HDI.HadoopCommandLine][image-hadoopcommandline]


	For more information on Hadoop commands, see [Hadoop commands reference](http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/CommandsManual.html).

In the previous screenshot, the folder name has the Hadoop version number embedded. The version number can changed based on the version of the Hadoop components installed on the cluster. You can use Hadoop environment variables to refer to those folders. For example:

	cd %hadoop_home%
	cd %hive_home%
	cd %pig_home%
	cd %sqoop_home%
	cd %hcatalog_home%

##Scale clusters
See [Scale Hadoop clusters in HDInsight](/documentation/articles/hdinsight-hadoop-cluster-scaling).

##Next steps
In this article, you have learned how to create an HDInsight cluster by using the Azure Management Portal, and how to open the Hadoop command-line tool. To learn more, see the following articles:

* [Administer HDInsight Using Azure PowerShell](/documentation/articles/hdinsight-administer-use-powershell)
* [Administer HDInsight Using Azure CLI](/documentation/articles/hdinsight-administer-use-command-line)
* [Provision HDInsight clusters](/documentation/articles/hdinsight-provision-clusters)
* [Submit Hadoop jobs programmatically](/documentation/articles/hdinsight-submit-hadoop-jobs-programmatically)
* [Get Started with Azure HDInsight](/documentation/articles/hdinsight-get-started)
* [What version of Hadoop is in Azure HDInsight?](/documentation/articles/hdinsight-component-versioning)

[image-cluster-quickcreate]: ./media/hdinsight-administer-use-management-portal-v1/HDI.QuickCreateCluster.png
[image-cluster-landing]: ./media/hdinsight-administer-use-management-portal-v1/HDI.ClusterLanding.PNG "Cluster landing page"
[image-hdi-create-rpd-user]: ./media/hdinsight-administer-use-management-portal-v1/HDI.CreateRDPUser.png
[image-hadoopcommandline]: ./media/hdinsight-administer-use-management-portal-v1/HDI.HadoopCommandLine.PNG "Hadoop command line"
[image-hdiclustercreate-uploadcert]: ./media/hdinsight-administer-use-management-portal-v1/HDI.ClusterCreate.UploadCert.png
