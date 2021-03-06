<properties 
   pageTitle="Pricing tier recommendations for Azure SQL Database" 
   description="When changing pricing tiers in the Azure Management Portal, pricing tier recommendations are provided that recommend the tier that is best suited for running an existing Azure SQL Databaseâs workload. Pricing tiers describe the service tier and performance level of a SQL database." 
   services="sql-database" 
   documentationCenter="" 
   authors="stevestein" 
   manager="jeffreyg" 
   editor="monicar"/>

<tags
	ms.service="sql-database"
	ms.date="12/01/2015"
	wacn.date=""/>

# SQL Database pricing tier recommendations

 Pricing tier recommendations are provided that recommend the service tier and performance level that is best suited for running an existing Azure SQL databaseâs workload.

> [AZURE.NOTE] Pricing tier recommendations are only available for Web and Business databases and elastic database pools -- and only available in the [Azure Management Portal](https://manage.windowsazure.cn).


Get pricing tier recommendations during the following tasks:

- [Change the service tier and performance level (pricing tier) of a SQL database](/documentation/articles/sql-database-scale-up)
- [Upgrade Azure SQL server to V12](/documentation/articles/sql-database-v12-upgrade)
- Browse to your V12 server - if your databases can [benefit in an elastic database pool](/documentation/articles/sql-database-elastic-pool-portal/#recommended-elastic-database-pools), the server blade will display a message indicating a recommended pool. Click the message to create the recommended pool.
- [Create an elastic database pool](/documentation/articles/sql-database-elastic-pool/#elastic-database-pool-pricing-tier-recommendations)





## Overview

The SQL Database service analyzes current performance and feature requirements by assessing historical resource usage for a SQL database. In addition, the minimum acceptable service tier is determined based on the size of the database, and enabled [business continuity](/documentation/articles/sql-database-business-continuity) features. 

This information is analyzed and the service tier and performance level that is best suited for running the databaseâs typical workload and maintaining it's current feature set is recommended.

- The service examines the previous 15 to 30 days of historical data (resource usage, database size, and database activity) and performs a comparison between the amount of resources consumed and the actual limitations of the currently available service tiers and performance levels.
- Data is analyzed in 15 second intervals and each interval's resultset is categorized into the existing service tier and performance level that is best suited for handling that resultset's workload.
- These 15 second samples are then aggregated into the larger 15-30 day analysis and the service tier and performance level that can optimally handle 95% of the historical workload is recommended.

### Recommendations

Based on your database's usage, there are currently 2 categories of recommendations that can be encountered:


| Recommendation | Description |
| :--- | :--- |
| Upgrade | Upgrade to a new tier. |
| Unavailable | A database requires a minimum workload or approximately 14 days of activity. There is not enough data to provide a valid recommendation. |

## Getting pricing tier recommendations

Get pricing tier recommendations by selecting an existing Web or Business database and clicking on the **Pricing tier** tile. (Pricing tier recommendations are also available when you [Upgrade Azure SQL server to V12](/documentation/articles/sql-database-v12-upgrade).)

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn).
2. Click **BROWSE** > **SQL databases**.
4. In the **SQL databases** blade, click the database that you want to see a recommendation for:

    ![Select database][1]

5. On the database blade, select the **Pricing tier** tile.

    ![Pricing tier][2]


7. After clicking the **Pricing tier** tile you will be presented with the **Recommended pricing tiers** blade where you can click the suggested tier and then click the **Select** button to change to that tier.

    ![Sign up for the preview][4]

8. Optionally, click **View usage details** to open the **Pricing Tier Recommendation Details** blade where you can view the recommended tier for the database, a feature comparison between current and recommended tiers, and a graph of the  historical resource usage analysis.

    ![Sign up for the preview][5]



## Summary

Pricing tier recommendations provide an automated experience for gathering telemetry data for each SQL database and recommending the best service tier/performance level combination based on a database's actual performance needs and feature requirements. Click the **Pricing tier** tile on a database blade to see pricing tier recommendations.



## Next steps

Depending on the details of your specific database, performing an upgrade or downgrade usually does not happen instantaneously. The portal will provide notifications as the database transitions to it's new tier, or you can monitor the upgrade status by querying the [sys.dm_operation_status (Azure SQL Database)](https://msdn.microsoft.com/zh-cn/library/dn270022.aspx) view in the SQL Database Server's master database.


<!--Image references-->
[1]: ./media/sql-database-service-tier-advisor/select-database.png
[2]: ./media/sql-database-service-tier-advisor/pricing-tier.png
[3]: ./media/sql-database-service-tier-advisor/preview-sign-up.png
[4]: ./media/sql-database-service-tier-advisor/choose-pricing-tier.png
[5]: ./media/sql-database-service-tier-advisor/usage-details.png


 