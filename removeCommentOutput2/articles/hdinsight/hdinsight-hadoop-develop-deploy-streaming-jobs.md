<!-- rename to hdinsight-hadoop-streaming-python -->

<properties
	pageTitle="Develop C# Hadoop streaming programs for HDInsight | Azure"
	description="Learn how to develop Hadoop streaming MapReduce programs in C#, and how to deploy them to Azure HDInsight."
	services="hdinsight"
	documentationCenter=""
	tags="azure-portal"
	authors="mumian"
	manager="paulettm"
	editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="01/28/2016"
	wacn.date=""/>



# Develop C# Hadoop streaming programs for HDInsight

Hadoop provides a streaming API for MapReduce that enables you to write map and reduce functions in languages other than Java. This tutorial walks you through creating a C# word-count program, which counts the occurrences of a given word in the input data you provide. The following illustration shows how the MapReduce framework does a word count:

![HDI.WordCountDiagram][image-hdi-wordcountdiagram]

This tutorial shows you how to:

- Develop a Hadoop streaming MapReduce program by using C# 
- Run the MapReduce job on Azure HDInsight
- Retrieve the results of the MapReduce job

##<a name="prerequisites"></a> Prerequisites

Before you begin this tutorial, you must have done the following:

- A workstation with [Azure PowerShell][powershell-install], and [Microsoft Visual Studio](https://www.visualstudio.com/).
- Obtain an Azure subscription. For instructions, see [Purchase Options][azure-purchase-options], [Trial][azure-trial].


##<a name="develop"></a> Develop a word-count Hadoop streaming program in C&#35;

The word-count solution contains two console application projects: mapper and reducer. The mapper application streams each word into the console, and the reducer application counts the number of words that are streamed from a document. Both the mapper and the reducer read characters, line by line, from the standard input stream (stdin) and write to the standard output stream (stdout).

**To create the mapper program**

1. Open Visual Studio and create a C# console application called **WordCountMapper**.
2. In Solution Explorer, rename **Program.cs** to **WordCountMapper.cs**. Click **Yes** to confirm renaming all references.
3. Replace the code in WordCountMapper.cs with the following:

        using System;
        using System.IO;

        namespace WordCountMapper
        {
            class WordCountMapper
            {
                static void Main(string[] args)
                {
                    if (args.Length > 0)
                    {
                        Console.SetIn(new StreamReader(args[0]));
                    }

                    string line;
                    string[] words;

                    while ((line = Console.ReadLine()) != null)
                    {
                        words = line.Split(' ');

                        foreach (string word in words)
                            Console.WriteLine(word.ToLower());
                    }
                }
            }
        }

4. Build the solution, and make sure there is no compilation errors.

**To create the reducer program**

1. Add another C# console application to the solution called **WordCountReducer**".

		Location|C:\Tutorials\WordCount

2. In Solution Explorer, rename **Program.cs** to **WordCountReducer.cs**. Click **Yes** to confirm renaming all references.
3. Replace the code in WordCountReducer.cs with the following:

        using System;
        using System.IO;

        namespace WordCountReducer
        {
            class WordCountReducer
            {
                static void Main(string[] args)
                {
                    string word, lastWord = null;
                    int count = 0;

                    if (args.Length > 0)
                    {
                        Console.SetIn(new StreamReader(args[0]));
                    }

                    while ((word = Console.ReadLine()) != null)
                    {
                        if (word != lastWord)
                        {
                            if (lastWord != null)
                                Console.WriteLine("{0}[{1}]", lastWord, count);

                            count = 1;
                            lastWord = word;
                        }
                        else
                        {
                            count += 1;
                        }
                    }
                    Console.WriteLine(count);
                }
            }
        }

4. Build the solution, and make sure there is no compilation errors.

You shall get the mapper and reducer executables:

- ..\WordCountMapper\bin\Debug\WordCountMapper.exe
- ..\WordCountReducer\bin\Debug\WordCountReducer.exe


##<a id="upload"></a>Upload data to Azure Blob storage
Azure HDInsight uses Azure Blob storage as the default file system. You can configure an HDInsight cluster to use additional Blob storage for the data files. In this section, you will create an Azure Storage account and upload the data files to the Blob storage. The data files are the .txt files in the %hadoop_home%\share\doc\hadoop\common directory.


**To create a Storage account and a container**

1. Open Azure PowerShell.
2. Set the variables, and then run the commands:

		$subscriptionName = "<AzureSubscriptionName>"
		$storageAccountName = "<AzureStorageAccountName>"  
		$containerName = "<ContainerName>"
		$location = "<MicrosoftDataCenter>"  # For example, "China East"

3. Run the following commands to create a Storage account and a Blob storage container on the account:

		# Select an Azure subscription
		Select-AzureSubscription $subscriptionName

		# Create a Storage account
		New-AzureStorageAccount -StorageAccountName $storageAccountName -location $location

		# Create a Blob storage container
		$storageAccountKey = Get-AzureStorageKey $storageAccountName | %{ $_.Primary }
		$destContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey  
		New-AzureStorageContainer -Name $containerName -Context $destContext

4. Run the following commands to verify the Storage account and the container:

		Get-AzureStorageAccount -StorageAccountName $storageAccountName
		Get-AzureStorageContainer -Context $destContext

**To upload the data files**

1. In the Azure PowerShell window, set the values for the local and destination folders:

		$localFolder = "C:\hdp\hadoop-2.4.0.2.1.3.0-1981\share\doc\hadoop\common"
		$destFolder = "WordCount/Input"

	Notice the local source file folder is **C:\hdp\hadoop-2.4.0.2.1.3.0-1981\share\doc\hadoop\common**, and the destination folder is **WordCount/Input**. The source location is the location of the .txt files on the HDInsight Emulator. The destination is the folder structure that will be reflected under the Azure Blob container.

3. Run the following commands to get a list of the .txt files in the source file folder:

		# Get a list of the .txt files
		$filesAll = Get-ChildItem $localFolder
		$filesTxt = $filesAll | where {$_.Extension -eq ".txt"}

5. Run the following snippet to copy the files:

		# Copy the files from the local workstation to the Blob container
		foreach ($file in $filesTxt){

		    $fileName = "$localFolder\$file"
		    $blobName = "$destFolder/$file"

		    write-host "Copying $fileName to $blobName"

		    Set-AzureStorageBlobContent -File $fileName -Container $containerName -Blob $blobName -Context $destContext
		}

6. Run the following command to list the uploaded files:

		# List the uploaded files in the Blob storage container
		Get-AzureStorageBlob -Container $containerName  -Context $destContext -Prefix $destFolder


**To upload the word-count applications**

1. In the Azure PowerShell window, set the following variables:

		$mapperFile = "C:\Tutorials\WordCount\WordCountMapper\bin\Debug\WordCountMapper.exe"
		$reducerFile = "C:\Tutorials\WordCount\WordCountReducer\bin\Debug\WordCountReducer.exe"
		$blobFolder = "WordCount/Apps"

	Notice the destination folder is **WordCount/Apps**, which is the structure that will be reflected in the Azure Blob container.

2. Run the following commands to copy the applications:

		Set-AzureStorageBlobContent -File $mapperFile -Container $containerName -Blob "$blobFolder/WordCountMapper.exe" -Context $destContext
		Set-AzureStorageBlobContent -File $reducerFile -Container $containerName -Blob "$blobFolder/WordCountReducer.exe" -Context $destContext

3. Run the following command to list the uploaded files:

		# List the uploaded files in the Blob storage container
		Get-AzureStorageBlob -Container $containerName  -Context $destContext -Prefix $blobFolder

	You shall see both application files listed there.


##<a name="run"></a>Run the MapReduce job on Azure HDInsight

This section provides an Azure PowerShell script that performs all the tasks related to running a MapReduce job. The list of tasks includes:

1. Provision an HDInsight cluster

	1. Create a Storage account that will be used as the default HDInsight cluster file system
	2. Create a Blob storage container
	3. Create an HDInsight cluster

2. Submit the MapReduce job

	1. Create a streaming MapReduce job definition
	2. Submit a MapReduce job
	3. Wait for the job to finish
	4. Display standard error
	5. Display standard output

3. Delete the cluster

	1. Delete the HDInsight cluster
	2. Delete the Storage account used as the default HDInsight cluster file system


**To run the Azure PowerShell script**

1. Open Notepad.
2. Copy and paste the following code:

		# ====== STORAGE ACCOUNT AND HDINSIGHT CLUSTER VARIABLES ======
		$subscriptionName = "<AzureSubscriptionName>"
		$stringPrefix = "<StringForPrefix>"     ### Prefix to cluster, Storage account, and container names
		$storageAccountName_Data = "<TheDataStorageAccountName>"
		$containerName_Data = "<TheDataBlobStorageContainerName>"
		$location = "<MicrosoftDataCenter>"     ### Must match the data storage account location
		$clusterNodes = 1

		$clusterName = $stringPrefix + "hdicluster"

		$storageAccountName_Default = $stringPrefix + "hdistore"
		$containerName_Default =  $stringPrefix + "hdicluster"

		# ====== THE STREAMING MAPREDUCE JOB VARIABLES ======
		$mrMapper = "WordCountMapper.exe"
		$mrReducer = "WordCountReducer.exe"
		$mrMapperFile = "wasb://$containerName_Data@$storageAccountName_Data.blob.core.chinacloudapi.cn/WordCount/Apps/WordCountMapper.exe"
		$mrReducerFile = "wasb://$containerName_Data@$storageAccountName_Data.blob.core.chinacloudapi.cn/WordCount/Apps/WordCountReducer.exe"
		$mrInput = "wasb://$containerName_Data@$storageAccountName_Data.blob.core.chinacloudapi.cn/WordCount/Input/"
		$mrOutput = "wasb://$containerName_Data@$storageAccountName_Data.blob.core.chinacloudapi.cn/WordCount/Output/"
		$mrStatusOutput = "wasb://$containerName_Data@$storageAccountName_Data.blob.core.chinacloudapi.cn/WordCount/MRStatusOutput/"

		Select-AzureSubscription $subscriptionName

		#====== CREATE A STORAGE ACCOUNT ======
		Write-Host "Create a storage account" -ForegroundColor Green
		New-AzureStorageAccount -StorageAccountName $storageAccountName_Default -location $location

		#====== CREATE A BLOB STORAGE CONTAINER ======
		Write-Host "Create a Blob storage container" -ForegroundColor Green
		$storageAccountKey_Default = Get-AzureStorageKey $storageAccountName_Default | %{ $_.Primary }
		$destContext = New-AzureStorageContext -StorageAccountName $storageAccountName_Default -StorageAccountKey $storageAccountKey_Default

		New-AzureStorageContainer -Name $containerName_Default -Context $destContext

		#====== CREATE AN HDINSIGHT CLUSTER ======
		Write-Host "Create an HDInsight cluster" -ForegroundColor Green
		$storageAccountKey_Data = Get-AzureStorageKey $storageAccountName_Data | %{ $_.Primary }

		$config = New-AzureHDInsightClusterConfig -ClusterSizeInNodes $clusterNodes |
		    Set-AzureHDInsightDefaultStorage -StorageAccountName "$storageAccountName_Default.blob.core.chinacloudapi.cn" -StorageAccountKey $storageAccountKey_Default -StorageContainerName $containerName_Default |
		    Add-AzureHDInsightStorage -StorageAccountName "$storageAccountName_Data.blob.core.chinacloudapi.cn" -StorageAccountKey $storageAccountKey_Data

		Select-AzureSubscription $subscriptionName
		New-AzureHDInsightCluster -Name $clusterName -Location $location -Config $config

		#====== CREATE A STREAMING MAPREDUCE JOB DEFINITION ======
		Write-Host "Create a streaming MapReduce job definition" -ForegroundColor Green

		$mrJobDef = New-AzureHDInsightStreamingMapReduceJobDefinition -JobName mrWordCountStreamingJob -StatusFolder $mrStatusOutput -Mapper $mrMapper -Reducer $mrReducer -InputPath $mrInput -OutputPath $mrOutput
		$mrJobDef.Files.Add($mrMapperFile)
		$mrJobDef.Files.Add($mrReducerFile)

		#====== RUN A STREAMING MAPREDUCE JOB ======
		Write-Host "Run a streaming MapReduce job" -ForegroundColor Green
		Select-AzureSubscription $subscriptionName
		$mrJob = Start-AzureHDInsightJob -Cluster $clusterName -JobDefinition $mrJobDef
		Wait-AzureHDInsightJob -Job $mrJob -WaitTimeoutInSeconds 3600

		Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $mrJob.JobId -StandardError
		Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $mrJob.JobId -StandardOutput

		#====== DELETE THE HDINSIGHT CLUSTER ======
		Write-Host "Delete the HDInsight cluster" -ForegroundColor Green
		Select-AzureSubscription $subscriptionName
		Remove-AzureHDInsightCluster -Name $clusterName

		#====== DELETE THE STORAGE ACCOUNT ======
		Write-Host "Delete the storage account" -ForegroundColor Green
		Remove-AzureStorageAccount -StorageAccountName $storageAccountName_Default

3. Set the first four variables in the script. The **$stringPrefix** variable is used to prefix the specified string to the HDInsight cluster name, the Storage account name, and the Blob storage container name. Because the names for these must be 3 to 24 characters, make sure the string you specify and the names this script uses, together, do not exceed the character limit for the name. You must use all lowercase for **$stringPrefix**.

	The **$storageAccountName_Data** and **$containerName_Data** variables are the Storage account and container that you already created in the previous steps. So, you must provide the names for those. These are used for storing the data files and the applications. The **$location** variable must match the data storage account location.

4. Review the rest of the variables.
5. Save the script file.
6. Open Azure PowerShell.
7. Run the following command to set the execution policy to RemoteSigned:

		PowerShell -File <FileName> -ExecutionPolicy RemoteSigned

8. When prompted, enter the user name and password for the HDInsight cluster. Make sure the password is at least 10 characters and contains one uppercase letter, one lowercase letter, a number, and a special character. If you don't want to get prompted for the credentials, see [Working with Passwords, Secure Strings and Credentials in Windows PowerShell][powershell-PSCredential].

For an HDInsight .NET SDK sample on submitting Hadoop streaming jobs, see [Submit Hadoop jobs programmatically][hdinsight-submit-jobs].


##<a name="retrieve"></a> Retrieve the MapReduce job output
This section shows you how to download and display the output. For information on displaying the results in Excel, see [Connect Excel to HDInsight with the Microsoft Hive ODBC Driver][hdinsight-ODBC] and [Connect Excel to HDInsight with Power Query][hdinsight-power-query].


**To retrieve the output**

1. Open the Azure PowerShell window.
2. Set the values, and then run the commands:

		$subscriptionName = "<AzureSubscriptionName>"
		$storageAccountName = "<TheDataStorageAccountName>"
		$containerName = "<TheDataBlobStorageContainerName>"
		$blobName = "WordCount/Output/part-00000"

3. Run the following commands to create an Azure Storage context object:

		Select-AzureSubscription $subscriptionName
		$storageAccountKey = Get-AzureStorageKey $storageAccountName | %{ $_.Primary }
		$storageContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey  

4. Run the following commands to download and display the output:

		Get-AzureStorageBlobContent -Container $ContainerName -Blob $blobName -Context $storageContext -Force
		cat "./$blobName" | findstr "there"



##<a id="nextsteps"></a> Next steps
In this tutorial, you have learned how to develop a Hadoop streaming MapReduce job, how to test the application on the HDInsight Emulator, and how to write an Azure PowerShell script to provision an HDInsight cluster and run a MapReduce job on the cluster. To learn more, see the following articles:

- [Get started with Azure HDInsight](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1/)
- [Get started with the HDInsight Emulator][hdinsight-get-started-emulator]
- [Develop Java MapReduce programs for HDInsight][hdinsight-develop-mapreduce]
- [Use Azure Blob storage with HDInsight][hdinsight-storage]
- [Administer HDInsight using Azure PowerShell][hdinsight-admin-powershell]
- [Upload data to HDInsight][hdinsight-upload-data]
- [Use Hive with HDInsight][hdinsight-use-hive]
- [Use Pig with HDInsight][hdinsight-use-pig]

[azure-purchase-options]: /pricing/overview/
[azure-trial]: /pricing/1rmb-trial/

[hdinsight-develop-mapreduce]: /documentation/articles/hdinsight-develop-deploy-java-mapreduce/
[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically/

[hdinsight-get-started-emulator]: /documentation/articles/hdinsight-hadoop-emulator-get-started/
[hdinsight-emulator-wasb]: /documentation/articles/hdinsight-hadoop-emulator-get-started/#blobstorage
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data/
[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage/
[hdinsight-admin-powershell]: /documentation/articles/hdinsight-administer-use-powershell/

[hdinsight-use-hive]: /documentation/articles/hdinsight-use-hive/
[hdinsight-use-pig]: /documentation/articles/hdinsight-use-pig/
[hdinsight-ODBC]: /documentation/articles/hdinsight-connect-excel-hive-ODBC-driver/
[hdinsight-power-query]: /documentation/articles/hdinsight-connect-excel-power-query/

[powershell-PSCredential]: http://social.technet.microsoft.com/wiki/contents/articles/4546.working-with-passwords-secure-strings-and-credentials-in-windows-powershell.aspx
[powershell-install]: /documentation/articles/powershell-install-configure/

[image-hdi-wordcountdiagram]: ./media/hdinsight-hadoop-develop-deploy-streaming-jobs/HDI.WordCountDiagram.gif "MapReduce wordcount application flow"
