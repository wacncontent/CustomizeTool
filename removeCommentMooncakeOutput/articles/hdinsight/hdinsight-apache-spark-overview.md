<!-- not suitable for Mooncake -->

<properties 
	pageTitle="An overview of Apache Spark in HDInsight | Azure" 
	description="An introduction to Apache Spark in HDInsight and scenarios in which to use Spark on HDInsight in your applications." 
	services="hdinsight" 
	documentationCenter="" 
	authors="nitinme" 
	manager="paulettm" 
	editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="06/06/2016"
	wacn.date=""/>

# Overview: Apache Spark on HDInsight Linux
 
<a href="http://spark.apache.org/" target="_blank">Apache Spark</a> is an open-source parallel processing framework that supports in-memory processing to boost the performance of big-data analytic applications. Spark processing engine is built for speed, ease of use, and sophisticated analytics. Spark's in-memory computation capabilities make it a good choice for iterative algorithms in machine learning and graph computations. Spark is also compatible with Azure Blob storage (WASB) so your existing data stored in Azure can easily be processed via Spark.

When you create a Spark cluster in HDInsight, you create Azure compute resources with Spark installed and configured. It only takes about ten minutes to create a Spark cluster in HDInsight. The data to be processed is stored in Azure Blob storage. See [Use Azure Blob Storage with HDInsight][hdinsight-storage].

![Apache Spark on Azure HDInsight](./media/hdinsight-apache-spark-overview/hdispark.architecture.png  "Apache Spark on Azure HDInsight")


**Want to get started with Apache Spark on Azure HDInsight?** See [QuickStart: create a Spark cluster on HDInsight Linux and run sample applications using Jupyter](/documentation/articles/hdinsight-apache-spark-jupyter-spark-sql/).

>[AZURE.NOTE] For a list of known issues and limitations with the current release, see [Known issues of Apache Spark in Azure HDInsight (Linux)](/documentation/articles/hdinsight-apache-spark-jupyter-spark-sql/).


## Why use Spark on Azure HDInsight? 

Azure HDInsight offers a fully managed Spark service. Benefits of using Spark on HDInsight are:

