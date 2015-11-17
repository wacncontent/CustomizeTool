deletion:

deleted:

		or Linux

reason: ()

deleted:

		[Provision Linux-based Hadoop on HDInsight](/documentation/articles/hdinsight-provision-clusters) or

reason: ()

deleted:

		## Run the job on a Windows-based cluster
		
		> [AZURE.NOTE] The following steps use Windows PowerShell. For other methods of running MapReduce jobs, see [Use MapReduce in Hadoop on HDInsight](/documentation/articles/hdinsight-use-mapreduce).
		
		1. [Install and configure Azure PowerShell](/documentation/articles/install-configure-powershell).
		
		2. Download [hdinsight-tools.psm1](https://github.com/Blackmist/hdinsight-tools/blob/master/hdinsight-tools.psm1) and save to a file named **hdinsight-tools.psm1**.
		
		3. Open a new **Azure PoweShell** session and enter the following command. If hdinsight-tools.psm1 isn't in the current directory, provide the path to the file:
		
		        import-module hdinsight-tools.psm1
		
		    This imports several functions for working with files in HDInsight.
		
		4. Use the following commands to upload the jar file containing the WordCount job. Replace `CLUSTERNAME` with the name of your HDInsight cluster:
		
		        $clusterName="CLUSTERNAME"
		        Add-HDInsightFile -clusterName $clusterName -localPath \path\to\scaldingwordcount-1.0-SNAPSHOT.jar -destinationPath example/jars/scaldingwordcount-1.0-SNAPSHOT.jar
		
		5. Once the upload has completed, use the following commands to run the job:
		
		        $jobDef=New-AzureHDInsightMapReduceJobDefinition -JobName ScaldingWordCount -JarFile wasb:///example/jars/scaldingwordcount-1.0-SNAPSHOT.jar -ClassName com.microsoft.example.WordCount -arguments "--hdfs", "--input", "wasb:///example/data/gutenberg/davinci.txt", "--output", "wasb:///example/wordcountout"
		        $job = start-azurehdinsightjob -cluster $clusterName -jobdefinition $jobDef
		        wait-azurehdinsightjob -Job $job -waittimeoutinseconds 3600
		
		6. Once the job completes, use the following to download the job output:
		
		        Get-HDInsightFile -clusterName $clusterName -remotePath example/wordcountout/part-00000 -localPath output.txt
		
		7. The output consists of tab delimited word and count values. use the following command to display the results.
		
		        cat output.txt
		
		    The file should contain values similar to the following:
		
		        writers 9
		        writes  18
		        writhed 1
		        writing 51
		        writings        24
		        written 208
		        writtenthese    1
		        wrong   11
		        wrongly 2
		        wrongplace      1
		        wrote   34
		        wrotefootnote   1
		        wrought 7

reason: ()

replacement:

deleted:

		Linux-based

replaced by:

		Windows-based

reason: ()

deleted:

		SSH and the Hadoop command

replaced by:

		Windows PowerShell

reason: ()

deleted:

		1. Use the following command to upload the package to your HDInsight cluster:
		
		        scp target/scaldingwordcount-1.0-SNAPSHOT.jar username@clustername-ssh.azurehdinsight.cn:
		
		    This copies the files from the local system to the head node.
		
		    > [AZURE.NOTE] If you used a password to secure your SSH account, you will be prompted for the password. If you used an SSH key, you may have to use the `-i` parameter and the path to the private key. For example, `scp -i /path/to/private/key target/scaldingwordcount-1.0-SNAPSHOT.jar username@clustername-ssh.azurehdinsight.cn:.`
		
		2. Use the following command to connect to the cluster head node:
		
		        ssh username@clustername-ssh.azurehdinsight.cn
		
		    > [AZURE.NOTE] If you used a password to secure your SSH account, you will be prompted for the password. If you used an SSH key, you may have to use the `-i` parameter and the path to the private key. For example, `ssh -i /path/to/private/key username@clustername-ssh.azurehdinsight.cn`
		
		3. Once connected to the head node, use the following command to run the word cound job
		
		        hadoop jar scaldingwordcount-1.0-SNAPSHOT.jar com.microsoft.example.WordCount --hdfs --input wasb:///example/data/gutenberg/davinci.txt --output wasb:///example/wordcountout
		
		    This runs the WordCount class you implemented earlier. `--hdfs` instructs the job to use HDFS. `--input` specifies the input text file, while `--output` specifies the output location.
		
		4. After the job completes, use the following to view the output.
		
		        hadoop fs -text wasb:///example/wordcountout/part-00000
		
		    This will display information similar to the following:

replaced by:

		1. [Install and configure Azure PowerShell](/documentation/articles/install-configure-powershell).
		
		2. Download [hdinsight-tools.psm1](https://github.com/Blackmist/hdinsight-tools/blob/master/hdinsight-tools.psm1) and save to a file named **hdinsight-tools.psm1**.
		
		3. Open a new **Azure PoweShell** session and enter the following command. If hdinsight-tools.psm1 isn't in the current directory, provide the path to the file:
		
		        import-module hdinsight-tools.psm1
		
		    This imports several functions for working with files in HDInsight.
		
		4. Use the following commands to upload the jar file containing the WordCount job. Replace `CLUSTERNAME` with the name of your HDInsight cluster:
		
		        $clusterName="CLUSTERNAME"
		        Add-HDInsightFile -clusterName $clusterName -localPath \path\to\scaldingwordcount-1.0-SNAPSHOT.jar -destinationPath example/jars/scaldingwordcount-1.0-SNAPSHOT.jar
		
		5. Once the upload has completed, use the following commands to run the job:
		
		        $jobDef=New-AzureHDInsightMapReduceJobDefinition -JobName ScaldingWordCount -JarFile wasb:///example/jars/scaldingwordcount-1.0-SNAPSHOT.jar -ClassName com.microsoft.example.WordCount -arguments "--hdfs", "--input", "wasb:///example/data/gutenberg/davinci.txt", "--output", "wasb:///example/wordcountout"
		        $job = start-azurehdinsightjob -cluster $clusterName -jobdefinition $jobDef
		        wait-azurehdinsightjob -Job $job -waittimeoutinseconds 3600
		
		6. Once the job completes, use the following to download the job output:
		
		        Get-HDInsightFile -clusterName $clusterName -remotePath example/wordcountout/part-00000 -localPath output.txt
		
		7. The output consists of tab delimited word and count values. use the following command to display the results.
		
		        cat output.txt
		
		    The file should contain values similar to the following:

reason: ()

