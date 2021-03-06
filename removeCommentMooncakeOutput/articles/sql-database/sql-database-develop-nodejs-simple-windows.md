<properties
	pageTitle="Connect to SQL Database by using Node.js on Windows"
	description="Presents a Node.js code sample you can use to connect to Azure SQL Database. The sample runs on a Windows client computer."
	services="sql-database"
	documentationCenter=""
	authors="meet-bhagdev"
	manager="jeffreyg"
	editor=""/>


<tags
	ms.service="sql-database"
	ms.date="12/17/2015"
	wacn.date=""/>


# Connect to SQL Database by using Node.js on Windows


> [AZURE.SELECTOR]
- [C#](/documentation/articles/sql-database-develop-dotnet-simple)
- [PHP](/documentation/articles/sql-database-develop-php-simple-windows)
- [Python](/documentation/articles/sql-database-develop-python-simple-windows)
- [Ruby](/documentation/articles/sql-database-develop-ruby-simple-windows)
- [Java](/documentation/articles/sql-database-develop-java-simple-windows)
- [Node.js](/documentation/articles/sql-database-develop-nodejs-simple-windows)


This topic presents a Node.js code sample that you can use to connect to Azure SQL Database. The Node.js program runs on a Windows client computer. To manage the connection, the msnodesql driver is used.


## Prerequisites


The following software items must exist on your client development computer.


-  Node.js â [Version 0.8.9 (32 bit version)](http://blog.nodejs.org/2012/09/11/node-v0-8-9-stable/). Scroll and click the download for Window Installer for 32 bit x86, and not for Windows x64 Installer 64 bit.
- [Python 2.7.6](https://www.python.org/download/releases/2.7.6/), the installer for either x86 or x64.
- [Visual C++ 2010](https://app.vssps.visualstudio.com/profile/review?download=true&family=VisualStudioCExpress&release=VisualStudio2010&type=web&slcid=0x409&context=eyJwZSI6MSwicGMiOjEsImljIjoxLCJhbyI6MCwiYW0iOjEsIm9wIjpudWxsLCJhZCI6bnVsbCwiZmEiOjAsImF1IjpudWxsLCJjdiI6OTY4OTg2MzU1LCJmcyI6MCwic3UiOjAsImVyIjoxfQ2) - the Express edition is freely available from Microsoft.
- SQL Server Native Client 11.0 - available as Microsoft SQL Server 2012 Native Client found in the [SQL Server 2012 Feature Pack](http://www.microsoft.com/zh-cn/download/details.aspx?id=29065).


### Install the required modules

Once you satisfy the requirements, make sure you are on Node.js version 0.8.9. You can check this by using the following command from your command line terminal: node -v.
<br>In a **cmd.exe** command line window, navigate to your project directory- for example C:\NodeJSSQLProject. Enter the following commands in the sequence shown.

	npm init
	npm install msnodesql

Next navigate to node_modules\msnodesql folder and run the **msnodesql-0.2.1-v0.8-ia32** executible. Follow the steps from the installation wizard and hit finish when you are done. At this point you should have the Node.js SQL Server driver installed. Follow the next steps to get your connection string and then you should be able to connect to Azure SQL DB from your Node.js application.


### A SQL database

See the [getting started page](/documentation/articles/sql-database-get-started) to learn how to create a sample database.  It is important you follow the guide to create an **AdventureWorks database template**. The samples shown below only work with the **AdventureWorks schema**.


## Step 1: Get Connection Details

[AZURE.INCLUDE [sql-database-include-connection-string-details-20-portalshots](../includes/sql-database-include-connection-string-details-20-portalshots.md)]

## Step 2: Connect


- Copy the following code in a .js file located in your project directory.


		var http = require('http');
		var sql = require('msnodesql');
		var http = require('http');
		var fs = require('fs');
		var useTrustedConnection = false;
		var conn_str = "Driver={SQL Server Native Client 11.0};Server=tcp:yourserver.database.chinacloudapi.cn;" +
		(useTrustedConnection == true ? "Trusted_Connection={Yes};" : "UID=yourusername;PWD=yourpassword;") +
		"Database={AdventureWorks};"
		sql.open(conn_str, function (err, conn) {
		    if (err) {
		        console.log("Error opening the connection!");
		        return;
		    }
		    else
		        console.log("Successfuly connected");
		});


- Now run your .js file by issuing the following command.


		node index.js


## Step 3:  Execute a query


	var http = require('http');
	var sql = require('msnodesql');
	var http = require('http');
	var fs = require('fs');
	var useTrustedConnection = false;
	var conn_str = "Driver={SQL Server Native Client 11.0};Server=tcp:yourserver.database.chinacloudapi.cn;" +
	(useTrustedConnection == true ? "Trusted_Connection={Yes};" : "UID=yourusername;PWD=yourpassword;") +
	"Database={AdventureWorks};"
	sql.open(conn_str, function (err, conn) {
	    if (err) {
	        console.log("Error opening the connection!");
	        return;
	    }
	    else
	        console.log("Successfuly connected");


	    conn.queryRaw("SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;", function (err, results) {
	        if (err) {
	            console.log("Error running query1!");
	            return;
	        }
	        for (var i = 0; i < results.rows.length; i++) {
	            console.log(results.rows[i]);
	        }
	    });
	});


## Step 4:  Insert a row


	var http = require('http');
	var sql = require('msnodesql');
	var http = require('http');
	var fs = require('fs');
	var useTrustedConnection = false;
	var conn_str = "Driver={SQL Server Native Client 11.0};Server=tcp:yourserver.database.chinacloudapi.cn;" +
	(useTrustedConnection == true ? "Trusted_Connection={Yes};" : "UID=yourusername;PWD=yourpassword;") +
	"Database={AdventureWorks};"
	sql.open(conn_str, function (err, conn) {
	    if (err) {
	        console.log("Error opening the connection!");
	        return;
	    }
	    else
	        console.log("Successfuly connected");


	    conn.queryRaw("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express', 'SQLEXPRESS', 0, 0, CURRENT_TIMESTAMP)", function (err, results) {
	        if (err) {
	            console.log("Error running query!");
	            return;
	        }
	        for (var i = 0; i < results.rows.length; i++) {
	            console.log("Product ID Inserted : "+results.rows[i]);
	        }
	    });
	});


## Step 5:  Rollback a transaction


The method **conn.beginTransactions** will not work in Azure SQL Database. Instead, follow the code sample to perform transactions in SQL Database.


	var http = require('http');
	var sql = require('msnodesql');
	var http = require('http');
	var fs = require('fs');
	var useTrustedConnection = false;
	var conn_str = "Driver={SQL Server Native Client 11.0};Server=tcp:yourserver.database.chinacloudapi.cn;" +
	(useTrustedConnection == true ? "Trusted_Connection={Yes};" : "UID=yourusername;PWD=yourpassword;") +
	"Database={AdventureWorks};"
	sql.open(conn_str, function (err, conn) {
	    if (err) {
	        console.log("Error opening the connection!");
	        return;
	    }
	    else
	        console.log("Successfuly connected");


	    conn.queryRaw("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express New ', 'SQLEXPRESS New', 1, 1, CURRENT_TIMESTAMP)", function (err, results) {
	        if (err) {
	            console.log("Error running query!");
	            return;
	        }
	        for (var i = 0; i < results.rows.length; i++) {
	            console.log("Product ID Inserted : "+results.rows[i]);
	        }
	    });

	    conn.queryRaw("ROLLBACK TRANSACTION; ", function (err, results) {
            	if (err) {
        		console.log("Rollback failed");
        		return;
        	}
    	    });
	});


## Step 6: Stored Procedures

For this code sample to work, you must first have or create a stored procedure that inputs no parameters. You can create a stored procedure with a tool such as SQL Server Management Studio (SSMS.exe).


	var http = require('http');
	var sql = require('msnodesql');
	var http = require('http');
	var fs = require('fs');
	var useTrustedConnection = false;
	var conn_str = "Driver={SQL Server Native Client 11.0};Server=tcp:yourserver.database.chinacloudapi.cn;" +
	(useTrustedConnection == true ? "Trusted_Connection={Yes};" : "UID=yourusername;PWD=yourpassword;") +
	"Database={AdventureWorks};"
	sql.open(conn_str, function (err, conn) {
	    if (err) {
	        console.log("Error opening the connection!");
	        return;
	    }
	    else
	        console.log("Successfuly connected");

	    conn.query("exec NameOfStoredProcedure", function (err, results) {
	    	if (err) {
			console.log("Error running query8!");
			return;
		}
	    });
	});


## Next steps

For more information, see the [Node.js Developer Center](/develop/nodejs/).
