﻿<properties
    pageTitle="Use Beeline to work with Hive on HDInsight (Hadoop) | Azure"
    description="Learn how to use SSH to connect to a Hadoop cluster in HDInsight, and then interactively submit Hive queries by using Beeline. Beeline is a utility for working with HiveServer2 over JDBC."
    services="hdinsight"
    documentationcenter=""
    author="Blackmist"
    manager="jhubbard"
    editor="cgronlun"
    tags="azure-portal" />
<tags
    ms.assetid="3adfb1ba-8924-4a13-98db-10a67ab24fca"
    ms.service="hdinsight"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="big-data"
    ms.date="10/10/2016"
    wacn.date=""
    ms.author="larryfr" />

# Use Hive with Hadoop in HDInsight with Beeline
[AZURE.INCLUDE [hive-selector](../../includes/hdinsight-selector-use-hive.md)]

In this article, you will learn how to use Secure Shell (SSH) to connect to a Linux-based HDInsight cluster, and then interactively submit Hive queries by using the [Beeline](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients#HiveServer2Clients-Beeline-NewCommandLineShell) command-line tool.

> [AZURE.NOTE]
> Beeline uses JDBC to connect to Hive. For more information on using JDBC with Hive, see [Connect to Hive on Azure HDInsight using the Hive JDBC driver](/documentation/articles/hdinsight-connect-hive-jdbc-driver/).
> 
> 

## <a id="prereq"></a>Prerequisites
To complete the steps in this article, you will need the following:

* A Linux-based Hadoop on HDInsight cluster.
* An SSH client. Linux, Unix, and Mac OS should come with an SSH client. Windows users must download a client, such as [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

## <a id="ssh"></a>Connect with SSH
Connect to the fully qualified domain name (FQDN) of your HDInsight cluster by using the SSH command. The FQDN will be the name you gave the cluster, then **.azurehdinsight.cn**. For example, the following would connect to a cluster named **myhdinsight**:

    ssh admin@myhdinsight-ssh.azurehdinsight.cn

**If you provided a certificate key for SSH authentication** when you created the HDInsight cluster, you may need to specify the location of the private key on your client system:

    ssh admin@myhdinsight-ssh.azurehdinsight.cn -i ~/mykey.key

**If you provided a password for SSH authentication** when you created the HDInsight cluster, you will need to provide the password when prompted.

For more information on using SSH with HDInsight, see [Use SSH with Linux-based Hadoop on HDInsight from Linux, OS X, and Unix](/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix/).

### PuTTY (Windows-based clients)
Windows does not provide a built-in SSH client. We recommend using **PuTTY**, which can be downloaded from [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

For more information on using PuTTY, see [Use SSH with Linux-based Hadoop on HDInsight from Windows ](/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows/).

## <a id="beeline"></a>Use the Beeline command
1. Once connected, use the following to start Beeline:
   
        beeline -u 'jdbc:hive2://localhost:10001/;transportMode=http' -n admin
   
    This will start the Beeline client, and connect to the JDBC url. Here, `localhost` is used since HiveServer2 runs on both head nodes in the cluster, and we're running Beeline directly on the primary headnode.
   
    Once the command completes, you will arrive at a `jdbc:hive2://localhost:10001/>` prompt.
2. Beeline commands usually begin with a `!` character, for example `!help` displays help. However the `!` can often be omitted. For example, `help` will also work.
   
    If you view help, you will notice `!sql`, which is used to execute HiveQL statements. However, HiveQL is so commonly used that you can omit the preceding `!sql`. The following two statements have exactly the same results; displaying the tables currently available through Hive:
   
        !sql show tables;
        show tables;
   
    On a new cluster, only one table should be listed: **hivesampletable**.
3. Use the following to display the schema for the hivesampletable:
   
        describe hivesampletable;
   
    This will return the following information:
   
        +-----------------------+------------+----------+--+
        |       col_name        | data_type  | comment  |
        +-----------------------+------------+----------+--+
        | clientid              | string     |          |
        | querytime             | string     |          |
        | market                | string     |          |
        | deviceplatform        | string     |          |
        | devicemake            | string     |          |
        | devicemodel           | string     |          |
        | state                 | string     |          |
        | country               | string     |          |
        | querydwelltime        | double     |          |
        | sessionid             | bigint     |          |
        | sessionpagevieworder  | bigint     |          |
        +-----------------------+------------+----------+--+
   
    This displays the columns in the table. While we could perform some queries against this data, let's instead create a brand new table to demonstrate how to load data into Hive and apply a schema.
4. Enter the following statements to create a new table named **log4jLogs** by using sample data provided with the HDInsight cluster:
   
        DROP TABLE log4jLogs;
        CREATE EXTERNAL TABLE log4jLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string)
        ROW FORMAT DELIMITED FIELDS TERMINATED BY ' '
        STORED AS TEXTFILE LOCATION 'wasbs:///example/data/';
        SELECT t4 AS sev, COUNT(*) AS count FROM log4jLogs WHERE t4 = '[ERROR]' AND INPUT__FILE__NAME LIKE '%.log' GROUP BY t4;
   
    These statements perform the following actions:
   
   * **DROP TABLE** - Deletes the table and the data file, in case the table already exists.
   * **CREATE EXTERNAL TABLE** - Creates a new 'external' table in Hive. External tables only store the table definition in Hive. The data is left in the original location.
   * **ROW FORMAT** - Tells Hive how the data is formatted. In this case, the fields in each log are separated by a space.
   * **STORED AS TEXTFILE LOCATION** - Tells Hive where the data is stored (the example/data directory), and that it is stored as text.
   * **SELECT** - Selects a count of all rows where column **t4** contains the value **[ERROR]**. This should return a value of **3** as there are three rows that contain this value.
   * **INPUT__FILE__NAME LIKE '%.log'** - Tells Hive that we should only return data from files ending in .log. Normally, you would only have data with the same schema within the same folder when querying with hive, however this example log file is stored with other data formats.
     
     > [AZURE.NOTE]
     > External tables should be used when you expect the underlying data to be updated by an external source, such as an automated data upload process, or by another MapReduce operation, but always want Hive queries to use the latest data.
     > 
     > Dropping an external table does **not** delete the data, only the table definition.
     > 
     > 
     
     The output of this command should be similar to the following:

     ```
     INFO  : Tez session hasn't been created yet. Opening session
     INFO  :
     
     INFO  : Status: Running (Executing on YARN cluster with App id application_1443698635933_0001)
     
     INFO  : Map 1: -/-      Reducer 2: 0/1
     INFO  : Map 1: 0/1      Reducer 2: 0/1
     INFO  : Map 1: 0/1      Reducer 2: 0/1
     INFO  : Map 1: 0/1      Reducer 2: 0/1
     INFO  : Map 1: 0/1      Reducer 2: 0/1
     INFO  : Map 1: 0(+1)/1  Reducer 2: 0/1
     INFO  : Map 1: 0(+1)/1  Reducer 2: 0/1
     INFO  : Map 1: 1/1      Reducer 2: 0/1
     INFO  : Map 1: 1/1      Reducer 2: 0(+1)/1
     INFO  : Map 1: 1/1      Reducer 2: 1/1
     +----------+--------+--+
     |   sev    | count  |
     +----------+--------+--+
     | [ERROR]  | 3      |
     +----------+--------+--+
     1 row selected (47.351 seconds)
     ```
5. To exit Beeline, use `!quit`.

## <a id="file"></a>Run a HiveQL file
Beeline can also be used to run a file that contains HiveQL statements. Use the following steps to create a file, then run it using Beeline.

1. Use the following command to create a new file named **query.hql**:
   
        nano query.hql
2. Once the editor opens, use the following as the contents of the file. This query will create a new 'internal' table named **errorLogs**:
   
        CREATE TABLE IF NOT EXISTS errorLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) STORED AS ORC;
        INSERT OVERWRITE TABLE errorLogs SELECT t1, t2, t3, t4, t5, t6, t7 FROM log4jLogs WHERE t4 = '[ERROR]' AND INPUT__FILE__NAME LIKE '%.log';
   
    These statements perform the following actions:
   
   * **CREATE TABLE IF NOT EXISTS** - Creates a table, if it does not already exist. Since the **EXTERNAL** keyword is not used, this is an internal table, which is stored in the Hive data warehouse and is managed completely by Hive.
   * **STORED AS ORC** - Stores the data in Optimized Row Columnar (ORC) format. This is a highly optimized and efficient format for storing Hive data.
   * **INSERT OVERWRITE ... SELECT** - Selects rows from the **log4jLogs** table that contain **[ERROR]**, then inserts the data into the **errorLogs** table.
     
     > [AZURE.NOTE]
     > Unlike external tables, dropping an internal table will delete the underlying data as well.
     > 
     > 
3. To save the file, use **Ctrl**+**_X**, then enter **Y**, and finally **Enter**.
4. Use the following to run the file using Beeline. Replace **HOSTNAME** with the name obtained earlier for the head node, and **PASSWORD** with the password for the admin account:
   
        beeline -u 'jdbc:hive2://localhost:10001/;transportMode=http' -n admin -i query.hql
   
   > [AZURE.NOTE]
   > The `-i` parameter starts Beeline, runs the statements in the query.hql file, and remains in Beeline at the `jdbc:hive2://localhost:10001/>` prompt. You can also run a file using the `-f` parameter, which returns you to Bash after the file has been processed.
   > 
   > 
5. To verify that the **errorLogs** table was created, use the following statement to return all the rows from **errorLogs**:
   
        SELECT * from errorLogs;
   
    Three rows of data should be returned, all containing **[ERROR]** in column t4:
   
        +---------------+---------------+---------------+---------------+---------------+---------------+---------------+--+
        | errorlogs.t1  | errorlogs.t2  | errorlogs.t3  | errorlogs.t4  | errorlogs.t5  | errorlogs.t6  | errorlogs.t7  |
        +---------------+---------------+---------------+---------------+---------------+---------------+---------------+--+
        | 2012-02-03    | 18:35:34      | SampleClass0  | [ERROR]       | incorrect     | id            |               |
        | 2012-02-03    | 18:55:54      | SampleClass1  | [ERROR]       | incorrect     | id            |               |
        | 2012-02-03    | 19:25:27      | SampleClass4  | [ERROR]       | incorrect     | id            |               |
        +---------------+---------------+---------------+---------------+---------------+---------------+---------------+--+
        3 rows selected (1.538 seconds)

## More about Beeline connectivity
The steps in this document use `localhost` to connect to HiveServer2 running on the cluster headnode. While you can also use the hostname or the fully qualified domain name of the headnode those require additional steps to the process (steps to find the hostname or FQDN). Using `localhost` is sufficient when using Beeline from the headnode.

If you have an edge node in your cluster, with Beeline installed, you will need to use the hostname or FQDN of the headnode to connect.

If you have Beeline installed on a client outside of your cluster, you can connect using the following command. Replace **CLUSTERNAME** with the name of your HDInsight cluster. Replace **PASSWORD** with the password for the admin (HTTP login) account.

    beeline -u 'jdbc:hive2://CLUSTERNAME.azurehdinsight.cn:443/default;ssl=true?hive.server2.transport.mode=http;hive.server2.thrift.http.path=hive2' -n admin -p PASSWORD

Note that the parameters/URI is different than when running directly on a headnode or from an edge node within the cluster. This is because connecting to the cluster from the internet uses a public gateway that routes traffic over port 443. Also, several other services are exposed through the public gateway on port 443, so the URI is different than when connecting directly. When connecting from the internet you must also authenticate the session by providing the password.

## <a id="summary"></a><a id="nextsteps"></a>Next steps
As you can see, the Beeline command provides an easy way to interactively run Hive queries on an HDInsight cluster.

For general information on Hive in HDInsight:

* [Use Hive with Hadoop on HDInsight](/documentation/articles/hdinsight-use-hive/)

For information on other ways you can work with Hadoop on HDInsight:

* [Use Pig with Hadoop on HDInsight](/documentation/articles/hdinsight-use-pig/)
* [Use MapReduce with Hadoop on HDInsight](/documentation/articles/hdinsight-use-mapreduce/)

If you are using Tez with Hive, see the following documents for debugging information:

* [Use the Tez UI on Windows-based HDInsight](/documentation/articles/hdinsight-debug-tez-ui/)
* [Use the Ambari Tez view on Linux-based HDInsight](/documentation/articles/hdinsight-debug-ambari-tez-view/)

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

[putty]: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html


[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters-v1/
[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically/
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data/


[powershell-here-strings]: http://technet.microsoft.com/zh-cn/library/ee692792.aspx

