deletion:

deleted:

		- [Use pre-compiled resources](#bPS4)

reason: ()

deleted:

		> [AZURE.IMPORTANT] Script actions must complete within 15 minutes, or they will timeout. During node provisioning, the script is ran concurrently with other setup and configuration processes. Competition for resources such as CPU time or network bandwidth may cause the script to take longer to finish than it does in your development environment.

reason: ()

deleted:

		### <a name="bPS4"></a>Use pre-compiled resources
		
		To minimize the time it takes to run the script, avoid operations that compile resources from source code. Instead, pre-compile the resources and store the binary version in Azure Blob storage so that it can quickly be downloaded to the cluster from your script.

reason: ()

