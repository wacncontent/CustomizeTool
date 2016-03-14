<!-- not suitable for Mooncake -->

<properties
   pageTitle="Learn Hadoop in HDInsight with the Sample Gallery | Windows Azure"
   description="Quickly learn Hadoop by running sample applications from the HDInsight Getting Started Gallery. Use sample data or supply your own."
   services="hdinsight"
   documentationCenter=""
   tags="azure-portal"
   authors="mumian"
   manager="paulettm"
   editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="02/04/2016"
	wacn.date=""/>

# Learn Hadoop by using the Azure HDInsight Getting Started Gallery

The HDInsight Getting Started Gallery provides an easy and quick way learn Hadoop by running sample applications in HDInsight. Some of the samples come with sample data. You can supply your own data for the remaining samples. Currently, there are the following six samples (with more coming):

- Solutions with your Azure data
	- Windows Azure website log analysis
	- Windows Azure storage analytics
- Solutions with sample data
	- Sensor data analysis
	- Website log analysis
	- Mahout movie recommendation

![HDInsight Hadoop, Storm, and HBase Getting Started Gallery solutions including sample data.][hdinsight.sample.gallery]

The Dashboard can be accessed by browsing to http://<YourHDInsightClusterName>.azurehdinsight.cn/ or from the Azure Management Portal.

**To run a sample from the Getting Started Gallery**

1.	Sign in to the [Azure Management Portal][azure.portal].
2.	Click **HDInsight** in the left menu. You will see a list of existing HDInsight clusters, including Hadoop, Storm, and HBase clusters. 
3.	Click the cluster where you want to run the sample.
4.	Click **QUERY CONSOLE** at the bottom of the page.
5.	Enter the Hadoop user name and password for the cluster.
6.	Click **Getting Started Gallery** at the top of the page.

## Next steps
Other ways to learn about HDInsight include:

- [HDInsight infographic][hdinsight.infographic]

<!--Image references-->
[hdinsight.sample.gallery]: ./media/hdinsight-learn-hadoop-use-sample-gallery/HDInsight-Getting-Started-Gallery.png
[hdinsight.twitter.sample]: ./media/hdinsight-learn-hadoop-use-sample-gallery/HDInsight-Twitter-Trend-Analysis-sample.png

<!--Link references-->
[hdinsight.learn.map]: /documentation/articles/hdinsight-learn-map
[hdinsight.infographic]: http://go.microsoft.com/fwlink/?linkid=523960
[azure.portal]:https://manage.windowsazure.cn
