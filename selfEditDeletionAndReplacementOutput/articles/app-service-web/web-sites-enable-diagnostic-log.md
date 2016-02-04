deletion:

deleted:

		## How to: View logs in Application Insights
		
		Visual Studio Application Insights provides tools for filtering and searching logs, and for correlating the logs with requests and other events.
		
		1. Add the Application Insights SDK to your project in Visual Studio.
		 * In Solution Explorer, right click your project and choose Add Application Insights. You'll be guided through steps that include creating an Application Insights resource. [Learn more](/documentation/articles/app-insights-start-monitoring-app-health-usage)
		2. Add the Trace Listener package to your project.
		 * Right click your project and choose Manage NuGet Packages. Select `Microsoft.ApplicationInsights.TraceListener` [Learn more](/documentation/articles/app-insights-asp-net-trace-logs)
		3. Upload your project and run it to generate log data.
		4. In the [Azure preview portal](http://manage.windowsazure.cn/), browse to your new Application Insights resource, and open **Search**. You'll see your log data, along with request, usage and other telemetry. Some telemetry might take a few minutes to arrive: click Refresh. [Learn more](/documentation/articles/app-insights-diagnostic-search)
		
		[Learn more about performance tracking with Application Insights](/documentation/articles/insights-perf-analytics)

reason: ({application insight})

deleted:

		> [AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

reason: (“Try it now”)

deleted:

		## What's changed
		* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
		* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

reason: (terminology: Azure App Service Web, the new Ibiza portal)

deleted:

		[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)]

reason: (terminology: Azure App Service Web)

replacement:

deleted:

		This article uses the [Azure preview portal](https://manage.windowsazure.cn/), Azure PowerShell, and the Azure Command-Line Interface (Azure CLI) to work with diagnostic logs. For information on working with diagnostic logs using Visual Studio, see [Troubleshooting Azure in Visual Studio](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio).

replaced by:

		This article uses the [Azure Management Portal](https://manage.windowsazure.cn/), Azure PowerShell, and the Azure Command-Line Interface (Azure CLI) to work with diagnostic logs. For information on working with diagnostic logs using Visual Studio, see [Troubleshooting Azure in Visual Studio](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio).

reason: (the new Ibiza portal)

deleted:

		To enable diagnostics in the [Azure preview portal](https://manage.windowsazure.cn), go to the blade for your web app and click **Settings > Diagnostics logs**.
		
		<!-- todo:cleanup dogfood addresses in screenshot -->
		![Logs part](./media/web-sites-enable-diagnostic-log/logspart.png)
		
		When you enable **application diagnostics** you also choose the **Level**. This setting allows you to filter the information captured to **informational**, **warning** or **error** information. Setting this to **verbose** will log all information produced by the application.
		
		> [AZURE.NOTE] Unlike changing the web.config file, enabling Application diagnostics or changing diagnostic log levels does not recycle the app domain that the application runs within.

replaced by:

		Diagnostics can be enabled by visiting the **Configure** page of your Azure  Website in the [Azure Management Portal](https://manage.windowsazure.cn). On the **Configure** page, use the **application diagnostics** and **site diagnostics** sections to enable logging.
		
		When enabling **application diagnostics** you must also select the **logging level** and whether to enable logging to the **file system**, **table storage**, or **blob storage**. While all three storage locations provide the same basic information for logged events, **table storage** and **blob storage** log additional information such as the instance ID, thread ID, and a more granular timestamp (tick format) than logging to **file system**.
		
		When enabling **site diagnostics**, you must select **storage** or **file system** for **web server logging**. Selecting **storage** allows you to select a storage account, and then a blob container that the logs will be written to. All other logs for **site diagnostics** are written to the file system only.

reason: (the new Ibiza portal)

