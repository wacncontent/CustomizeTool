<properties
   pageTitle="Analyze sensor data with Apache Storm and HBase | Azure"
   description="Learn how to connect to Apache Storm with a virtual network. Use Storm with HBase to process sensor data from an event hub and visualize it with D3.js."
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="jhubbard"
   editor="cgronlun"/>

<tags
   ms.service="hdinsight"
   ms.devlang="java"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="big-data"
   ms.date="07/05/2016"
   wacn.date=""
   ms.author="larryfr"/>

# Analyze sensor data with Apache Storm, Event Hub, and HBase in HDInsight (Hadoop) 


Learn how to use Apache Storm on HDInsight to process sensor data from Azure Event Hub, store it into Apache HBase on HDInsight, and visualize it by using D3.js running as an Azure Web App.

The Azure Resource Manager template used in this document demonstrates how to create multiple Azure resources in a resource group. Specifically, it creates an Azure Virtual Network, two HDInsight clusters (Storm and HBase,) and an Azure Web App. A node.js implementation of a real-time web dashboard is automatically deployed to the web app.

> [AZURE.NOTE] The information in this document, and the example provided, have been tested using Linux-based HDInsight 3.3 and 3.4 cluster versions.


Learn how to use Apache Storm on HDInsight to process sensor data from Azure Event Hub, and visualize it by using D3.js. This document also describes how to use an Azure virtual network to connect Storm on HDInsight with HBase on HDInsight, and store data from the topology into HBase.


## Prerequisites

* An Azure subscription. See [Get Azure trial](/pricing/1rmb-trial/).


    > [AZURE.IMPORTANT] You do not need an existing HDInsight cluster; the steps in this document will create the following resources:
    >
    > * An Azure Virtual Network
    > * A Storm on HDInsight cluster (Linux-based, 2 worker nodes)
    > * An HBase on HDInsight cluster (Linux-based, 2 worker nodes)
    > * An Azure Web App that hosts the web dashboard

