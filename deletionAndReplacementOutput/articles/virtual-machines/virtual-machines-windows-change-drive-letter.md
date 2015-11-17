replacement:

deleted:

		#Change the drive letter of the Windows temporary disk on a virtual machine created with the classic deployment model
		
		[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.

replaced by:

		#Change the drive letter of the Windows temporary disk

reason: ()

deleted:

		> [AZURE.WARNING] If you resize or "Stop (Deallocate)" a virtual machine, this may trigger placement of the virtual machine to a new hypervisor. A planned or unplanned maintenance event may also trigger this placement. In this scenario, the temporary disk will be reassigned to the first available drive letter. If you have an application that specifically requires the "D" drive, ensure that after moving the pagefile, you assign a new persistent disk and assign it the letter D. Azure will not take back the letter D.
		
		> [AZURE.WARNING] If you resize a virtual machine after explicitly moving the pagefile, note that you may encounter an error on boot if the new virtual machine's temporary disk is not large enough to contain the pagefile of the original VM size. You may also encounter this error if the temporary drive was not set to the next available drive letter, causing Windows to reference an invalid drive letter in pagefile configuration while Azure creates the temporary drive with the next available drive letter.

replaced by:

		> [AZURE.WARNING] If you resize a virtual machine and doing that moves the virtual machine to a different host, the temporary disk changes back to the D drive.

reason: ()

