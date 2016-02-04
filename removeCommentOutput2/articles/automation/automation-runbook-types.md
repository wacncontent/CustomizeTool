<properties 
   pageTitle="Azure Automation Runbook Types"
   description="Describes the difference types of runbooks that you can use in Azure Automation and considerations that you should take into account when determining which type to use. "
   services="automation"
   documentationCenter=""
   authors="bwren"
   manager="stevenka"
   editor="tysonn" />
<tags
	ms.service="automation"
	ms.date="11/13/2015"
	wacn.date=""/>

# Azure Automation runbook types

Azure Automation supports three types of runbooks that are  briefly described in the following table.  The sections below provide further information about each type including considerations on when to use each.


| Type |  Description |
|:---|:---|
| [PowerShell Workflow](#powershell-workflow-runbooks) | Text runbook based on Windows PowerShell Workflow. |

## PowerShell Workflow runbooks

PowerShell Workflow runbooks are text runbooks based on [Windows PowerShell Workflow](/documentation/articles/automation-powershell-workflow).  You directly edit the code of the runbook using the text editor in the Azure Management Portal.  You can also use any offline text editor and [import the runbook](/documentation/articles/automation-creating-importing-runbook) into Azure Automation.

### Advantages

- Implement all complex logic with PowerShell Workflow code.
- Use [checkpoints](/documentation/articles/automation-powershell-workflow#checkpoints) to resume runbook in case of error.
- Use [parallel processing](/documentation/articles/automation-powershell-workflow#parallel-processing) to perform multiple actions in parallel.
- Can include other PowerShell Workflow runbooks as child runbooks to create high level workflows.


### Limitations

- Author must be familiar with PowerShell Workflow.
- Runbook must deal with the additional complexity of PowerShell Workflow such as [deserialized objects](/documentation/articles/automation-powershell-workflow#code-changes).
- Runbook takes longer to start than PowerShell runbooks since it needs to be compiled before running.
- PowerShell runbooks can only be included as child runbooks by using the Start-AzureAutomationRunbook cmdlet which creates a new job.

## Considerations

You should take into account the following additional considerations when determining which type to use for a particular runbook.

- You can't convert runbooks from one type to another.
- There are limitations using runbooks of different types as a child runbook.  See [Child runbooks in Azure Automation](/documentation/articles/automation-child-runbooks) for more information.



  
## Related articles

- [Learning Windows PowerShell Workflow](/documentation/articles/automation-powershell-workflow)
- [Creating or Importing a Runbook](/documentation/articles/automation-creating-importing-runbook)
- [Creating or Importing a Runbook](/documentation/articles/automation-creating-importing-runbook)


