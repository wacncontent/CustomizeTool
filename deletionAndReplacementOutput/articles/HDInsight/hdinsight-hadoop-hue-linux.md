deletion:

deleted:

		* If the cluster username is "admin", you only need to specify the password within single quotes.
				* If the cluster username is anything other than "admin", you must specify the paramter as `-u [username] [password in single quotes]`

reason: ()

replacement:

deleted:

		Important considerations while providing

replaced by:

		You must specify

reason: ()

deleted:

		:

replaced by:

		within single quotes.

reason: ()

deleted:

		1. Use the information in [Use SSH Tunneling to access Ambari web UI, ResourceManager, JobHistory, NameNode, Oozie, and other web UI's](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel) to create an SSH tunnel from your client system to the HDInsight cluster, and then configure your Web browser to use the SSH tunnel as a proxy.
		
		2. Once you have created an SSH tunnel and configured your browser to proxy traffic through it, use the browser to open the Hue portal at http://headnode0:8888.
		
		    > [AZURE.NOTE] When you log in for the first time, you will be prompted to create an account to log into the Hue portal. The credentials you specify here will be limited to the portal and are not related to the admin or SSH user credentials you specified while provision the cluster.
		
			![Login to the Hue portal](./media/hdinsight-hadoop-hue-linux/HDI.Hue.Portal.Login.png "Specify credentials for Hue portal")

replaced by:

		> [AZURE.NOTE] The instructions below assume that you have a Firefox Web browser with [FoxyProxy](https://addons.mozilla.org/firefox/addon/foxyproxy-standard/) extension installed.
		
		1. Enable SSH tunneling from your desktop computer and configure your Firefox Web browser to use the SSH tunnel. While configuring tunneling, use a port other than port 8888.
		
			* For instructions on enabling SSH tunneling from a Linux computer, see [Use SSH with Linux-based Hadoop on HDInsight from Linux, Unix, or OS X](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel#usessh).
			* For instructions on enabling SSH tunneling from a Windows computer, see [Use SSH with Linux-based Hadoop on HDInsight from Windows](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel#useputty).
		
			Keep the PuTTY session running.
		 
		2. From your computer, use the Firefox Web browser with FoxyProxy configured to launch the Hue portal at http://headnode0:8888. When you log in for the first time, you are prompted to create an account to log into the Hue portal. The credentials you specify here will be limited to the portal and are not related to the admin or SSH user credentials you specified while provision the cluster.
		
			![Login to the Hue portal](./media/hdinsight-hadoop-hue-linux/HDI.Hue.Portal.Login.png "Specify credentials for Hue portal")

reason: ()

