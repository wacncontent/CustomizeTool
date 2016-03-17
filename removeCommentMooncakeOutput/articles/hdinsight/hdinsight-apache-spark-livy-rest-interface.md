<!-- not suitable for Mooncake -->

<properties 
	pageTitle="Submit Spark jobs remotely using Livy | Azure" 
	description="Learn how to use Livy with HDInsight clusters to submit Spark jobs remotely." 
	services="hdinsight" 
	documentationCenter="" 
	authors="nitinme" 
	manager="paulettm" 
	editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="02/05/2016"
	wacn.date=""/>


# Submit Spark jobs remotely using Livy with Spark clusters on HDInsight (Linux)

Apache Spark cluster on Azure HDInsight includes Livy, a REST interface for submitting jobs remotely to a Spark cluster from anywhere. For detailed documentation, see [Livy](https://github.com/cloudera/hue/tree/master/apps/spark/java#welcome-to-livy-the-rest-spark-server).

You can use Livy to run interactive Spark shells or submit batch jobs to be run on Spark. This article talks about using Livy to submit batch jobs. The syntax below uses Curl to make REST calls to the Livy endpoint.

**Prerequisites:**

You must have the following:

- An Azure subscription. See [Get Azure trial](/pricing/1rmb-trial/).
- An Apache Spark cluster on HDInsight Linux. For instructions, see [Create Apache Spark clusters in Azure HDInsight](/documentation/articles/hdinsight-apache-spark-jupyter-spark-sql).

## Submit a batch job the cluster

Before you submit a batch job, you must upload the application jar on the cluster storage associated with the cluster. You can use [**AzCopy**](/documentation/articles/storage-use-azcopy), a command line utility, to do so. There are a lot of other clients you can use to upload data. You can find more about them at [Upload data for Hadoop jobs in HDInsight](/documentation/articles/hdinsight-upload-data).

	curl -k --user "<hdinsight user>:<user password>" -v -H <content-type> -X POST -d '{ "file":"<path to application jar>", "className":"<classname in jar>" }' 'https://<spark_cluster_name>.azurehdinsight.cn/livy/batches'

**Examples**:

* If the jar file is on the cluster storage (WASB)

		curl -k --user "admin:mypassword1!" -v -H 'Content-Type: application/json' -X POST -d '{ "file":"wasb://mycontainer@mystorageaccount.blob.core.chinacloudapi.cn/data/SparkSimpleTest.jar", "className":"com.microsoft.spark.test.SimpleFile" }' "https://mysparkcluster.azurehdinsight.cn/livy/batches"

* If the you want to pass the jar filename and the classname as part of an input file (in this example, input.txt)
		
		curl -k  --user "admin:mypassword1!" -v -H "Content-Type: application/json" -X POST --data @C:\Temp\input.txt "https://mysparkcluster.azurehdinsight.cn/livy/batches"

## Get information on batches running on the cluster

	curl -k --user "<hdinsight user>:<user password>" -v -X GET "https://<spark_cluster_name>.azurehdinsight.cn/livy/batches"

**Examples**:

* If you want to retrieve all the batches running on the cluster:

		curl -k --user "admin:mypassword1!" -v -X GET "https://mysparkcluster.azurehdinsight.cn/livy/batches"

* If you want to retrieve a specific batch with a given batchId

		curl -k --user "admin:mypassword1!" -v -X GET "https://mysparkcluster.azurehdinsight.cn/livy/batches/{batchId}"


## Delete a batch job

	curl -k --user "<hdinsight user>:<user password>" -v -X DELETE "https://<spark_cluster_name>.azurehdinsight.cn/livy/batches/{batchId}"

**Example**:

	curl -k --user "admin:mypassword1!" -v -X DELETE "https://mysparkcluster.azurehdinsight.cn/livy/batches/{batchId}"

## Show me an example

In this section, we look at examples on how to use Livy to submit a Spark application, monitor the progress of the application, and then delete the job. The application we use in this example is the one developed in the article [Create a standalone Scala application and to run on HDInsight Spark cluster](/documentation/articles/hdinsight-apache-spark-create-standalone-application). The steps below assume the following:

* You have already copied over the application jar to the storage account associated with the cluster.
* You have CuRL installed on the computer where you are trying these steps.

Perform the following steps.

1. Let us first verify that Livy is running on the cluster. We can do so by getting a list of running batches. If this is the first time you are running a job using Livy, this should return zero.

		curl -k --user "admin:mypassword1!" -v -X GET "https://mysparkcluster.azurehdinsight.cn/livy/batches"

	You should get an output similar to the following:

		< HTTP/1.1 200 OK
		< Content-Type: application/json; charset=UTF-8
		< Server: Microsoft-IIS/8.5
		< X-Powered-By: ARR/2.5
		< X-Powered-By: ASP.NET
		< Date: Fri, 20 Nov 2015 23:47:53 GMT
		< Content-Length: 34
		<
		{"from":0,"total":0,"sessions":[]}* Connection #0 to host mysparkcluster.azurehdinsight.cn left intact

	Notice how the last line in the output says **total:0**, which suggests no running batches.

2. Let us now submit a batch job. The snippet below uses an input file (input.txt) to pass the jar name and the class name as parameters. This is the recommended approach if you are running these steps from a Windows computer.

		curl -k --user "admin:mypassword1!" -v -H "Content-Type: application/json" -X POST --data @C:\Temp\input.txt "https://mysparkcluster.azurehdinsight.cn/livy/batches"

	The parameters in the file **input.txt** are defined as follows:

		{ "file":"wasb:///example/jars/SparkSimpleApp.jar", "className":"com.microsoft.spark.example.WasbIOTest" }

	You should see an output similar to the following:

		< HTTP/1.1 201 Created
		< Content-Type: application/json; charset=UTF-8
		< Location: /0
		< Server: Microsoft-IIS/8.5
		< X-Powered-By: ARR/2.5
		< X-Powered-By: ASP.NET
		< Date: Fri, 20 Nov 2015 23:51:30 GMT
		< Content-Length: 36
		<
		{"id":0,"state":"starting","log":[]}* Connection #0 to host mysparkcluster.azurehdinsight.cn left intact

	Notice how the last line of the output says **state:starting**. It also says, **id:0**. This is the batch ID.

3. You can now retrieve the the status of this specific batch using the batch ID.

		curl -k --user "admin:mypassword1!" -v -X GET "https://mysparkcluster.azurehdinsight.cn/livy/batches/0"

	You should see an output similar to the following:

		< HTTP/1.1 200 OK
		< Content-Type: application/json; charset=UTF-8
		< Server: Microsoft-IIS/8.5
		< X-Powered-By: ARR/2.5
		< X-Powered-By: ASP.NET
		< Date: Fri, 20 Nov 2015 23:54:42 GMT
		< Content-Length: 509
		<
		{"id":0,"state":"success","log":["\t diagnostics: N/A","\t ApplicationMaster host: 10.0.0.4","\t ApplicationMaster RPC port: 0","\t queue: default","\t start time: 1448063505350","\t final status: SUCCEEDED","\t tracking URL: http://hn0-myspar.lpel1gnnvxne3gwzqkfq5u5uzh.jx.internal.chinacloudapp.cn:8088/proxy/application_1447984474852_0002/","\t user: root","15/11/20 23:52:47 INFO Utils: Shutdown hook called","15/11/20 23:52:47 INFO Utils: Deleting directory /tmp/spark-b72cd2bf-280b-4c57-8ceb-9e3e69ac7d0c"]}* Connection #0 to host mysparkcluster.azurehdinsight.cn left intact

	The output now shows **state:success**, which suggests that the job was successfully completed.

4. If you want, you can now delete the batch. 

		curl -k --user "admin:mypassword1!" -v -X DELETE "https://mysparkcluster.azurehdinsight.cn/livy/batches/0"

	You should see an output similar to the following:

		< HTTP/1.1 200 OK
		< Content-Type: application/json; charset=UTF-8
		< Server: Microsoft-IIS/8.5
		< X-Powered-By: ARR/2.5
		< X-Powered-By: ASP.NET
		< Date: Sat, 21 Nov 2015 18:51:54 GMT
		< Content-Length: 17
		<
		{"msg":"deleted"}* Connection #0 to host mysparkcluster.azurehdinsight.cn left intact

	The last line of the output shows that the batch was successfully deleted. If you delete a job while it is running, it will essentially kill the job. If you delete a job that has completed, successfully or otherwise, it deletes the job information completely.

## <a name="seealso"></a>See also


* [Overview: Apache Spark on Azure HDInsight](/documentation/articles/hdinsight-apache-spark-overview)

### Scenarios

* [Spark with BI: Perform interactive data analysis using Spark in HDInsight with BI tools](/documentation/articles/hdinsight-apache-spark-use-bi-tools)

* [Spark with Machine Learning: Use Spark in HDInsight for analyzing building temperature using HVAC data](/documentation/articles/hdinsight-apache-spark-ipython-notebook-machine-learning)

* [Spark with Machine Learning: Use Spark in HDInsight to predict food inspection results](/documentation/articles/hdinsight-apache-spark-machine-learning-mllib-ipython)

* [Spark Streaming: Use Spark in HDInsight for building real-time streaming applications](/documentation/articles/hdinsight-apache-spark-eventhub-streaming)

* [Website log analysis using Spark in HDInsight](/documentation/articles/hdinsight-apache-spark-custom-library-website-log-analysis)

### Create and run applications

* [Create a standalone application using Scala](/documentation/articles/hdinsight-apache-spark-create-standalone-application)

### Tools and extensions

* [Use HDInsight Tools Plugin for IntelliJ IDEA to create and submit Spark Scala applicatons](/documentation/articles/hdinsight-apache-spark-intellij-tool-plugin)

* [Use Zeppelin notebooks with a Spark cluster on HDInsight](/documentation/articles/hdinsight-apache-spark-use-zeppelin-notebook)

* [Kernels available for Jupyter notebook in Spark cluster for HDInsight](/documentation/articles/hdinsight-apache-spark-jupyter-notebook-kernels)

### Manage resources

* [Manage resources for the Apache Spark cluster in Azure HDInsight](/documentation/articles/hdinsight-apache-spark-resource-manager)