deletion:

deleted:

		Prefer watching to reading? Have a look at the below video from May 2015, when Azure Automation DSC was first announced. **Note:** While the concepts and lifecycle discussed in this video are correct, Azure Automation DSC has progressed a lot since this video was recorded. It is now in public preview, has a more extensive UI in the Azure Management Portal, and supports additional capabilities.
		
		> [AZURE.VIDEO microsoft-ignite-2015-heterogeneous-configuration-management-using-microsoft-azure-automation]

reason: (video)

deleted:

		- When onboarding an Azure VM for management with Azure Automation DSC using `Register-AzureAutomationDscNode`, `Set-AzureVMExtension`, or the Azure Automation DSC VM extension in the Azure preview portal, if registration fails with **The computer name was not specified and the configuration directory does not have any configuration files**, this is a false alarm and the VM registration actually succeeded. Successful registration can be verified using the `Get-AzureAutomationDscNode` cmdlet.
		
		- When onboarding an Azure VM for management with Azure Automation DSC using `Register-AzureAutomationDscNode`, `Set-AzureVMExtension`, or the Azure Automation DSC VM extension in the Azure preview portal, it could take up to an hour for the VM to show up as a DSC node in Azure Automation. This is due to the installation of Windows Management Framework 5.0 on the VM by the Azure VM DSC extension, which is required to onboard the VM to Azure Automation DSC.

reason: (DSC)

