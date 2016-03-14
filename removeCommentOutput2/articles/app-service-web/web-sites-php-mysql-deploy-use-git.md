<properties
	pageTitle="Create a PHP-MySQL web app in Azure and deploy using Git"
	description="A tutorial that demonstrates how to create a PHP web app that stores data in MySQL and use Git deployment to Azure."
	services="app-service\web"
	documentationCenter="php"
	authors="tfitzmac"
	manager="wpickett"
	editor="mollybos"
	tags="mysql"/>

<tags
	ms.service="app-service-web"
	ms.date="02/09/2016"
	wacn.date=""/>

#Create a PHP-MySQL web app in Azure and deploy using Git

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/web-sites-dotnet-get-started)
- [Node.js](/documentation/articles/web-sites-nodejs-develop-deploy-mac)
- [Java](/documentation/articles/web-sites-java-get-started)
- [PHP - Git](/documentation/articles/web-sites-php-mysql-deploy-use-git)
- [PHP - FTP](/documentation/articles/web-sites-php-mysql-deploy-use-ftp)
- [Python](/documentation/articles/web-sites-python-ptvs-django-mysql)

This tutorial shows you how to create a PHP-MySQL web app and how to deploy it to [Azure Web App](/documentation/services/web-sites/) using Git. You will use [PHP][install-php], the MySQL Command-Line Tool (part of [MySQL][install-mysql]), and [Git][install-git] installed on your computer. The instructions in this tutorial can be followed on any operating system, including Windows, Mac, and  Linux. Upon completing this guide, you will have a PHP/MySQL web app running in Azure.

You will learn:

