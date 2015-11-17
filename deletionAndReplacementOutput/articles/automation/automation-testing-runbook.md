deletion:

deleted:

		- [Graphical runbooks in Azure Automation](/documentation/articles/automation-graphical-authoring-intro)

reason: ()

replacement:

deleted:

		The procedure to test each [type of runbook](/documentation/articles/automation-runbook-types) is the same, and there is no difference in testing between the textual editor and the graphical editor in the Azure preview portal.  
		
		
		## To test a runbook in the Azure preview portal
		
		You can work with any [runbook type](/documentation/articles/automation-runbook-types) in the Azure preview portal.
		
		1. Open the Draft version of the runbook in either the [textual editor](/documentation/articles/automation-editing-a-runbook#Portal) or [graphical editor](/documentation/articles/automation-graphical-authoring-intro).
		2. Click the **Test** button to open the Test blade.
		3. If the runbook has parameters, they will be listed in the left pane where you can provide values to be used for the test.
		4. If you want to run the test on a [Hybrid Runbook Worker](/documentation/articles/automation-hybrid), then change **Run Settings** to **Hybrid Worker** and select the name of the target group.  Otherwise, keep the default **Azure** to run the test in the cloud.
		5. Click the **Start** button to start the test.
		6. If the runbook is [PowerShell Workflow](/documentation/articles/automation-runbook-types#powershell-workflow-runbooks) or [Graphical](/documentation/articles/automation-runbook-types#graphical-runbooks), then you can stop or suspend it while it is being tested with the buttons underneath the Output Pane. When you suspend the runbook, it completes the current activity before being suspended. Once the runbook is suspended, you can stop it or restart it.
		7. Inspect the output from the runbook in the output pane.

replaced by:

		The procedure to test each [type of runbook](/documentation/articles/automation-runbook-types) is the same.

reason: ()

