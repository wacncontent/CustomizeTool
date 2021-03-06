<properties 
	pageTitle="How to create a data analytics processing job for Stream Analytics | Windows Azure" 
	description="Create a data analytics processing job for Stream Analytics | learning path segment."
	keywords="data analytics processing"
	documentationCenter=""
	services="stream-analytics"
	authors="jeffstokes72" 
	manager="paulettm" 
	editor="cgronlun"/>

<tags
	ms.service="stream-analytics"
	ms.date="12/04/2015"
	wacn.date=""/> 

# How to create a data analytics processing job for Stream Analytics

The top-level resource in Azure Stream Analytics is a Stream Analytics Job.  It consists of one or more input data sources, a query expressing the data transformation, and one or more output targets that results are written to. Together these enable the user to perform data analytics processing for streaming data scenarios.

To start using Stream Analytics, begin by creating a new Stream Analytics job.  Note that this action has no billing implications until the job is started.

1.  Sign in on the online [Windows Azure Management Portal](http://manage.windowsazure.cn) or the Azure preview portal.
2.  In the Azure Management Portal: **Click New**, then click **Data Services**, and then click **Stream Analytics** and **Quick Create**.

    ![Data analytics processing job wizard](./media/stream-analytics-create-a-job/1-stream-analytics-create-a-job.png)  

    In the Azure preview portal: Click New, then click Data + Analytics, and then click Azure Stream Analytics.  

    ![Create data analytics processing job](./media/stream-analytics-create-a-job/4-stream-analytics-create-a-job.png)  

3.  Specify the desired configuration for the Stream Analytics job.
	- In the **Job Name** box, enter a name to identify the Stream Analytics job. When the **Job Name** is validated, a green check mark appears in the Job Name box. The **Job Name** may contain only alphanumeric characters and the '-' character, and must be between 3 and 63 characters.
	- Use **Region** in the Azure Management Portal or **Location** in the Azure preview portal to specify the geographic location where you want to run the job.
	- If using the Azure Management Portal, select or create a storage account to use as the **Regional Monitoring Storage Account**. This storage account is used to store monitoring data for all Stream Analytics jobs running in this region.
	- If using the Azure preview portal, specify a new or existing **Resource Group** to hold related resources for your application.

4.  Once the new Stream Analytics job options are configured, click **Create Stream Analytics Job**. It can take a few minutes for the Stream Analytics job to be created. To check the status, you can monitor the progress in the Notifications hub.

    ![Data analytics processing job notfications hub](./media/stream-analytics-create-a-job/2-stream-analytics-create-a-job.png)  

    ![Azure Preview Portal Data analytics processing job create Job](./media/stream-analytics-create-a-job/5-stream-analytics-create-a-job.png)  

5.  The new job will be shown with a status of **Created**. Notice that the **Start** button is disabled. You must configure the job input, query, and output before you can start the job.

    ![Data analytics processing job job Status](./media/stream-analytics-create-a-job/3-stream-analytics-create-a-job.png)  

    ![Azure Preview Portal Data analytics processing job job status](./media/stream-analytics-create-a-job/6-stream-analytics-create-a-job.png)  

## Get help
For further assistance, try our [Azure Stream Analytics forum](https://social.msdn.microsoft.com/Forums/home?forum=AzureStreamAnalytics)

## Next steps

- [Introduction to Azure Stream Analytics](/documentation/articles/stream-analytics-introduction)
- [Get started using Azure Stream Analytics](/documentation/articles/stream-analytics-get-started)
- [Scale Azure Stream Analytics jobs](/documentation/articles/stream-analytics-scale-jobs)
- [Azure Stream Analytics Query Language Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn834998.aspx)
- [Azure Stream Analytics Management REST API Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn835031.aspx)