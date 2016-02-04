<properties
	pageTitle="What is SQL Database? Intro to SQL Database | Windows Azure"
	description="Get an introduction to SQL Database: technical details and capabilities of Microsoft's relational database management system (RDBMS) in the cloud."
	keywords="introduction to sql,intro to sql,what is sql database,DTU"
	services="sql-database"
	documentationCenter=""
	authors="shontnew"
	manager="jeffreyg"
	editor="cgronlun"/>

<tags
	ms.service="sql-database"
	ms.date="09/30/2015"
	wacn.date=""/>

# What is SQL Database? Introduction to SQL Database, technical details, and an explanation of DTUs

SQL Database is a relational database service in the cloud based on the market-leading Microsoft SQL Server engine, with mission-critical capabilities. SQL Database delivers predictable performance, scalability with no downtime, business continuity and data protection—all with near-zero administration. You can focus on rapid app development and accelerating your time to market, rather than managing virtual machines and infrastructure. Because it's based on the [SQL Server](https://msdn.microsoft.com/zh-cn/library/bb545450.aspx) engine, SQL Database supports existing SQL Server tools, libraries and APIs, which makes it easier for you to move and extend to the cloud.

This article is an introduction to SQL Database core concepts and features related to performance, scalability, and manageability, with links to explore details. If you're ready to jump in, you can [Create your first SQL database](/documentation/articles/sql-database-get-started) or [Create an elastic database pool](/documentation/articles/sql-database-elastic-pool-portal) in minutes. If you want a deeper dive, watch this 30 minute video.


> [AZURE.VIDEO azurecon-2015-get-started-with-azure-sql-database]


## Adjust performance and scale without downtime
SQL databases is available in Basic, Standard, and Premium *service tiers*. Each service tier offers [different levels of performance and capabilities](/documentation/articles/sql-database-service-tiers) to support lightweight to heavyweight database workloads. You can build your first app on a small database for a few bucks a month, then [change the service tier](/documentation/articles/sql-database-scale-up) manually or programmatically at any time as your app goes viral worldwide, without downtime to your app or your customers.

For many businesses and apps, being able to create databases and dial single database performance up or down on demand is enough, especially if usage patterns are relatively predictable. But if you have unpredictable usage patterns, it can make it hard to manage costs and your business model. 

[Elastic database pools](/documentation/articles/sql-database-elastic-pool) in SQL Database solve this problem. The concept is simple. You allocate performance to a pool, and pay for the collective performance of the pool rather than single database performance. You don't need to dial database performance up or down. The databases in the pool, called *elastic databases*, automatically scale up and down to meet demand. Elastic databases consume but don't exceed the limits of the pool, so your cost remains predictable even if database usage doesn't. What's more, you can [add and remove databases to the pool](/documentation/articles/sql-database-elastic-pool-portal), scaling your app from a handful of databases to thousands, all within a budget that you control.

Either way you go—single or elastic—you're not locked in. You can blend single databases with elastic database pools, and change the service tiers of single databases and pools to create innovate designs. Moreover, with the power and reach of Azure, you can mix-and-match Azure services with SQL Database to meet your unique modern app design needs, drive cost and resource efficiencies, and unlock new business opportunities.

But how can you compare the relative performance of databases and database pools? How do you know the right click-stop when you dial up and down? The answer is the database transaction unit (DTU) for single databases and the elastic DTU (eDTU) for elastic databases and database pools.

## Understand DTUs

[AZURE.INCLUDE [SQL DB DTU description](../includes/sql-database-understanding-dtus.md)]

## Keep your app and business running

Azure's industry leading 99.99% availability service level agreement [(SLA)](/support/legal/sla/), powered by a global network of Microsoft-managed datacenters, helps keep your app running 24/7. With every SQL database, you take advantage of built-in data protection, fault tolerance, and data protection that you would otherwise have to design, buy, build, and manage. Even so, depending on the demands of your business, you may demand additional layers of protection to ensure your app and your business can recover quickly in the event of a disaster, an error, or something else. With SQL Database, each service tier offers a different menu of features you can use to get up and running. You can use point-in-time restore to return a database to an earlier state, as far back as 35 days. In addition, if the datacenter hosting your databases experiences an outage, you can failover to database replicas in a different region. Or you can use replicas for upgrades or relocation to different regions.

![SQL Database geo-replication](./media/sql-database-technical-overview/azure_sqldb_map.png)


See [Business Continuity](/documentation/articles/sql-database-business-continuity) for details about the different business continuity features available for different service tiers.

## Secure your data
SQL Server has a tradition of solid  data security that SQL Database upholds  with features that limit access, protect data, and help you monitor activity. See [Securing your SQL database](/documentation/articles/sql-database-security) for a quick rundown of security options you have in SQL Database. See the [Security Center for SQL Server Database Engine and SQL Database](https://msdn.microsoft.com/zh-cn/library/bb510589) for a more comprehensive view of security features. And visit the [Azure Trust Center](/support/trust-center/security/) for information about Azure's platform security.

## Next steps
Now that you've read an introduction to SQL Database and answered the question "What is SQL Database?", you're ready for the following:

- See the [pricing page](/home/features/sql-database/#price) for single database and elastic database pricing and calculators.

- Get started by [creating your first database](/documentation/articles/sql-database-get-started). Then build your first app in [C#](/documentation/articles/sql-database-connect-query), [Java](/documentation/articles/sql-database-develop-java-simple-windows), [Node.js](/documentation/articles/sql-database-develop-nodejs-simple-windows), [PHP](/documentation/articles/sql-database-develop-php-retry-windows), [Python](/documentation/articles/sql-database-develop-python-simple-windows), or [Ruby](/documentation/articles/sql-database-develop-ruby-simple-linux). 