* [Node.js](http://nodejs.org/): This is used to preview the web dashboard locally on your development environment.


* An [Apache Storm on HDInsight cluster](/documentation/articles/hdinsight-apache-storm-tutorial-get-started/)

* [Node.js](http://nodejs.org/): Used for the web dashboard and to send sensor data to Event Hub.


* [Java and the JDK 1.7](http://www.oracle.com/technetwork/java/javase/downloads/index.html) : Used to develop the Storm topology. 

* [Maven](http://maven.apache.org/what-is-maven.html) : Used to build and compile the project. 

* [Git](http://git-scm.com/) : Used to download the project from GitHub. 


* An __SSH__ client: Used to connect to the Linux-based HDInsight clusters. For more information on using SSH with HDInsight, see the following documents.

    * [Use SSH with HDInsight from a Windows client](/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows/)

    * [Use SSH with HDInsight from a Linux, Unix, or Mac client](/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix/)

    > [AZURE.NOTE] You must also have access to the `scp` command, which is used to copy files between your local development environment and the HDInsight cluster using SSH.


> [AZURE.NOTE] Java, the JDK, Maven, and Git are also available through the [Chocolatey NuGet](http://chocolatey.org/) package manager.


## Architecture

![architecture diagram](./media/hdinsight-storm-sensor-data-analysis/devicesarchitecture.png)

This example consists of the following components:


* **Azure Event Hubs**: Contains data that is collected from sensors. For this example, an application is provided that generates the data.


* **Azure Event Hub**: Provides data that is collected from sensors. For this example, an application is provided that generates fake data.


* **Storm on HDInsight**: Provides real-time processing of data from Event Hub.


* **HBase on HDInsight**: Provides a persistent NoSQL data store for data after it has been procedd by Storm.


* **HBase on HDInsight** (optional): Provides a persistent NoSQL data store.


* **Azure Virtual Network service**  (optional, required if using HBase) : Enables secure communications between the Storm on HDInsight and HBase on HDInsight clusters.


    > [AZURE.NOTE] A virtual network is required in order to use the Java HBase client API, as it is not exposed over the public gateway for HBase clusters. Installing HBase and Storm clusters into the same virtual network allows the Storm cluster (or any other system on the virtual network,) to directly access HBase using client API.


* **Dashboard website**: An example dashboard that charts data in real time.

	* The website is implemented in Node.js, so it can run on any client operating system for testing, or it can be deployed to Azure Websites.

	* [Socket.io](http://socket.io/) is used for real-time communication between the Storm topology and the website.

		> [AZURE.NOTE] This is an implementation detail. You can use any communications framework, such as raw WebSockets or SignalR.

	* [D3.js](http://d3js.org/) is used to graph the data that is sent to the website.


The topology reads data from Event Hub by using the [org.apache.storm.eventhubs.spout.EventHubSpout](http://storm.apache.org/releases/0.10.1/javadocs/org/apache/storm/eventhubs/spout/class-use/EventHubSpout.html) class, and writes data into HBase using the [org.apache.storm.hbase.bolt.HBaseBolt](https://storm.apache.org/javadoc/apidocs/org/apache/storm/hbase/bolt/class-use/HBaseBolt.html) class. Communication with the website is accomplished by using [socket.io-client.java](https://github.com/nkzawa/socket.io-client.java).


The topology reads data from Event Hub by using the **com.microsoft.eventhubs.spout.EventHubSpout** class, which is provided in the Storm on HDInsight cluster. Communication with the website is accomplished by using [socket.io-client.java](https://github.com/nkzawa/socket.io-client.java).

Optionally, communication with HBase is accomplished by using the [org.apache.storm.hbase.bolt.HBaseBolt](https://storm.apache.org/javadoc/apidocs/org/apache/storm/hbase/bolt/class-use/HBaseBolt.html) class, which is provided as part of Storm.


The following is a diagram of the topology.

![topology diagram](./media/hdinsight-storm-sensor-data-analysis/sensoranalysis.png)

> [AZURE.NOTE] This is a very simplified view of the topology. At run time, an instance of each component is created for each partition for the Event Hub that is being read. These instances are distributed across the nodes in the cluster, and data is routed between them as follows:
>
> * Data from the spout to the parser is load balanced.
> * Data from the parser to the Dashboard and HBase  (if used)  is grouped by Device ID, so that messages from the same device always flow to the same component.


### Topology components

* **EventHub Spout**: The spout is provided as part of Apache Storm version 0.10.0 and higher.

    > [AZURE.NOTE] The Event Hubs spout used in this example requires an Storm on HDInsight cluster version 3.3 or 3.4. For information on how to use Event Hubs with an older version of Storm on HDInsight, see [Process events from Azure Event Hubs with Storm on HDInsight](/documentation/articles/hdinsight-storm-develop-java-event-hub-topology/).


### Components

* **EventHub Spout**: The spout is provided as part of the [HDInsight Storm Examples](https://github.com/hdinsight/hdinsight-storm-examples) on GitHub.


* **ParserBolt.java**: The data that is emitted by the spout is raw JSON, and occasionally more than one event is emitted at a time. This bolt demonstrates how to read the data emitted by the spout, and emit it to a new stream as a tuple that contains multiple fields.

* **DashboardBolt.java**: This demonstrates how to use the Socket.io client library for Java to send data in  real-time  real time  to the web dashboard.

## Prepare your environment


Before you use this example, you must create an Azure Event Hub, which the Storm topology reads from.


Before you use this example, you must create an Azure Event Hub, which the Storm topology reads. You must also create a Storm on HDInsight topology because the component used to read data from Event Hub is only available in the cluster.

> [AZURE.NOTE] Eventually the Event Hub spout will be available from Maven.


### Configure Event Hub

Event Hub is the data source for this example. Use the following steps to create a new Event Hub.

1. From the [Azure Classic Management Portal](https://manage.windowsazure.cn), select **NEW | Service Bus | Event Hub | Custom Create**.

2. In the **Add a new Event Hub** dialog box, enter an **Event Hub Name**, select the **Region** to create the hub in, and then create a new namespace or select an existing one. Finally, click the arrow to continue.

2. In the **Configure Event Hub** dialog box, enter the **Partition count** and **Message Retention** values. For this example, use a partition count of 10 and a message retention of 1.

3. When the event hub has been created, select the namespace, then select **Event Hubs**. Finally, select the event hub that you created earlier.

4. Select **Configure**, then create two new access policies by using the following information.

	| Name | Permissions |
    | ----- | ----- |
	| devices | Send |
	| storm | Listen |

	After creating permissions, select the **Save** icon at the bottom of the page. This creates the shared access policies that will be used to send messages to and read messages from this hub.

5. After saving the policies, use the **Shared access key generator** at the bottom of the page to retrieve the key for the **devices** and **storm** policies. Save these because you will use them later.


### Create the Storm on HDInsight cluster

1. Sign in to the [Azure Classic Management Portal](https://manage.windowsazure.cn/).

2. Click **HDInsight** in the left pane, and then click **+NEW** in the lower-left corner of the page.

3. Click the HDInsight icon in the second column, and then select **Custom**.

4. On the **Cluster Details** page, enter the name of the new cluster, and select **Storm** for the **Cluster Type**. Click the arrow to continue.

5. Enter 1 for the number of **Data Nodes** to use for this cluster.

	> [AZURE.NOTE] To minimize the cost for the cluster used for this article, reduce the **Cluster Size** to 1, and delete the cluster after you have finished using it.

6. Enter the administrator **User Name** and **Password**, and then click the arrow to continue.

4. For **Storage Account**, select **Create New Storage** or select an existing storage account. Select or enter the **Account Name** and **Default container** to use. Select the check mark icon in the lower-left corner to create the Storm cluster.

## Download and install the EventHubSpout

1. Download the [HDInsight Storm Examples project](https://github.com/hdinsight/hdinsight-storm-examples/). Once downloaded, find the **lib/eventhubs/eventhubs-storm-spout-0.9-jar-with-dependencies.jar** file.

2. From the command prompt, use the following command to install the **eventhubs-storm-spout-0.9-jar-with-dependencies.jar** file into the local Maven store. This will allow you to easily add it as a reference in the Storm project in a later step.

		mvn install:install-file -Dfile=target/eventhubs-storm-spout-0.9-jar-with-dependencies.jar -DgroupId=com.microsoft.eventhubs -DartifactId=eventhubs-storm-spout -Dversion=0.9 -Dpackaging=jar


## Download and configure the project

Use the following to download the project from GitHub.

	git clone https://github.com/Blackmist/hdinsight-eventhub-example

After the command completes, you will have the following directory structure:

	hdinsight-eventhub-example/
		TemperatureMonitor/ - this is the Java topology
			conf/
				Config.properties
				hbase-site.xml
			src/
			test/
			dashboard/ - this is the node.js web dashboard
			SendEvents/ - utilities to send fake sensor data

> [AZURE.NOTE] This document does not go in to full details of the code included in this sample; however, the code is fully commented.

Open the **Config.properties** file and add the information you previously used when creating the Event Hub  for the entries listed below . Save the file after you add this information.

	eventhubspout.username = storm

	eventhubspout.password = <the key of the 'storm' policy>

	eventhubspout.namespace = <the event hub namespace>

	eventhubspout.entitypath = <the event hub name>

	eventhubspout.partitions.count = <the number of partitions for the event hub>


	## if not provided, will use storm's zookeeper settings
	## zookeeper.connectionstring=localhost:2181

	eventhubspout.checkpoint.interval = 10

	eventhub.receiver.credits = 1024


## Compile and test locally

Before testing, you must start the dashboard to view the output of the topology and generate data to store in Event Hub.


> [AZURE.IMPORTANT] The HBase component of this topology is not active when testing locally, as the Java API for the HBase cluster cannot be accessed from outside the Azure Virtual Network that contains the clusters.


### Start the web application

1. Open a new command prompt or terminal, and change directories to the **hdinsight-eventhub-example/dashboard**, then use the following command to install the dependencies needed by the web application:

		npm install

2. Use the following command to start the web application:

		node server.js

	You should see a message similar to the following:

		Server listening at port 3000

2. Open a web browser and enter **http://localhost:3000/** as the address. You should see a page similar to the following:

	![web dashboard](./media/hdinsight-storm-sensor-data-analysis/emptydashboard.png)

	Leave this command prompt or terminal open. After testing, use Ctrl-C to stop the web server.

### Start generating data

> [AZURE.NOTE] The steps in this section use Node.js so that they can be used on any platform. For other language examples, see the **SendEvents** directory.

1. Open a new command prompt or terminal, and change directories to **hdinsight-eventhub-example/SendEvents/nodejs**, then use the following command to install the dependencies needed by the application:

		npm install

2. Open the **app.js** file in a text editor and add the Event Hub information you obtained earlier:

		// ServiceBus Namespace
		var namespace = 'servicebusnamespace';
		// Event Hub Name
		var hubname ='eventhubname';
		// Shared access Policy name and key (from Event Hub configuration)
		var my_key_name = 'devices';
		var my_key = 'key';

2. Use the following command to insert new entries in Event Hub:

		node app.js

	You should see several lines of output that contain the data sent to Event Hub. These will appear similar to the following:

		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"0","Temperature":7}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"1","Temperature":39}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"2","Temperature":86}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"3","Temperature":29}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"4","Temperature":30}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"5","Temperature":5}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"6","Temperature":24}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"7","Temperature":40}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"8","Temperature":43}
		{"TimeStamp":"2015-02-10T14:43.05.00320Z","DeviceId":"9","Temperature":84}

### Start the topology

2. Start the topology locally by using the following command:

        mvn compile exec:java -Dstorm.topology=com.microsoft.examples.Temperature

	This will start the topology, read files from Event Hub, and send them to the dashboard running in Azure Websites. You should see lines appear in the web dashboard, similar to the following:

	![dashboard with data](./media/hdinsight-storm-sensor-data-analysis/datadashboard.png)


    > [AZURE.NOTE] If you are running this command from a PowerShell prompt, you must use double quotes around the `-Dstorm.topology=com.microsoft.examples.Temperature` parameter. For example, `mvn compile exec:java "-Dstorm.topology=com.microsoft.examples.Temperature"`.

3. While the dashboard is running, use the `node app.js` command from the previous steps to send new data to Event Hubs. Because the temperature values are randomly generated, the graph should update to show large changes in temperature.



3. While the dashboard is running, use the `node app.js` command from the previous steps to send new data to the dashboard. Because the temperature values are randomly generated, the graph should update to show the new values.


3. After verifying that this works, stop the topology  using  by typing  Ctrl+C. To stop the SendEvent app, select the window and press any key. You can use Ctrl+C to stop the web server also.


## Create a Storm and HBase cluster

In order to run the topology on HDInsight, and to enable the HBase bolt, you must create a new Storm cluster and HBase cluster. The steps in this section use an [Azure Resource Manager template](/documentation/articles/resource-group-template-deploy/) to create a new Azure Virtual Network and a Storm and HBase cluster on the virtual network. The template also creates an Azure Web App and deploys a copy of the dashboard into it.

> [AZURE.NOTE] A virtual network is used so that the topology running on the Storm cluster can directly communicate with the HBase cluster using the HBase Java API.

The Resource Manager template used in this document is located in a public blob container at __https://hditutorialdata.blob.core.windows.net/armtemplates/create-linux-based-hbase-storm-cluster-in-vnet.json__.

1. Click the following button to sign in to Azure and open the Resource Manager template in the Azure Portal.

    <a href="https://portal.azure.cn/#create/Microsoft.Template/uri/https%3A%2F%2Fhditutorialdata.blob.core.windows.net%2Farmtemplates%2Fcreate-linux-based-hbase-storm-cluster-in-vnet.json" target="_blank"><img src="https://acom.azurecomcdn.net/80C57D/cdn/mediahandler/docarticles/dpsmedia-prod/azure.microsoft.com/documentation/articles/hdinsight-hbase-tutorial-get-started-v1/20160201111850/deploy-to-azure.png" alt="Deploy to Azure"></a>

2. From the **Parameters** blade, enter the following:

    ![HDInsight parameters](./media/hdinsight-storm-sensor-data-analysis/parameters.png)
    
    * **BASECLUSTERNAME**: This value will be used as the base name for the Storm and HBase clusters. For example, entering __hdi__ will create a Storm cluster named __storm-hdi__ and an HBase cluster named __hbase-hdi__.
    * __CLUSTERLOGINUSERNAME__: The admin user name for the Storm and HBase clusters.
    * __CLUSTERLOGINPASSWORD__: The admin user password for the Storm and HBase clusters.
    * __SSHUSERNAME__: The SSH user to create for the Storm and HBase clusters.
    * __SSHPASSWORD__: The password for the SSH user for the Storm and HBase clusters.
    * __LOCATION__: The region that the clusters will be created in.
    
    Click __OK__ to save the parameters.
    
3. Use the __Resource group__ section to create a new resource group or select an existing one.

4. In the __Resource group location__ dropdown menu, select the same location as you selected for the __LOCATION__ parameter.

5. Select __Legal terms__, and then select __Create__.

6. Finally, check __Pin to dashboard__ and then select __Create__. It will take about 20 minutes to create the clusters.

Once the resources have been created, you will be redirected to a blade for the resource group that contains the clusters and web dashboard.

![Resource group blade for the vnet and clusters](./media/hdinsight-storm-sensor-data-analysis/groupblade.png)

> [AZURE.IMPORTANT] Notice that the names of the HDInsight clusters are __storm-BASENAME__ and __hbase-BASENAME__, where BASENAME is the name you provided to the template. You will use these names in later steps when connecting to the clusters. Also note that the name of the dashboard site is __basename-dashboard__. You will use this later when viewing the dashboard.

## Configure the Dashboard bolt

In order to send data to the dashboard deployed as a web app, you must modify the following line in the __DashboardBolt.java__ file:

    socket = IO.socket("http://localhost:3000");

Change `http://localhost:3000` to `http://BASENAME-dashboard.chinacloudsites.cn` and save the file. Replace __BASENAME__ with the base name you provided in the previous step. You can also use the resource group created previously to select the dashboard and view the URL.

## Create the HBase table

In order to store data in HBase, we must first create a table. You generally want to pre-create resources that Storm needs to write to, as trying to create resources from inside a Storm topology can result in multiple, distributed copies of the code trying to create the same resource. Create the resources outside the topology and just use Storm for reading/writing and analytics.

1. Use SSH to connect to the HBase cluster using the SSH user and password you supplied to the template during cluster creation. For example, if connecting using the `ssh` command, you would use the following syntax:

        ssh USERNAME@hbase-BASENAME-ssh.azurehdinsight.cn
    
    In this command, replace __USERNAME__ with the SSH user name you provided when creating the cluster, and __BASENAME__ with the base name you provided. When prompted, enter the password for the SSH user.

2. From the SSH session, start the HBase shell.

    	hbase shell
	Once the shell has loaded, you will see an `hbase(main):001:0>` prompt.

3. From the HBase shell, enter the following command to create a table to store the sensor data:

    	create 'SensorData', 'cf'

4. Verify that the table has been created by using the following command:

    	scan 'SensorData'
		
	This should return information similar to the followig, indicating that there are 0 rows in the table.
		ROW                   COLUMN+CELL                                       0 row(s) in 0.1900 seconds

5. Enter the following to exit the HBase shell:

		exit

## Configure the HBase bolt

To write to HBase from the Storm cluster, you must provide the HBase bolt with the configuration details of your HBase cluster. The easiest way to do this is to download the __hbase-site.xml__ from the cluster and include it in your project. You must also uncomment several dependencies in the __pom.xml__ file, which load the storm-hbase component and required dependencies.

> [AZURE.IMPORTANT] You must also download the storm-hbase.jar file provided on your Storm on HDInsight cluster 3.3 or 3.4 cluster; this version is compiled to work with HBase 1.1.x, which is used for HBase on HDInsight 3.3 and 3.4 clusters. If you use a storm-hbase component from elsewhere, it may be compiled against an older version of HBase.

### Download the hbase-site.xml

From a command prompt, use SCP to download the __hbase-site.xml__ file from the cluster. In the following example, replace __USERNAME__ with the SSH user you provided when creating the cluster, and __BASENAME__ with the base name you provided earlier. When prompted, enter the password for the SSH user. Replace the `/path/to/TemperatureMonitor/conf/hbase-site.xml` with the path to this file in the TemperatureMonitor project.

    scp USERNAME@hbase-BASENAME-ssh.azurehdinsight.cn:/etc/hbase/conf/hbase-site.xml /path/to/TemperatureMonitor/conf/hbase-site.xml

This will download the __hbase-site.xml__ to the path specified.

### Download and install the storm-hbase component

1. From a command prompt, use SCP to download the __storm-hbase.jar__ file from the Storm cluster. In the following example, replace __USERNAME__ with the SSH user you provided when creating the cluster, and __BASENAME__ with the base name you provided earlier. When prompted, enter the password for the SSH user.

        scp USERNAME@storm-BASENAME-ssh.azurehdinsight.cn:/usr/hdp/current/storm-client/contrib/storm-hbase/storm-hbase*.jar .

    This will download a file named `storm-hbase-####.jar`, where #### is the version number of Storm for this cluster. Make a note of this number, as it is used later.

2. Use the following command to install this component into the local Maven repository on your develoment environment. This enables Maven to find the package when compiling the project. Replace __####__ with the version number included in the file name.

        mvn install:install-file -Dfile=storm-hbase-####.jar -DgroupId=org.apache.storm -DartifactId=storm-hbase -Dversion=#### -Dpackaging=jar

### Enable the storm-hbase component in the project

1. Open the __TemperatureMonitor/pom.xml__ file and delete the following lines:

        <!-- uncomment this section to enable the hbase-bolt
        end comment for hbase-bolt section -->
    
    > [AZURE.IMPORTANT] Only delete these two lines; do not delete any of the lines between them.
    
    This enables several components that are needed when communicating with HBase using the hbase bolt.

2. Find the following lines, and then replace __####__ with the version number of the storm-hbase file you downloaded earlier.

        <dependency>
            <groupId>org.apache.storm</groupId>
            <artifactId>storm-hbase</artifactId>
            <version>####</version>
        </dependency>

    > [AZURE.IMPORTANT] The version number must match the version you used when installing the component into the local Maven repository, as Maven uses this information to load the component when building the project.

2. Save the __pom.xml__ file.

3. Open **TemperatureMonitor/src/main/java/com/microsoft/examples/Temperature.java** in a text editor, and uncomment the following lines by removing the `//` from the beginning of each.



## Package and deploy the topology to HDInsight

In your development environment, use the following steps to run the Temperature topology on your HDInsight Storm cluster.

### Publish the website dashboard

1. To deploy the dashboard to an Azure Website, follow the steps in [Build and deploy a Node.js website to Azure](/documentation/articles/web-sites-nodejs-develop-deploy-mac/). Note the URL of the website, which will be similar to **mywebsite.chinacloudsites.cn**.

2. When the website is created, go to the site in the Azure Classic Management Portal and select the **Configure** tab. Enable **Web Sockets**, and then click **Save** at the bottom of the page.

2. Open **hdinsight-eventhub-example\TemperatureMonitor\src\main\java\com\microsoft\examples\bolts\DashboardBolt.java** and change the following line to point to the URL of the published dashboard:

		socket = IO.socket("http://mywebsite.chinacloudsites.cn");

3. Save the **DashboardBolt.java** file.

### Package and deploy the topology

1. Use the following command to create a JAR package from your project:

		mvn package

	This will create a file named **TemperatureMonitor-1.0-SNAPSHOT.jar** in the **target** directory of your project.

2. Follow the steps in [Deploy and manage Storm topologies](/documentation/articles/hdinsight-storm-deploy-monitor-topology/) to upload and start the topology on your Storm on HDInsight cluster by using the **Storm Dashboard**.

3. After the topology has started, open a browser to the website you published on Azure, then use the `node app.js` command to send data to Event Hub. You should see the web dashboard update to display the information.

	![dashboard](./media/hdinsight-storm-sensor-data-analysis/datadashboard.png)

## Optional: Use HBase

To use Storm and HBase together, you must create an Azure virtual network and then create a Storm and HBase cluster within the network.

### Create an Azure virtual network (optional)

If you plan to use HBase with this example, you must create an Azure virtual network that will contain a Storm on HDInsight cluster and an HBase on HDInsight cluster.

1. Sign in to the [Azure Classic Management Portal](https://manage.windowsazure.cn).

2. On the bottom of the page, click **+NEW** > **Network Services** > **Virtual Network** > **Quick Create**.

3. Type or select the following values:

	- **Name**: The name of your virtual network.

	- **Address space**: Choose an address space for the virtual network that is large enough to provide addresses for all nodes in the cluster. Otherwise, the provision will fail.

	- **Maximum VM count**: Choose one of the maximum virtual machine counts.

	- **Location**: The location must be the same as the HBase cluster that you will create.

	- **DNS server**: This article uses the internal DNS server provided by Azure; therefore, you can choose **None**. More advanced networking configurations with custom DNS servers are also supported. For the detailed guidance, see [Name Resolution (DNS)](/documentation/articles/virtual-networks-name-resolution-for-vms-and-role-instances/).

4. Click **Create a Virtual Network**. The new virtual network name will appear in the list. Wait until the Status column shows **Created**.

5. In the main pane, click the virtual network you just created.

6. On the top of the page, click **DASHBOARD**.

7. Under **quick glance**, make a note of **VIRTUAL NETWORK ID**. You will need it when provisioning the Storm and HBase clusters.

8. At the top of the page, click **CONFIGURE**.

9. At the bottom of the page, the default subnet name is **Subnet-1**. Use the **add subnet** button to add **Subnet-2**. These subnets will house the Storm and HBase clusters.

	> [AZURE.NOTE] In this article, we will be using clusters with only one node. If you are creating multinode clusters, you must verify the **CIDR(ADDRESS COUNT)** for the subnet that will be used for the cluster. The address count must be greater than the number of worker nodes plus seven (Gateway: 2, Headnode: 2, Zookeeper: 3). For example, if you need a 10 node HBase cluster, the address count for the subnet must be greater than 17 (10+7). Otherwise, the deployment will fail.
	> <p>It is highly recommended to designate a single subnet for one cluster.

11. Click **Save** at the bottom of the page.

### Create a Storm and HBase cluster on the virtual network

1. Sign in to the [Azure Classic Management Portal](https://manage.windowsazure.cn/).

2. Click **HDInsight** in the left pane, and then click **+NEW** in the lower-left corner of the page.

3. Click the HDInsight icon in the second column, and then select **Custom**.

4. On the **Cluster Details** page, enter the name of the new cluster, and select **Storm** for the **Cluster Type**. Click the arrow to continue.

5. Enter 1 for the number of **Data Nodes** to use for this cluster. For **Region/Virtual Network**, select the Azure virtual network that you created earlier. For **Virtual Network Subnets**, select **Subnet-1**.

	> [AZURE.NOTE] To minimize the cost for the cluster used for this article, reduce the **Cluster Size** to 1, and delete the cluster after you have finished using it.

6. Enter the administrator **User Name** and **Password**, then click the arrow to continue.

4. For **Storage Account**, select **Create New Storage** or select an existing storage account. Select or enter the **Account Name** and **Default container** to use. Select the check mark icon in the lower-left corner to create the Storm cluster.

5. Repeat these steps to create a new **HBase** cluster. The following are the key differences:

	* **Cluster Type**: Select **HBase**

	* **Virtual Network Subnets**: Select **Subnet-2**

	* **Storage Account**: You should use a different container than the one used for the Storm cluster.

### Discover the HBase DNS suffix

To write to HBase from the Storm cluster, you must use the fully qualified domain name (FQDN) for the HBase cluster. Use the following command to discover this information:

	curl -u <username>:<password> -k https://<clustername>.azurehdinsight.cn/ambari/api/v1/clusters/<clustername>.azurehdinsight.cn/services/hbase/components/hbrest

In the JSON data returned, find the **"host_name"** entry. This will contain the FQDN for the nodes in the cluster, for example:

	...
	"host_name": "wordkernode0.<clustername>.b1.chinacloudapp.cn
	...

The portion of the domain name beginning with the cluster name is the DNS suffix, for example, **mycluster.b1.chinacloudapp.cn**.

### Enable the HBase bolt

1. Open **hdinsight-eventhub-example\TemperatureMonitor\conf\hbase-site.xml** and replace the `suffix` entries in the following line with the DNS suffix obtained previously for the HBase cluster. Save the file after you make these changes.

		<value>zookeeper0.suffix,zookeeper1.suffix,zookeeper2.suffix</value>

	This will be used by the HBase bolt to communicate with the HBase cluster.

1. Open **hdinsight-eventhub-example\TemperatureMonitor\src\main\java\com\microsoft\examples\bolts\** in a text editor, and uncomment the following lines by removing the `//` from the beginning. Save the file after you make this change.


		topologyBuilder.setBolt("HBase", new HBaseBolt("SensorData", mapper).withConfigKey("hbase.conf"), spoutConfig.getPartitionCount())
    	  .fieldsGrouping("Parser", "hbasestream", new Fields("deviceid")).setNumTasks(spoutConfig.getPartitionCount());

	This enables the HBase bolt.

	> [AZURE.NOTE] You should only enable the HBase bolt when you are deploying to the Storm cluster, not when you are testing locally.


4. Save the __Temperature.java__ file.
    
## Build, package and deploy the solution to HDInsight

In your development environment, use the following steps to deploy the Storm topology to the storm cluster.

1. Use the following command to perform a new build and create a JAR package from your project:

		mvn clean compile package

	This will create a file named **TemperatureMonitor-1.0-SNAPSHOT.jar** in the **target** directory of your project.

2. Use scp to upload the __TemperatureMonitor-1.0-SNAPSHOT.jar__ file to your Storm cluster. In the following example, replace __USERNAME__ with the SSH user you provided when creating the cluster, and __BASENAME__ with the base name you provided earlier. When prompted, enter the password for the SSH user.

        scp target\TemperatureMonitor-1.0-SNAPSHOT.jar USERNAME@storm-BASENAME-ssh.azurehdinsight.cn:
    
    > [AZURE.NOTE] It may take several minutes to upload the file, as it will be several megabytes in size.

3. Once the file has been uploaded, connect to the cluster using SSH.

        ssh USERNAME@storm-BASENAME-ssh.azurehdinsight.cn

4. From the SSH session, use the following command to start the topology.

        storm jar TemperatureMonitor-1.0-SNAPSHOT.jar com.microsoft.examples.Temperature tempmonitor
    
    This starts the topology using the class __com.microsoft.examples.Temperature__ contained in the package, using __tempmonitor__ as the friendly name for this instance of the topology.

3. After the topology has started, open a browser to the website you published on Azure, then use the `node app.js` command to send data to Event Hub. You should see the web dashboard update to display the information.

	![dashboard](./media/hdinsight-storm-sensor-data-analysis/datadashboard.png)

## View HBase data

After you have submitted data to the topology using `node app.js`, use the following steps to connect to HBase and verify that the data has been written to the table you created earlier.

1. Use SSH to connect to the HBase cluster.

        ssh USERNAME@hbase-BASENAME-ssh.azurehdinsight.cn

2. From the SSH session, start the HBase shell.

    	hbase shell
	Once the shell has loaded, you will see an `hbase(main):001:0>` prompt.

2. View rows from the table:



### HBase and Storm data

Before running the topology, you must prepare HBase to accept the data.

1. Use Remote Desktop to connect to the HBase cluster.

2. From the desktop, start the HDInsight command-line and enter the following commands:

    cd %HBASE_HOME%
    	bin\hbase shell

3. From the HBase shell, enter the following command to create a table to store the sensor data:

    create 'SensorData', 'cf'

4. Verify that the table contains no data by entering the following command:


    	scan 'SensorData'

		
	This should return information similar to the following, indicating that there are 0 rows in the table.
		hbase(main):002:0> scan 'SensorData'
        ROW                             COLUMN+CELL
        \x00\x00\x00\x00               column=cf:temperature, timestamp=1467290788277, value=\x00\x00\x00\x04
        \x00\x00\x00\x00               column=cf:timestamp, timestamp=1467290788277, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x01               column=cf:temperature, timestamp=1467290788348, value=\x00\x00\x00M
        \x00\x00\x00\x01               column=cf:timestamp, timestamp=1467290788348, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x02               column=cf:temperature, timestamp=1467290788268, value=\x00\x00\x00R
        \x00\x00\x00\x02               column=cf:timestamp, timestamp=1467290788268, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x03               column=cf:temperature, timestamp=1467290788269, value=\x00\x00\x00#
        \x00\x00\x00\x03               column=cf:timestamp, timestamp=1467290788269, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x04               column=cf:temperature, timestamp=1467290788356, value=\x00\x00\x00>
        \x00\x00\x00\x04               column=cf:timestamp, timestamp=1467290788356, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x05               column=cf:temperature, timestamp=1467290788326, value=\x00\x00\x00\x0D
        \x00\x00\x00\x05               column=cf:timestamp, timestamp=1467290788326, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x06               column=cf:temperature, timestamp=1467290788253, value=\x00\x00\x009
        \x00\x00\x00\x06               column=cf:timestamp, timestamp=1467290788253, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x07               column=cf:temperature, timestamp=1467290788229, value=\x00\x00\x00\x12
        \x00\x00\x00\x07               column=cf:timestamp, timestamp=1467290788229, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x08               column=cf:temperature, timestamp=1467290788336, value=\x00\x00\x00\x16
        \x00\x00\x00\x08               column=cf:timestamp, timestamp=1467290788336, value=2015-02-10T14:43.05.00320Z
        \x00\x00\x00\x09               column=cf:temperature, timestamp=1467290788246, value=\x00\x00\x001
        \x00\x00\x00\x09               column=cf:timestamp, timestamp=1467290788246, value=2015-02-10T14:43.05.00320Z
        10 row(s) in 0.1800 seconds

    > [AZURE.NOTE] This scan operation will only return a maximum of 10 rows from the table.



When you have started the topology on the Storm cluster and processed data, you can use the `scan 'SensorData'` command again to verify that data was inserted into HBase.


## Delete your clusters

[AZURE.INCLUDE [delete-cluster-warning](../../includes/hdinsight-delete-cluster-warning.md)]


To delete the clusters, storage, and web app at one time, delete the resource group that contains them.


## Next steps


You have now learned how to use Storm to read data from Event Hubs, store it into HBase, and send visualize the information on an external dashboard by using Socket.io and D3.js.


You have now learned how to use Storm to read data from Event Hub and display information from Storm on an external dashboard by using SignalR and D3.js. If you used the optional steps, you also learned how to configure HDInsight in a virtual network and how to communicate between a Storm topology and HBase by using the HBase bolt.


* For more examples of Storm topologies with HDinsight, see:

    * [Example topologies for Storm on HDInsight](/documentation/articles/hdinsight-storm-example-topology/)

* For more information about Apache Storm, see the  [Apache Storm](https://storm.incubator.apache.org/) site.

* For more information about HBase on HDInsight, see the [HBase with HDInsight Overview](/documentation/articles/hdinsight-hbase-overview/).

* For more information about Socket.io, see the [socket.io](http://socket.io/) site.

* For more information about D3.js, see [D3.js - Data Driven Documents](http://d3js.org/).

* For information about creating topologies in Java, see [Develop Java topologies for Apache Storm on HDInsight](/documentation/articles/hdinsight-storm-develop-java-topology/).

* For information about creating topologies in .NET, see [Develop C# topologies for Apache Storm on HDInsight using Visual Studio](/documentation/articles/hdinsight-storm-develop-csharp-visual-studio-topology/).


[azure-portal]: https://portal.azure.cn


[azure-portal]: https://manage.windowsazure.cn/

