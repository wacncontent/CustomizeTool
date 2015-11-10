<properties
   pageTitle="Windows Azure AD Connect - Upgrade from Windows Azure AD sync tool (DirSync) | Windows Azure"
   description="Learn how to upgrade from DirSync to Azure AD Connect.  This articles describes the steps for upgrading your current Windows Azure AD sync tool (DirSync) to Azure AD Connect."
   services="active-directory"
   documentationCenter=""
   authors="shoatman"
   manager="stevenpo"
   editor="billmath"/>

<tags
	ms.service="active-directory"
	ms.date="09/02/2015"
	wacn.date=""/>

# Upgrading Windows Azure Active Directory sync (DirSync) to Azure Active Directory Connect

The following documentation will help you upgrade your existing DirSync installation to Azure AD Connect

## Download Azure AD Connect

To get started using Azure AD Connect you can download the latest version using the following: [Download Azure AD Connect](http://go.microsoft.com/fwlink/?LinkId=615771)

## Before you install Azure AD Connect
<!-- deleted by customization
Before you install Azure AD Connect and upgrade from DirSync, here are a few things you will need:  
-->
<!-- keep by customization: begin -->
Before you install Azure AD Connect, and upgrade from DirSync here are a few things you will need.  
<!-- keep by customization: end -->

- The password of the existing global administrator account for your Azure AD instance (The install will remind you which account this is)
- An Enterprise Administrator account for your local Active Directory
- Optional: If you configured DirSync to use a full version of SQL Server - The information for that database instance <!-- keep by customization: begin -->. <!-- keep by customization: end -->

### Parallel deployment

If you are currently synchronizing more than 50K objects then you will be given an option to perform a parallel deployment.  Parallel deployment requires a separate server or set of servers (if you require a separate server for SQL Server).  The benefit of parallel deployment is the opportunity to avoid synchronization downtime.  The Azure AD Connect installation will attempt to estimate the downtime that we expect, but if you've upgraded DirSync in the past <!-- deleted by customization, --> your own experience is likely to be the best guide.

## Installing Azure AD Connect

Download Azure AD Connect and copy to your existing DirSync server.  

1. Navigate to and double-click on AzureADConnect.msi
2. Begin stepping through the wizard

<!-- deleted by customization
For an in-place upgrade, the following high level steps occur:
-->
<!-- keep by customization: begin -->
For in-place upgrade the following high level steps occur:
<!-- keep by customization: end -->

1. Welcome to Azure AD Connect
2. Analysis of current DirSync Configuration
3. Collect Azure AD global admin password
4. Collect credentials for an enterprise admin account (only used during the installation of Azure AD Connect)
5. Installation of AAD Connect
<!-- deleted by customization
    * Uninstall DirSync
-->
<!-- keep by customization: begin -->
    * Unintall DirSync
<!-- keep by customization: end -->
	* Install AAD Connect
<!-- deleted by customization
	* Optionally begin synchronization

Additional steps/information are required when:
-->
<!-- keep by customization: begin -->
	* Optionally begin Synchronization

Additional steps/information is required when:
<!-- keep by customization: end -->

* You're currently using Full SQL Server - Local or Remote
* You have more than 50K objects in scope for synchronization

## In-place upgrade - less than 50K objects - SQL Express (Walkthrough)

0. Launch the Azure AD Connect Installer (MSI) <!-- deleted by customization. -->

1. Review and agree to license terms and privacy notice.

![Welcome to Azure AD](./media/active-directory-aadconnect-dirsync-upgrade-get-started/Welcome.png)

2. Click next to be analysis of your existing DirSync installation

![Analyzing existing Directory Sync installation](./media/active-directory-aadconnect-dirsync-upgrade-get-started/Analyze.png)

3. When the analysis completes <!-- deleted by customization, --> we will make recommendations on how to proceed.  In this scenario (less than 50K objects using SQL Express) the following screen is displayed <!-- deleted by customization: --><!-- keep by customization: begin -->. <!-- keep by customization: end -->

![Analysis completed ready to upgrade from DirSync](./media/active-directory-aadconnect-dirsync-upgrade-get-started/AnalysisReady.png)

4. Provide the password for the account you currently use to connect to Azure AD.

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/ConnectToAzureAD.png)

5. Provide an enterprise admin account for Active Directory.

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/ConnectToADDS.png)

6. You're now ready to configure.  When you <!-- deleted by customization click "Next," --><!-- keep by customization: begin --> clieck next <!-- keep by customization: end --> DirSync will be uninstalled and Azure AD Connect will be configured and begin synchronizing.

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/ReadyToConfigure.png)


## In-place upgrade - more than 50K objects
At step #3 you will see a different message if you have more than 50K objects in scope for synchronization.  A screen similar to the following will be displayed:

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/AnalysisRecommendParallel.png)

