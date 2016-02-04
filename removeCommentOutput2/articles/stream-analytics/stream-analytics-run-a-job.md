<properties 
	pageTitle="How to start streaming jobs in Stream Analytics | Windows Azure" 
	description="How run a streaming job in Azure Stream Analytics | learning path segment."
    keywords="streaming jobs"
	documentationCenter=""
	services="stream-analytics"
	authors="jeffstokes72" 
	manager="paulettm" 
	editor="cgronlun"/>

<tags
	ms.service="stream-analytics"
	ms.date="12/04/2015"
	wacn.date=""/>

# How to run a streaming job in Azure Stream Analytics

When a job input, query and output have all been specified you can start the Stream Analytics job.

To start your job:

1.	In the Azure Management Portal, from the job dashboard, click **Start** at the bottom of the page.

    ![Start job Button](./media/stream-analytics-run-a-job/1-stream-analytics-run-a-job.png)  

    In the Azure preview portal, click **Start** at the top of your job page.

    ![Azure preview portal Start job Button](./media/stream-analytics-run-a-job/4-stream-analytics-run-a-job.png)  

2.	Specify a **Start Output** value to determine when this job will start producing output. The default setting for jobs that have not previously been started is **Job Start Time**, which means that the job will immediately start processing data. You can also specify a **Custom** time in the past (for consuming historical data) or the future (to delay processing until a future time). For cases when a job has been previously started and stopped, the option **Last Stopped Time** is available in order to resume the job from the last output time and avoid data loss.  

    ![Start streaming job Time](./media/stream-analytics-run-a-job/2-stream-analytics-run-a-job.png)  

    ![Azure preview portal Start streaming job Time](./media/stream-analytics-run-a-job/5-stream-analytics-run-a-job.png)  

3.	Confirm your selection. The job status will change to *Starting* and will shortly move to *Running* once the job has started. You can monitor the progress of the **Start** operation in the **Notification Hub**:

    ![streaming job progress](./media/stream-analytics-run-a-job/3-stream-analytics-run-a-job.png)  

    ![Azure preview portal stremaing job progress](./media/stream-analytics-run-a-job/6-stream-analytics-run-a-job.png)  

## Get help
For further assistance, try our [Azure Stream Analytics forum](https://social.msdn.microsoft.com/Forums/home?forum=AzureStreamAnalytics)

## Next steps

- [Introduction to Azure Stream Analytics](/documentation/articles/stream-analytics-introduction)
- [Get started using Azure Stream Analytics](/documentation/articles/stream-analytics-get-started)
- [Scale Azure Stream Analytics jobs](/documentation/articles/stream-analytics-scale-jobs)
- [Azure Stream Analytics Query Language Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn834998.aspx)
- [Azure Stream Analytics Management REST API Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn835031.aspx)
