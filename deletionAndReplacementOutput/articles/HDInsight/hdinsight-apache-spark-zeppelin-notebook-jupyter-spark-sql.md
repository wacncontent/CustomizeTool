deletion:

deleted:

		[AZURE.INCLUDE [hdinsight-azure-preview-portal](../includes/hdinsight-azure-preview-portal.md)]
		
		* [Provision Apache Spark on HDInsight and run interactive queries using Spark SQL](/documentation/articles/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql-v1)

reason: ()

deleted:

		an

reason: ()

replacement:

deleted:

		trial](/pricing/1rmb-trial/)

replaced by:

		trial][azure-trial]

reason: ()

deleted:

		## <a name="provision"></a>Provision an HDInsight Spark cluster

replaced by:

		##<a name="provision"></a>Provision an HDInsight Spark cluster

reason: ()

deleted:

		1. Sign in to the [Azure preview portal](https://manage.windowsazure.cn/).
		
		2. Click **NEW**, click **Data + Analytics**, and then click **HDInsight**.
		
		    ![Creating a new cluster in the Azure preview portal](./media/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql/HDI.CreateCluster.1.png "Creating a new cluster in the Azure preview portal")
		
		3. Enter a **Cluster Name**, select **Hadoop** for the **Cluster Type**, and from the **Cluster Operating System** drop-down menu, select **Windows Server 2012 R2 Datacenter**. A green check appears beside the cluster name if it is available.
		
			![Enter cluster name and type](./media/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql/HDI.CreateCluster.2.png "Enter cluster name and type")
		
		4. If you have more than one subscription, click the **Subscription** entry to select the Azure subscription to use for the cluster.
		
		5. Click **Resource Group** to see a list of existing resource groups and select where to create the cluster. Or, you can click **Create New** and then enter the name of the new resource group. A green check appears to indicate if the new group name is available.
		
			> [AZURE.NOTE] This entry defaults to one of your existing resource groups, if any are available.
		
		6. Click **Credentials**, and then enter a **Cluster Login Username** and **Cluster Login Password**. If you want to enable Remote Desktop on the cluster node, for **Enable Remote Desktop**, click **Yes**, and then specify the required values. This tutorial does not require remote desktop so you can skip this. Click **Select** at the bottom to save the credentials configuration.
		
			![Provide cluster credentials](./media/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql/HDI.CreateCluster.3.png "Provide cluster credentials")
		
		7. Click **Data Source** to choose an existing data source for the cluster, or create a new one. When you provision a Hadoop cluster in HDInsight, you specify an Azure Storage account. A specific Blob storage container from that account is designated as the default file system, like in the Hadoop distributed file system (HDFS). By default, the HDInsight cluster is provisioned in the same data center as the storage account you specify. For more information, see [Use Azure Blob storage with HDInsight][hdinsight-storage]
		
			![Data source blade](./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.CreateCluster.4.png "Provide data source configuration")
		
			Currently you can select an Azure Storage Account as the data source for an HDInsight cluster. Use the following to understand the entries on the **Data Source** blade.
		
			- **Selection Method**: Set this to **From all subscriptions** to enable browsing of storage accounts from all your subscriptions. Set this to **Access Key** if you want to enter the **Storage Name** and **Access Key** of an existing storage account.
		
			- **Select storage account / Create New**: Click **Select storage account** to browse and select an existing storage account you want to associate with the cluster. Or, click **Create New** to create a new storage account. Use the field that appears to enter the name of the storage account. A green check appears if the name is available.
		
			- **Choose Default Container**: Use this to enter the name of the default container to use for the cluster. While you can enter any name here, we recommend using the same name as the cluster so that you can easily recognize that the container is used for this specific cluster.
		
			- **Location**: The geographic region that the storage account is in, or will be created in.
		
				> [AZURE.IMPORTANT] Selecting the location for the default data source also sets the location of the HDInsight cluster. The cluster and default data source must be located in the same region.
		
			Click **Select** to save the data source configuration.
		
		8. Click **Node Pricing Tiers** to display information about the nodes that will be created for this cluster. Set the number of worker nodes that you need for the cluster. The estimated cost of the cluster will be shown within the blade.
		
			![Node pricing tiers blade](./media/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql/HDI.CreateCluster.5.png "Specify number of cluster nodes")
		
			Click **Select** to save the node pricing configuration.
		
		9. On the **New HDInsight Cluster** blade, ensure that **Pin to Startboard** is selected, and then click **Create**. This creates the cluster and adds a tile for it to the Startboard of your Azure Management Portal. The icon will indicate that the cluster is provisioning, and will change to display the HDInsight icon once provisioning has completed.
		
			| While provisioning | Provisioning complete |
			| ------------------ | --------------------- |
			| ![Provisioning indicator on startboard](./media/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql/provisioning.png) | ![Provisioned cluster tile](./media/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql/provisioned.png) |
		
			> [AZURE.NOTE] It will take some time for the cluster to be created, usually around 15 minutes. Use the tile on the Startboard, or the **Notifications** entry on the left of the page to check on the provisioning process.
		
		10. Once the provisioning is complete, click the tile for the Spark cluster from the Startboard to launch the cluster blade.
		
		
		## <a name="zeppelin"></a>Run interactive Spark SQL queries using a Zeppelin notebook

replaced by:

		1. Sign in to the [Azure Management Portal][azure-management-portal]. 
		
		2. Click **NEW** in the lower-left corner and then enter the values as shown in the image.
		
			![Create a Spark cluster in HDInsight](./media/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql/HDI.QuickCreateCluster.png "Create a Spark cluster in HDInsight")
		
		
		##<a name="zeppelin"></a>Run interactive Spark SQL queries using a Zeppelin notebook

reason: ()

deleted:

		1. From the [Azure Preview Portal](https://manage.windowsazure.cn/), from the startboard, click the tile for your Spark cluster (if you pinned it to the startboard). You can also navigate to your cluster under **Browse All** > **HDInsight Clusters**.   
		
		2. From the Spark cluster blade, click **Quick Links**, and then from the **Cluster Dashboard** blade, click **Zeppelin Notebook**. If prompted, enter the admin credentials for the cluster.
		
			> [AZURE.NOTE] You may also reach the Zeppelin Notebook for your cluster by opening the following URL in your browser. Replace __CLUSTERNAME__ with the name of your cluster:
			>
			> `https://CLUSTERNAME.azurehdinsight.cn/zeppelin`

replaced by:

		1. Launch the Zeppelin notebook. Select your newly-created Spark cluster on the Azure Management Portal, and from the portal task bar at the bottom, click **Zeppelin Notebook**. When prompted, enter the admin credentials for the cluster. Follow the instructions on the page that opens up to launch the notebook.

reason: ()

deleted:

		webpage

replaced by:

		web page

reason: ()

deleted:

		## <a

replaced by:

		##<a

reason: ()

deleted:

		1. From the [Azure Preview Portal](https://manage.windowsazure.cn/), from the startboard, click the tile for your Spark cluster (if you pinned it to the startboard). You can also navigate to your cluster under **Browse All** > **HDInsight Clusters**.   
		
		2. From the Spark cluster blade, click **Quick Links**, and then from the **Cluster Dashboard** blade, click **Jupyter Notebook**. If prompted, enter the admin credentials for the cluster.
		
			> [AZURE.NOTE] You may also reach the Jupyter Notebook for your cluster by opening the following URL in your browser. Replace __CLUSTERNAME__ with the name of your cluster:
			>
			> `https://CLUSTERNAME.azurehdinsight.cn/jupyter`

replaced by:

		1. Launch the Jupyter notebook. Select your Spark cluster on the Azure Management Portal, and from the portal task bar at the bottom, click **Jupyter Notebook**. When prompted, enter the admin credentials for the Spark cluster.

reason: ()

deleted:

		## <a name="seealso"></a>See also

replaced by:

		##<a name="seealso"></a>See also

reason: ()

deleted:

		[azure-purchase-options]: /pricing/overview/
		[azure-member-offers]: /pricing/member-offers/
		[azure-trial]: /pricing/1rmb-trial/

replaced by:

		[azure-purchase-options]: http://www.windowsazure.cn/pricing/overview/
		[azure-trial]: http://www.windowsazure.cn/pricing/1rmb-trial/

reason: ()