In this case we recommend you consider a parallel upgrade on a separate server.  Our reason for this recommendation is that depending on the size of your organization an in-place upgrade may impact your service level agreements with your business regarding how quickly changes in local Active Directory are reflected in Azure <!-- deleted by customization AD/Office --><!-- keep by customization: begin --> AD / Office <!-- keep by customization: end --> 365.  We attempt to estimate how long it may take for the first synchronization using Azure AD Connect.  As mentioned above, your own experience with the original installation of DirSync or upgrades to DirSync are likely to be the best indicator.

Parallel deployment requires a separate server or servers (if you are required to run SQL Server on a separate server from Azure AD Connect).  For that reason <!-- deleted by customization, --> it's completely reasonable to consider an in-place upgrade if it can be scheduled in <!-- deleted by customization a --> way to avoid impacts within your organization.

<!-- deleted by customization
To proceed with an in-place upgrade, click the checkbox next to this message: "Continue upgrading DirSync on this computer."
-->
<!-- keep by customization: begin -->
To proceed with an in-place upgrade click the checkbox next to the message: "Continue upgrading DirSync on this computer".
<!-- keep by customization: end -->

## In-place upgrade - Full SQL Server

At step #3 you will see a different message if your DirSync installation is using a local or remote full version of SQL Server.  A screen similar to the following will be displayed:

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/AnalysisReadyFullSQL.png)

The information regarding the existing SQL Server database server being used by DirSync is displayed to you.  <!-- deleted by customization Make --><!-- keep by customization: begin --> If need be make <!-- keep by customization: end --> the appropriate adjustments <!-- deleted by customization if needed -->.  Clicking "Next" will continue the installation.

## Parallel deployment - more than 50K objects

At step #3 <!-- deleted by customization, --> if you have more than 50K objects the Azure AD Connect installation will recommend a parallel deployment.  See "In-place upgrade - more than 50K objects" above for information on whether to choose in-place or pallell deployment of Azure AD Connect.   A screen similar to the following will be displayed:

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/AnalysisRecommendParallel.png)

If you want to proceed with parallel deployment you will need to perform the following steps:

- Click the "Export settings" button.  When you install Azure AD Connect on a separate server these settings will be imported to migrate any settings from your <!-- deleted by customization current --><!-- keep by customization: begin --> Current <!-- keep by customization: end --> DirSync to your new AAD Connect installation.

Once your settings have <!-- deleted by customization been --><!-- keep by customization: begin --> beens <!-- keep by customization: end --> successfully exported <!-- deleted by customization, --> you can exit the Azure AD Connect wizard on the DirSync server.

### Installation of Azure AD Connect on separate server

When you install Azure AD Connect on a new server it won't find DirSync and will assume that you want to perform a clean install of Azure AD Connect.  There are a couple of special steps here:

1. Run the Azure AD Connect installer (MSI) <!-- deleted by customization. -->
<!-- deleted by customization
2. When you see the "Welcome to Azure AD Connect" screen, exit the wizard by clicking the "X" in the top right corner of the window.
3. Open a command prompt <!-- deleted by customization. -->
-->
<!-- keep by customization: begin -->
2. When you see the "Welecome to Azure AD Connect" screen.  Exit the wizard by clicking the "X" in the top right corner of the windows.
3. Open a command prompt <!-- deleted by customization. -->
<!-- keep by customization: end -->
4. From the install location of Azure AD Connect (Default: C:\Program Files\Windows Azure Active Directory Connect) execute the following command:
<!-- deleted by customization
    * `AzureADConnect.exe /migrate`

Azure AD Connect connects and presents you with the following UI:

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/ImportSettings.png)

5. Select the settings file that exported from your DirSync installation.
6. Configure any advanced options including:
    * A custom installation location for Azure AD Connect
	* An existing instance of SQL Server (Default: Azure AD Connect installs SQL Server 2012 Express)
	* A service account used to connect to SQL Server (If your SQL Server database is remote then this account must be a domain service account)

See those options in the following UI:

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/advancedsettings.png)

7. Click "Next."
8. On the "Ready to configure" page, leave the "Start the synchronization process as soon as the configuration completes" checked.
[AZURE.NOTE] Synchronization between Windows Server Active Directory and Azure Active Directory will begin, but no changes will be exported to Azure AD.  Only one synchronization tool can be actively exporting changes at a time.
-->
<!-- keep by customization: begin -->
    * AzureADConnect.exe /migrate  

Azure AD Connects and presents you with the following UI:

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/ImportSettings.png)
 
5. Select the settings file that exported from your DirSync installation.    
6. Configure any advanced options including:  
   * A custom installation location for Azure AD Connect
   * An existing instance of SQL Server (Default: Azure AD Connect installs SQL Server 2012 Express)
   * A service account used to connect to SQL Server (If your SQL Server database is remote then this account must be a domain service account)

