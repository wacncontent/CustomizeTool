<properties
	pageTitle="Elastic database jobs overview | Windows Azure" 
	description="Illustrates the elastic database job service" 
	metaKeywords="azure sql database elastic databases" 
	services="sql-database" documentationCenter=""  
	manager="jeffreyg" 
	authors="ddove"/>

<tags
	ms.service="sql-database"
	ms.date="11/04/2015"
	wacn.date=""/>

# Elastic Database jobs overview

The **Elastic Database jobs** feature (preview) enables you to  reliably execute a Transact-SQL (T-SQL) script or apply a DACPAC ([data-tier application](https://msdn.microsoft.com/zh-cn/library/ee210546.aspx)) across a group of databases, including:

* a custom-defined collection of databases (explained below)
* all databases in an [Elastic Database pool](/documentation/articles/sql-database-elastic-pool)
* a shard set (created using [Elastic Database client library](/documentation/articles/sql-database-elastic-database-client-library)). 
 
For instructions on installation, go to [Installing the Elastic Database job components](/documentation/articles/sql-database-elastic-jobs-service-installation).

**Elastic Database jobs** is currently a customer-hosted Azure Cloud Service that enables the execution of ad-hoc and scheduled administrative tasks, which are called **jobs**. With jobs, you can easily and reliably manage large groups of Azure SQL Databases by running Transact-SQL scripts to perform administrative operations. 

![Elastic database job service][1]

## Benefits
* Easily manage schema changes, credentials management, reference data updates, performance data collection or tenant (customer) telemetry collection.
* Reduce overhead: Normally, you must connect to each database independently in order to run Transact-SQL statements or perform other administrative tasks. A job handles the task of logging in to each database in the target group.
* Accounting: Jobs run the script and log the status of execution for each database. 
* Flexibility: Define custom groups of Azure SQL Databases
* Define, maintain and persist Transact-SQL scripts to be executed across a group of Azure SQL Databases 
* Deploy a data-tier application (DACPAC)
* Automatic retry when running scripts
* Define execution schedules
* Aggregate data from a collection of Azure SQL Databases into a single destination table

> [AZURE.NOTE] In the Azure Management Portal, only a reduced set of functions limited to SQL Azure elastic pools is available. Use the PowerShell APIs to access the full set of current functionality.

## Scenarios

* Performance administrative task, such as deploy new schema
* Update reference data, for example product information common across all databases, even using schedules to automate the updates every weekday after hours.
* Rebuild indexes to improve query performance. The rebuilding can be configured to execute across a collection of databases on a recurring basis, such as during off-peak hours.
* Collect query results from a set of databases into a central table on an on-going basis. Performance queries can be continually executed and configured to trigger additional tasks to be executed.
* Execute longer running data processing queries across a large set of databases, for example the collection of customer telemetry. Results are collected into a single destination table for further analysis.

## Elastic Database jobs: end-to-end 
1.	Install the **Elastic Database jobs** components. For more information, see [Installing Elastic Database jobs](/documentation/articles/sql-database-elastic-jobs-service-installation). If the installation fails, see [how to uninstall](/documentation/articles/sql-database-elastic-jobs-uninstall).
2.	Use the PowerShell APIs to access more functionality, for example creating custom-defined database collections, adding schedules and/or gathering results sets. Use the portal for simple installation and creation/monitoring of jobs limited to execution against a **Elastic Database pool**. 
3.	Create encrypted credentials for job execution and [add the user (or role) to each database in the group](/documentation/articles/sql-database-security).
4.	Create an idempotent T-SQL script that can be run against every database in the group. 
5.	Follow these steps to create jobs using the Azure Management Portal: [Creating and managing Elastic Database jobs](/documentation/articles/sql-database-elastic-jobs-create-and-manage). 
6.	Or use PowerShell scripts: [Create and manage a SQL Database elastic database jobs using PowerShell (preview)](/documentation/articles/sql-database-elastic-jobs-powershell).

## The importance of idempotent scripts
The scripts must be [idempotent](https://en.wikipedia.org/wiki/Idempotence). In simple terms, "idempotent" means that if the script succeeds, and it is run again, the same result occurs. A script may fail due to transient network issues. In that case, the job will automatically retry running the script a preset number of times before desisting. An idempotent script has the same result even if has been successfully run twice. 

A simple tactic is to test for the existence of an object before creating it.  

	IF NOT EXIST (some_object)
	-- Create the object 
	-- If it exists, drop the object before recreating it.

Similarly, a script must be able to execute successfully by logically testing for and countering any conditions it finds.

## Failures and logs

If a script fails after multiple attempts, the job logs the error and continues. After a job ends (meaning a run against all databases in the group), you can check its list of failed attempts. The logs provide details to debug faulty scripts. 

## Group types and creation

There are two kinds of groups: 

1. Shard sets
2. Custom groups

Shard set groups are created using the [Elastic Database tools](/documentation/articles/sql-database-elastic-scale-introduction). When you create a shard set group, databases are added or removed from the group automatically. For example, a new shard will be automatically in the group. A jobs will run against the group with no adjustment.

Custom groups, on the other hand, are rigidly defined. You must explicitly add or remove databases from custom groups. If a database in the group is dropped, the job will attempt to run the script against the database resulting in an eventual failure. Groups created using the Azure Management Portal currently are custom groups. 


## Components and pricing 
The following components work together to create an Azure Cloud service that enables ad-hoc execution of administrative jobs. The components are installed and configured automatically during setup, in your subscription. You can identify the services as they all have the same auto-generated name. The name is unique, and consists of the prefix "edj" followed by 21 randomly generated characters.

* **Azure Cloud Service**: elastic database jobs (preview) is delivered as a customer-hosted Azure Cloud service to perform execution of the requested tasks. From the portal, the service is deployed and hosted in your Windows Azure subscription. The default deployed service runs with the minimum of two worker roles for high availability. The default size of each worker role (ElasticDatabaseJobWorker) runs on an A0 instance. For pricing, see [Cloud services pricing](/home/features/cloud-services/#price). 
* **Azure SQL Database**: The service uses an Azure SQL Database known as the **control database** to store all of the job metadata. The default service tier is a S0. For pricing, see [SQL Database Pricing](/home/features/sql-database/#price).
* **Azure Service Bus**: An Azure Service Bus is for coordination of the work within the Azure Cloud Service. See [Service Bus Pricing](/home/features/service-bus/#price).
* **Azure Storage**: An Azure Storage account is used to store diagnostic output logging in the event that an issue requires further debugging (a common practice for [Azure diagnostics](/documentation/articles/cloud-services-dotnet-diagnostics)). For pricing, see [Azure Storage Pricing](/home/features/storage/#price).

## How Elastic Database jobs work
1.	An Azure SQL Database is designated a control database which stores all meta-data and state data.
2.	The control database is accessed by  **Elastic Database jobs** to both launch and track jobs to execute.
3.	Two different roles communicate with the control database: 
	* Controller: Determines which jobs require tasks to perform the requested job, and retries failed jobs by creating new job tasks.
	* Job Task Execution: Carries out the job tasks.

### Job task types
There are multiple types of job tasks that carry out execution of jobs:

* ShardMapRefresh: Queries the shard map to determine all the databases used as shards
* ScriptSplit: Splits the script across 'GO' statements into batches
* ExpandJob: Creates child jobs for each database from a job that targets a group of databases
* ScriptExecution: Executes a script against a particular database using defined credentials
* Dacpac: Applies a DACPAC to a particular database using particular credentials

## End-to-End job execution work-flow
1.	Using either the Portal or the PowerShell API, a job is inserted into the  **control database**. The job requests execution of a Transact-SQL script against a group of databases using specific credentials.
2.	The controller identifies the new job. Job tasks are created and executed to split the script and to refresh the group's databases. Lastly, a new job is created and executed to expand the job and create new child jobs where each child job is specified to execute the Transact-SQL script against an individual database in the group.
3.	The controller identifies the created child jobs. For each job, the controller creates and triggers a job task to execute the script against a database. 
4.	After all job tasks have completed, the controller updates the jobs to a completed state. 
At any point during job execution, the PowerShell API can be used to view the current state of job execution. All times returned by the PowerShell APIs are represented in UTC. If desired, a cancellation request can be initiated to stop a job. 

## Next steps
[Install the components](/documentation/articles/sql-database-elastic-jobs-service-installation), then [create and add a log in to each database in the group of databases](/documentation/articles/sql-database-security). To further understand job creation and management, see [creating and managing elastic database jobs](/documentation/articles/sql-database-elastic-jobs-create-and-manage).

[AZURE.INCLUDE [elastic-scale-include](../includes/elastic-scale-include.md)]

<!--Image references-->
[1]: ./media/sql-database-elastic-jobs-overview/elastic-jobs.png
<!--anchors-->

 
