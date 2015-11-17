deletion:

deleted:

		[preview-portal]: https://manage.windowsazure.cn/

reason: ()

replacement:

deleted:

		Windows](/documentation/articles/xplat-cli-install)

replaced by:

		Windows](/documentation/articles/xplat-cli)

reason: ()

deleted:

		when creating a cluster using

replaced by:

		, such as the HDInsight wizard in

reason: ()

deleted:

		preview portal

replaced by:

		Management Portal

reason: ()

deleted:

		preview portal**

replaced by:

		Management Portal**

reason: ()

deleted:

		* **Azure CLI for Mac, Linux and Windows** - Uses command-line commands to create the cluster.
		
		Each of these methods will require the public key. For complete information on creating a Linux-based HDInsight cluster, see [Provision<!-- keep by customization: begin --> <a href="/documentation/articles/hdinsight-provision-clusters/" target="_blank">Provision <!-- keep by customization: end --> Linux-based HDInsight clusters](/documentation/articles/hdinsight-provision-clusters)<!-- keep by customization: begin --> clusters</a> <!-- keep by customization: end -->.
		
		###Azure preview portal
		
		When using the [Azure preview portal][preview-portal] to create a Linux-based HDInsight cluster, you must enter an **SSH Username**, and select to enter a **PASSWORD** or **SSH PUBLIC KEY**.
		
		If you select **SSH PUBLIC KEY**, you can either paste the public key (displayed in the __Public key for pasting into OpenSSH authorized\_keys file__ field in PuttyGen,) into the __SSH PublicKey__ field, or select __Select a file__ to browse and select the file that contains the public key.
		
		![Image of form asking for public key](./media/hdinsight-hadoop-linux-use-ssh-windows/ssh-key.png)

replaced by:

		* **Azure Cross-Platform Command-Line Interface (xplat-cli)** - Uses command-line commands to create the cluster.
		
		Each of these methods will require the public key. For complete information on creating a Linux-based HDInsight cluster, see <!-- keep by customization: begin --> <a href="/documentation/articles/hdinsight-provision-clusters/" target="_blank">Provision

reason: ()

deleted:

		###Azure Command-Line Interface for Mac, Linux, and Windows
		
		You can use the [Azure CLI for Mac, Linux and Windows](/documentation/articles/xplat-cli-install) to create a new cluster by using the `azure hdinsight cluster create` command.
		
		For more information on using this command, see [Provision Hadoop Linux clusters in HDInsight using custom options](/documentation/articles/hdinsight-provision-clusters).

replaced by:

		###Azure Cross-Platform Command-Line Interface
		
		You can use the <a href="/documentation/articles/xplat-cli/" target="_brad">Azure Cross-Platform Command-Line Interface</a> to create a new cluster by using the `azure hdinsight cluster create` command.
		
		For more information on using this command, see <a href="/documentation/articles/hdinsight-provision-clusters/" target="_blank">Provision Hadoop Linux clusters in HDInsight using custom options</a>.

reason: ()

