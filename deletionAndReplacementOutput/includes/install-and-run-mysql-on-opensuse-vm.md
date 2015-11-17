deletion:

deleted:

		5. Type this to run the script MySQL installation script:

reason: ()

replacement:

deleted:

		type

replaced by:

		run

reason: ()

deleted:

		2. To install MySQL Community Server edition, type:

replaced by:

		2. Run the following command to install MySQL Community Server edition:

reason: ()

deleted:

		3. To set MySQL to start when the system boots, type:

replaced by:

		3. To set MySQL to start when the system boots, execute the following command:

reason: ()

deleted:

		4. Start the MySQL daemon (mysqld) manually with this command:

replaced by:

		4. Now you can manually start the MySQL daemon (mysqld) with the following command:

reason: ()

deleted:

		type

replaced by:

		run

reason: ()

deleted:

		To stop the MySQL daemon, type:

replaced by:

		If you want to stop the MySQL daemon, run:

reason: ()

deleted:

		> [AZURE.IMPORTANT]

replaced by:

		5. Warning!

reason: ()

deleted:

		We

replaced by:

		It's

reason: ()

deleted:

		The script prompts

replaced by:

		When running **mysql\_secure\_installation**,

reason: ()

deleted:

		We

replaced by:

		It is

reason: ()

deleted:

		log in

replaced by:

		login

reason: ()

deleted:

		9. To log in from another computer, type:

replaced by:

		9. To login from another computer, execute the following:

reason: ()

deleted:

		10. To exit the MySQL database administration utility, type:

replaced by:

		10. To exit the MySQL database administration utility, issue the following command:

reason: ()

deleted:

		11. After MySQL is installed, you'll need to configure an endpoint to access MySQL remotely. Log in to the [Azure  Portal][AzurePortal]. Click **Virtual Machines**, click the name of your new virtual machine, and then click **Endpoints**.
		
		12. Click **Add** at the bottom of the page.
		
		13. Add an endpoint named "MySQL" with protocol **TCP**, and **Public** and **Private** ports set to "3306".
		
		14. To remotely connect to the virtual machine from your computer, type:

replaced by:

		11. Once MySQL is installed you must configure an endpoint so that MySQL can be accessed remotely. Log in to the [Azure Management Portal][AzurePreviewPortal]. In the Azure Management Portal, click **Virtual Machines**, then click the name of your new VM, then click **Endpoints**.
		
			![Endpoints][Image7]
		
		12. Click **Add Endpoint** at the bottom of the page.
			![Endpoints][Image8]
		
		13. Add an endpoint with name "MySQL", protocol **TCP**, and both **Public** and **Private** ports set to "3306". This will allow MySQL to be accessed remotely.
			![Endpoints][Image9]
		
		14. To remotely connect to MySQL running on your OpenSUSE virtual machine in Azure, run the following command on your local computer:

reason: ()

deleted:

		type this

replaced by:

		the

reason: ()

deleted:

		[AzurePortal]: http://manage.windowsazure.cn

replaced by:

		[AzurePreviewPortal]: http://manage.windowsazure.cn
		[Image7]: ./media/install-and-run-mysql-on-opensuse-vm/LinuxVmAddEndpoint.png
		[Image8]: ./media/install-and-run-mysql-on-opensuse-vm/LinuxVmAddEndpoint2.png

reason: ()

