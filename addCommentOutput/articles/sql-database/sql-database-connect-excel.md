<properties
	pageTitle="Connect Excel to SQL Database | Windows Azure"
	description="Learn how to connect Microsoft Excel to Azure SQL database in the cloud. Import data into Excel for reporting and data exploration."
	services="sql-database"
	keywords="connect excel to sql, import data to excel"
	documentationCenter=""
	authors="joseidz"
	manager="jeffreyg"
	editor="jeffreyg"/>


<tags
	ms.service="sql-database"
	ms.date="10/09/2015"
	wacn.date=""/>


<!-- deleted by customization
# Connect Excel to an Azure SQL database and create a report 
-->
<!-- keep by customization: begin -->
# Connect to an Azure SQL database with Excel
<!-- keep by customization: end -->

> [AZURE.SELECTOR]
- [C#](/documentation/articles/sql-database-connect-query)
- [SSMS](/documentation/articles/sql-database-connect-query-ssms)
- [Excel](/documentation/articles/sql-database-connect-excel)

<!-- deleted by customization
Learn how to connect Excel to a SQL database in order to import data into Excel. Then, create a report over the data.

You'll need a SQL database first. If you don't have one, seeÂ [Create your first SQL database](/documentation/articles/sql-database-get-started) to get a database with sample data up and running in a few minutes. In this article, you'll import sample data into Excel from that article, but you can follow similar steps on your own data.
-->
<!-- keep by customization: begin -->
This article shows you how to connect Excel to an Azure SQL database and create a report over the data in the database. You'll need a SQL database first. If you don't have one, seeÂ [Create your first SQL database](/documentation/articles/sql-database-get-started) to get a database with sample data up and running in a few minutes. This article is based on the sample data from that article, but you can follow similar steps on your own data.
<!-- keep by customization: end -->

You'll also need a copy of Excel. This article uses [Microsoft Excel 2016](https://products.office.com/).

<!-- deleted by customization
## Connect Excel to a SQL database and create a report

1.	To connect Excel to SQL database, open Excel and then create a new workbook.
	 	Or, open an existing Excel workbook you want to connect to SQL database.
-->
<!-- keep by customization: begin -->
## Connect and create a report

1.	Open Excel and then create a new workbook or open the workbook you want to connect.
<!-- keep by customization: end -->

2.	In the menu bar at the top of the page click **Data**, click **From Other Sources**, and then click **From SQL Server**.
<!-- deleted by customization
	![Select data source: Connect Excel to SQL database.](./media/sql-database-connect-excel/excel_data_source.png)
-->
<!-- keep by customization: begin -->
	
	![Select data source](./media/sql-database-connect-excel/excel_data_source.png)
<!-- keep by customization: end -->

	The Data Connection Wizard opens.

3.	In the **Connect to Database Server** dialog box, type the **Server name** that hosts the logical server you want to connect to in the form **<*servername*>.database.chinacloudapi.cn**. For example, **adventureserver.database.chinacloudapi.cn**.

4.	In the **Log on Credentials** section, click **Use the following User Name and Password**, type the **User Name** and **Password** you set up for the SQL Database server when you created it, and then click **Next**.

	> [AZURE.TIP] Both [PowerPivot](https://www.microsoft.com/download/details.aspx?id=102) and [Power Query](https://www.microsoft.com/download/details.aspx?id=39379) add-ins for Excel have similar experiences.

5. In the **Select Database and Table** dialog, select the **AdventureWorks** database from the pull-down menu and select **vGetAllCategories** from the list of tables and views, then click **Next**.

<!-- deleted by customization
	![Select a database and table.][5]
-->
<!-- keep by customization: begin -->
	![Select a database and table][5]
<!-- keep by customization: end -->

6. In the **Save Data Connection File and Finish** dialog, click **Finish**.

7. In the **Import Data** dialog, select **PivotChart** and click **OK**.

<!-- deleted by customization
	![Import data into Excel: In Import data dialog box select PivotChart.][2]
-->
<!-- keep by customization: begin -->
	![Select Import Data][2]
<!-- keep by customization: end -->

8. In the **PivotChart Fields** dialog, select the following configuration to create a report for the count of products per category.

<!-- deleted by customization
	![Configure database report.][3]
-->
<!-- keep by customization: begin -->
	![Configuration][3]
<!-- keep by customization: end -->

	Success looks like this:

<!-- deleted by customization
	![Sucess: Excel connected to SQL database.][4]
-->
<!-- keep by customization: begin -->
	![success][4]
<!-- keep by customization: end -->

## Next steps

If you are a Software as a Service (SaaS) developer, learn about [Elastic Database pools](/documentation/articles/sql-database-elastic-pool). You can easily manage large collections of databases using [Elastic Database jobs](/documentation/articles/sql-database-elastic-jobs-overview).

<!--Image references-->
[1]: ./media/sql-database-connect-excel/connect-to-database-server.png
[2]: ./media/sql-database-connect-excel/import-data.png
[3]: ./media/sql-database-connect-excel/power-pivot.png
[4]: ./media/sql-database-connect-excel/power-pivot-results.png
[5]: ./media/sql-database-connect-excel/select-database-and-table.png