<properties
	pageTitle="Troubleshoot backup and restore with Azure SQL Database"
	description="Learn how to recover a cloud database from errors and outages using backups and replicas in Azure SQL Database."
	services="sql-database"
	documentationCenter=""
	authors="dalechen"
	manager="msmets"
	editor=""/>

<tags
	ms.service="sql-database"
	ms.date="12/10/2015"
	wacn.date=""/>

# Restore a database to a previous point in time, restore a deleted database, or recover from a data center outage

SQL Database keeps replicas of your database so you can recover from outages and user error. Available options depend on the database service tier and options you choose. See the [Business Continuity Overview](/documentation/articles/sql-database-business-continuity) for details and design considerations.

##To restore a database to a previous point in time
1.	In the [Azure Management <!-- deleted by customization Portal](https://azure.microsoft.com/) --><!-- keep by customization: begin --> Portal](http://www.windowsazure.cn) <!-- keep by customization: end -->, click **SQL databases**.
2.	Select your database from the list and then click **Restore**.
3.	Type a new name for the database, choose the date and time to restore from, and then click **Create.**
4.	Make app adjustments as necessary to reference the new database. See [Recover a database from user error](/documentation/articles/sql-database-user-error-recovery).

##To restore an accidentally deleted database
1.	In the [Azure Management <!-- deleted by customization Portal](https://azure.microsoft.com/) --><!-- keep by customization: begin --> Portal](http://www.windowsazure.cn) <!-- keep by customization: end -->, click **SQL servers**.
2.	Select the server that hosted the database from the list.
3.	On the Server blade, scroll down and click **Deleted databases**.
4.	Select the database to restore, and then click **Create**.
5.	Make app adjustments as necessary to reference the new database. See [Recover a database from user error](/documentation/articles/sql-database-user-error-recovery).

##To recover from a regional datacenter outage
With Standard and Premium databases, if you set up geo-replicated secondaries, you can recover using these secondaries. This gives you the ability to restore a database with a less potential for data loss. See [Recover an Azure SQL database from an outage](/documentation/articles/sql-database-disaster-recovery) for details.

Azure also provides backups of every database in a different region (a geo-redundant backup). You can create a new database from these backups, which is called Geo-restore, but it's likely that you'll experience data loss if you rely on this method alone.

**To recover a database using geo-restore:**

- In the [Azure Management <!-- deleted by customization Portal](https://azure.microsoft.com/) --><!-- keep by customization: begin --> Portal](http://www.windowsazure.cn) <!-- keep by customization: end -->, click **New**, click **Data and Storage**, click **SQL Database**, and then select **Backup** as the database source. See [Recover an Azure SQL database from an outage](/documentation/articles/sql-database-disaster-recovery) for details.
