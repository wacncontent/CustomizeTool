deletion:

deleted:

		### <a name="datarpt"></a>SQL Data Reporting using Virtual Machines
		
		Once a database contains data, somebody will probably want to create reports using that data. Azure can run SQL Server Reporting Services (SSRS) in Azure Virtual Machines, which is functionally equivalent to running SQL Server Reporting Services on-premises. Then you can use SSRS to run reports on data stored in an Azure SQL Database.  [Figure 5](#Fig5) shows how the process works.
		
		<a name="Fig5"></a>![Diagram of SQL reporting][SQL-report]
		 
		**Figure 5: SQL Server Reporting Services running in an Azure Virtual Machines provides reporting services for data in SQL Database. .**
		
		Before a user can see a report, someone defines what that report should look like (step 1). With SSRS on a VM, this can be done using either of two tools: SQL Server Data Tools, part of SQL Server 2012, or its predecessor, Business Intelligence (BI) Development Studio. As with SSRS, these report definitions are expressed in the Report Definition Language (RDL). After the RDL files for a report have been created, they are uploaded to a VM in the cloud (step 2). The report definition is now ready to use.
		
		Next, a user of the application accesses the report (step 3). The application passes this request to the SSRS VM (step 4), which contacts SQL Database or other data sources to get the data it needs (step 5). SSRS uses this data and the relevant RDL files to render the report (step 6), then returns the report to the application (step 7), which displays it to the user (step 8).
		
		Embedding a report in an application, the scenario shown here, isn't the only option. It's also possible to view reports in Report Manager on the VM, SharePoint on the VM, or in other ways. Reports can also be combined, with one report containing a link to another.
		
		SSRS on an Azure VM gives you full functionality as a reporting solution in the cloud. Reports can use any data source supported by SSRS. Applications and reports can include embedded code or assemblies to support custom behaviors. Report execution and rendering are fast because report server content and engine run together on the same virtual server.

reason: ()

