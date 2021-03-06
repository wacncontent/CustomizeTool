<properties 
   pageTitle="Azure SDK for .NET 2.6 Release Notes" 
   description="Azure SDK for .NET 2.6 Release Notes" 
   services="app-service/web" 
   documentationCenter=".net" 
   authors="Juliako" 
   manager="dwrede" 
   editor=""/>

<tags
	ms.service="app-service"
	ms.date="08/08/2015"
	wacn.date=""/>


# Azure SDK for .NET 2.6 Release Notes

This document contains the release notes for the Azure SDK for .NET 2.6 release. 

With Azure SDK 2.6 you can develop cloud service applications (PaaS) targeting .NET 4.5.2 or .NET 4.6 provided that you manually install the target .NET Framework on the Cloud Service Role. See [Install .NET on a Cloud Service Role](/documentation/articles/cloud-services-dotnet-install-dotnet/).


##Service Bus updates

- Event Hubs: 

	- Now allows targeted access control when sending events by exposing additional publisher endpoint for Event Hubs.
	- Additional stability and improvement added to Event Hubs feature.
	- Adding support of Amqp protocol over WebSocket for messaging and Event Hubs.

##HDInsight Tools for Visual Studio updates

- **IntelliSense enhancement**: remote metadata suggestion

	Now HDInsight Tools for Visual Studio supports getting remote metadata when you are editing your Hive script. For example, you can type **SELECT * FROM** and all the table names will be shown. Also, the column names will be shown after specifying a table.

- **HDInsight emulator support**

	Now HDInsight Tools for Visual Studio support connecting to HDInsight emulator, so you could develop your Hive scripts locally without introducing any cost, then execute those scripts against your HDInsight clusters. 

	For more information, refer to [this manual](/documentation/articles/hdinsight-hadoop-emulator-get-started/).

- **HDInsight Tools for Visual Studio support for generic Hadoop clusters** (Preview)

	Now HDInsight Tools for Visual Studio support generic Hadoop clusters, so you can use HDInsight Tools for Visual Studio to do the following:

	- connect to your cluster, 
	- write Hive query with enhanced IntelliSense/auto-completion support, 
	- view all the jobs in your cluster with an intuitive UI. 

	For more information, refer to [this manual](/documentation/articles/hdinsight-hadoop-emulator-get-started/).

##In-Role Cache updates

- **In-Role Cache** was updated to use **Microsoft Azure Storage SDK** version 4.3. Until now, the **In-Role Cache** was using Azure Storage SDK version 1.7.

	Customers using Azure SDK 2.5 or below should update to Azure SDK 2.6 and move to the new version of Azure Storage SDK. Note that Azure Storage version 2011-08-18 will be removed on December 9th, 2015. For more details read [this announcement](http://azure.microsoft.com/blog/2014/08/04/microsoft-azure-storage-service-version-removal/). 

	For more information, see [In-Role Cache for Azure Cache](https://msdn.microsoft.com/zh-cn/library/azure/dn386103.aspx).

##Azure Websites Tools

The following items were updated in the Azure SDK 2.6 release.

- Azure publishing enhanced to include Azure API Apps as a deployment target.
- API Apps provisioning functionality to enable users with API App creation and provisioning functionality.
- Server Explorer changed to reflect new Azure Websites node, with Web, Mobile, and API apps grouped by Resource Group.
- Add Azure API App Client gesture added to most C# projects that will enable automatic generation of Swagger-enabled API Apps running in a user’s Azure subscription.
- API Apps tooling and Azure Websites nodes in Server Explorer are available in Visual Studio 2013 only. 

##Azure Resource Manager Tools updates

The Azure resource manager tools have been updated to include templates for Virtual Machines, Networking and Storage. The JSON editing experience has been updated to include a new outline view for templates and the ability to edit the templates using JSON snippets. Templates deployed from Visual Studio use a PowerShell script provided with the project, so any changes made to the script will be used by Visual Studio.

##Diagnostics improvements for Cloud Services

Azure SDK 2.6 brings back support for collecting diagnostics logs in the Azure compute emulator and transferring them to development storage. Any diagnostics logs (including application trace Logs, Event Tracing for Windows (ETW) logs, performance counters, infrastructure logs and windows event logs) generated when the application is running in the emulator can be transferred to development storage to verify that your diagnostics logging is working on your local machine. 

The Diagnostics storage account can now be specified in the service configuration (.cscfg) file making it easier to use different diagnostics storage accounts for different environments. There are some notable differences between how the connection string worked in Azure SDK 2.4 and Azure SDK 2.6. For more information on how to use the Diagnostics Storage connection string and how it impacts your projects see [Configuring Diagnostics for Azure Cloud Services](https://msdn.microsoft.com/zh-cn/library/azure/dn186185.aspx#BKBM_Changes).

##Breaking changes

###Azure Resource Manager Tools 

- The **Cloud Deployment Projects** project type available in the Azure SDK 2.5 has been renamed to **Azure Resource Group**.
- **Cloud Deployment Projects** type of projects created in the Azure SDK 2.5 can be used in 2.6 but deploying the template from Visual Studio will fail. However, deploying with the PowerShell script will still work as it did previously.  For information on how to use **Cloud Deployment Projects** in 2.6 read this [post](https://msdn.microsoft.com/zh-cn/library/azure/dn872471.aspx).
 
##Known issues

- Collecting diagnostics logs in the emulator requires a 64-bit operating system. Diagnostics logs will not be collected when running on a 32-bit operating system. This does not affect any other emulator functionality. 

- Azure SDK 2.6 released on 4/29/2015 had two issues: 

	- Universal App could not be loaded in Visual Studio 2015 when Azure SDK 2.6 was installed on the machine.
	- Debugging a Cloud Service project would fail in Visual Studio 2013 and Visual Studio 2015 where Visual Studio becomes unresponsive and crashes while displaying a dialog box with the message "Configuring diagnostics for emulator".
	
	An update to Azure SDK 2.6 was released on 5/18/2015. The updated version is 2.6.30508.1601; it contains fixes for two issues described above. You can identify the build of the SDK from Control Panel -> Programs and Features -> Microsoft Azure Tools for Microsoft Visual Studio 2013 – v 2.6. The Version column will display the build number.

	If you are still facing the above issues, install the latest version of the Azure 2.6 SDK for [VS 2012](http://go.microsoft.com/fwlink/p/?linkid=323511&clcid=0x409), [VS 2013](https://www.microsoft.com/web/handlers/webpi.ashx/getinstaller/VWDOrVs2013AzurePack.appids) or [VS 2015](http://go.microsoft.com/fwlink/?linkid=518003&clcid=0x409).
 
##See Also

[Support and Retirement Information for the Azure SDK for .NET and APIs](https://msdn.microsoft.com/zh-cn/library/azure/dn479282.aspx/)
