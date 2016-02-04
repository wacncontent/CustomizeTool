<properties
	pageTitle="Troubleshoot Azure SQL database permissions and access"
	description="Quick steps to troubleshoot common permissions, access, user, and login issues"
	services="sql-database"
	documentationCenter=""
	authors="v-shysun"
	manager="msmets"
	editor=""/>

<tags
	ms.service="sql-database"
	ms.date="12/11/2015"
	wacn.date=""/>

#Troubleshoot common Azure SQL database permissions and access issues
Use this topic for quick steps to grant and remove access to an Azure SQL database. For more comprehensive information, see:

- [Managing databases and logins in Azure SQL Database](/documentation/articles/sql-database-manage-logins)
- [Securing your SQL database](/documentation/articles/sql-database-security)
- [Security Center for SQL Server Database Engine and Azure SQL Database](https://msdn.microsoft.com/zh-cn/library/bb510589)

##To change the administrative password for a logical server
- In the [Azure Management Portal](https://manage.windowsazure.cn) click **SQL Servers**, select the server from the list, and then click **Reset Password**.
##To help make sure only authorized IP addresses are allowed to access the server
- See [How to: Configure firewall settings on SQL Database](/documentation/articles/sql-database-configure-firewall-settings).

##To create contained database users in the user database
- Use the [CREATE USER](https://msdn.microsoft.com/zh-cn/library/ms173463.aspx) statement and see Contained Database [Users - Making Your Database Portable](https://msdn.microsoft.com/zh-cn/library/ff929188.aspx).

## To authenticate contained database users by using your Azure Active Directory
- See Connecting to [SQL Database By Using Azure Active Directory Authentication](/documentation/articles/sql-database-aad-authentication).

## To create additional logins for high-privileged users in the virtual master database
-Use the [CREATE LOGIN](https://msdn.microsoft.com/zh-cn/library/ms189751.aspx) statement, and see the Managing Logins section of [Managing databases and logins in Azure SQL Database](/documentation/articles/sql-database-manage-logins) for more detail.
