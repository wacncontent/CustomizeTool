<properties
    pageTitle="Fix 502 bad gateway, 503 service unavailable errors | Azure"
    description="Troubleshoot 502 bad gateway and 503 service unavailable errors in your web app hosted in Azure App Service."
    services="app-service\web"
    documentationcenter=""
    author="cephalin"
    manager="wpickett"
    editor=""
    tags="top-support-issue"
    keywords="502 bad gateway, 503 service unavailable, error 503, error 502" />
<tags
    ms.assetid="51cd331a-a3fa-438f-90ef-385e755e50d5"
    ms.service="app-service-web"
    ms.workload="web"
    ms.tgt_pltfrm="na"
    ms.devlang="na"
    ms.topic="article"
    ms.date="07/06/2016"
    wacn.date=""
    ms.author="cephalin" />

# Troubleshoot HTTP errors of "502 bad gateway" and "503 service unavailable" in your Azure web apps
"502 bad gateway" and "503 service unavailable" are common errors in your web app hosted in [Azure App Service](/documentation/articles/app-service-changes-existing-services/). This article helps you troubleshoot these errors.

If you need more help at any point in this article, you can contact the Azure experts on [the MSDN Azure and the CSDN Azure](/support/forums/). Alternatively, you can also file an Azure support incident. Go to the [Azure Support site](/support/contact/) and click on **Get Support**.

## Symptom
When you browse to the web app, it returns a HTTP "502 Bad Gateway" error or a HTTP "503 Service Unavailable" error.

## Cause
This problem is often caused by application level issues, such as:

* requests taking a long time
* application using high memory/CPU
* application crashing due to an exception.

## Troubleshooting steps to solve "502 bad gateway" and "503 service unavailable" errors
Troubleshooting can be divided into three distinct tasks, in sequential order:

1. [Observe and monitor application behavior](#observe)
2. [Collect data](#collect)
3. [Mitigate the issue](#mitigate)

[App Service Web Apps](/home/features/app-service/web-apps/) gives you various options at each step.

### <a name="observe"></a> 1. Observe and monitor application behavior
#### Track Service health
Azure publicizes each time there is a service interruption or performance degradation. You can track the health of the service on the [Azure Portal Preview](https://portal.azure.cn/). For more information, see [Track service health](/documentation/articles/insights-service-health/).

#### Monitor your web app
This page let you find out if your application is having any issues. In Azure Classic Management Portal, click **Monitor** of your web app.

Some of the metrics that you might want to monitor for your web app are

* Average memory working set
* Average response time
* CPU time
* Memory working set
* Requests

![monitor web app towards solving HTTP errors of 502 bad gateway and 503 service unavailable](./media/app-service-web-troubleshoot-HTTP-502-503/1-monitor-metrics.png)

For more information, see:

* [Monitor Web Apps in Azure App Service](/documentation/articles/web-sites-monitor/)
* [Receive alert notifications](/documentation/articles/insights-receive-alert-notifications/)

### <a name="collect"></a> 2. Collect data
#### Use the Azure App Service Support Portal
Web Apps provides you with the ability to troubleshoot issues related to your web app by looking at HTTP logs, event logs, process dumps, and more. You can access all this information using our Support portal at **http://&lt;your app name>.scm.chinacloudsites.cn/Support**

The Azure App Service Support portal provides you with three separate tabs to support the three steps of a common troubleshooting scenario:

1. Observe current behavior
2. Analyze by collecting diagnostics information and running the built-in analyzers
3. Mitigate

If the issue is happening right now, click **Analyze** > **Diagnostics** > **Diagnose Now** to create a diagnostic session for you, which will collect HTTP logs, event viewer logs, memory dumps, PHP error logs and PHP process report.

Once the data is collected, it will also run an analysis on the data and provide you with an HTML report.

In case you want to download the data, by default, it would be stored in the D:\home\data\DaaS folder.

For more information on the Azure App Service Support portal, see [New Updates to Support Site Extension for Azure Websites](http://azure.microsoft.com/blog/new-updates-to-support-site-extension-for-azure-websites).

#### Use the Kudu Debug Console
Web Apps comes with a debug console that you can use for debugging, exploring, uploading files, as well as JSON endpoints for getting information about your environment. This is called the *Kudu Console* or the *SCM Dashboard* for your web app.

You can access this dashboard by going to the link **https://&lt;Your app name>.scm.chinacloudsites.cn/**.

Some of the things that Kudu provides are:

* environment settings for your application
* log stream
* diagnostic dump
* debug console in which you can run Powershell cmdlets and basic DOS commands.

Another useful feature of Kudu is that, in case your application is throwing first-chance exceptions, you can use Kudu and the SysInternals tool Procdump to create memory dumps. These memory dumps are snapshots of the process and can often help you troubleshoot more complicated issues with your web app.

For more information on features available in Kudu, see
[Azure Websites online tools you should know about](https://azure.microsoft.com/blog/windows-azure-websites-online-tools-you-should-know-about/).

### <a name="mitigate"></a> 3. Mitigate the issue
#### Scale the web app
In Azure App Service, for increased performance and throughput,  you can adjust the scale at which you are running your application. Scaling up a web app involves two related actions: changing your App Service plan to a higher pricing tier, and configuring certain settings after you have switched to the higher pricing tier.

For more information on scaling, see [Scale a web app in Azure App Service](/documentation/articles/web-sites-scale/).

Additionally, you can choose to run your application on more than one instance . This not only provides you with more processing capability, but also gives you some amount of fault tolerance. If the process goes down on one instance, the other instance will still continue serving requests.

You can set the scaling to be Manual or Automatic.

#### Use AutoHeal
AutoHeal recycles the worker process for your app based on settings you choose (like configuration changes, requests, memory-based limits, or the time needed to execute a request). Most of the time, recycle the process is the fastest way to recover from a problem. Though you can always restart the web app from directly within the Azure Portal Preview, AutoHeal will do it automatically for you. All you need to do is add some triggers in the root web.config for your web app. Note that these settings would work in the same way even if your application is not a .Net one.

For more information, see [Auto-Healing Azure Web Sites](/blog/auto-healing-windows-azure-web-sites/).

#### Restart the web app
This is often the simplest way to recover from one-time issues. On the [Azure Portal Preview](https://portal.azure.cn/), on your web app's blade, you have the options to stop or restart your app.

 ![restart app to solve HTTP errors of 502 bad gateway and 503 service unavailable](./media/app-service-web-troubleshoot-HTTP-502-503/2-restart.png)

You can also manage your web app using Azure Powershell. For more information, see
[Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager/).

