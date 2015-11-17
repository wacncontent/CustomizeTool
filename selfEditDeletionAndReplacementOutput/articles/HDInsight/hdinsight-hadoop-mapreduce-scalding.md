deletion:

deleted:

		or Linux

reason: ()

deleted:

		[Provision Linux-based Hadoop on HDInsight](/documentation/articles/hdinsight-provision-clusters) or

reason: ()

deleted:

		## Run the job on a Linux-based cluster
		
		> [AZURE.NOTE] The following steps use SSH and the Hadoop command. For other methods of running MapReduce jobs, see [Use MapReduce in Hadoop on HDInsight](/documentation/articles/hdinsight-use-mapreduce).
		
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

