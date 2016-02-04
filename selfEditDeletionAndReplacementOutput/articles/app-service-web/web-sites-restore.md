deletion:

deleted:

		[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)]

reason: (terminology: Azure App Service Web)

deleted:

		>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

reason: (“Try it now”)

deleted:

		## What's changed
		* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
		* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

reason: (terminology: Azure App Service Web, the new Ibiza portal)

deleted:

		Note that the Premium mode allows a greater number of daily backups to be performed over the Standard mode.

reason: (Premium mode)

replacement:

deleted:

		preview portal

replaced by:

		Management Portal

reason: (the new Ibiza portal)

deleted:

		1. On the **Settings** blade of your web app in the Azure Management Portal, click the **Backups** option to display the **Backups** blade. Scroll in this blade and select one of the backup item based on the **BACKUP TIME** and the **STATUS** from the backup list.
			
			![Choose backup source][ChooseBackupSource]
			
		2. Select **Restore Now** at the top of the **Backups** blade. 
		
			![Choose restore now][ChooseRestoreNow]
		
		3. In the **Restore** blade, to restore the existing web app, verify all the displayed details and then click **OK**. 
			
		You can also restore your web app to a new web app by selecting the **WEB APP** part from the **Restore** blade and selecting the **Create a new web app** part.

replaced by:

		1. On the **Backups** tab, click **Restore Now** in the command bar at the bottom of the portal page. The **Restore Now** dialog box appears.
			
			![Choose backup source][ChooseBackupSource]
			
		2. Under **Choose backup source**, select **Previous Backup for this  Website**.
		3. Select the date of the backup that you want to restore, and then click the right arrow to continue.
		4. Follow the steps in the [Choose Your  Website Restore Settings](#RestoreSettings) section later in this article.

reason: (the new Ibiza portal)

deleted:

		1. From the main **Browse** blade of the Azure Management Portal, select **Storage Accounts**.
			
			A list of your existing storage accounts will be displayed. 
			
		2. Select the storage account that contains the backup that you want to download or delete.
			
			The **STORAGE** blade will be displayed.
		
		3. Select the **Containers** part in the **STORAGE** blade to display the **Containers** blade.
			
			A list of containers will be displayed. This list will also show the URL and the date of when this container was last modified.
			
			![View Containers][ViewContainers]
		
		4. In the list, select the container and display the blade that shows a list of file names, along with the size of each file.
			
		5. By selecting a file, you can either choose to **Download** or **Delete** the file. Note that there are two primary file types, .zip files and .xml files.

replaced by:

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

reason: (the new Ibiza portal)

deleted:

		1. To see details about the success or failure of the web app restore operation, select the **Audit Log** part of the main **Browse** blade. 
			
			The **Audio log** blade displays all of your operations, along with level, status, resource, and time details.
			
		2. Scroll the blade to find operations related to your web app.
		3. To view additional details about an operation, select the operation in the list.
			
		The details blade will display the available information related to the operation.

replaced by:

		1. To see details about the success or failure of the  Website restore operation, go to the  Website's Dashboard tab. In the **Quick Glance** section, under **Management Services**, click **Operation Logs**.
			
			![Dashboard - Operation Logs Link][DashboardOperationLogsLink]
			
		2. You are taken to the Management Services portal **Operation Logs** page, where you can see the log for your restore operation in the list of operation logs:
			
			![Management Services Operation Logs page][ManagementServicesOperationLogsList]
			
		3. To view details about the operation, select the operation in the list, and then click the **Details** button in the command bar.
			
			![Details Button][DetailsButton]
			
			When you do so, the **Operations Details** window opens and shows you the copiable contents of the log file:
			
			![Operation Details][OperationDetails]

reason: (the new Ibiza portal)

