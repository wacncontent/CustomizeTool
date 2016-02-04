<properties
	pageTitle="Troubleshoot database performance in Azure SQL Database."
	description="Quick steps to troubleshoot database performance."
	services="sql-database"
	documentationCenter=""
	authors="v-shysun"
	manager="msmets"
	editor=""/>

<tags
	ms.service="sql-database"
	ms.date="12/17/2015"
	wacn.date=""/>

# Troubleshoot database performance using Azure SQL Database
You can change the [service tier](/documentation/articles/sql-database-service-tiers) of a single database or increase the eDTUs of an elastic database pool at any time to improve performance, but you may want to identify opportunities to improve and optimize query performance first. Missing indexes and poorly optimized queries are common reasons for poor database performance.

## Steps to evaluate and tune database performance
1.	In the [Azure Management Portal](https://manage.windowsazure.cn), click **SQL databases**, select the database, and then use the Monitoring chart to look for resources approaching their maximum. DTU consumption is shown by default. Click **Edit** to change the time range and values shown.
2.	Use [Query Performance Insight](/documentation/articles/sql-database-query-performance) to evaluate the queries using DTUs, and then use [Index Advisor](/documentation/articles/sql-database-index-advisor) to recommend and create indexes.
3.	You can use dynamic management views (DMVs), Extended Events (Xevents), and the Query Store in SSMS to get performance parameters in real time. See the [performance guidance topic](/documentation/articles/sql-database-performance-guidance) for detailed monitoring and tuning tips.

## Steps to improve database performance with more resources
1.	For single databases, you can [change service tiers](/documentation/articles/sql-database-scale-up) on-demand to improve database performance.
2.	For multiple databases, consider using [elastic database pools](/documentation/articles/sql-database-elastic-pool-guidance) to scale resources automatically.

If performance problems continue, contact support to open a support case.
