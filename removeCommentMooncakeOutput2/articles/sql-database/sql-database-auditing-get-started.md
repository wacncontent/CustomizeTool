<properties 
	pageTitle="Get started with SQL database auditing | Windows Azure" 
	description="Get started with SQL database auditing" 
	services="sql-database" 
	documentationCenter="" 
	authors="jeffgoll" 
	manager="jeffreyg" 
	editor=""/>

<tags
	ms.service="sql-database"
	ms.date="10/08/2015"
	wacn.date=""/>
 
# Get started with SQL database auditing 
<p> Azure SQL Database Auditing tracks database events and writes audited events to an audit log in your Azure Storage account. Auditing is generally available for Basic, Standard, and Premium service tiers.

Auditing can help you maintain regulatory compliance, understand  database activity, and gain insight into discrepancies and anomalies that could indicate business concerns or suspected security violations. 

Auditing tools enable and facilitate adherence to compliance standards but don't guarantee compliance. For more information about Azure programs that support standards compliance, see the <a href="/support/trust-center/compliance/" target="_blank">Azure Trust Center</a>.

+ [Azure SQL Database Auditing basics] 
+ [Set up auditing for your database]
+ [Analyze audit logs and reports]

##<a id="subheading-1"></a>Azure SQL Database Auditing basics

The following sections describe the configuration of Auditing using the Azure Preview Portal. You may also [Set up auditing for your database using the Classic Azure Management Portal].

SQL Database auditing allows you to:

- **Retain** an audit trail of selected events. You can define categories of database actions  to be audited.
- **Report** on database activity. You can use preconfigured reports and a dashboard to get started quickly with activity and event reporting.
- **Analyze** reports. You can find suspicious events, unusual activity, and trends.

You can configure auditing for the following event categories:

**Plain SQL** and **Parameterized SQL** for which the collected audit logs are classified as  

- **Access to data**
- **Schema changes (DDL)**
- **Data changes (DML)**
- **Accounts, roles, and permissions (DCL)**

**Stored Procedure**, **Login** and, **Transaction Management**.

For each Event Category, Auditing of **Success** and **Failure** operations are configured separately.

For further details about the activities and events audited, see the <a href="http://download.microsoft.com/download/D/8/D/D8D90BA1-977F-466B-A839-7823FF37FD02/03-Azure%20SQL%20DB%20Audit%20Logs%20Format%20Specification.docx" target="_blank">Audit Log Format Reference (doc file download)</a>. 

Audit logs are stored in your Azure storage account. You can define an audit log retention period.

An auditing policy can be defined for a specific database or as a default server policy. A default server auditing policy will apply to all databases on a server which do not have a specific overriding database auditing policy defined.

Before setting up audit auditing check if you are using a ["Downlevel Client"](/documentation/articles/sql-database-auditing-and-dynamic-data-masking-downlevel-clients).


##<a id="subheading-2"></a>Set up auditing for your database

1. Launch the <a href="https://manage.windowsazure.cn" target="_blank">Azure Preview Portal</a> at https://manage.windowsazure.cn. Alternatively, you can also launch the <a href= "https://manage.windowsazure.cn/" target="_bank">Classic Azure Management Portal</a> at https://manage.windowsazure.cn/. Refer to details below.

2. navigate to the configuration blade of the SQL Database / SQL Server you want to audit. Click the **Settings** button on top and then, in the Setting blade, and select **Auditing**.

	![][1]

3. In the auditing configuration blade, select STORAGE DETAILS to open the Audit Logs Storage Blade. Select the Azure storage account where logs will be saved and, the retention period. **Tip:** Use the same storage account for all audited databases to get the most out of the preconfigured reports templates.

	![][2]

4. Under **LOGGING BY EVENT**, click **SUCCESS** and **FAILURE** to log all events, or choose individual event categories.


5. If you are configuring Auditing for a SQL Database, Click on **To enforce auditing click here ...** and on **SECURITY ENABLED ACCESS** select **REQUIRED**. If you are configuring Auditing for a SQL Server you have two options: (a) after step #6, navigate for each SQL database on the server and apply this step, or (2) [Modify Server FDQN in the connection string](/documentation/articles/sql-database-auditing-and-dynamic-data-masking-downlevel-clients).


	![][5]

6. Click **OK**.



##<a id="subheading-3">Analyze audit logs and reports</a>

Audit logs are aggregated in a collection of Store Tables with a **SQLDBAuditLogs** prefix in the Azure storage account you chose during setup. You can view log files using a tool such as <a href="http://azurestorageexplorer.codeplex.com/" target="_blank">Azure Storage Explorer</a>.

A preconfigured dashboard report template is available as a <a href="http://download.microsoft.com/download/D/8/D/D8D90BA1-977F-466B-A839-7823FF37FD02/01-Azure%20SQL%20DB%20Audit%20Logs%20Report%20Template.xlsx" target="_blank">downloadable Excel spreadsheet</a> to help you quickly analyze log data. To use the template on your audit logs, you need Excel 2013 or later and Power Query, which you can download <a href="http://www.microsoft.com/download/details.aspx?id=39379">here</a>. 