* How to create a web app and a MySQL database using the [Azure Management Portal](https://manage.windowsazure.cn). Because PHP is enabled in [Azure Web Apps](/documentation/services/web-sites/) by default, nothing special is required to run your PHP code.
* How to publish and re-publish your application to Azure using Git.

By following this tutorial, you will build a simple registration web app in PHP. The application will be hosted in Web Apps. A screenshot of the completed application is below:

![Azure PHP web site][running-app]

##Set up the development environment

This tutorial assumes you have [PHP][install-php], the MySQL Command-Line Tool (part of [MySQL][install-mysql]), and [Git][install-git] installed on your computer.


##<a id="create-web-site-and-set-up-git"></a>Create a web app and set up Git publishing

Follow these steps to create a web app and a MySQL database:

1. Login to the [Azure Management Portal][management-portal].
2. Click the **New** icon on the bottom left of the portal.

	![Create New Azure  Website][new-website]

3. Click **Web Apps**, then **Custom Create**.

	![Custom Create a new  Website][custom-create]
	
	Enter a value for **URL**, select **No Database** from the **Database** dropdown,  and select the data center for your  Website in the **Region** dropdown. Click ok to create the web site.

	![Fill in  Website details][Website-details]

4. Click **New** --> **Storage** --> **MYSQL DATABASE ON AZURE** --> **Quick Create**, to create a MYSQL Database for your web site.

	![Create new MySQL database][new-mysql-db]

	When the  Website has been created you will see the text **Creation of  Website "[SITENAME]" completed successfully**. Now, you can enable Git publishing.

6. Click the name of the  Website displayed in the list of  Websites to open the  Website's **QuickStart** dashboard.

	![Open  Website dashboard][go-to-dashboard]


7. At the bottom of the **QuickStart** page, click **Set up Git publishing**. 

	![Set up Git publishing][setup-git-publishing]

8. To enable Git publishing, you must provide a user name and password. Make a note of the user name and password you create. (If you have set up a Git repository before, this step will be skipped.)

	![Create publishing credentials][credentials]

	It will take a few seconds to set up your repository.

9. When your repository is ready, you will see instructions for pushing your application files to the repository. Make note of these instructions - they will be needed later.

	![Git instructions][git-instructions]

##Get remote MySQL connection information

To connect to the MySQL database that is running in Web Apps, your will need the connection information. To get MySQL connection information, follow these steps:

1. In Azure Management Portal, click **MYSQL DATABASE ON AZURE**, and open your MYSQL database server. In **Dashboard** page, under **quick glance**, you can get your host and port.

	![connection][connection-string-info]

2. In **Account** page, you can get all account name, and reset password.

3. in **Database** page, you can get all Database under this MYSQL Database Server.

	The Data source would be `tcp:<your MYSQL server name>.database.chinacloudapi.cn,<port>`

##Build and test your app locally

Now that you have created a web app, you can develop your application locally, then deploy it after testing.

The Registration application is a simple PHP application that allows you to register for an event by providing your name and email address. Information about previous registrants is displayed in a table. Registration information is stored in a MySQL database. The application consists of one file (copy/paste code available below):

* **index.php**: Displays a form for registration and a table containing registrant information.

To build and run the application locally, follow the steps below. Note that these steps assume you have the PHP and MySQL Command-Line Tool (part of MySQL) set up on your local machine, and that you have enabled the [PDO extension for MySQL][pdo-mysql].

1. Connect to the remote MySQL server, using the value for `Data Source`, `User Id`, `Password`, and `Database` that you retrieved earlier:

		<pre><code class="prettyprint">mysql -h{Data Source] -u[User Id] -p[Password] -D[Database]</code></pre> 

2. The MySQL command prompt will appear:

		<pre><code class="prettyprint">mysql></code></pre> 

3. Paste in the following `CREATE TABLE` command to create the `registration_tbl` table in your database:

		CREATE TABLE registration_tbl(id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(id), name VARCHAR(30), email VARCHAR(30), date DATE);

4. In the root of your local application folder create **index.php** file.

5. Open the **index.php** file in a text editor or IDE and add the following code, and complete the necessary changes marked with `//TODO:` comments.


		<html>
		<head>
		<Title>Registration Form</Title>
		<style type="text/css">
			body { background-color: #fff; border-top: solid 10px #000;
			    color: #333; font-size: .85em; margin: 20; padding: 20;
			    font-family: "Segoe UI", Verdana, Helvetica, Sans-Serif;
			}
			h1, h2, h3,{ color: #000; margin-bottom: 0; padding-bottom: 0; }
			h1 { font-size: 2em; }
			h2 { font-size: 1.75em; }
			h3 { font-size: 1.2em; }
			table { margin-top: 0.75em; }
			th { font-size: 1.2em; text-align: left; border: none; padding-left: 0; }
			td { padding: 0.25em 2em 0.25em 0em; border: 0 none; }
		</style>
		</head>
		<body>
		<h1>Register here!</h1>
		<p>Fill in your name and email address, then click <strong>Submit</strong> to register.</p>
		<form method="post" action="index.php" enctype="multipart/form-data" >
		      Name  <input type="text" name="name" id="name"/></br>
		      Email <input type="text" name="email" id="email"/></br>
		      <input type="submit" name="submit" value="Submit" />
		</form>
		<?php
			// DB connection info
			//TODO: Update the values for $host, $user, $pwd, and $db
			//using the values you retrieved earlier from the Azure Management Portal.
			$host = "value of Data Source";
			$user = "value of User Id";
			$pwd = "value of Password";
			$db = "value of Database";
			// Connect to database.
			try {
				$conn = new PDO( "mysql:host=$host;dbname=$db", $user, $pwd);
				$conn->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
			}
			catch(Exception $e){
				die(var_dump($e));
			}
			// Insert registration info
			if(!empty($_POST)) {
			try {
				$name = $_POST['name'];
				$email = $_POST['email'];
				$date = date("Y-m-d");
				// Insert data
				$sql_insert = "INSERT INTO registration_tbl (name, email, date)
						   VALUES (?,?,?)";
				$stmt = $conn->prepare($sql_insert);
				$stmt->bindValue(1, $name);
				$stmt->bindValue(2, $email);
				$stmt->bindValue(3, $date);
				$stmt->execute();
			}
			catch(Exception $e) {
				die(var_dump($e));
			}
			echo "<h3>Your're registered!</h3>";
			}
			// Retrieve data
			$sql_select = "SELECT * FROM registration_tbl";
			$stmt = $conn->query($sql_select);
			$registrants = $stmt->fetchAll();
			if(count($registrants) > 0) {
				echo "<h2>People who are registered:</h2>";
				echo "<table>";
				echo "<tr><th>Name</th>";
				echo "<th>Email</th>";
				echo "<th>Date</th></tr>";
				foreach($registrants as $registrant) {
					echo "<tr><td>".$registrant['name']."</td>";
					echo "<td>".$registrant['email']."</td>";
					echo "<td>".$registrant['date']."</td></tr>";
		    	}
		 		echo "</table>";
			} else {
				echo "<h3>No one is currently registered.</h3>";
			}
		?>
		</body>
		</html>

4.  In a terminal go to your application folder and type the following command:

		php -S localhost:8000

You can now browse to **http://localhost:8000/** to test the application.


##Publish your app

After you have tested your app locally, you can publish it to Web Apps using Git. You will initialize your local Git repository and publish the application.

> [AZURE.NOTE]
> These are the same steps shown in the Azure Management Portal at the end of the Create a web app and Set up Git Publishing section above.

1. (Optional)  If you've forgotten or misplaced your Git remote repostitory URL, navigate to the web app properties on the Azure Management Portal.

1. Open GitBash (or a terminal, if Git is in your `PATH`), change directories to the root directory of your application, and run the following commands:

		git init
		git add .
		git commit -m "initial commit"
		git remote add azure [URL for remote repository]
		git push azure master

	You will be prompted for the password you created earlier.

	![Initial Push to Azure via Git][git-initial-push]

2. Browse to **http://[site name].chinacloudsites.cn/index.php** to begin using the application (this information will be stored on your account dashboard):

	![Azure PHP web site][running-app]

After you have published your app, you can begin making changes to it and use Git to publish them.

##Publish changes to your app

To publish changes to your app, follow these steps:

1. Make changes to your app locally.
2. Open GitBash (or a terminal, it Git is in your `PATH`), change directories to the root directory of your app, and run the following commands:

		git add .
		git commit -m "comment describing changes"
		git push azure master

	You will be prompted for the password you created earlier.

	![Pushing site changes to Azure via Git][git-change-push]

3. Browse to **http://[site name].chinacloudsites.cn/index.php** to see your app and any changes you may have made:

	![Azure PHP web site][running-app]
	
[go-to-dashboard]: ./media/web-sites-php-mysql-deploy-use-git/go_to_dashboard.png
[install-php]: http://www.php.net/manual/en/install.php
[install-SQLExpress]: http://www.microsoft.com/download/details.aspx?id=29062
[install-Drivers]: http://www.microsoft.com/download/details.aspx?id=20098
[install-git]: http://git-scm.com/
[install-mysql]: http://dev.mysql.com/downloads/mysql/

[pdo-mysql]: http://www.php.net/manual/en/ref.pdo-mysql.php
[running-app]: ./media/web-sites-php-mysql-deploy-use-git/running_app_2.png
[new-website]: ./media/web-sites-php-mysql-deploy-use-git/new_website.jpg
[custom-create]: ./media/web-sites-php-mysql-deploy-use-git/custom_create.png
[website-details]: ./media/web-sites-php-mysql-deploy-use-git/website_details.jpg
[new-mysql-db]: ./media/web-sites-php-mysql-deploy-use-git/new_mysql_db.jpg
[go-to-webapp]: ./media/web-sites-php-mysql-deploy-use-git/select_webapp.png
[setup-git-publishing]: ./media/web-sites-php-mysql-deploy-use-git/setup_git_publishing.png
[credentials]: ./media/web-sites-php-mysql-deploy-use-git/save_credentials.png
[resource-group]: ./media/web-sites-php-mysql-deploy-use-git/set_group.png
[new-web-app]: ./media/web-sites-php-mysql-deploy-use-git/create_wa.png
[setup-publishing]: ./media/web-sites-php-mysql-deploy-use-git/setup_deploy.png
[setup-repository]: ./media/web-sites-php-mysql-deploy-use-git/select_local_git.png
[select-database]: ./media/web-sites-php-mysql-deploy-use-git/select_database.png
[select-properties]: ./media/web-sites-php-mysql-deploy-use-git/select_properties.png
[note-properties]: ./media/web-sites-php-mysql-deploy-use-git/note-properties.png

[git-instructions]: ./media/web-sites-php-mysql-deploy-use-git/git-instructions.png
[git-change-push]: ./media/web-sites-php-mysql-deploy-use-git/php-git-change-push.png
[git-initial-push]: ./media/web-sites-php-mysql-deploy-use-git/php-git-initial-push.png
[deployments-list]: ./media/web-sites-php-mysql-deploy-use-git/php-deployments-list.png
[connection-string-info]: ./media/web-sites-php-mysql-deploy-use-git/connection_string_info.png
[management-portal]: https://manage.windowsazure.cn
[sql-database-editions]: http://msdn.microsoft.com/zh-cn/library/azure/ee621788.aspx
 
