<properties
	pageTitle="Troubleshoot: performance degradation in a web app"
	description="This article helps you troubleshoot performance issues in your web app hosted in Azure Web App."
	services="app-service\web"
	documentationCenter=""
	authors="cephalin"
	manager="wpickett"
	editor=""
	tags="top-support-issue"/>

<tags
	ms.service="app-service-web"
	ms.date="01/13/2016"
	wacn.date=""/>

# Troubleshoot: performance degradation in a web app

This article helps you troubleshoot performance issues in your web app hosted in [Azure Web App](/documentation/services/web-sites/).

If you need more help at any point in this article, you can contact the Azure experts on [the MSDN Azure and the CSDN Azure](/support/forums/). Alternatively, you can also file an Azure support incident. Go to the [Azure Support site](/support/contact/) and click on **Get Support**.

## Symptom

When you browse the web app, the pages load slowly and sometimes timeout.

## Cause

This problem is often caused by application level issues, such as:

-	requests taking a long time
-	application using high memory/CPU
-	application crashing due to an exception.

## Troubleshooting steps

Troubleshooting can be divided into three distinct tasks, in sequential order:

1.	[Observe and monitor application behavior](#observe)
2.	[Collect data](#collect)
3.	[Mitigate the issue](#mitigate)

[Azure Web Apps](/home/features/web-site/) gives you various options at each step.

<a name="observe"></a>
### 1. Observe and monitor application behavior

#### Monitor your web app

This option enables you to find out if your application is having any issues. In your web appâs blade, click the **Requests and errors** tile. The **Metric** blade will show you all the metrics you can add.

Some of the metrics that you might want to monitor for your web app are

-	Average memory working set
-	Average response time
-	CPU time
-	Memory working set
-	Requests

![](./media/app-service-web-troubleshoot-performance-degradation/1-monitor-metrics.png)

For more information, see:

-	[Monitor Web Apps in Azure](/documentation/articles/web-sites-monitor)
-	[Receive alert notifications](/documentation/articles/insights-receive-alert-notifications)

#### Monitor web endpoint status

If you are running your web app in the **Standard** pricing tier, Web Apps lets you monitor 2 endpoints from 3 geographic locations.

Endpoint monitoring configures web tests from geo-distributed locations that test response time and uptime of web URLs. The test performs an HTTP GET operation on the web URL to determine the response time and uptime from each location. Each configured location runs a test every five minutes.

Uptime is monitored using HTTP response codes, and response time is measured in milliseconds. A monitoring test fails if the HTTP response code is greater than or equal to 400 or if the response takes more than 30 seconds. An endpoint is considered available if its monitoring tests succeed from all the specified locations.

To set it up, see [How to: Monitor web endpoint status](/documentation/articles/web-sites-monitor#webendpointstatus).

<a name="collect"></a>
### 2. Collect data

####	Enable diagnostics logging for your web app

The Web Apps environment provides diagnostic functionality for logging information from both the web server and the web application. These are logically separated into web server diagnostics and application diagnostics.

##### Web server diagnostics

You can enable or disable the following kinds of logs:

-	**Detailed Error Logging** - Detailed error information for HTTP status codes that indicate a failure (status code 400 or greater). This may contain information that can help determine why the server returned the error code.
-	**Failed Request Tracing** - Detailed information on failed requests, including a trace of the IIS components used to process the request and the time taken in each component. This can be useful if you are attempting to improve web app performance or isolate what is causing a specific HTTP error.
-	**Web Server Logging** - Information about HTTP transactions using the W3C extended log file format. This is useful when determining overall web app metrics, such as the number of requests handled or how many requests are from a specific IP address.

##### Application diagnostics

Application diagnostics enables you to capture information produced by a web application. ASP.NET applications can use the `System.Diagnostics.Trace` class to log information to the application diagnostics log.

For detailed instructions on how to configure your application for logging, see [Enable diagnostics logging for web apps in Azure](/documentation/articles/web-sites-enable-diagnostic-log).

#### Use Remote Profiling

In Azure Web App, Web Apps and WebJobs can be remotely profiled. If your process is running slower than expected, or the latency of HTTP requests are higher than normal and the CPU usage of the process is also high, you can remotely profile your process and get the CPU sampling call stacks to analyze the process activity and code hot paths.

For more information on, see [Remote Profiling support in Azure Web App](/blog/remote-profiling-support-in-azure-app-service).

<a name="mitigate"></a>
### 3. Mitigate the issue

####	Scale the web app

In Azure Web App, for increased performance and throughput,  you can adjust the scale at which you are running your application. Scaling up a web app involves two related actions: changing your App Service plan to a higher pricing tier, and configuring certain settings after you have switched to the higher pricing tier.

For more information on scaling, see [Scale a web app in Azure](/documentation/articles/web-sites-scale).

Additionally, you can choose to run your application on more than one instance . This not only provides you with more processing capability, but also gives you some amount of fault tolerance. If the process goes down on one instance, the other instance will still continue serving requests.

You can set the scaling to be Manual or Automatic.

####	Use AutoHeal

AutoHeal recycles the worker process for your app based on settings you choose (like configuration changes, requests, memory-based limits, or the time needed to execute a request). Most of the time, recycle the process is the fastest way to recover from a problem. Though you can always restart the web app from directly within the Azure Management Portal, AutoHeal will do it automatically for you. All you need to do is add some triggers in the root web.config for your web app. Note that these settings would work in the same way even if your application is not a .Net one.

For more information, see [Auto-Healing Azure Web Sites](/blog/auto-healing-windows-azure-web-sites/).

####	Restart the web app

This is often the simplest way to recover from one-time issues. On the [Azure Management Portal](https://manage.windowsazure.cn/), on your web appâs blade, you have the options to stop or restart your app.

 ![](./media/app-service-web-troubleshoot-performance-degradation/2-restart.png)

You can also manage your web app using Azure Powershell. For more information, see
[Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager).
