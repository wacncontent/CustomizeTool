<properties 
   pageTitle="Use Apache Phoenix and SQuirreL in HDInsight | Azure" 
   description="Learn how to use Apache Phoenix in HDInsight, and how to install and configure SQuirreL on your workstation to connect to an HBase cluster in HDInsight." 
   services="hdinsight" 
   documentationCenter="" 
   authors="mumian" 
   manager="paulettm" 
   editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="12/02/2015"
	wacn.date=""/>

# Use Apache Phoenix and SQuirreL with HBase clusters in HDinsight  

Learn how to use [Apache Phoenix](http://phoenix.apache.org/) in HDInsight, and how to install and configure SQuirreL on your workstation to connect to an HBase cluster in HDInsight. For more information about Phoenix, see [Phoenix in 15 minutes or less](http://phoenix.apache.org/Phoenix-in-15-minutes-or-less.html). For the Phoenix grammar, see [Phoenix Grammar](http://phoenix.apache.org/language/index.html).

>[AZURE.NOTE] For the Phoenix version information in HDInsight, see [What's new in the Hadoop cluster versions provided by HDInsight?][hdinsight-versions].

##Use SQLLine
[SQLLine](http://sqlline.sourceforge.net/) is a command line utility to execute SQL. 

###Prerequisites
Before you can use SQLLine, you must have the following:

- **A HBase cluster in HDInsight**. For information on provision HBase cluster, see [Get started with Apache HBase in HDInsight][hdinsight-hbase-get-started].
- **Connect to the HBase cluster via the remote desktop protocol**. For instructions, see [Manage Hadoop clusters in HDInsight by using the Azure Management Portal][hdinsight-manage-portal].

**To find out the host name**

1. Open **Hadoop Command Line** from the desktop.
2. Run the following command to get the DNS suffix:

		ipconfig

	Write down **Connection-specific DNS Suffix**. For example, *myhbasecluster.f5.internal.chinacloudapp.cn*. When you connect to an HBase cluster, you will need to connect to one of the Zookeepers using FQDN. Each HDInsight cluster has 3 Zookeepers. They are *zookeeper0*, *zookeeper1*, and *zookeeper2*. The FQDN will be something like *zookeeper2.myhbasecluster.f5.internal.chinacloudapp.cn*.

**To use SQLLine**

1. Open **Hadoop Command Line** from the desktop.
2. Run the following commands to open SQLLine:

		cd %phoenix_home%\bin
		sqlline.py [The FQDN of one of the Zookeepers]

	![hdinsight hbase phoenix sqlline][hdinsight-hbase-phoenix-sqlline]

	The commands used in the sample:

		CREATE TABLE Company (COMPANY_ID INTEGER PRIMARY KEY, NAME VARCHAR(225));
		
		!tables;
		
		UPSERT INTO Company VALUES(1, 'Microsoft');
		
		SELECT * FROM Company;

For more information, see [SQLLine manual](http://sqlline.sourceforge.net/#manual) and [Phoenix Grammar](http://phoenix.apache.org/language/index.html).


















##Use SQuirreL

[SQuirreL SQL Client](http://squirrel-sql.sourceforge.net/) is a graphical Java program that will allow you to view the structure of a JDBC compliant database, browse the data in tables, issue SQL commands etc. It can be used to connect to Apache Phoenix on HDInsight.


###Prerequisites

Before following the procedures, you must have the following:

- An HBase cluster deployed to an Azure virtual network with a DNS virtual machine.  For instructions, see [Provision HBase clusters on Azure Virtual Network][hdinsight-hbase-provision-vnet-v1]. 

	>[AZURE.IMPORTANT] You must install a DNS server to the virtual network. For instructions, see [Configure DNS between two Azure virtual networks](/documentation/articles/hdinsight-hbase-geo-replication-configure-DNS)

- Get the HBase cluster cluster Connection-specific DNS suffix. To get it, RDP into the cluster, and then run IPConfig.  The DNS suffix is similar to:

		myhbase.b7.internal.chinacloudapp.cn
- Download and install [Microsoft Visual Studio Express 2013 for Windows Desktop](https://www.visualstudio.com/products/visual-studio-express-vs.aspx) on your workstation. You will need makecert from the package to create your certificate.  
- Download and install [Java Runtime Environment](http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html) on your workstation.  SQuirreL SQL client version 3.0 and higher requires JRE version 1.6 or higher.  

###Install and configure SQuirreL on your workstation

**To install SQuirreL**

1. Download the SQuirreL SQL client jar file from [http://squirrel-sql.sourceforge.net/#installation](http://squirrel-sql.sourceforge.net/#installation).
2. Open/run the jar file. It requires the [Java Runtime Environment](http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html).
3. Click **Next** twice.
4. Specify a path where you have the write permission, and then click **Next**.
	>[AZURE.NOTE] The default installation folder is in the C:\Program Files\squirrel-sql-3.6 folder.  In order to write to this path, the installer must be granted the administrator privilege. You can open a command prompt as administrator, navigate to Java's bin folder, and then run 

	><p>`java.ejava.exe -jar [the path of the SQuirreL jar file]`
5. Click **OK** to confirm creating the target directory.
6. The default setting is to install the Base and Standard packages.  Click **Next**.
7. Click **Next** twice, and then click **Done**.


**To install the Phoenix driver**

The phoenix driver jar file is located on the HBase cluster. The path is similar to the following based on the versions:

	C:\apps\dist\phoenix-4.0.0.2.1.11.0-2316\phoenix-4.0.0.2.1.11.0-2316-client.jar
You need to copy it to your workstation under the [SQuirreL installation folder]/lib path.  The easiest way is to RDP into the cluster, and then use file copy/paste (CTRL+C and CTRL+V) to copy it to your workstation.

**To add a Phoenix driver to SQuirreL**

1. Open SQuirreL SQL Client from your workstation.
2. Click the **Driver** tab on the left.
2. From the **Drivers** menu, click **New Driver**.
3. Enter the following information:

	- **Name**: Phoenix
	- **Example URL**: jdbc:phoenix:zookeeper2.contoso-hbase-eu.f5.internal.chinacloudapp.cn
	- **Class Name**: org.apache.phoenix.jdbc.PhoenixDriver

	>[AZURE.WARNING] User all lower case in the Example URL. You can use they full zookeeper quorum in case one of them is down.  The hostnames are zookeeper0, zookeeper1, and zookeeper2.

	![HDInsight HBase Phoenix SQuirreL driver][img-squirrel-driver]
4. Click **OK**.

**To create an alias to the HBase cluster**

1. From SQuirreL, Click the **Aliases** tab on the left.
2. From the **Aliases** menu, click **New Alias**.
3. Enter the following information:

	- **Name**: The name of the HBase cluster or any name you prefer.
	- **Driver**: Phoenix.  This must match the driver name you created in the last procedure.
	- **URL**: The URL is copied from your driver configuration. Make sure to user all lower case.
	- **User name**: It can be any text.  Because you use VPN connec
	- **Password**: It can be any text.

	![HDInsight HBase Phoenix SQuirreL driver][img-squirrel-alias]
4. Click **Test**. 
5. Click **Connect**. When it makes the connection, SQuirreL looks like:

	![HBase Phoenix SQuirreL][img-squirrel]

**To run a test**

1. Click the **SQL** tab right next to the **Objects** tab.
2. Copy and paste the following code:

		CREATE TABLE IF NOT EXISTS us_population (state CHAR(2) NOT NULL, city VARCHAR NOT NULL, population BIGINT  CONSTRAINT my_pk PRIMARY KEY (state, city))
3. Click the run button.

	![HBase Phoenix SQuirreL][img-squirrel-sql]
4. Switch back to the **Objects** tab.
5. Expand the alias name, and then expand **TABLE**.  You shall see the new table listed under.
 
##Next steps
In this article, you have learned how to use Apache Phoenix in HDInsight.  To learn more, see

- [HDInsight HBase overview][hdinsight-hbase-overview]:
HBase is an Apache, open-source, NoSQL database built on Hadoop that provides random access and strong consistency for large amounts of unstructured and semistructured data.
- [Provision HBase clusters on Azure Virtual Network][hdinsight-hbase-provision-vnet-v1]:
With virtual network integration, HBase clusters can be deployed to the same virtual network as your applications so that applications can communicate with HBase directly.
- [Configure HBase replication in HDInsight](/documentation/articles/hdinsight-hbase-geo-replication): Learn how to configure HBase replication across two Azure datacenters. 

[azure-portal]: https://manage.windowsazure.cn
[vnet-point-to-site-connectivity]: https://msdn.microsoft.com/zh-cn/library/azure/09926218-92ab-4f43-aa99-83ab4d355555#BKMK_VNETPT

[hdinsight-versions]: /documentation/articles/hdinsight-component-versioning-v1
[hdinsight-hbase-get-started]: /documentation/articles/hdinsight-hbase-tutorial-get-started-v1
[hdinsight-manage-portal]: /documentation/articles/hdinsight-administer-use-management-portal-v1#connect-to-hdinsight-clusters-by-using-rdp
[hdinsight-hbase-provision-vnet-v1]: /documentation/articles/hdinsight-hbase-provision-vnet-v1
[hdinsight-hbase-overview]: /documentation/articles/hdinsight-hbase-overview
[hdinsight-hbase-phoenix-sqlline]: ./media/hdinsight-hbase-phoenix-squirrel/hdinsight-hbase-phoenix-sqlline.png
[img-certificate]: ./media/hdinsight-hbase-phoenix-squirrel/hdinsight-hbase-vpn-certificate.png
[img-vnet-diagram]: ./media/hdinsight-hbase-phoenix-squirrel/hdinsight-hbase-vnet-point-to-site.png
[img-squirrel-driver]: ./media/hdinsight-hbase-phoenix-squirrel/hdinsight-hbase-squirrel-driver.png
[img-squirrel-alias]: ./media/hdinsight-hbase-phoenix-squirrel/hdinsight-hbase-squirrel-alias.png
[img-squirrel]: ./media/hdinsight-hbase-phoenix-squirrel/hdinsight-hbase-squirrel.png
[img-squirrel-sql]: ./media/hdinsight-hbase-phoenix-squirrel/hdinsight-hbase-squirrel-sql.png


 
