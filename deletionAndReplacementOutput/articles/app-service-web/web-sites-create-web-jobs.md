deletion:

deleted:

		>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

reason: ()

deleted:

		## What's changed
		* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
		* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

reason: ()

replacement:

deleted:

		[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)]

replaced by:

		## Table of Contents ##
		- [Acceptable File Types for Scripts](#acceptablefiles)
		- [Create an On Demand Task](#CreateOnDemand)
		- [Create a Continuously Running Task](#CreateContinuous)
		- [Create a Scheduled Task](#CreateScheduled)
			- [Scheduled jobs and Azure Scheduler](#Scheduler)
		- [View the Job History](#ViewJobHistory)
		- [Notes](#WHPNotes)
		- [Next Steps](#NextSteps)

reason: ()

deleted:

		1. In the **Web App** blade of the [Azure Management Portal](http://manage.windowsazure.cn), click **All settings > WebJobs** to show the **WebJobs** blade.
			
			![WebJob blade](./media/web-sites-create-web-jobs/wjblade.png)
			
		5. Click **Add**. The **Add WebJob** dialog appears.
			
			![Add WebJob blade](./media/web-sites-create-web-jobs/addwjblade.png)
			
		2. Under **Name**, provide a name for the WebJob. The name must start with a letter or a number and cannot contain any special characters other than "-" and "_".

replaced by:

		1. In the command bar of the **WebJobs** page, click **Add**. The **New Job** dialog appears.
			
			![On Demand Task][OnDemandWebJob]
			
		2. Under **Name**, provide a name for the task. The name must start with a letter or a number and cannot contain any special characters other than "-" and "_".
			
		3. In the **Content (Zip Files - 100MB Max)** box, browse to the zip file that contains your script. The zip file should contain your executable (.exe .cmd .bat .sh .php .py .js) as well as any supporting files needed to run the program or script.

reason: ()

deleted:

		3. In the **File Upload** box, click the folder icon and browse to the zip file that contains your script. The zip file should contain your executable (.exe .cmd .bat .sh .php .py .js) as well as any supporting files needed to run the program or script.
			
		5. Check **Create** to upload the script to your web app. 
			
			The name you specified for the WebJob appears in the list on the **WebJobs** blade.
			
		6. To run the WebJob, right-click its name in the list and click **Run**.
			
			![Run WebJob](./media/web-sites-create-web-jobs/runondemand.png)
			
		## <a name="CreateContinuous"></a>Create a continuously running WebJob
		
		1. To create a continuously executing WebJob, follow the same steps for creating a WebJob that runs once, but in the **How to Run** box, choose **Continuous**.
		
		2. To start or stop a continuous WebJob, right-click the WebJob in the list and click **Start** or **Stop**.
			
		> [AZURE.NOTE] If your web app runs on more than one instance, a continuously running WebJob will run on all of your instances. On-demand and scheduled WebJobs run on a single instance selected for load balancing by Windows Azure.
			
		> For Continuous WebJobs to run reliably and on all instances, enable the Always On* configuration setting for the web app otherwise they can stop running when the SCM host site has been idle for too long.

replaced by:

		5. Check the check mark on the bottom right of the dialog to upload the script to your website. The name you specified for the task appears in the list:
			
			![Task List][WebJobsList]
			
		6. To run the script, select its name in the list and click **Run Once** in the command bar at the bottom of the portal page.
			
			![Run Once][RunOnce]
		
		## <a name="CreateContinuous"></a>Create a Continuously Running Task
		
		1. To create a continuously executing task, follow the same steps for creating a task that runs once, but in the **How to Run** box, choose **Run continuously**.
			
			![New Continuous Task][NewContinuousJob]
			
		2. To start or stop a continuously running task, select the task in the list and click **Start** or **Stop** in the command bar.
		
		> [AZURE.NOTE] If your website runs on more than one instance, a continuously running task will run on all of your instances. On-demand and scheduled tasks run on a single instance selected for load balancing by Windows Azure.
		
		> [AZURE.NOTE]
		> For continuous tasks, it is recommended that you enable **Always On** on the Configure page for your website. The Always On feature, available in Basic and Standard mode, prevents websites from being unloaded, even if they have been idle for some time. If your website is always loaded, your continuously running task may run more reliably.

reason: ()

