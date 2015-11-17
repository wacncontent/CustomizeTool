deletion:

deleted:

		**Linux-based HDInsight**
		
			add file wasb:///streaming.py;
		
			SELECT TRANSFORM (clientid, devicemake, devicemodel)
			  USING 'streaming.py' AS
			  (clientid string, phoneLable string, phoneHash string)
			FROM hivesampletable
			ORDER BY clientid LIMIT 50;

reason: ()

replacement:

deleted:

		If you are using a Linux-based HDInsight cluster, use the **SSH** steps below. If you are using a Windows-based HDInsight cluster and a Windows client, use the **PowerShell** steps.
		
		###SSH
		
		For more information on using SSH, see <a href="/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix" target="_blank">Use SSH with Linux-based Hadoop on HDInsight from Linux, Unix, or OS X</a> or <a href="/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows" target="_blank">Use SSH with Linux-based Hadoop on HDInsight from Windows</a>.
		
		1. Using the Python examples [streaming.py](#streamingpy) and [jython.py](#jythonpy), create local copies of the files on your development machine.
		
		2. Use `scp` to copy the files to your HDInsight cluster. For example, the following would copy the files to a cluster named **mycluster**.
		
				scp streaming.py jython.py myuser@mycluster-ssh.azurehdinsight.cn:
		
		3. Use SSH to connect to the cluster. For example, the following would connect to a cluster named **mycluster** as user **myuser**.
		
				ssh myuser@mycluster-ssh.azurehdinsight.cn
		
		4. From the SSH session, add the python files uploaded previously to the WASB storage for the cluster.
		
				hadoop fs -copyFromLocal streaming.py /streaming.py
				hadoop fs -copyFromLocal jython.py /jython.py
		
		After uploading the files, use the following steps to run the Hive and Pig jobs.

replaced by:

		If you are using a Windows-based HDInsight cluster and a Windows client, use the **PowerShell** steps.

reason: ()

