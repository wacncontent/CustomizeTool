<properties
	pageTitle="Connect to SQL Database by using Python on Mac OS"
	description="Presents a Python code sample you can use to connect to Azure SQL Database from a Mac. The sample uses the pymssql driver."
	services="sql-database"
	documentationCenter=""
	authors="meet-bhagdev"
	manager="jeffreyg"
	editor=""/>


<tags
	ms.service="sql-database"
	ms.date="12/17/2015"
	wacn.date=""/>


# Connect to SQL Database by using Python on Mac OS


> [AZURE.SELECTOR]
- [Node.js](/documentation/articles/sql-database-develop-nodejs-simple-mac)
- [Python](/documentation/articles/sql-database-develop-python-simple-mac-osx)
- [Ruby](/documentation/articles/sql-database-develop-ruby-simple-mac-osx)


This topic presents a code sample written in Python. The sample runs on a Mac computer. The sample and connects to Azure SQL Database by using the **pymssql** driver. 


## Prerequisites


- [Python 2.7.6](https://www.python.org/download/releases/2.7.6).
- [FreeTDS](https://github.com/brianb/FreeTDS)
- [Pymssql](https://github.com/pymssql/pymssql)

### Install the required modules


Open your terminal and install

**1) Homebrew**: Run the following command from your terminal. This will download the Homebrew package manager on your machine.

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

**2) FreeTDS**: Run the following command from your terminal. This will download FreeTDS on your machine. FreeTDS is required for pymmsql to work.

    brew install FreeTDS

**3) Pymmsql**: Run the following command from your terminal. This will install pymmsql on your machine.

    sudo -H pip install pymssql

### A SQL database

See the [getting started page](/documentation/articles/sql-database-get-started) to learn how to create a sample database.  It is important you follow the guide to create an **AdventureWorks database template**. The samples shown below only work with the **AdventureWorks schema**.

## Step 1: Get Connection Details

[AZURE.INCLUDE [sql-database-include-connection-string-details-20-portalshots](../includes/sql-database-include-connection-string-details-20-portalshots.md)]

## Step 2:  Connect

The [pymssql.connect](http://pymssql.org/en/latest/ref/pymssql.html) function is used to connect to SQL Database.

	import pymssql
	conn = pymssql.connect(server='yourserver.database.chinacloudapi.cn', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')


## Step 3:  Execute a query

The [cursor.execute](http://pymssql.org/en/latest/ref/pymssql.html#pymssql.Cursor.execute) function can be used to retrieve a result set from a query against SQL Database. This function essentially accepts any query and returns a result set which can be iterated over with the use of [cursor.fetchone()](http://pymssql.org/en/latest/ref/pymssql.html#pymssql.Cursor.fetchone).


	import pymssql
	conn = pymssql.connect(server='yourserver.database.chinacloudapi.cn', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')
	cursor = conn.cursor()
	cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')
	row = cursor.fetchone()
	while row:
	    print str(row[0]) + " " + str(row[1]) + " " + str(row[2]) 	
	    row = cursor.fetchone()


## Step 4:  Insert a row

In this example you will see how to execute an [INSERT](https://msdn.microsoft.com/zh-cn/library/ms174335.aspx) statement safely, pass parameters which protect your application from [SQL injection](https://technet.microsoft.com/zh-cn/library/ms161953(v=sql.105).aspx) vulnerability, and retrieve the auto-generated [Primary Key](https://msdn.microsoft.com/zh-cn/library/ms179610.aspx) value.  



	import pymssql
	conn = pymssql.connect(server='yourserver.database.chinacloudapi.cn', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')
	cursor = conn.cursor()
	cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express', 'SQLEXPRESS', 0, 0, CURRENT_TIMESTAMP)")
	row = cursor.fetchone()
	while row:
	    print "Inserted Product ID : " +str(row[0])
	    row = cursor.fetchone()


## Step 5:  Rollback a transaction


This code example demonstrates the use of transactions in which you:


-Begin a transaction

-Insert a row of data

-Rollback your transaction to undo the insert


	import pymssql
	conn = pymssql.connect(server='yourserver.database.chinacloudapi.cn', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')
	cursor = conn.cursor()
	cursor.execute("BEGIN TRANSACTION")
	cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express New', 'SQLEXPRESS New', 0, 0, CURRENT_TIMESTAMP)")
	cnxn.rollback()


## Next steps

For more information, see the [Python Developer Center](/develop/python).
