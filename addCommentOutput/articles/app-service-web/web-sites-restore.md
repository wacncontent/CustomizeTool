<properties 
	pageTitle="Restore an app in Azure Web App" 
	description="Learn how to restore your app from a backup." 
	services="app-service" 
	documentationCenter="" 
	authors="cephalin" 
	manager="wpickett" 
	editor="jimbe"/>

<tags
	ms.service="app-service"
	ms.date="01/26/2016"
	wacn.date=""/>

# Restore an app in Azure

This article shows you how to restore an Azure Web App that you have previously backed up by using the [Azure Web  App](/documentation/services/web-sites/)  App](/documentation/services/web-sites)  Backup feature. For more information, see [Azure  Web App  Backups](/documentation/articles/web-sites-backup/).

The Azure  web app  Restore feature lets you restore your app with its linked databases (SQL Database or MySQL) on-demand to a previous state, or create a new app based on one of your original app's backup. Creating a new app that runs in parallel to the latest version can be useful for A/B testing.


The Azure Restore feature, available on the **Backups** blade in the [Azure Portal](https://portal.azure.cn), is available only in Standard and Premium pricing tiers. For information about scaling your app using Standard or Premium tier, see [Scale an app in Azure Web App](/documentation/articles/web-sites-scale/). Note that the Premium tier allows a greater number of daily backups to be performed over the Standard tier.


The Azure web app Restore feature, available on the **Backups** blade in the [Azure Classic Management Portal](https://manage.windowsazure.cn), is available only in Standard pricing tiers. For information about scaling your app using Standard tier, see [Scale an app in Azure Web App](/documentation/articles/web-sites-scale/).


<a name="PreviousBackup"></a>
## To Restore an app from a previously made backup


1. On the **Settings** blade of your app in the Azure Portal, click **Backups** to display the **Backups** blade. Then click **Restore Now** in the command bar. 
	
	![Choose restore now][ChooseRestoreNow]

3. In the **Restore** blade, first select the backup source. 

	![](./media/web-sites-restore/021ChooseSource.png)
	
	The **App backup** option shows you all the backups that are created directly by the app itself, since these are the only ones that the apps are aware of. You can easily select one. 
	The **Storage** option lets you select the actual backup ZIP file from the storage account and container that's configured in your **Backups** blade. If there are backup files from any other apps in 
	the container, then you can select them to restore as well.  

4. Then, specify the destination for the app restore in **Restore destination**.

	![](./media/web-sites-restore/022ChooseDestination.png)
	
	>[AZURE.WARNING] If you choose **Overwrite**, all data related to your existing app will be erased. Before you click **OK**,
	make sure that it is exactly what you want to do.
	
	You can select **Existing App** to restore the app backup to another app in the same resoure group. Before you use this option, 
	you should have already created another app in your resource group with mirroring database configuration to the one defined
	in the app backup. 
	
5. Click **OK**.



1. On the **Backups** tab, click **Restore Now** in the command bar at the bottom of the portal page. The **Restore Now** dialog box appears.
	
	![Choose backup source][ChooseBackupSource]
	
2. Under **Choose backup source**, select **Previous Backup for this  Website**.
3. Select the date of the backup that you want to restore, and then click the right arrow to continue.
4. Follow the steps in the [Choose Your  Website Restore Settings](#RestoreSettings) section later in this article.

<a name="StorageAccount"></a>
## Download or delete a backup from a storage account

	
1. From the main **Browse** blade of the Azure Portal, select **Storage Accounts**.
	
	A list of your existing storage accounts will be displayed. 
	
2. Select the storage account that contains the backup that you want to download or delete.
	
	The **STORAGE** blade will be displayed.

3. Select the **Containers** part in the **STORAGE** blade to display the **Containers** blade.
	
	A list of containers will be displayed. This list will also show the URL and the date of when this container was last modified.
	
	![View Containers][ViewContainers]

4. In the list, select the container and display the blade that shows a list of file names, along with the size of each file.
	
5. By selecting a file, you can either choose to **Download** or **Delete** the file. Note that there are two primary file types, .zip files and .xml files. 



1. On the **Backups** tab, click **Restore Now** in the command bar at the bottom of the portal page. The **Restore Now** dialog box appears.
	
	![Choose backup source][ChooseBackupSource]
	
2. Under **Choose backup source**, select **Storage Account File**. Here you can directly specify the URL for the storage account file, or click the folder icon to navigate to blob storage and specify the backup file. This example chooses the folder icon.
	
	![Storage Account File][StorageAccountFile]
	
3. Click the folder icon to open the **Browse Cloud Storage** dialog box.
	
	![Browse Cloud Storage][BrowseCloudStorage]
	

4. Expand the name of the storage account that you want to use, and then select ** Websitebackups**, which contains your backups.
5. Select the zip file containing the backup that you want to restore, and then click **Open**.
6. The Storage account file has been selected and shows in the storage account box. Click the right arrow to continue.
	
	![Storage Account File Selected][StorageAccountFileSelected]
	
7. Continue with the section that follows, [Choose Your  Website Restore Settings and Start the Restore Operation](#RestoreSettings).

<a name="RestoreSettings"></a>
##Choose Your  Website Restore Settings and Start the Restore Operation
1. Under **Choose your  Website restore settings**, **Restore To**, select either **Current  Website** or **New  Website instance**.
	
	![Choose your  Website restore settings][ChooseRestoreSettings]
	
	If you select **Current  Website**, your existing  Website will be overwritten by the backup that you selected (destructive restore). All changes you have made to the  Website since the time of the chosen backup will be permanently removed, and the restore operation cannot be undone. During the restore operation, your current  Website will be temporarily unavailable, and you will be warned to this effect.
	
	If you select **New  Website instance**, a new  Website will be created in the same region with the name that you specify. (By default, the new name is **restored-***old WebsiteName*.) 
	
	The site that you restore will contain the same content and configuration that were made in the portal for the original site. It will also include any databases that you choose to include in the next step.
2. If you want to restore a database along with your  Website, under **Included Databases**, select the name of the database server that you want to restore the database to by using the dropdown under **Restore To**. You can also choose to create a new database server to restore to, or choose **Don't Restore** to not restore the database, which is the default. 
	
	After you have chosen the server name, specify the name of the target database for the restore in the **Database Name** box.
	
	If your restore includes one or more databases, you can select **Automatically adjust connection strings** to update your connection strings stored in the backup to point to your new database, or database server, as appropriate. You should verify that all functionality related to databases works as expected after the restore completes.
	
	![Choose database server host][ChooseDBServer]
	
	> [AZURE.NOTE] You cannot restore a SQL database with the same name to the same SQL Server. You must choose either a different database name or a different SQL Server host to restore the database to. 
	
	> [AZURE.NOTE] You can restore a MySQL database with the same name to the same server, but be aware that this will clear out the existing content stored in the MySQL database.	
	
3. If you choose to restore an existing database, you will need to provide a user name and password. If you choose to restore to a new database, you will need to provide a new database name:
	
	![Restore to a new SQL database][RestoreToNewSQLDB]
	
	Click the right arrow to continue.	
4. If you chose to create a new database, you will need to provide credentials and other initial configuration information for the database in the next dialog. The example here shows a new SQL database. (The options for a new MySQL database are somewhat different.)
	
	![New SQL database settings][NewSQLDBConfig]
	
5. Click the check mark to start the restore operation. When it completes, the new  Website instance (if that is the restore option you chose) will be visible in the list of  Websites in the portal.
	
	![Restored Contoso  Website][RestoredContoso Website]


<a name="OperationLogs"></a>
## View the Audit Logs

	
1. To see details about the success or failure of the app restore operation, select the **Audit Log** part of the main **Browse** blade. 
	
	The **Audit log** blade displays all of your operations, along with level, status, resource, and time details.
	
2. Scroll the blade to find operations related to your app.
3. To view additional details about an operation, select the operation in the list.
	
The details blade will display the available information related to the operation.
	
>[AZURE.NOTE] If you want to get started with Azure before signing up for an Azure account, go to [Try Azure Web App](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure. No credit cards required; no commitments.
## Next Steps
You can also backup and restore Azure Web Apps using REST API (see [Use REST to back up and restore Azure Web Apps](/documentation/articles/websites-csm-backup/)).

## What's changed
* For a guide to the change from Websites to Azure see: [Azure and Its Impact on Existing Azure Services](/documentation/services/web-sites/)



1. To see details about the success or failure of the  Website restore operation, go to the  Website's Dashboard tab. In the **Quick Glance** section, under **Management Services**, click **Operation Logs**.
	
	![Dashboard - Operation Logs Link][DashboardOperationLogsLink]
	
2. You are taken to the Management Services portal **Operation Logs** page, where you can see the log for your restore operation in the list of operation logs:
	
	![Management Services Operation Logs page][ManagementServicesOperationLogsList]
	
3. To view details about the operation, select the operation in the list, and then click the **Details** button in the command bar.
	
	![Details Button][DetailsButton]
	
	When you do so, the **Operations Details** window opens and shows you the copiable contents of the log file:
	
	![Operation Details][OperationDetails]


<!-- IMAGES -->

[RestoredContoso Website]: ./media/web-sites-restore/09RestoredContosoWebSite.png

[ChooseRestoreNow]: ./media/web-sites-restore/02ChooseRestoreNow.png
[ViewContainers]: ./media/web-sites-restore/03ViewContainers.png
[StorageAccountFile]: ./media/web-sites-restore/02StorageAccountFile.png
[BrowseCloudStorage]: ./media/web-sites-restore/03BrowseCloudStorage.png
[StorageAccountFileSelected]: ./media/web-sites-restore/04StorageAccountFileSelected.png
[ChooseRestoreSettings]: ./media/web-sites-restore/05ChooseRestoreSettings.png
[ChooseDBServer]: ./media/web-sites-restore/06ChooseDBServer.png
[RestoreToNewSQLDB]: ./media/web-sites-restore/07RestoreToNewSQLDB.png
[NewSQLDBConfig]: ./media/web-sites-restore/08NewSQLDBConfig.png
[RestoredContosoWebSite]: ./media/web-sites-restore/09RestoredContosoWebSite.png
[DashboardOperationLogsLink]: ./media/web-sites-restore/10DashboardOperationLogsLink.png
[ManagementServicesOperationLogsList]: ./media/web-sites-restore/11ManagementServicesOperationLogsList.png
[DetailsButton]: ./media/web-sites-restore/12DetailsButton.png
[OperationDetails]: ./media/web-sites-restore/13OperationDetails.png
