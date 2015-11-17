deletion:

deleted:

		### Application Insights
		
		![Application Insights](./media/fundamentals-introduction-to-azure/ApplicationInsights.png)  
		
		*Figure: Application Insights monitors performance and usage of your live web or device app.*
		
		When you have published your app - whether it runs on mobile devices, desktops, or web browsers - Application Insights tells you how it is performing and what users are doing with it. It will keep a count of crashes and slow response, alert you if the figures cross unacceptable thresholds, and help you diagnose any problems. 
		
		When you develop a new feature, plan to measure its success with users. By analysing usage patterns, you understand what works best for your customers and enhance your app in every development cycle.
		
		Although it's hosted in Azure, Application Insights works for a wide and growing range of apps, both on an off Azure. Both J2EE and ASP.NET web apps are covered, as well as iOS, Android, OSX and Windows applications. Telemetry is sent from an SDK built with the app, to be analyzed and displayed in the Application Insights service in Azure.
		
		If you want more specialized analytics, export the telemetry stream to a database, or to Power BI, or any other tools.
		
		**Application Insights scenarios**
		
		You are developing an app. It might be a web app or a device app, or a device app with a web back end. 
		
		* Tune the performance of your app after it is published, or while it is in load testing.  Application Insights aggregates telemetry from all the installed instances, and presents you with charts of response times, request and exception counts, dependency response times, and other performance indicators. These help you tune your app's performance. You can insert code to report more specific data if you need it.
		* Detect and diagnose problems in your live app. You can get alerts by email if performance indicators cross acceptable thresholds. You can investigate specific user sessions, for example to see the request that caused an exception. 
		* Track usage to assess the success of each new feature. When you design a new user story, plan to measure how much it is used, and whether users achieve their expected goals. Application Insights gives you basic usage data such as web page views, and you can insert code to track the user experience in more detail.

reason: ()

replacement:

deleted:

		Visual Studio Online also offers support for agile development with features like continuous integration builds, Kanban boards and virtual team rooms.

replaced by:

		Visual Studio Online also offers a service called Application Insights, which gives you an analysis of your entire application. It provides stats on performance and how your application is being used. If you are already using System Center Operations Manager, it can also hook to it and raise alerts when issues arise. 		+Visual Studio Online also offers support for agile development with features like continuous integration builds, Kanban boards and virtual team rooms. 
			
		Additionally, there is support for agile development with features like continuous integration builds, Kanban boards and virtual team rooms.

reason: ()

