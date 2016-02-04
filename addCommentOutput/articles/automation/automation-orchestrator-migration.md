<properties
   pageTitle="Migrating from Orchestrator to Azure Automation | Windows Azure"
   description="Describes how to migrate runbooks and integration packs from System Center Orchestrator to Azure Automation."
   services="automation"
   documentationCenter=""
   authors="bwren"
   manager="stevenka"
   editor="tysonn" />
<tags
	ms.service="automation"
	ms.date="11/11/2015"
	wacn.date=""/>


# Migrating from Orchestrator to Azure Automation <!-- deleted by customization (Beta) -->

Runbooks in [System Center Orchestrator](http://technet.microsoft.com/zh-cn/library/hh237242.aspx) are based on activities from integration packs that are written specifically for Orchestrator while runbooks in Azure Automation are based on Windows PowerShell <!-- keep by customization: begin --> Workflows <!-- keep by customization: end -->.  [Graphical runbooks](/documentation/articles/automation-runbook-types#graphical-runbooks) in Azure Automation have a similar appearance to Orchestrator runbooks with their activities representing PowerShell cmdlets, child runbooks, and assets.

The [System Center Orchestrator Migration Toolkit](http://www.microsoft.com/download/details.aspx?id=47323&WT.mc_id=rss_alldownloads_all) includes tools to assist you in converting runbooks from Orchestrator to Azure Automation.  In addition to converting the runbooks themselves, you must convert the integration packs with the activities that <!-- deleted by customization the runbooks --><!-- keep by customization: begin --> they <!-- keep by customization: end --> use to integration modules with Windows PowerShell cmdlets.

Following is the the basic process for converting Orchestrator runbooks to Azure Automation.  Each of these steps is described in detail in the sections below.

1.  Download the [System Center Orchestrator Migration Toolkit](http://www.microsoft.com/download/details.aspx?id=47323&WT.mc_id=rss_alldownloads_all) which contains the tools and modules discussed in this article.
2.  <!-- deleted by customization Import --><!-- keep by customization: begin --> Install <!-- keep by customization: end --> [Standard Activities Module](#standard-activities-module) into Azure Automation.  This includes converted versions of standard Orchestrator activities that may be used by converted runbooks.
<!-- deleted by customization
3.  Import [System Center Orchestrator Integration Modules](#system-center-orchestrator-integration-modules) into Azure Automation for those integration packs used by your runbooks that access System Center.
4.  Convert custom and third party integration packs using the [Integration Pack Converter](#integration-pack-converter) and import into Azure Automation.
5.  Convert Orchestrator runbooks using the [Runbook Converter](#runbook-converter) and install in Azure Automation.
6.  Manually create required Orchestrator assets in Azure Automation since the Runbook Converter does not convert these resources.
7.  Configure a [Hybrid Runbook Worker](#hybrid-runbook-worker) in your local data center to run converted runbooks that will access local resources.
-->
<!-- keep by customization: begin -->
2.  Install [System Center Orchestrator Integration Modules](#system-center-orchestrator-integration-modules) into Azure Automation for those integration packs used by your runbooks.
3.  Convert custom and third party integration packs using the [Integration Pack Converter](#integration-pack-converter) and install in Azure Automation.
4.  Manually recreate global assets in Orchestrator in Azure Automation since there is no automated method to perform this migration.
5.  Convert Orchestrator runbooks using the [Runbook Converter](#runbook-converter-coming-soon)(coming soon) and install in Azure Automation.
6.  Configure a [Hybrid Runbook Worker](#hybrid-runbook-worker) in your local data center to run the converted runbooks.
<!-- keep by customization: end -->

## Service Management Automation

[Service Management Automation](http://technet.microsoft.com/zh-cn/library/dn469260.aspx) (SMA) stores and runs runbooks in your local data center like Orchestrator, and it uses the same integration modules as Azure Automation. <!-- deleted by customization The --><!-- keep by customization: begin -->  When it is available, the <!-- keep by customization: end --> [Runbook <!-- deleted by customization Converter](#runbook-converter) --><!-- keep by customization: begin --> Converter](#runbook-converter-coming-soon) <!-- keep by customization: end --><!-- deleted by customization converts --><!-- keep by customization: begin --> will convert <!-- keep by customization: end --> Orchestrator runbooks to graphical runbooks though which are not supported in SMA.  You can still install the [Standard Activities Module](#standard-activities-module) and [System Center Orchestrator Integration Modules](#system-center-orchestrator-integration-modules) into SMA, but you must manually [rewrite your runbooks](http://technet.microsoft.com/zh-cn/library/dn469262.aspx).

## Hybrid Runbook Worker

Runbooks in Orchestrator are stored on a database server and run on runbook servers, both in your local data center.  Runbooks in Azure Automation are stored in the Azure cloud and can run in your local data center using a [Hybrid Runbook Worker](/documentation/articles/automation-hybrid-runbook-worker).  This is how you will usually run runbooks converted from Orchestrator since they are designed to run on local servers.

## Integration Pack Converter

The Integration Pack Converter converts integration packs that were created using the <!-- deleted by customization [Orchestrator --><!-- keep by customization: begin --> Orchestrator <!-- keep by customization: end --> Integration Toolkit <!-- deleted by customization (OIT)](http://technet.microsoft.com/zh-cn/library/hh855853.aspx) --><!-- keep by customization: begin --> (OIT) <!-- keep by customization: end --> to integration modules based on Windows PowerShell that can be imported into Azure Automation or Service Management Automation.

When you run the Integration Pack Converter, you are presented with a wizard that will allow you to select an integration pack (.oip) file.  The wizard then lists the activities included in that integration pack and allows you to select which will be migrated.  When you complete the wizard, it creates <!-- deleted by customization an integration --><!-- keep by customization: begin --> a <!-- keep by customization: end --> module that includes a corresponding cmdlet for each of the activities in the original integration pack.


### Parameters

Any properties of an activity in the integration pack are converted to parameters of the corresponding cmdlet in the integration module.  Windows PowerShell cmdlets have a set of [common parameters](http://technet.microsoft.com/zh-cn/library/hh847884.aspx) that can be used with all cmdlets.  For example, the -Verbose parameter causes a cmdlet to output detailed information about its operation.  No cmdlet may have a parameter with the same name as a common parameter.  If an activity does have a property with the same name as a common parameter, the wizard will prompt you to provide another name for the parameter.

### Monitor activities

Monitor runbooks in Orchestrator start with a [monitor activity](http://technet.microsoft.com/zh-cn/library/hh403827.aspx) and run continuously waiting to be invoked by a particular event.  Azure Automation does not support monitor runbooks, so any monitor activities in the integration pack will not be converted.  Instead, a placeholder cmdlet is created in the integration module for the monitor activity.  This cmdlet has no functionality, but it allows any converted runbook that uses it to be installed.  This runbook will not be able to run in Azure Automation, but it can be installed so that <!-- deleted by customization you --><!-- keep by customization: begin --> the user <!-- keep by customization: end --> can modify it.

### Integration packs that cannot be converted

<!-- deleted by customization
Integration packs that were not created with OIT cannot be converted with the Integration Pack Converter. There are also some integration packs provided by Microsoft that cannot currently be converted with this tool.  Converted versions of these integration packs have been [provided for download](#system-center-orchestrator-integration-modules) so that they can be installed in Azure Automation or Service Management Automation.
-->
<!-- keep by customization: begin -->
Integration packs that were not created with OIT, including some created by Microsoft, cannot be converted with this tool.  Integration packs provided by Microsoft have been converted to integration modules so that they can be installed in Azure Automation or Service Management Automation.
<!-- keep by customization: end -->


## Standard Activities Module

Orchestrator includes a set of [standard activities](http://technet.microsoft.com/zh-cn/library/hh403832.aspx) that are not included in an integration pack but are used by many runbooks.  The Standard Activities module is a integration module that includes a cmdlet equivalent for each of these activities.  You must install this integration module in Azure Automation before importing any converted runbooks that use a standard activity.

In addition to supporting converted runbooks, the cmdlets in the standard activities module can be used by someone familiar with Orchestrator to build new runbooks in Azure Automation.  While the functionality of all of the standard activities can be performed with cmdlets, they may operate differently.  The cmdlets in the converted standard activities module will work the same as their corresponding activities and use the same parameters.  This can help the existing Orchestrator runbook author in their transition to Azure Automation runbooks.

## System Center Orchestrator Integration Modules
<!-- deleted by customization

Microsoft provides [integration packs](http://technet.microsoft.com/zh-cn/library/hh295851.aspx) for building runbooks to automate System Center components and other products.  Some of these integration packs are currently based on OIT but cannot currently be converted to integration modules because of known issues.  [System Center Orchestrator Integration Modules](https://www.microsoft.com/download/details.aspx?id=49555) includes converted versions of these integration packs that can be imported into Azure Automation and Service Management Automation.  

By the RTM version of this tool, updated versions of the integration packs based on OIT that can be converted with the Integration Pack Converter will be published.  Guidance will also be provided to assist you in converting runbooks using activities from the integration packs not based on OIT.

## Runbook Converter

The Runbook Converter converts Orchestrator runbooks into [graphical runbooks](/documentation/articles/automation-runbook-types#graph-runbooks) that can be imported into Azure Automation.  

Runbook Converter is implemented as a PowerShell module with a cmdlet called **ConvertFrom-SCORunbook** that performs the conversion.  When you install the tool, it will create a shortcut to a PowerShell session that loads the cmdlet.   

Following is the basic process to convert an Orchestrator runbook and import it into Azure Automation.  The following sections provide further details on using the tool and working with converted runbooks.

1. Export one or more runbooks from Orchestrator.
2. Obtain integration modules for all activities in the runbook.
3. Convert the Orchestrator runbooks in the exported file.
4. Review information in logs to validate the conversion and to determine any required manual tasks.
4. Import converted runbooks into Azure Automation.
5. Create any required assets in Azure Automation.
6. Edit the runbook in Azure Automation to modify any required activities.

### Using Runbook Converter

The syntax for **ConvertFrom-SCORunbook** is as follows:

	ConvertFrom-SCORunbook -RunbookPath <string> -Module <string[]> -OutputFolder <string> 

- RunbookPath - Path to the export file containing the runbooks to convert.
- Module - Comma delimited list of integration modules containing activities in the runbooks.
- OutputFolder - Path to the folder to create converted graphical runbooks. 


The following example command converts the runbooks in an export file called **MyRunbooks.ois_export**.  These runbooks use the Active Directory and Data Protection Manager integration packs.

	ConvertFrom-SCORunbook -RunbookPath "c:\runbooks\MyRunbooks.ois_export" -Module c:\ip\SystemCenter_IntegrationModule_ActiveDirectory.zip,c:\ip\SystemCenter_IntegrationModule_DPM.zip -OutputFolder "c:\runbooks" 


### Log files

The Runbook Converter will create the following log files in the same location as the converted runbook.  If the files already exists, then they will be overwritten with information from the last conversion.

| File | Contents |
|:---|:---|
| Runbook Converter - Progress.log | Detailed steps of the conversion including information for each activity successfully converted and warning for each activity not converted. |
| Runbook Converter - Summary.log  | Summary of the last conversion including any warnings and follow up tasks that you need to perform such as creating a variable required for the converted runbook.  |

### Exporting runbooks from Orchestrator

The Runbook Converter works with an export file from Orchestrator that contains one or more runbooks.  It will create a corresponding Azure Automation runbook for each Orchestrator runbook in the export file.  

To export a runbook from Orchestrator, right-click the name of the runbook in Runbook Designer and select **Export**.  To export all runbooks in a folder, right-click the name of the folder and select **Export**.


### Runbook activities

The Runbook Converter converts each activity in the Orchestrator runbook to a corresponding activity in Azure Automation.  For those activities that can't be converted, a placeholder activity is created in the runbook with warning text.  After you import the converted runbook into Azure Automation, you must replace any of these activities with valid activities that perform the required functionality.

Any Orchestrator activities in the [Standard Activities Module](#standard-activities-module) will be converted.  There are some standard Orchestrator activities that are not in this module though and are not converted.  For example, **Send Platform Event** has no Azure Automation equivalent since the event is specific to Orchestrator.

[Monitor activities](https://technet.microsoft.com/zh-cn/library/hh403827.aspx) are not converted since there is no equivalent to them in Azure Automation.  The exception are monitor activities in [converted integration packs](#integration-pack-converter) that will be converted to the placeholder activity.

Any activity from a [converted integration pack](#integration-pack-converter) will be converted if you provide the path to the integration module with the **modules** parameter.  For System Center Integration Packs, you can use the [System Center Orchestrator Integration Modules](#system-center-orchestrator-integration-modules).


### Orchestrator resources

The Runbook Converter only converts runbooks, not other Orchestrator resources such as counters, variables, or connections.  Counters are not supported in Azure Automation.  Variables and connections are supported, but you must create them manually.  The log files will inform you if the runbook requires such resources and specify corresponding resources that you need to create in Azure Automation for the converted runbook to operate properly.

For example, a runbook may use a variable to populate a particular value in an activity.  The converted runbook will convert the activity and specify a variable asset in Azure Automation with the same name as the Orchestrator variable.  This will be noted in the **Runbook Converter - Summary.log** file that is created after the conversion.  You will need to manually create this variable asset in Azure Automation before using the runbook. 

 
### Input parameters

Runbooks in Orchestrator accept input parameters with the **Initialize Data** activity.  If the runbook being converted includes this activity, then an [input parameter](/documentation/articles/automation-graphical-authoring-intro#runbook-input-and-output) in the Azure Automation runbook is created for each parameter in the activity.  A [Workflow Script control](/documentation/articles/automation-graphical-authoring-intro#activities) activity is created in the converted runbook that retrieves and returns each parameter.  Any activities in the runbook that use an input parameter refer to the output from this activity.

The reason that this strategy is used is to best mirror the functionality in the Orchestrator runbook.  Activities in new graphical runbooks should refer directly to input parameters using a Runbook input data source.


### Invoke Runbook activity

Runbooks in Orchestrator start other runbooks with the **Invoke Runbook** activity. If the runbook being converted includes this activity and the **Wait for completion** option is set, then a runbook activity is created for it in the converted runbook.  If the **Wait for completion** option is not set, then a Workflow Script activity is created that uses **Start-AzureAutomationRunbook** to start the runbook.  After you import the converted runbook into Azure Automation, you must modify this activity with the information specified in the activity.



-->
<!-- keep by customization: begin -->
Microsoft provides [integration packs](http://technet.microsoft.com/zh-cn/library/hh295851.aspx) for building runbooks to automate System Center components and other products.  Currently, when you download some of these integration packs from [TechNet](http://www.microsoft.com/download/details.aspx?id=39622), they cannot be converted with the Integration Pack Converter due to known issue which will be fixed with RC release of System Center Orchestrator Migration Toolkit.  [System Center Orchestrator Integration Modules](http://www.microsoft.com/download/details.aspx?id=47324&WT.mc_id=rss_alldownloads_all) includes converted versions of these integration packs that can be imported in Azure Automation and Service Management Automation prior to this release.

## Runbook Converter (coming soon)

This tool will convert Orchestrator runbooks into [graphical runbooks](/documentation/articles/automation-runbook-types#graph-runbooks) that can be imported into Azure Automation.  Further details on this tool will be provided here when it comes available.
<!-- keep by customization: end -->

## Related articles

- [System Center 2012 - Orchestrator](http://technet.microsoft.com/zh-cn/library/hh237242.aspx)
- [Service Management Automation](https://technet.microsoft.com/zh-cn/library/dn469260.aspx)
- [Hybrid Runbook Worker](/documentation/articles/automation-hybrid-runbook-worker)
- [Orchestrator Standard Activities](http://technet.microsoft.com/zh-cn/library/hh403832.aspx)
 