The template has fictional sample data in it, and you can set up Power Query to import your audit log directly from your Azure storage account. 

For more detailed instructions on working with the report template, read the <a href="http://go.microsoft.com/fwlink/?LinkId=506731">How To (doc download)</a>.

![][6]


##<a id="subheading-4"></a>Set up auditing for your database using the Classic Azure Management Portal

1. Launch the <a href= "https://manage.windowsazure.cn/" target="_bank">Classic Azure Management Portal</a> at https://manage.windowsazure.cn/.
 
2.   Click the SQL Database / SQL Server you want to audit, and then click the **AUDITING & SECURITY** tab. 

3.   If you are configuring Auditing for a SQL Database, On **SECURITY ENABLED ACCESS** select **REQUIRED**. If you are configuring Auditing for a SQL Server you have two options: (a) after step #7, navigate for each SQL database on the server and apply this step, or (2) [Modify Server FDQN in the connection string](/documentation/articles/sql-database-auditing-and-dynamic-data-masking-downlevel-clients).

4. At the auditing section click **ENABLED**.


	![][7]

5. Edit the **LOGGING BY EVENT** as needed.

	![][8]

6. Select a **STORAGE ACCOUNT** and configure **RETENTION**. 

	![][11]

7. Click **SAVE**.




##<a id="subheading-3">Practices for usage in production</a>
The description in this section refers to screen captures above. Either <a href="https://manage.windowsazure.cn" target="_blank">Azure Preview Portal</a> or <a href= "https://manage.windowsazure.cn/" target="_bank">Classic Azure Management Portal</a> may be used.
 

##<a id="subheading-4"></a>Storage Key Regeneration

In production you are likely to refresh your storage keys periodically. When refresh your keys you need to re-save the policy. The process is as follows:.


1. In the auditing configuration blade (described above in the set up auditing section) switch the **Storage Access Key** from *Primary* to *Secondary* and **SAVE**.
![][10]
2. Go to the storage configuration blade and **regenerate** the *Primary Access Key*.

3. Go back to the auditing configuration blade, switch the **Storage Access Key** from *Secondary* to *Primary* and press **SAVE**.

4. Go back to the storage UI and **regenerate** the *Secondary Access Key* (as preparation for the next keys refresh cycle.
  
##<a id="subheading-4"></a>Automation
There are several PowerShell cmdlets you can use to configure auditing in Azure SQL Database:

- [Get-AzureRMSqlDatabaseAuditingPolicy](https://msdn.microsoft.com/zh-cn/library/azure/mt603731.aspx)
- [Get-AzureRMSqlServerAuditingPolicy](https://msdn.microsoft.com/zh-cn/library/azure/mt619329.aspx)
- [Remove-AzureRMSqlDatabaseAuditing](https://msdn.microsoft.com/zh-cn/library/azure/mt603796.aspx)
- [Remove-AzureRMSqlServerAuditing](https://msdn.microsoft.com/zh-cn/library/azure/mt603574.aspx)
- [Set-AzureRMSqlDatabaseAuditingPolicy](https://msdn.microsoft.com/zh-cn/library/azure/mt603531.aspx)
- [Set-AzureRMSqlServerAuditingPolicy](https://msdn.microsoft.com/zh-cn/library/azure/mt603794.aspx)
- [Use-AzureRMSqlServerAuditingPolicy](https://msdn.microsoft.com/zh-cn/library/azure/mt619353.aspx)






<!--Anchors-->
[Azure SQL Database Auditing basics]: #subheading-1
[Set up auditing for your database]: #subheading-2
[Analyze audit logs and reports]: #subheading-3
[Set up auditing for your database using the Classic Azure Management Portal]: #subheading-4


<!--Image references-->
[1]: ./media/sql-database-auditing-get-started/sql-database-get-started-auditingpreview.png
[2]: ./media/sql-database-auditing-get-started/sql-database-get-started-storageaccount.png
[3]: ./media/sql-database-auditing-get-started/sql-database-auditing-eventtype.png
[5]: ./media/sql-database-auditing-get-started/sql-database-get-started-connectionstring.png
[6]: ./media/sql-database-auditing-get-started/sql-database-auditing-dashboard.png
[7]: ./media/sql-database-auditing-get-started/sql-database-auditing-classic-portal-enable.png
[8]: ./media/sql-database-auditing-get-started/sql-database-auditing-classic-portal-configure.png
[9]: ./media/sql-database-auditing-get-started/sql-database-auditing-security-enabled-access.png
[10]: ./media/sql-database-auditing-get-started/sql-database-auditing-storage-account.png
[11]: ./media/sql-database-auditing-get-started/sql-database-auditing-classic-portal-configure-storage.png






<!--Link references-->
[Link 1 to another azure.microsoft.com documentation topic]: /documentation/articles/virtual-machines-windows-tutorial
[Link 2 to another azure.microsoft.com documentation topic]: /documentation/articles/web-sites-custom-domain-name
[Link 3 to another azure.microsoft.com documentation topic]: /documentation/articles/storage-whatis-account

 