| Feature                             | Description       |
|-------------------------------------|-------------------|
| Ease of creating clusters            | You can create a new Spark cluster on HDInsight in minutes using the Azure Management Portal, Azure PowerShell, or the HDInsight .NET SDK. See [Get started with Spark cluster in HDInsight](/documentation/articles/hdinsight-apache-spark-jupyter-spark-sql/) |
| Ease of use                     | Spark in HDInsight clusters includes Jupyter notebooks pre-configured. You can use these for interactive data processing and visualization. The URLs for the is https://CLUSTERNAME.azurehdinsight.cn/jupyter. Replace __CLUSTERNAME__ with the name of your Spark HDInsight cluster.|
| REST APIs                       | Spark in HDInsight includes [Livy](https://github.com/cloudera/hue/tree/master/apps/spark/java#welcome-to-livy-the-rest-spark-server), a REST-API based Spark job server to remotely submit and monitor running jobs. |
| Support for Azure Data Lake Store | Spark on HDInsight can be configured to use Azure Data Lake Store as an additional storage. For more information on Data Lake Store, see [Overview of Azure Data Lake Store](/documentation/articles/data-lake-store-overview/).
| Integration with Azure services | Spark on HDInsight comes with a connector to Azure Event Hubs. Customers can build streaming applications using the Event Hubs, in addition to [Kafka](http://kafka.apache.org/), which is already available as part of Spark. |
| Support for R Server  | You can set up a R Server on HDInsight Spark cluster to run distributed R computations with the speeds promised with a Spark cluster. For more information, see [Get started using R Server on HDInsight](/documentation/articles/hdinsight-hadoop-r-server-get-started/).   |
| Integration with IntelliJ IDEA  | You can use the HDInsight Plugin for IntelliJ to create and submit applications to an HDInsight Spark cluster. For more information see [Use HDInsight Tools Plugin for IntelliJ IDEA to create Spark applications for HDInsight Spark Linux cluster](/documentation/articles/hdinsight-apache-spark-intellij-tool-plugin/). |
| Concurrent Queries              | Spark in HDInsight supports concurrent queries. This enables multiple queries from one user or multiple queries from various users and applications to share the same cluster resources. |
| Caching on SSDs                 | You can choose to cache data either in memory or in SSDs attached to the cluster nodes. Caching in memory provides the best query performance but could be expensive; caching in SSDs provides a great option for improving query performance without the need to create a cluster of a size that is required to fit the entire dataset in memory.|
| Integration with BI Tools       | Spark for HDInsight provides connectors for  BI tools such as [Power BI](http://www.powerbi.com/) and [Tableau](http://www.tableau.com/products/desktop) for data analytics.|
| Pre-loaded Anaconda libraries        | Spark clusters on HDInsight come with Anaconda libraries pre-installed. [Anaconda](http://docs.continuum.io/anaconda/) provides close to 200 libraries for machine learning, data analysis, visualization, etc.|
| Scalability                     | Although you can specify the number of nodes in your cluster during creation, you may want to grow or shrink the cluster to match workload. All HDInsight clusters allow you to change the number of nodes in the cluster. Also, Spark clusters can be dropped with no loss of data since all the data is stored in Azure Blob Storage. |
| 24/7 Support					  | Spark on HDInsight comes with  enterprise-level 24/7 support and an SLA of 99.9% up-time.|



## What are the use cases for Spark on HDInsight?

Apache Spark in HDInsight enables the following key scenarios.

### Interactive data analysis and BI

[Look at a tutorial](/documentation/articles/hdinsight-apache-spark-use-bi-tools/)

Apache Spark in HDInsight stores data in Azure Blobs. Business experts and key decision makers can analyze and build reports over that data and use Microsoft Power BI to build interactive reports from the analyzed data. Analysts can start from unstructured/semi structured data in Azure storage, define a schema for the data using notebooks and then build data models using Microsoft Power BI. Spark in HDInsight also supports a number of third party BI tools such as Tableau, Qlikview, and SAP Lumira making it an ideal platform for data analysts, business experts, and key decision makers.

### Iterative Machine Learning

[Look at a tutorial: Predict building temperatures uisng HVAC data](/documentation/articles/hdinsight-apache-spark-ipython-notebook-machine-learning/)

[Look at a tutorial: Predict food inspection results](/documentation/articles/hdinsight-apache-spark-machine-learning-mllib-ipython/)

Apache Spark comes with [MLlib](http://spark.apache.org/mllib/), a machine learning library built on top of Spark. In addition to this, Spark on HDInsight also includes Anaconda, a Python distribution with a variety of packages for machine learning. Couple this with a built-in support for Jupyter notebooks, and you have a top-of-the-line environment for creating machine learning applications.  

### Streaming and real-time data analysis

[Look at a tutorial](/documentation/articles/hdinsight-apache-spark-eventhub-streaming/)

Real-time data analysis is used for scenarios ranging from reducing time to data insight by processing data as it lands, to building a true streaming solution. Spark in HDInsight offers a rich support for building real-time analytics solutions. While Spark already has connectors to ingest data from many sources like Kafka, Flume, Twitter, ZeroMQ, or TCP sockets, Spark in HDInsight adds first-class support for ingesting data from Azure Event Hubs. Event Hubs are the most widely used queuing service on Azure. Having an out-of-the-box support for Event Hubs makes Spark in HDInsight an ideal platform for building real time analytics pipeline.

##<a name="next-steps"></a>What components are included as part of a Spark cluster?

Spark in HDInsight includes the following components that are available on the clusters by default.

- [Spark Core](https://spark.apache.org/docs/1.5.1/). Includes Spark Core, Spark SQL, Spark streaming APIs, GraphX, and MLlib.
- [Anaconda](http://docs.continuum.io/anaconda/)
- [Livy](https://github.com/cloudera/hue/tree/master/apps/spark/java#welcome-to-livy-the-rest-spark-server)
- [Jupyter Notebook](https://jupyter.org)

Spark in HDInsight also provides an [ODBC driver](http://go.microsoft.com/fwlink/?LinkId=616229) for connectivity to Spark clusters in HDInsight from BI tools such as Microsoft Power BI and Tableau.

## Where do I start?

Start with creating a Spark cluster on HDInsight Linux. See [QuickStart: create a Spark cluster on HDInsight Linux and run sample applications using Jupyter](/documentation/articles/hdinsight-apache-spark-jupyter-spark-sql/). 

## Next Steps

### Scenarios

* [Spark with BI: Perform interactive data analysis using Spark in HDInsight with BI tools](/documentation/articles/hdinsight-apache-spark-use-bi-tools/)

* [Spark with Machine Learning: Use Spark in HDInsight for analyzing building temperature using HVAC data](/documentation/articles/hdinsight-apache-spark-ipython-notebook-machine-learning/)

* [Spark with Machine Learning: Use Spark in HDInsight to predict food inspection results](/documentation/articles/hdinsight-apache-spark-machine-learning-mllib-ipython/)

* [Spark Streaming: Use Spark in HDInsight for building real-time streaming applications](/documentation/articles/hdinsight-apache-spark-eventhub-streaming/)

* [Website log analysis using Spark in HDInsight](/documentation/articles/hdinsight-apache-spark-custom-library-website-log-analysis/)

### Create and run applications

* [Create a standalone application using Scala](/documentation/articles/hdinsight-apache-spark-create-standalone-application/)

* [Run jobs remotely on a Spark cluster using Livy](/documentation/articles/hdinsight-apache-spark-livy-rest-interface/)

### Tools and extensions

* [Use HDInsight Tools Plugin for IntelliJ IDEA to create and submit Spark Scala applicatons](/documentation/articles/hdinsight-apache-spark-intellij-tool-plugin/)

* [Use HDInsight Tools Plugin for IntelliJ IDEA to debug Spark applications remotely](/documentation/articles/hdinsight-apache-spark-intellij-tool-plugin-debug-jobs-remotely/)

* [Use Zeppelin notebooks with a Spark cluster on HDInsight](/documentation/articles/hdinsight-apache-spark-use-zeppelin-notebook/)

* [Kernels available for Jupyter notebook in Spark cluster for HDInsight](/documentation/articles/hdinsight-apache-spark-jupyter-notebook-kernels/)

* [Use external packages with Jupyter notebooks](/documentation/articles/hdinsight-apache-spark-jupyter-notebook-use-external-packages/)

* [Install Jupyter on your computer and connect to an HDInsight Spark cluster](/documentation/articles/hdinsight-apache-spark-jupyter-notebook-install-locally/)

### Manage resources

* [Manage resources for the Apache Spark cluster in Azure HDInsight](/documentation/articles/hdinsight-apache-spark-resource-manager/)

* [Track and debug jobs running on an Apache Spark cluster in HDInsight](/documentation/articles/hdinsight-apache-spark-job-debugging/)


[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage/
