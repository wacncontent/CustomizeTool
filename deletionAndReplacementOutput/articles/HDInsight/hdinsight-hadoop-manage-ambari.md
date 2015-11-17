deletion:

deleted:

		or adding new services

reason: ()

replacement:

deleted:

		For information on creating an SSH tunnel to work with Ambari, see [Use SSH Tunneling to access Ambari web UI, ResourceManager, JobHistory, NameNode, Oozie, and other web UI's](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel).

replaced by:

		Use the following articles to create an SSH tunnel from a port on your local machine to the cluster:
		
		* <a href="/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix/#tunnel" target="_blank">Use SSH with Linux-based Hadoop on HDInsight from Linux, Unix, or OS X</a> - Steps on creating an SSH tunnel by using the `ssh` command.
		
		* <a href="/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows/#tunnel" target="_blank">Use SSH with Linux-based Hadoop on HDInsight from Windows</a> - Steps on using PuTTY to create an SSH tunnel

reason: ()

deleted:

		on

replaced by:

		or can be added to

reason: ()

deleted:

		web applications used to display this information are not exposed on the internet

replaced by:

		internal

reason: ()

deleted:

		> For information on using an SSL tunnel with HDInsight, see [Use SSH Tunneling to access Ambari web UI, ResourceManager, JobHistory, NameNode, Oozie, and other web UI's](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel)

replaced by:

		>* <a href="/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows/#tunnel" target="_blank">Use SSH with Linux-based Hadoop on HDInsight from Windows</a> - Steps on using PuTTY to create an SSH tunnel.

reason: ()

deleted:

		> [AZURE.WARNING] While __Add Service__ is listed in this menu, it should not be used to add services to the HDInsight cluster. New services should be added using a Script Action during cluster provisioning. For more information on using Script Actions, see [Customize HDInsight clusters using Script Actions](/documentation/articles/hdinsight-hadoop-customize-cluster).

replaced by:

		The following are the general steps to add a service:
		
		1. From the **Dashboard** or **Services** page, use the **Actions** button and select **Add Service**.
		
		2. From the **Add Service Wizard**, select the service to add, and then click **Next**.
		
			![add service](./media/hdinsight-hadoop-manage-ambari/add-service.png)
		
		3. Continue through the wizard, providing configuration information for the service. Consult the documentation on the specific service you are adding for more information on configuration requirements.
		
		4. From the **Review** page, you can **Print** the configuration information, or **Deploy** the service to the cluster.
		
		5. Once the service has been deployed, the **Install, Start and Test** page will display progress information as the service is installed and tested. Once the **Status** is green, select **Next**.
		
			![image of install, start, and test page](./media/hdinsight-hadoop-manage-ambari/install-start-test.png)
		
		6. The **Summary** page displays a summary of the install process, as well as any possible actions you need to take; for example, restarting other services. Select **Complete** to exit the wizard.

reason: ()

