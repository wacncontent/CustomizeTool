<properties
   pageTitle="Export a SQL Server database to a BACPAC file using SqlPackage"
   description="Windows Azure SQL Database, database migration, export database, export BACPAC file, sqlpackage"
   services="sql-database"
   documentationCenter=""
   authors="carlrabeler"
   manager="jeffreyg"
   editor=""/>

<tags
   ms.service="sql-database"
   ms.date="12/17/2015"
   wacn.date=""/>

# Export a SQL Server database to a BACPAC file using SqlPackage

> [AZURE.SELECTOR]
- [SSMS](/documentation/articles/sql-database-cloud-migrate-compatible-export-bacpac-ssms)
- [SqlPackage](/documentation/articles/sql-database-cloud-migrate-compatible-export-bacpac-sqlpackage)

This article shows how to export a SQL Server database to a [BACPAC](https://msdn.microsoft.com/zh-cn/library/ee210546.aspx#Anchor_4) file using the [SqlPackage](https://msdn.microsoft.com/zh-cn/library/hh550080.aspx) command-prompt utility. This utility ships with both Visual Studio and SQL Server. You can also [download](https://msdn.microsoft.com/zh-cn/library/mt204009.aspx) the latest version of SQL Server Data Tools to get this utility.

1. Open a command prompt and change a directory containing the sqlpackage.exe command line utility - this utility ships with both Visual Studio and SQL Server. Use search on your computer to find the path in your environment.
2. Execute the following sqlpackage.exe command with the following arguments for your environment:

	'sqlpackage.exe /Action:Export /ssn:< server_name > /sdn:< database_name > /tf:< target_file >

	| Argument  | Description  |
	|---|---|
	| < server_name >  | source server name  |
	| < database_name >  | source database name  |
	| < target_file >  | file name and location for BACPAC file  |

	![Export a data-tier application from the Tasks menu](./media/sql-database-cloud-migrate/TestForCompatibilityUsingSQLPackage01b.png)

## Next step: Import to SQL Database from a BACPAC file

- [SSMS](/documentation/articles/sql-database-cloud-migrate-compatible-import-bacpac-ssms)
- [SqlPackage](/documentation/articles/sql-database-cloud-migrate-compatible-import-bacpac-sqlpackage)
- [Azure Management Portal](/documentation/articles/sql-database-import)
- [PowerShell](/documentation/articles/sql-database-import-powershell)