See those options in the following UI:  

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/advancedsettings.png) 
 
7. Click Next.   
8. On the "Ready to configure" page leave the "Start the synchronization process as soon as the configuration completes" checked.  

> [AZURE.NOTE] Synchronization between Windows Server Active Directory and Azure Active Directory will begin, but no changes will be exported to Azure AD.  Only one synchronization tool can be actively exporting changes at a time.
<!-- keep by customization: end -->
9. Click "Install".

<!-- keep by customization: begin --> > <!-- keep by customization: end --> [AZURE.NOTE] We uncheck the start synchronization checkbox in order to ensure that DirSync, which is still installed and running <!-- deleted by customization, --> and Azure AD Connect do not attempt to write to AAD at the same time.

### Check that Azure AD Connect is ready to begin sychronization

In order to determine whether or not Azure AD Connect is ready to <!-- deleted by customization take over --><!-- keep by customization: begin --> takeover <!-- keep by customization: end --> from DirSync you'll need to open the Azure AD Connect Synchronization Service Manager.  Searching <!-- deleted by customization for --><!-- keep by customization: begin --> using <!-- keep by customization: end --> "Synchronization" <!-- deleted by customization in --><!-- keep by customization: begin --> at <!-- keep by customization: end --> the Start <!-- deleted by customization Menu --><!-- keep by customization: begin --> menu <!-- keep by customization: end --><!-- keep by customization: begin --> of Windows <!-- keep by customization: end --> will reveal this application.

Within the application you <!-- keep by customization: begin --> will <!-- keep by customization: end --> will need to view the "Operations" tab.  On this tab you are looking to confirm that the following operations have been completed:

- Import on the AD Management Agent
- Import on the Azure AD Management Agent
- Full Sync on the AD Management Agent
- Full Sync on the Azure AD Management Agent

Once these 4 operations have been completed you're ready to uninstall DirSync and enable Azure AD Connect Synchronization.

### Uninstall DirSync (old Server)

- From within "Add or remove programs" locate "Windows Azure Active Directory sync tool"
- Uninstall "Windows Azure Active Directory sync tool"

### Open Azure AD Connect (new Server)
After installation <!-- deleted by customization, --> re-opening Azure AD connect will provide you with a configuration experience.  Open Azure AD Connect.

You should see the following:

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/AdditionalTasks.png)

* Select "Configure staging mode"
    * Upgrading from DirSync using exported settings automatically puts Azure AD Connect in staging mode.  Staging mode basically means that Synchronization will occur within Azure AD connect, but changes will not be exported to Azure AD or AD.
* Turn off staging by unchecking the "Enabled staging mode" checkbox.

![Enter your Azure AD credentials](./media/active-directory-aadconnect-dirsync-upgrade-get-started/configurestaging.png)

* Click the install button

<!-- deleted by customization
Congratulations! You've successfully migrated to Azure AD Connect using parallel deployment.
-->
<!-- keep by customization: begin -->
Congratulations you've successfully migrated to Azure AD Connect using Parallel deployment.
<!-- keep by customization: end -->

## Azure AD Connect supporting components

The following is a list of <!-- deleted by customization prerequisites --><!-- keep by customization: begin --> per-requisites <!-- keep by customization: end --> and supporting components that Azure AD Connect will install on the server that you set <!-- deleted by customization it --><!-- keep by customization: begin --> Azure AD Connect <!-- keep by customization: end --> up on.  This list is for a basic Express installation.  If you choose to use a different SQL Server on the Install <!-- deleted by customization Synchronization Services --><!-- keep by customization: begin --> synchronization services <!-- keep by customization: end --> page <!-- keep by customization: begin --> then <!-- keep by customization: end -->, <!-- deleted by customization then --> the SQL Server 2012 components listed below are not installed <!-- deleted by customization: --><!-- keep by customization: begin -->. <!-- keep by customization: end -->

- Forefront Identity Manager Azure Active Directory Connector
- Microsoft SQL Server 2012 Command Line Utilities
- Microsoft SQL Server 2012 Native Client
- Microsoft SQL Server 2012 Express LocalDB
- Azure Active Directory Module for Windows PowerShell
- Microsoft Online Services Sign-In Assistant for IT Professionals
- Microsoft Visual C++ 2013 Redistribution Package


**Additional Resources**

* [Use your on-premises identity infrastructure in the cloud](/documentation/articles/active-directory-aadconnect)
* [How Azure AD Connect works](/documentation/articles/active-directory-aadconnect-how-it-works)
* [Whats Next with Azure AD Connect](/documentation/articles/active-directory-aadconnect-whats-next)
* [Learn More](/documentation/articles/active-directory-aadconnect-learn-more)
* [Azure AD Connect on MSDN](/documentation/articles/active-directory-aadconnect)