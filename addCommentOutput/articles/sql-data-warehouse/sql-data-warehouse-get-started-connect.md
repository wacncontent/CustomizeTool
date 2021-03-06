<properties
   pageTitle="Connect to SQL Data Warehouse with Visual Studio | Windows Azure"
   description="Get started with connecting to SQL Data Warehouse and running some queries."
   services="sql-data-warehouse"
   documentationCenter="NA"
   authors="twounder"
   manager="barbkess"
   editor=""/>

<tags
	ms.service="sql-data-warehouse"
	ms.date="10/22/2015"
	wacn.date=""/>

# Connect to SQL Data Warehouse with Visual Studio

> [AZURE.SELECTOR]
- [Visual Studio](/documentation/articles/sql-data-warehouse-get-started-connect)
- [SQLCMD](/documentation/articles/sql-data-warehouse-get-started-connect-sqlcmd)

This walkthrough shows how to get connected to an Azure SQL Data Warehouse database in just a few minutes by using SQL Server Data Tools in Visual Studio.  Once connected, you will run a simple query.

## Prerequisites

+ AdventureWorksDW sample database in SQL Data Warehouse. To create this, see [Create a SQL Data Warehouse database](/documentation/articles/sql-data-warehouse-get-started-create). 
+ SQL Server Data Tools for Visual Studio. For installation instructions and options, see [Install Visual Studio and/OR SSDT](/documentation/articles/sql-data-warehouse-install-visual-studio)

## Step 1: Find the fully qualified Azure SQL server name

Your database is associated with an Azure SQL server. To connect to your database you need the fully qualified name of the <!-- deleted by customization server(**servername**.database.chinacloudapi.cn*) --><!-- keep by customization: begin --> server(**servername**.chinacloudapi.cn*) <!-- keep by customization: end -->.

To find the fully qualified server name.

1. Go to the [Azure preview <!-- deleted by customization portal](https://manage.windowsazure.cn) --><!-- keep by customization: begin --> portal](https://manage.windowsazure.cn/) <!-- keep by customization: end -->.
2. Click **SQL databases** and click the database you want to connect to. This example uses the AdventureWorksDW sample database.
3. Locate the full server name.

    ![Full server name][1]

## Step 2: Connect to your SQL database

1. Open Visual Studio.
2. Open SQL Server Object Explorer. To do this, select **View** > **SQL Server Object Explorer**.
 
    ![SQL Server Object Explorer][2]

3. Click the **Add SQL Server** icon.

    ![Add SQL Server][3]

1. Fill in the fields in the Connect to Server window.

    ![Connect to Server][4]

    - **Server name**. Enter the *server name* we located previously.
    - **Authentication**. Select SQL Server Authentication.
    - **Login** and **password**. Enter login and password for the Azure SQL server.
    - Click **Connect**.

1. To explore, expand your Azure SQL server. You can view the databases associated with the server. Expand AdventureWorksDW to see the tables in your sample database.

    ![Explore AdventureWorksDW][5]


## Step 3: Run a sample query

Now that we have connected to the server, let's go ahead and write a query. 

1. Right-click your database in SQL Server Object Explorer. 

2. Select **New Query**. A new query window opens.

    ![New query][6]

3. Copy this TSQL query into the query window:

	```
	SELECT COUNT(*) FROM dbo.FactInternetSales;
	```

4. Run the query. To do this, click the green arrow or use the following shortcut: `CTRL`+`SHIFT`+`E`.

    ![Run query][7]

1. Look at the query results. In this example, the FactInternetSales table has 60398 rows.

    ![Query results][8]

## Next steps

Now that you can connect and query, try [visualizing the data with PowerBI][].

[visualizing the data with PowerBI]: ./sql-data-warehouse-get-started-visualize-with-power-bi.md  


<!--Image references-->

[1]: ./media/sql-data-warehouse-get-started-connect/get-server-name.png
[2]: ./media/sql-data-warehouse-get-started-connect/open-ssdt.png
[3]: ./media/sql-data-warehouse-get-started-connect/add-server.png
[4]: ./media/sql-data-warehouse-get-started-connect/connection-dialog.png
[5]: ./media/sql-data-warehouse-get-started-connect/explore-sample.png
[6]: ./media/sql-data-warehouse-get-started-connect/new-query2.png
[7]: ./media/sql-data-warehouse-get-started-connect/run-query.png
[8]: ./media/sql-data-warehouse-get-started-connect/query-results.png