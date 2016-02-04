<properties
   pageTitle="Migrating a SQL Server database to Azure SQL Database"
   description="Windows Azure SQL Database, database deploy, database migration, import database, export database, migration wizard"
   services="sql-database"
   documentationCenter=""
   authors="carlrabeler"
   manager="jeffreyg"
   editor=""/>

<tags
	ms.service="sql-database"
	ms.date="12/17/2015"
	wacn.date=""/>

# Import from BACPAC to SQL Database using SSMS

> [AZURE.SELECTOR]
- [SSMS](/documentation/articles/sql-database-cloud-migrate-compatible-import-bacpac-ssms)
- [SqlPackage](/documentation/articles/sql-database-cloud-migrate-compatible-import-bacpac-sqlpackage)
- [Azure Management Portal](/documentation/articles/sql-database-import)
- [PowerShell](/documentation/articles/sql-database-import-powershell)

This article shows how to import from a [BACPAC](https://msdn.microsoft.com/zh-cn/library/ee210546.aspx#Anchor_4) file to SQL Database using the Export Data Tier Application Wizard in SQL Server Management Studio.

> [AZURE.NOTE] The steps below assume that you have already provisioned your Azure SQL logical instance and have the connection information on hand.

1. Verify that you have the latest version of SQL Server Management Studio. New versions of Management Studio are updated monthly to remain in sync with updates to the Azure Management Portal.

	 > [AZURE.IMPORTANT] It is recommended that you always use the latest version of Management Studio to remain synchronized with updates to Windows Azure and SQL Database. [Update SQL Server Management Studio](https://msdn.microsoft.com/zh-cn/library/mt238290.aspx).

2. Open Management Studio and connect to your source database in Object Explorer.

	![Export a data-tier application from the Tasks menu](./media/sql-database-cloud-migrate/MigrateUsingBACPAC01.png)

3. Once the BACPAC has been created, connect to your Azure SQL Database server, right-click the **Databases** folder and click **Import Data-tier Application...**

    ![Import data-tier application menu item](./media/sql-database-cloud-migrate/MigrateUsingBACPAC03.png)

4.	In the import wizard, choose the BACPAC file you just exported to create the new database in Azure SQL Database.

    ![Import settings](./media/sql-database-cloud-migrate/MigrateUsingBACPAC04.png)

5.	Provide the **New database name** for the database on Azure SQL DB, set the **Edition of Windows Azure SQL Database** (service tier), **Maximum database size** and **Service Objective** (performance level).

    ![Database settings](./media/sql-database-cloud-migrate/MigrateUsingBACPAC05.png)

6.	Click **Next** and then click **Finish** to import the BACPAC file into a new database in the Azure SQL Database server.

7. Using Object Explorer, connect to your migrated database in your Azure SQL Database server.

8.	Using the Azure Management Portal, view your database and its properties.

