<properties
   pageTitle="Use MapReduce and PowerShell with Hadoop | Windows Azure"
   description="Learn how to use PowerShell to remotely run MapReduce jobs with Hadoop on HDInsight."
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="paulettm"
   editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="12/04/2015"
	wacn.date=""/>

#Run Hive queries with Hadoop on HDInsight using PowerShell

[AZURE.INCLUDE [mapreduce-selector](../includes/hdinsight-selector-use-mapreduce.md)]

This document provides an example of using Azure PowerShell to run a MapReduce job in a Hadoop on HDInsight cluster.

##<a id="prereq"></a>Prerequisites

To complete the steps in this article, you will need the following:

<!-- deleted by customization
- **An Azure HDInsight (Hadoop on HDInsight) cluster (Windows-based or Linux-based)**
-->
<!-- keep by customization: begin -->
- **An Azure HDInsight (Hadoop on HDInsight) cluster (Windows-based)** 
<!-- keep by customization: end -->

- **A workstation with Azure PowerShell**. See [Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure)

##<a id="powershell"></a>Run a MapReduce job using Azure PowerShell

Azure PowerShell provides *cmdlets* that allow you to remotely run MapReduce jobs on HDInsight. Internally, this is accomplished by using REST calls to [WebHCat](https://cwiki.apache.org/confluence/display/Hive/WebHCat) (formerly called Templeton) running on the HDInsight cluster.

The following cmdlets are used when running MapReduce jobs in a remote HDInsight cluster.

* <!-- deleted by customization **Login-AzureRmAccount** --><!-- keep by customization: begin --> **Add-AzureAccount** <!-- keep by customization: end -->: Authenticates Azure PowerShell to your Azure subscription

* <!-- deleted by customization **New-AzureRmHDInsightMapReduceJobDefinition** --><!-- keep by customization: begin --> **New-AzureHDInsightMapReduceJobDefinition** <!-- keep by customization: end -->: Creates a new *job definition* by using the specified MapReduce information

* <!-- deleted by customization **Start-AzureRmHDInsightJob** --><!-- keep by customization: begin --> **Start-AzureHDInsightJob** <!-- keep by customization: end -->: Sends the job definition to HDInsight, starts the job, and returns a *job* object that can be used to check the status of the job

* <!-- deleted by customization **Wait-AzureRmHDInsightJob** --><!-- keep by customization: begin --> **Wait-AzureHDInsightJob** <!-- keep by customization: end -->: Uses the job object to check the status of the job. It waits until the job completes or the wait time is exceeded.

* <!-- deleted by customization **Get-AzureRmHDInsightJobOutput** --><!-- keep by customization: begin --> **Get-AzureHDInsightJobOutput** <!-- keep by customization: end -->: Used to retrieve the output of the job

The following steps demonstrate how to use these cmdlets to run a job in your HDInsight cluster.

1. Using an editor, save the following code as **mapreducejob.ps1**. You must replace **CLUSTERNAME** with the name of your HDInsight cluster.

<!-- deleted by customization
        #Specify the values
        $clusterName = "CLUSTERNAME"
                
        # Login to your Azure subscription
-->
<!-- keep by customization: begin -->
		#Login to your Azure subscription
<!-- keep by customization: end -->
        # Is there an active Azure subscription?
<!-- deleted by customization
        $sub = Get-AzureRmSubscription -ErrorAction SilentlyContinue
-->
<!-- keep by customization: begin -->
		$sub = Get-AzureSubscription -ErrorAction SilentlyContinue
<!-- keep by customization: end -->
        if(-not($sub))
<!-- deleted by customization
        {
            Login-AzureRmAccount
        }

        #Get HTTPS/Admin credentials for submitting the job later
        $creds = Get-Credential
        #Get the cluster info so we can get the resource group, storage, etc.
        $clusterInfo = Get-AzureRmHDInsightCluster -ClusterName $clusterName
        $resourceGroup = $clusterInfo.ResourceGroup
        $storageAccountName=$clusterInfo.DefaultStorageAccount.split('.')[0]
        $container=$clusterInfo.DefaultStorageContainer
        $storageAccountKey=Get-AzureRmStorageAccountKey `
            -Name $storageAccountName `
            -ResourceGroupName $resourceGroup `
            | %{ $_.Key1 }

        #Create a storage content and upload the file
        $context = New-AzureStorageContext `
            -StorageAccountName $storageAccountName `
            -StorageAccountKey $storageAccountKey
            
        #Define the MapReduce job
-->
<!-- keep by customization: begin -->
		{
		    Add-AzureAccount
		}

		#Specify the cluster name
		$clusterName = "CLUSTERNAME"

		#Define the MapReduce job
<!-- keep by customization: end -->
        #NOTE: If using an HDInsight 2.0 cluster, use hadoop-examples.jar instead.
        # -JarFile = the JAR containing the MapReduce application
        # -ClassName = the class of the application
        # -Arguments = The input file, and the output directory
<!-- deleted by customization
        $wordCountJobDefinition = New-AzureRmHDInsightMapReduceJobDefinition `
            -JarFile "wasb:///example/jars/hadoop-mapreduce-examples.jar" `
            -ClassName "wordcount" `
            -Arguments `
                "wasb:///example/data/gutenberg/davinci.txt", `
                "wasb:///example/data/WordCountOutput"
-->
<!-- keep by customization: begin -->
		$wordCountJobDefinition = New-AzureHDInsightMapReduceJobDefinition -JarFile "wasb:///example/jars/hadoop-mapreduce-examples.jar" `
		                          -ClassName "wordcount" `
		                          -Arguments "wasb:///example/data/gutenberg/davinci.txt", "wasb:///example/data/WordCountOutput"
<!-- keep by customization: end -->

        #Submit the job to the cluster
        Write-Host "Start the MapReduce job..." -ForegroundColor Green
<!-- deleted by customization
        $wordCountJob = Start-AzureRmHDInsightJob `
            -ClusterName $clusterName `
            -JobDefinition $wordCountJobDefinition `
            -HttpCredential $creds
-->
<!-- keep by customization: begin -->
		$wordCountJob = Start-AzureHDInsightJob -Cluster $clusterName -JobDefinition $wordCountJobDefinition
<!-- keep by customization: end -->

        #Wait for the job to complete
        Write-Host "Wait for the job to complete..." -ForegroundColor Green
<!-- deleted by customization
        Wait-AzureRmHDInsightJob `
            -ClusterName $clusterName `
            -JobId $wordCountJob.JobId `
            -HttpCredential $creds
        # Download the output
        Get-AzureStorageBlobContent `
            -Blob 'example/data/WordCountOutput/part-r-00000' `
            -Container $container `
            -Destination output.txt `
            -Context $context
        # Print the output
        Get-AzureRmHDInsightJobOutput `
            -Clustername $clusterName `
            -JobId $wordCountJob.JobId `
            -DefaultContainer $container `
            -DefaultStorageAccountName $storageAccountName `
            -DefaultStorageAccountKey $storageAccountKey `
            -HttpCredential $creds
            
-->
<!-- keep by customization: begin -->
		Wait-AzureHDInsightJob -Job $wordCountJob -WaitTimeoutInSeconds 3600

		# Print the output
		Write-Host "Display the standard output..." -ForegroundColor Green
		Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $wordCountJob.JobId -StandardOutput

<!-- keep by customization: end -->
2. Open a new **Azure PowerShell** command prompt. Change directories to the location of the **mapreducejob.ps1** file, then use the following command to run the script:

		.\mapreducejob.ps1
    
    When you run the script, you may be prompted to authenticate to your Azure subscription. You will also be asked to provide the HTTPS/Admin account name and password for the HDInsight cluster.

3. When the job completes, you should receive output similar to the following:

		Cluster         : CLUSTERNAME
		ExitCode        : 0
		Name            : wordcount
		PercentComplete : map 100% reduce 100%
		Query           :
		State           : Completed
		StatusDirectory : f1ed2028-afe8-402f-a24b-13cc17858097
		SubmissionTime  : 12/5/2014 8:34:09 PM
		JobId           : job_1415949758166_0071

	This output indicates that the job completed successfully.

	> [AZURE.NOTE] If the **ExitCode** is a value other than 0, see [Troubleshooting](#troubleshooting).

<!-- deleted by customization
    This example will also store the downloaded files to the  **example/data/WordCountOutput** folder in the directory that you run the script from.

##View output
-->
<!-- keep by customization: begin -->
##View output

The MapReduce job stored the results of the operation to Azure Blob storage, in the **wasb:///example/data/WordCountOutput** path that was specified as an argument for the job. Azure Blob storage is accessible through Azure PowerShell, but you must know the storage account name, key, and the  container that is used by your HDInsight cluster to directly access the files.

Fortunately, you can obtain this information by using the following Azure PowerShell cmdlets:

* **Get-AzureHDInsightCluster**: Returns information about an HDInsight cluster, including any storage accounts associated with it. There will always be a default storage account associated with a cluster.
* **New-AzureStorageContext**: Given the storage account name and key retrieved using **Get-AzureHDInsightCluster**, returns a context object that can be used to access the storage account.
* **Get-AzureStorageBlob**: Given a context object and container name, returns a list of blobs within the container.
* **Get-AzureStorageBlobContent**: Given a context object, a file path and name, and a container name (returned from **Get-AzureHDinsightCluster**), downloads a file from Azure Blob storage.

The following example retrieves the storage information, then downloads the output from **wasb:///example/data/WordCountOutput**. Replace **CLUSTERNAME** with the name of your HDInsight cluster.

		#Login to your Azure subscription
		# Is there an active Azure subscription?
		$sub = Get-AzureSubscription -ErrorAction SilentlyContinue
		if(-not($sub))
		{
		    Add-AzureAccount
		}

		#Specify the cluster name
		$clusterName = "CLUSTERNAME"

		#Retrieve the cluster information
		$clusterInfo = Get-AzureHDInsightCluster -ClusterName $clusterName

		#Get the storage account information
		$storageAccountName = $clusterInfo.DefaultStorageAccount.StorageAccountName
		$storageAccountKey = $clusterInfo.DefaultStorageAccount.StorageAccountKey
		$storageContainer = $clusterInfo.DefaultStorageAccount.StorageContainerName

		#Create the context object
		$context = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey

		#Download the files from wasb:///example/data/WordCountOutput
		#Use the -blob switch to filter only blobs contained in example/data/WordCountOutput
		Get-AzureStorageBlob -Container $storageContainer -Blob example/data/WordCountOutput/* -Context $context | Get-AzureStorageBlobContent -Context $context

> [AZURE.NOTE] This example will store the downloaded files to the  **example/data/WordCountOutput** folder in the directory that you run the script from.

<!-- keep by customization: end -->

The output of the MapReduce job is stored in files with the name *part-r-#####*. Open the **example/data/WordCountOutput/part-r-00000** file in a text editor to see the words and counts produced by the job.

> [AZURE.NOTE] The output files of a MapReduce job are immutable. So if you rerun this sample, you need to change the name of the output file.

##<a id="troubleshooting"></a>Troubleshooting

If no information is returned when the job completes, an error may have occurred during processing. To view error information for this job, add the following command to the end of the **mapreducejob.ps1** file, save it, and then run it again.

	# Print the output of the WordCount job.
	Write-Host "Display the standard output ..." -ForegroundColor Green
<!-- deleted by customization
	Get-AzureRmHDInsightJobOutput `
            -Clustername $clusterName `
            -JobId $wordCountJob.JobId `
            -DefaultContainer $container `
            -DefaultStorageAccountName $storageAccountName `
            -DefaultStorageAccountKey $storageAccountKey `
            -HttpCredential $creds `
            -DisplayOutputType StandardError
-->
<!-- keep by customization: begin -->
	Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $wordCountJob.JobId -StandardError
<!-- keep by customization: end -->

This returns the information that was written to STDERR on the server when you ran the job, and it may help determine why the job is failing.

##<a id="summary"></a>Summary

As you can see, Azure PowerShell provides an easy way to run MapReduce jobs on an HDInsight cluster, monitor the job status, and retrieve the output.

##<a id="nextsteps"></a>Next steps

For general information about MapReduce jobs in HDInsight:

* [Use MapReduce on HDInsight Hadoop](/documentation/articles/hdinsight-use-mapreduce)

For information about other ways you can work with Hadoop on HDInsight:

* [Use Hive with Hadoop on HDInsight](/documentation/articles/hdinsight-use-hive)

* [Use Pig with Hadoop on HDInsight](/documentation/articles/hdinsight-use-pig)
