<properties
    pageTitle="Use Hadoop Hive on the Query Console in HDInsight | Azure"
    description="Learn how to use the web-based Query Console to run Hive queries on an HDInsight Hadoop cluster from your browser."
    services="hdinsight"
    documentationcenter=""
    author="Blackmist"
    manager="jhubbard"
    editor="cgronlun"
    tags="azure-portal" />
<tags
    ms.assetid="5ae074b0-f55e-472d-94a7-005b0e79f779"
    ms.service="hdinsight"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="big-data"
    ms.date="09/20/2016"
    wacn.date=""
    ms.author="larryfr" />

# Run Hive queries using the Query Console
[AZURE.INCLUDE [hive-selector](../../includes/hdinsight-selector-use-hive.md)]

In this article, you will learn how to use the HDInsight Query Console to run Hive queries on an HDInsight Hadoop cluster from your browser.

> [AZURE.NOTE] The Query Console is only available on Windows-based HDInsight clusters.


## <a id="prereq"></a>Prerequisites
To complete the steps in this article, you will need the following.

* A Windows-based HDInsight Hadoop cluster
* A modern web browser

## <a id="run"></a> Run Hive queries using the Query Console
1. Open the <a href="https://manage.windowsazure.cn" target="_blank">Azure Classic Management Portal</a> and select your HDInsight cluster. From the bottom of the page, select **Query Console**. When prompted, enter the username and password that you used when you created the cluster.
2. From the links at the top of the page, select **Hive Editor**. This displays a form that can be used to enter the HiveQL statements that you want to run in the HDInsight cluster.
   
    ![the hive editor](./media/hdinsight-hadoop-use-hive-query-console/queryconsole.png)
   
    Replace the text `Select * from hivesampletable` with the following HiveQL statements:
   
        set hive.execution.engine=tez;
        DROP TABLE log4jLogs;
        CREATE EXTERNAL TABLE log4jLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string)
        ROW FORMAT DELIMITED FIELDS TERMINATED BY ' '
        STORED AS TEXTFILE LOCATION 'wasbs:///example/data/';
        SELECT t4 AS sev, COUNT(*) AS count FROM log4jLogs WHERE t4 = '[ERROR]' AND INPUT__FILE__NAME LIKE '%.log' GROUP BY t4;
   
    These statements perform the following actions:
   
   * **DROP TABLE**: Deletes the table and the data file if the table already exists.
   * **CREATE EXTERNAL TABLE**: Creates a new 'external' table in Hive. External tables store only the table definition in Hive; the data is left in the original location.
     
     > [AZURE.NOTE]
     > External tables should be used when you expect the underlying data to be updated by an external source (such as an automated data upload process) or by another MapReduce operation, but you always want Hive queries to use the latest data.
     ><p> 
     > Dropping an external table does **not** delete the data, only the table definition.
     > 
     > 
   * **ROW FORMAT**: Tells Hive how the data is formatted. In this case, the fields in each log are separated by a space.
   * **STORED AS TEXTFILE LOCATION**: Tells Hive where the data is stored (the example/data directory) and that it is stored as text
   * **SELECT**: Select a count of all rows where column **t4** contain the value **[ERROR]**. This should return a value of **3** because there are three rows that contain this value.
   * **INPUT__FILE__NAME LIKE '%.log'** - Tells Hive that we should only return data from files ending in .log. This restricts the search to the sample.log file that contains the data, and keeps it from returning data from other example data files that do not match the schema we defined.
3. Click **Submit**. The **Job Session** at the bottom of the page should display details for the job.
4. When the **Status** field changes to **Completed**, select **View Details** for the job. On the details page, the **Job Output** contains `[ERROR]    3`. You can use the **Download** button under this field to download a file that contains the output of the job.

## <a id="summary"></a>Summary
As you can see, the Query Console provides an easy way to run Hive queries in an HDInsight cluster, monitor the job status, and retrieve the output.

To learn more about using Hive Query Console to run Hive jobs, select **Getting Started** at the top of the Query Console, then use the samples that are provided. Each sample walks through the process of using Hive to analyze data, including explanations about the HiveQL statements used in the sample.

## <a id="nextsteps"></a>Next steps
For general information about Hive in HDInsight:

* [Use Hive with Hadoop on HDInsight](/documentation/articles/hdinsight-use-hive/)

For information about other ways you can work with Hadoop on HDInsight:

* [Use Pig with Hadoop on HDInsight](/documentation/articles/hdinsight-use-pig/)
* [Use MapReduce with Hadoop on HDInsight](/documentation/articles/hdinsight-use-mapreduce/)

If you are using Tez with Hive, see the following documents for debugging information:

* [Use the Tez UI on Windows-based HDInsight](/documentation/articles/hdinsight-debug-tez-ui/)

[1]: /documentation/articles/hdinsight-hadoop-visual-studio-tools-get-started/

[hdinsight-sdk-documentation]: http://msdn.microsoft.com/zh-cn/library/dn479185.aspx

[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: /pricing/member-offers/
[azure-trial]: /pricing/1rmb-trial/

[apache-tez]: http://tez.apache.org
[apache-hive]: http://hive.apache.org/
[apache-log4j]: http://zh.wikipedia.org/wiki/Log4j
[hive-on-tez-wiki]: https://cwiki.apache.org/confluence/display/Hive/Hive+on+Tez
[import-to-excel]: /documentation/articles/hdinsight-connect-excel-power-query/


[hdinsight-use-oozie]: /documentation/articles/hdinsight-use-oozie/
[hdinsight-analyze-flight-data]: /documentation/articles/hdinsight-analyze-flight-delay-data/



[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage/

[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters-v1/
[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically/
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data/
[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1/

[Powershell-install-configure]: /documentation/articles/powershell-install-configure/
[powershell-here-strings]: http://technet.microsoft.com/zh-cn/library/ee692792.aspx


[img-hdi-hive-powershell-output]: ./media/hdinsight-use-hive/HDI.Hive.PowerShell.Output.png
