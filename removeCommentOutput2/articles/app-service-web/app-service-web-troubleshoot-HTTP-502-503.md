<!-- rename to app-service-web-troubleshoot-http-502-http-503 -->

<properties
	pageTitle="Troubleshoot: web app unavailable due to HTTP 502/503"
	description="This article helps you troubleshoot HTTP 502/503 errors in your web app hosted in Azure Web App."
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

# Troubleshoot: web app unavailable due to HTTP 502/503

This article helps you troubleshoot HTTP 502/503 errors in your web app hosted in [Azure Web App](/documentation/services/web-sites/).

If you need more help at any point in this article, you can contact the Azure experts on [the MSDN Azure and the CSDN Azure](/support/forums/). Alternatively, you can also file an Azure support incident. Go to the [Azure Support site](/support/contact/) and click on **Get Support**.

## Symptom

When you browse to the web app, it returns a HTTP "502 Bad Gateway" or a HTTP "503 Service Unavailable".

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

####	Monitor your web app

This page let you find out if your application is having any issues. In Azure Management Portal, click **Monitor** of your web app.

Some of the metrics that you might want to monitor for your web app are

-	Average memory working set
-	Average response time
-	CPU time
-	Memory working set
-	Requests

![](./media/app-service-web-troubleshoot-HTTP-502-503/1-monitor-metrics.png)

For more information, see:

-	[Monitor Web Apps in Azure](/documentation/articles/web-sites-monitor/)

<a name="collect"></a>
### 2. Collect data

####	Use the FTP Diagnostic Logs

Find the FTP Diagnostic Logs link in your web app's **Dashboard** page, which usually looks like `ftp://********.ftp.chinacloudsites.chinacloudapi.cn/LogFiles`. Click to enter, and download **eventlog.xml**

<a name="mitigate"></a>
### 3. Mitigate the issue

####	Scale the web app

In Azure Web App, for increased performance and throughput,  you can adjust the scale at which you are running your application. Scaling up a web app involves two related actions: changing your App Service plan to a higher pricing tier, and configuring certain settings after you have switched to the higher pricing tier.

For more information on scaling, see [Scale a web app in Azure](/documentation/articles/web-sites-scale/).

Additionally, you can choose to run your application on more than one instance . This not only provides you with more processing capability, but also gives you some amount of fault tolerance. If the process goes down on one instance, the other instance will still continue serving requests.

You can set the scaling to be Manual or Automatic.

####	Use AutoHeal

AutoHeal recycles the worker process for your app based on settings you choose (like configuration changes, requests, memory-based limits, or the time needed to execute a request). Most of the time, recycle the process is the fastest way to recover from a problem. Though you can always restart the web app from directly within the Azure Management Portal, AutoHeal will do it automatically for you. All you need to do is add some triggers in the root web.config for your web app. Note that these settings would work in the same way even if your application is not a .Net one.

For more information, see [Auto-Healing Azure Web Sites](/blog/auto-healing-windows-azure-web-sites/).


####	Restart the web app

This is often the simplest way to recover from one-time issues. On the [Azure Management Portal](https://manage.windowsazure.cn/), on your web app's blade, you have the options to stop or restart your app.

 ![](./media/app-service-web-troubleshoot-HTTP-502-503/2-restart.png)

You can also manage your web app using Azure Powershell. For more information, see
[Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager/).
