<properties 
   pageTitle="Azure SQL Database Web and Business Edition sunset FAQ | Windows Azure"
   description="Find out when the Azure SQL Web and Business databases will be retired and learn about the features and functionality of the new service tiers."
   services="sql-database"
   documentationCenter="na"
   authors="stevestein"
   manager="jeffreyg"
   editor="monicar" />
<tags
	ms.service="sql-database"
	ms.date="09/30/2015"
	wacn.date=""/>

# Web and Business Edition sunset FAQ

Azure SQL Web and Business databases are now retired. The Basic, Standard, Premium, and Elastic tiers replace the retiring Web and Business databases.

To assist you with upgrading Web and Business databases, the SQL Database service recommends an appropriate service tier and performance level (pricing tier) for each database based on its historical workload.

**To get pricing tier recommendations:**

- [Upgrade to SQL Database V12 using the Azure Management Portal](/documentation/articles/sql-database-v12-upgrade)
- [Upgrade to SQL Database V12 using PowerShell](/documentation/articles/sql-database-upgrade-server)
- [Change the pricing tier of a Web or Business database](/documentation/articles/sql-database-service-tier-advisor)
 


## Why does the Azure Management Portal show my Web and Business edition databases as Retired?

Because Web and Business edition databases will not be available after September 2015, the management portal labels Web and Business databases as Retired. Web and Business databases can still be provisioned and managed as usual, but the Retired label is a reminder that it is best to use the Basic, Standard, or Premium service tiers for new databases. The retired label also provides a reminder that any Web and Business databases should be upgraded to Standard, Basic, or Premium. For detailed information on upgrading existing Web or Business databases to the new service tiers, see [Upgrade SQL Database Web/Business Databases to New Service Tiers](/documentation/articles/sql-database-upgrade-new-service-tiers).

## Which new service tier is the best choice to upgrade my existing Web or Business database to?

Selecting an appropriate new service tier and performance level for your existing Web or Business database depends on the specific feature and performance requirements for your application. 

Use the pricing tier recommendations described above, or for detailed information to assist you in selecting an appropriate new service tier, see [Upgrade SQL Database Web/Business Databases to New Service Tiers](/documentation/articles/sql-database-upgrade-new-service-tiers).

## Why is Microsoft introducing new service tiers?

Based on customer feedback, Azure SQL Database is introducing new service tiers to help customers more easily support relational database workloads. The new tiers are designed to deliver predictable performance across a spectrum of seven levels for light-weight to heavy-weight transactional application demands. Additionally, the new tiers offer a range of business continuity features, a stronger uptime SLA, larger database sizes for less money, and an improved billing experience.

## Where can I learn more about the new service tiers?

For detailed information about the new service tiers and performance model, see [Service tiers](/documentation/articles/sql-database-service-tiers). For detailed pricing information for the new service tiers, see [SQL Database pricing](/home/features/sql-database/#price).

## What features or functionality will not be available in Basic, Standard, and Premium?

The Federations feature will be retired with Web and Business editions. Customers who need to scale-out their databases are encouraged to instead use or migrate to [Elastic database tools](/documentation/articles/sql-database-elastic-scale-get-started) for [Azure SQL Database](/documentation/articles/sql-database-elastic-scale-get-started), which simplifies building and managing an application that uses sharding. A .NET client library allows applications to define how data is mapped to shards and routes OLTP requests to appropriate databases. To support management operations that reconfigure how data is distributed among shards, an Azure cloud service template is included that you can host in your own Azure subscription. In addition to [Elastic database tools](/documentation/articles/sql-database-elastic-scale-get-started), Microsoft will continue to create and publish [custom sharding patterns and practices guidance](https://msdn.microsoft.com/zh-cn/library/azure/dn764977.aspx) based on learnings from deep customer engagements. New customers who need scale out functionality should check out [Elastic database tools](/documentation/articles/sql-database-elastic-scale-get-started) and/or contact Microsoft Support to evaluate their options.

Microsoft is also changing the database copy experience with Premium databases. Previously as premium database quota was limited, CREATE DATABASE … AS A COPY OF in T-SQL created a Suspended Premium database without reserved resources, which was charged at the same rate as a Business database. As premium quota is now more freely available, Suspended Premium is no longer supported. Database copies will now be created with the same edition and performance level as the source and will be billed accordingly. Customers can choose to downgrade copied databases to a different service tier or performance level to reduce their cost if desired. Existing Suspended Premium databases will be converted to Business edition as part of this release. It is anticipated that the introduction of point in time restore will reduce the need to make backup copies of databases.

## How does Basic, Standard, and Premium improve my billing experience?

Basic, Standard, and Premium Azure SQL Databases are billed by the hour, and you have the ability to scale each database up or down 4 times within a 24 hour period. You are billed at a fixed rate based on the highest service tier and performance level you choose for each hour. Additionally, performance levels (example: Basic, S1, and P2) are broken out in the bill to make it easier to see the number of database days/hours you incurred in a single month for each performance level. Web and Business databases continue to be billed using Database Units based on the database size. Please visit the [SQL Database pricing page](/home/features/sql-database/#price) to learn more about the pricing and differences between the new service tiers.


## See also

[Azure SQL Database](/documentation/services/sql-databases/)

[Service tiers](/documentation/articles/sql-database-service-tiers)

[Upgrade SQL Database Web/Business Databases to New Service Tiers](/documentation/articles/sql-database-upgrade-new-service-tiers)