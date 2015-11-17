
1. To escalate privileges, <!-- deleted by customization type --><!-- keep by customization: begin --> run <!-- keep by customization: end -->:

		sudo -s
	Enter your password.

<!-- deleted by customization
2. To install MySQL Community Server edition, type:
-->
<!-- keep by customization: begin -->
2. Run the following command to install MySQL Community Server edition:
<!-- keep by customization: end -->

		# zypper install mysql-community-server

	Wait while MySQL downloads and installs.
<!-- deleted by customization

3. To set MySQL to start when the system boots, type:
-->
<!-- keep by customization: begin -->
3. To set MySQL to start when the system boots, execute the following command:
<!-- keep by customization: end -->

		# insserv mysql
<!-- deleted by customization

4. Start the MySQL daemon (mysqld) manually with this command:
-->
<!-- keep by customization: begin -->
4. Now you can manually start the MySQL daemon (mysqld) with the following command:
<!-- keep by customization: end -->

		# rcmysql start

	To check the status of the MySQL daemon, <!-- deleted by customization type --><!-- keep by customization: begin --> run <!-- keep by customization: end -->:

		# rcmysql status

<!-- deleted by customization
	To stop the MySQL daemon, type:
-->
<!-- keep by customization: begin -->
	If you want to stop the MySQL daemon, run:
<!-- keep by customization: end -->

		# rcmysql stop

	<!-- deleted by customization > [AZURE.IMPORTANT] --><!-- keep by customization: begin --> 5. Warning! <!-- keep by customization: end --> After installation, the MySQL root password is empty by default. <!-- deleted by customization We --><!-- keep by customization: begin -->  It's <!-- keep by customization: end --> recommended that you run **mysql\_secure\_installation**, a script that helps secure MySQL. <!-- deleted by customization The script prompts --><!-- keep by customization: begin --> When running **mysql\_secure\_installation**, <!-- keep by customization: end --> you <!-- keep by customization: begin --> will be prompted <!-- keep by customization: end --> to change the MySQL root password, remove anonymous user accounts, disable remote root logins, remove test databases, and reload the privileges table. <!-- deleted by customization We --><!-- keep by customization: begin --> It is <!-- keep by customization: end --> recommended that you answer yes to all of these options and change the root password. <!-- keep by customization: begin --> Run the following command to execute the script: <!-- keep by customization: end -->
<!-- deleted by customization

5. Type this to run the script MySQL installation script:
-->

		$ mysql_secure_installation

6. After you run, you can <!-- deleted by customization log in --><!-- keep by customization: begin --> login <!-- keep by customization: end --> to MySQL:

		$ mysql -u root -p

	Enter the MySQL root password (which you changed in the previous step) and you'll be presented with a prompt where you can issue SQL statements to interact with the database.

7. To create a new MySQL user, run the following at the **mysql>** prompt:

		mysql> CREATE USER 'mysqluser'@'localhost' IDENTIFIED BY 'password';

	Note, the semi-colons (;) at the end of the lines are crucial for ending the commands.

8. To create a database and grant the `mysqluser` user permissions on it, issue the following commands:

		mysql> CREATE DATABASE testdatabase;
		mysql> GRANT ALL ON testdatabase.* TO 'mysqluser'@'localhost' IDENTIFIED BY 'password';

	Note that database user names and passwords are only used by scripts connecting to the database.  Database user account names do not necessarily represent actual user accounts on the system.

<!-- deleted by customization
9. To log in from another computer, type:
-->
<!-- keep by customization: begin -->
9. To login from another computer, execute the following:
<!-- keep by customization: end -->

		mysql> GRANT ALL ON testdatabase.* TO 'mysqluser'@'<ip-address>' IDENTIFIED BY 'password';

	where `ip-address` is the IP address of the computer from which you will connect to MySQL.
<!-- deleted by customization
10. To exit the MySQL database administration utility, type:
-->
<!-- keep by customization: begin -->
	
10. To exit the MySQL database administration utility, issue the following command:
<!-- keep by customization: end -->

		quit

<!-- deleted by customization
11. After MySQL is installed, you'll need to configure an endpoint to access MySQL remotely. Log in to the [Azure  Portal][AzurePortal]. Click **Virtual Machines**, click the name of your new virtual machine, and then click **Endpoints**.

12. Click **Add** at the bottom of the page.

13. Add an endpoint named "MySQL" with protocol **TCP**, and **Public** and **Private** ports set to "3306".

14. To remotely connect to the virtual machine from your computer, type:
-->
<!-- keep by customization: begin -->
11. Once MySQL is installed you must configure an endpoint so that MySQL can be accessed remotely. Log in to the [Azure Management Portal][AzurePreviewPortal]. In the Azure Management Portal, click **Virtual Machines**, then click the name of your new VM, then click **Endpoints**.

	![Endpoints][Image7]

12. Click **Add Endpoint** at the bottom of the page.
	![Endpoints][Image8]

13. Add an endpoint with name "MySQL", protocol **TCP**, and both **Public** and **Private** ports set to "3306". This will allow MySQL to be accessed remotely.
	![Endpoints][Image9]

14. To remotely connect to MySQL running on your OpenSUSE virtual machine in Azure, run the following command on your local computer:
<!-- keep by customization: end -->

		mysql -u mysqluser -p -h <yourservicename>.chinacloudapp.cn

	For example, using the virual machine we created in this tutorial, <!-- deleted by customization type this --><!-- keep by customization: begin --> the <!-- keep by customization: end --> command <!-- keep by customization: begin --> would be <!-- keep by customization: end -->:

		mysql -u mysqluser -p -h testlinuxvm.chinacloudapp.cn

<!-- keep by customization: begin -->
15. You've successfully configured MySQL, created a database, and a new user.  For more information on MySQL, see the [MySQL Documentation][MySQLDocs].	

<!-- keep by customization: end -->
[MySQLDocs]: http://dev.mysql.com/doc/
<!-- deleted by customization
[AzurePortal]: http://manage.windowsazure.cn
-->
<!-- keep by customization: begin -->
[AzurePreviewPortal]: http://manage.windowsazure.cn
[Image7]: ./media/install-and-run-mysql-on-opensuse-vm/LinuxVmAddEndpoint.png
[Image8]: ./media/install-and-run-mysql-on-opensuse-vm/LinuxVmAddEndpoint2.png
<!-- keep by customization: end -->
[Image9]: ./media/install-and-run-mysql-on-opensuse-vm/LinuxVmAddEndpointMySQL.png
