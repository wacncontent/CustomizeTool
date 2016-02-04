<properties
	pageTitle="Troubleshoot Database on server is not currently available for Azure SQL Database"
	description="Steps to identify and resolve connection errors for Azure SQL Database."
	services="sql-database"
	documentationCenter=""
	authors="dalechen"
	manager="msmets"
	editor=""/>

<tags
	ms.service="sql-database"
	ms.date="12/10/2015"
	wacn.date=""/>

# Troubleshoot "Database on server is not currently available. Please retry the connection later." and other connection errors
“Database <dbname> on server <servername> is not currently available...” is the most common transient connection error for Azure SQL Database. Transient connection errors are usually caused by a platform reconfiguration, such as failover to a new server or a temporary system outage, and are short-lived. If you are getting a different error, evaluate the [error message](/documentation/articles/sql-database-develop-error-messages) for clues about the cause, determine if the issue is transient or persistent, and use the guidance in this topic.

## Steps to resolve transient connectivity issues
1.	Make sure your app uses retry logic. See the [connectivity issues](/documentation/articles/sql-database-connectivity-issues) and the [best practices and design guidelines](/documentation/articles/sql-database-connect-central-recommendations) for general retry strategies. Then see [code samples](/documentation/articles/sql-database-develop-quick-start-client-code-samples) for specifics.
2.	As a database approaches its resource limits, it can look like a transient connectivity issue. See [Troubleshooting Performance Issues](/documentation/articles/sql-database-troubleshoot-performance).
3.	If connectivity problems continue, contact support to open a support case.

## Steps to resolve persistent connectivity issues
If the app can't connect at all, it's usually the IP and firewall configuration. This can include network reconfiguration on the client side (for example, a new IP address or proxy). Mistyped connection parameters, such as the connection string, are also common.

1.	Set up [firewall rules](/documentation/articles/sql-database-configure-firewall-settings) to allow the client IP address.
2.	On all firewalls between the client and the Internet, make sure that port 1433 is open for outbound connections.
3.	Verify your connection string and other connection settings. See the Connection String section in the [connectivity issues topic](/documentation/articles/sql-database-connectivity-issues).
4.	Check service health in the dashboard. If you think there's a regional outage, see [Recover from an outage](/documentation/articles/sql-database-disaster-recovery) for steps to recover to a new region.
5.	If connectivity problems continue, contact support to open a support case.
