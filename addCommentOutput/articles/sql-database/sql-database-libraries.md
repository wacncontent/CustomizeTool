<properties
	pageTitle="Connection libraries for SQL Database and SQL Server"
	description="Lists the minimum version number for each driver that client programs can use to connect to Azure SQL Database or to Microsoft SQL Server. A link is provided for version information about drivers that are released by the community rather than by Microsoft."
	services="sql-database"
	documentationCenter=""
	authors="pehteh"
	manager="jeffreyg"
	editor="genemi"/>

<tags
	ms.service="sql-database"
	ms.date="12/01/2015"
	wacn.date=""/>

# Connection libraries for SQL Database and SQL Server

This topic lists the minimum version number for each library/driver that client programs can use when connecting to Azure SQL Database or to Microsoft SQL Server.

## Table of driver libraries released by Microsoft

The following table displays libraries that are released by Microsoft. The **Libraries** column provides links you can use to download each library. The **Version** column lists the minimum version that is recommended for interacting with Azure SQL Database and Microsoft SQL Server.

| Platform | Oper Sys | Libraries<br/>for Download | Version<br/>of Driver | Description<br/>of Driver | More<br/>Info |
| :--- | :--- | :--- | :--- | :--- | :-- |
| .NET | Cross-platform (.NET) | [ADO.NET, System .Data <!-- deleted by customization .SqlClient](http://www.microsoft.com/download/details.aspx?id=30653) --><!-- keep by customization: begin --> .SqlClient](http://www.microsoft.com/zh-cn/download/details.aspx?id=30653) <!-- keep by customization: end --> | 4.5+ | SQL Server Provider for .NET Framework |. |
| PHP | Windows | [PHP for SQL <!-- deleted by customization Server](http://www.microsoft.com/download/details.aspx?id=20098) --><!-- keep by customization: begin --> Server](http://www.microsoft.com/zh-cn/download/details.aspx?id=20098) <!-- keep by customization: end --> | 2.0+ | PHP Driver for SQL Server | [Link](http://msdn.microsoft.com/zh-cn/library/dn865013.aspx) |
| Java | Windows | [JDBC for SQL <!-- deleted by customization Server](https://www.microsoft.com/download/details.aspx?id=11774) --><!-- keep by customization: begin --> Server](http://www.microsoft.com/zh-cn/download/details.aspx?id=11774) <!-- keep by customization: end --> | 2.0+ |  Type 4 JDBC driver that provides database connectivity through the standard JDBC API | [Link](http://msdn.microsoft.com/zh-cn/library/dn425070.aspx) |
| ODBC | Windows | [ODBC for SQL <!-- deleted by customization Server](http://www.microsoft.com/download/details.aspx?id=36434) --><!-- keep by customization: begin --> Server](http://www.microsoft.com/zh-cn/download/details.aspx?id=36434) <!-- keep by customization: end --> | 11.0+ | Microsoft ODBC Driver for SQL Server | [Link](http://msdn.microsoft.com/zh-cn/library/jj730308.aspx) |
| ODBC | Suse Linux | [ODBC for SQL <!-- deleted by customization Server](http://www.microsoft.com/download/details.aspx?id=34687) --><!-- keep by customization: begin --> Server](http://www.microsoft.com/zh-cn/download/details.aspx?id=34687) <!-- keep by customization: end --> | 11.0+ | Microsoft ODBC Driver for SQL Server |. |
| ODBC | Redhat Linux | [ODBC for SQL <!-- deleted by customization Server](http://www.microsoft.com/download/details.aspx?id=34687) --><!-- keep by customization: begin --> Server](http://www.microsoft.com/zh-cn/download/details.aspx?id=34687) <!-- keep by customization: end --> | 11.0+ | Microsoft ODBC Driver for SQL Server |. |

### ODBC support

When using the data source name (DSN) wizard to define a data source for Azure SQL Database, click the **With SQL Server Authentication using a login ID and password entered by the user** option and select the **Connect to SQL Server to obtain default settings for the additional configuration options**. Enter your user name and password to connect to your Azure SQL Database server as **Login ID** and **Password**. Clear the **Connect to SQL Server to obtain default settingsâŚ** checkbox. Click **Change the default database to:** and enter the name of your Azure SQL Database even if it does not show up in the list. Note that the wizard lists several languages in the **Change the language of SQL Server system messages to:** list.

In this release, Windows Azure SQL Database supports only English, so select English as a language. Windows Azure SQL Database does not support **Mirror Server** or **Attach Database**, so leave those items empty. Click **Test Connection**.

When using the SQL Server 2008 Native Client ODBC driver, the **Test Connection** button may result in an error that **master.dbo.syscharsets** is not supported. Ignore this error, save the DSN, and use it.

### OLEDB for DB2 and SQL Server, for DRDA design

The Microsoft OLE DB Provider for DB2 Version 5.0 (Data Provider) lets you create distributed applications targeting IBM DB2 databases. The Data Provider takes advantage of Microsoft SQL Server data access architecture together with a Microsoft network client for DB2 that functions as a Distributed Relational Database Architecture (DRDA) application requester. The Data Provider converts Microsoft Component Object Model (COM) OLE DB commands and data types to DRDA protocol code points and data formats.

For more information, see:

- [Microsoft OLE DB Provider for DB2 Version 5.0](http://msdn.microsoft.com/zh-cn/library/dn745875.aspx)
- [Microsoft OLEDB Provider for DB2 v4.0 for Microsoft SQL Server <!-- deleted by customization 2012](http://www.microsoft.com/download/details.aspx?id=29100) --><!-- keep by customization: begin --> 2012](http://www.microsoft.com/zh-cn/download/details.aspx?id=29100) <!-- keep by customization: end -->

## Third party libraries

> [AZURE.IMPORTANT] The following table displays libraries that are released by third parties under third party license terms. You are responsible for verifying and complying with the relevant third party licenses in order to use these libraries. You bear the risk of using these libraries. Microsoft makes no warranties, express or implied, with respect to the information provided here and has merely provided the information as a matter of convenience to the users. Nothing herein implies any kind of endorsement by Microsoft.
<br/><br/>It is up to the public community of developers to update and maintain the information that is in this "Third party libraries" section, by using the <!-- deleted by customization [azure-content](http://github.com/Azure/azure-content/) --><!-- keep by customization: begin --> [azure-content](http://github.com/Azure/azure-content) <!-- keep by customization: end --> repository owned by **Azure** on GitHub.com. Microsoft encourages developers to update this section. Microsoft personnel do *not* intend to maintain the information that is in this section, partly because other people are more expert with each particular third party library than we are.  Thank you.

The following table displays libraries that are released by third parties such as other companies or by the community. Libraries released by Microsoft are restricted to the earlier section in this topic.

| Platform | Libraries |
| :-- | :-- |
<!-- deleted by customization
| Python | [pymssql *(org, stable)*](http://pymssql.org/en/stable/)<br/><br/>[pymssql *(org)*](http://pymssql.org/) |
-->
<!-- keep by customization: begin -->
| Python | [pymssql *(org, stable)*](http://pymssql.org/en/stable)<br/><br/>[pymssql *(org)*](http://pymssql.org) |
<!-- keep by customization: end -->
| Node.js | [Tedious *(npmjs)*](http://www.npmjs.com/package/tedious) |
| Node.js | [Node-MSSQL *(github, patriksimek)*](https://github.com/patriksimek/node-mssql)<br/><br/>[Node-MSSQL *(npmjs)*](https://www.npmjs.com/package/node-mssql)<br/><br/>[Node-MSSQL-Connector *(npmjs)*](https://www.npmjs.com/package/node-mssql-connector) |
| Node.js | [Edge.js *(github com, tjanczuk)*](https://github.com/tjanczuk/edge)<br/><br/>[Edge.js *(tjanczuk, github <!-- deleted by customization io)*](http://tjanczuk.github.io/edge/) --><!-- keep by customization: begin --> io)*](http://tjanczuk.github.io/edge) <!-- keep by customization: end --> |
<!-- deleted by customization
| . | [FreeTDS *(org)*](http://www.freetds.org/) |
-->
<!-- keep by customization: begin -->
| . | [FreeTDS *(org)*](http://www.freetds.org) |
<!-- keep by customization: end -->

<!--
https://en.wikipedia.org/wiki/Draft:Microsoft_SQL_Server_Libraries/Drivers
-->
