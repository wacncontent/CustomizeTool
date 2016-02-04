<properties
	pageTitle="DataStax on Ubuntu with a Resource Manager template | Windows Azure"
	description="Learn to easily deploy a new DataStax cluster on Ubuntu VMs by using Azure PowerShell or the Azure CLI and a Resource Manager template"
	services="virtual-machines"
	documentationCenter=""
	authors="scoriani"
	manager="timlt"
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="04/29/2015"
	wacn.date=""/>

# DataStax on Ubuntu with a Resource Manager <!-- deleted by customization template --><!-- keep by customization: begin --> Template <!-- keep by customization: end -->

<!-- deleted by customization
[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-rm-include.md)] classic deployment model.


DataStax is a recognized industry leader in developing and delivering solutions based on Apache Cassandra--the commercially supported, enterprise-ready NoSQL distributed database technology that is widely acknowledged as agile, always on, and predictably scalable to any size. DataStax offers both the Enterprise (DSE) and Community (DSC) flavors. It also provides capabilities like in-memory computing, enterprise-level security, fast and powerful integrated analytics, and enterprise search.

In addition to what is already available in Azure Marketplace, now you can also easily deploy a new DataStax cluster on Ubuntu VMs by using a Resource Manager template deployed through [Azure PowerShell](/documentation/articles/powershell-install-configure) or the [Azure CLI](/documentation/articles/xplat-cli-install).
-->
<!-- keep by customization: begin -->
DataStax is a recognized industry leader in developing and delivering solutions based on Apache Cassandra™ - the commercially-supported, enterprise-ready NoSQL distributed database technology that is widely-acknowledged as agile, always-on, and predictably scalable to any size. DataStax offers both the Enterprise (DSE) and Community (DSC) flavors. It also provides capabilities like in-memory computing, enterprise-level security, fast and powerful integrated analytics, and enterprise search.

In addition to what is already available in Azure Marketplace, now you can also easily deploy a new DataStax cluster on Ubuntu VMs  using a Resource Manager template deployed through [Azure PowerShell](/documentation/articles/powershell-install-configure) or the [Azure CLI](/documentation/articles/xplat-cli).
<!-- keep by customization: end -->

Newly deployed clusters based on this template will have the topology described in the following diagram, although other topologies can be easily achieved by customizing the template presented in this article:

![cluster-architecture](./media/virtual-machines-datastax-template/cluster-architecture.png)

Using parameters, you can define the number of nodes that will be deployed in the new Apache Cassandra cluster. An instance of the DataStax <!-- deleted by customization Operations --><!-- keep by customization: begin --> Operation <!-- keep by customization: end --> Center service will be also deployed in a stand-alone VM within the same <!-- deleted by customization virtual network --><!-- keep by customization: begin --> VNET <!-- keep by customization: end -->, giving you the ability to monitor the status of the cluster and all individual nodes, add/remove nodes, and perform all administrative tasks related to that cluster.

Once the deployment is complete, you can access the <!-- deleted by customization DataStax --><!-- keep by customization: begin --> Datastax <!-- keep by customization: end --> Operations Center VM instance <!-- deleted by customization by --> using the configured DNS address. The OpsCenter VM has SSH port 22 enabled, as well as port 8443 for HTTPS. The DNS address for the operations center will include <!-- keep by customization: begin --> the <!-- keep by customization: end --> *dnsName* and *region* entered as parameters, resulting in the format `{dnsName}.{region}.chinacloudapp.cn`. If you created a deployment with the *dnsName* parameter set to "datastax” in the "China North” region <!-- deleted by customization, --> you could access the <!-- deleted by customization DataStax --><!-- keep by customization: begin --> Datastax <!-- keep by customization: end --> Operations Center VM for the deployment at `https://datastax.chinanorth.chinacloudapp.cn:8443`.

> [AZURE.NOTE] The certificate used in the deployment is a self-signed certificate that will create a browser warning. You can follow the process on the <!-- deleted by customization [DataStax](http://www.datastax.com/) website --><!-- keep by customization: begin --> [Datastax](http://www.datastax.com/) web site <!-- keep by customization: end --> for replacing the certificate with your own SSL certificate.

Before diving into more details related to <!-- keep by customization: begin --> the <!-- keep by customization: end --> Azure Resource Manager and the template we will use for this deployment, make sure you have Azure PowerShell or the Azure CLI configured correctly.

<!-- deleted by customization
[AZURE.INCLUDE [arm-getting-setup-powershell](../includes/arm-getting-setup-powershell.md)]

[AZURE.INCLUDE [xplat-getting-set-up-arm](../includes/xplat-getting-set-up-arm.md)]

## Create a Datastax-based Cassandra cluster by using a Resource Manager template

Follow these steps to create an Apache Cassandra cluster, based on DataStax, by using a Resource Manager template from the GitHub template repository. Each step will include directions for both Azure PowerShell and the Azure CLI.

### Step 1-a: Download the template files by using Azure PowerShell
-->
<!-- keep by customization: begin -->
[AZURE.INCLUDE [arm-getting-setup-powershell](../includes/arm-getting-setup-powershell)]

[AZURE.INCLUDE [xplat-getting-set-up-arm](../includes/xplat-getting-set-up-arm)]

## Create a Datastax-based Cassandra cluster with a Resource Manager template

Follow these steps to create an Apache Cassandra cluster, based on DataStax,  using a Resource Manager template from the Github template repository. Each step will include directions for both Azure PowerShell and the Azure CLI.

### Step 1-a: Download the template files using PowerShell
<!-- keep by customization: end -->

Create a local folder for the JSON template and other associated files (for example, C:\Azure\Templates\DataStax).

Substitute in the folder name of your local folder and run these commands:

	$folderName="C:\Azure\Templates\DataStax"
	$webclient = New-Object System.Net.WebClient
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/azuredeploy.json"
	$filePath = $folderName + "\azuredeploy.json"
	$webclient.DownloadFile($url,$filePath)
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/azuredeploy-parameters.json"
	$filePath = $folderName + "\azuredeploy-parameters.json"
	$webclient.DownloadFile($url,$filePath)
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/dsenode.sh"
	$filePath = $folderName + "\dsenode.sh"
	$webclient.DownloadFile($url,$filePath)
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/ephemeral-nodes-resources.json"
	$filePath = $folderName + "\ephemeral-nodes-resources.json"
	$webclient.DownloadFile($url,$filePath)
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/metadata.json"
	$filePath = $folderName + "\metadata.json"
	$webclient.DownloadFile($url,$filePath)
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/opscenter-install-resources.json"
	$filePath = $folderName + "\opscenter-install-resources.json"
	$webclient.DownloadFile($url,$filePath)
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/opscenter-resources.json"
	$filePath = $folderName + "\opscenter-resources.json"
	$webclient.DownloadFile($url,$filePath)
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/opscenter.sh"
	$filePath = $folderName + "\opscenter.sh"
	$webclient.DownloadFile($url,$filePath)
	$url = "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/datastax-on-ubuntu/shared-resources.json"
	$filePath = $folderName + "shared-resources.json"
	$webclient.DownloadFile($url,$filePath)

### Step 1-b: Download the template files <!-- deleted by customization by --> using the Azure CLI

<!-- deleted by customization
Clone the entire template repository by using a Git client of your choice, for example:
-->
<!-- keep by customization: begin -->
Clone the entire template repository using a git client of your choice, for example:
<!-- keep by customization: end -->

	git clone https://github.com/Azure/azure-quickstart-templates C:\Azure\Templates

When <!-- deleted by customization the cloning is --> completed, look for the **datastax-on-ubuntu** folder in your C:\Azure\Templates directory.

### Step 2: (optional) Understand the template parameters

When you deploy non-trivial solutions like an Apache Cassandra cluster based on DataStax, you must specify a set of configuration parameters to deal with a number of <!-- keep by customization: begin --> settings <!-- keep by customization: end --> required <!-- deleted by customization settings -->. By declaring these parameters in the template definition, it's possible to specify values during deployment through an external file or <!-- deleted by customization on --><!-- keep by customization: begin --> in <!-- keep by customization: end --> the <!-- deleted by customization command line --><!-- keep by customization: begin --> command-line <!-- keep by customization: end -->.

In the "parameters" section at the top of the <!-- deleted by customization azuredeploy.json --><!-- keep by customization: begin --> **azuredeploy.json** <!-- keep by customization: end --> file, you'll find the set of parameters that are required by the template to configure a DataStax cluster. Here is an example of the <!-- deleted by customization "parameters" --><!-- keep by customization: begin --> parameters <!-- keep by customization: end --> section from this template's azuredeploy.json file:

	"parameters": {
		"region": {
			"type": "string",
			"defaultValue": "China North",
			"metadata": {
				"Description": "Location where resources will be provisioned"
			}
		},
		"storageAccountPrefix": {
			"type": "string",
			"defaultValue": "uniqueStorageAccountName",
			"metadata": {
<!-- deleted by customization
				"Description": "Unique namespace for the storage account where the virtual machine's disks will be placed"
-->
<!-- keep by customization: begin -->
				"Description": "Unique namespace for the Storage Account where the Virtual Machine's disks will be placed"
<!-- keep by customization: end -->
			}
		},
		"dnsName": {
			"type": "string",
			"metadata" : {
				"Description": "DNS subname for the <!-- deleted by customization operations --><!-- keep by customization: begin --> opserations <!-- keep by customization: end --> center public IP"
			}
		},
		"virtualNetworkName": {
			"type": "string",
			"defaultValue": "myvnet",
			"metadata": {
				"Description": "Name of the virtual network provisioned for the cluster"
			}
		},
		"adminUsername": {
			"type": "string",
			"metadata": {
				"Description": "Administrator user name used when provisioning virtual machines"
			}
		},
		"adminPassword": {
			"type": "securestring",
			"metadata": {
				"Description": "Administrator password used when provisioning virtual machines"
			}
		},
		"opsCenterAdminPassword": {
			"type": "securestring",
			"metadata": {
				"Description": "Sets the operations center admin user password"
			}
		},
		"clusterVmSize": {
			"type": "string",
			"defaultValue": "Standard_D3",
			"allowedValues": [
				"Standard_D1",
				"Standard_D2",
				"Standard_D3",
				"Standard_D4",
				"Standard_D11",
				"Standard_D12",
				"Standard_D13",
				"Standard_D14"
			],
			"metadata": {
				"Description": "The size of the virtual machines used when provisioning cluster nodes"
			}
		},
		"clusterNodeCount": {
			"type": "int",
			"metadata": {
				"Description": "The number of nodes provisioned in the cluster"
			}
		},
		"clusterName": {
			"type": "string",
			"metadata": {
				"Description": "The name of the cluster provisioned"
			}
		}
	}

Each parameter has details such as data type and allowed values. This allows for validation of parameters passed during template execution in an interactive mode <!-- deleted by customization (e.g., Azure --><!-- keep by customization: begin --> (e.g. <!-- keep by customization: end --> PowerShell or Azure CLI), as well as a self-discovery UI that could be <!-- deleted by customization dynamically built --><!-- keep by customization: begin --> dynamically-built <!-- keep by customization: end --> by parsing the list of required parameters and their descriptions.

<!-- deleted by customization
### Step 3-a: Deploy a DataStax cluster by using a template via Azure PowerShell

Prepare a parameters file for your deployment by creating a JSON file that contains runtime values for all parameters. This file will then be passed as a single entity to the deployment command. If you do not include a parameters file, Azure PowerShell will use any default values specified in the template, and then prompt you to fill in the remaining values.

Here is an example set of parameters from the azuredeploy-parameters.json file:
-->
<!-- keep by customization: begin -->
### Step 3-a: Deploy a DataStax cluster with a template using PowerShell

Prepare a parameters file for your deployment by creating a JSON file containing runtime values for all parameters. This file will then be passed as a single entity to the deployment command. If you do not include a parameters file,  PowerShell will use any default values specified in the template, and then prompt you to fill in the remaining values.

Here is an example set of parameters from the **azuredeploy-parameters.json** file:
<!-- keep by customization: end -->

	{
		"storageAccountPrefix": {
			"value": "scorianisa"
		},
		"dnsName": {
			"value": "scorianids"
		},
		"virtualNetworkName": {
			"value": "datastax"
		},
		"adminUsername": {
			"value": "scoriani"
		},
		"adminPassword": {
			"value": ""
		},
		"region": {
			"value": "China North"
		},
		"opsCenterAdminPassword": {
			"value": ""
		},
		"clusterVmSize": {
			"value": "Standard_D3"
		},
		"clusterNodeCount": {
			"value": 3
		},
		"clusterName": {
			"value": "cl1"
		}
	}

Fill in an Azure deployment name, resource group name, Azure location, and the folder of your saved JSON deployment file. Then run these commands:

	$deployName="<deployment name>"
	$RGName="<resource group name>"
	$locName="<Azure location, such as China North>"
	$folderName="<folder name, such as C:\Azure\Templates\DataStax>"
	$templateFile= $folderName + "\azuredeploy.json"
	$templateParameterFile= $folderName + "\azuredeploy-parameters.json"

	New-AzureResourceGroup -Name $RGName -Location $locName

	New-AzureResourceGroupDeployment -Name $deployName -ResourceGroupName $RGName -TemplateParameterFile $templateParameterFile -TemplateFile $templateFile

When you run the **New-AzureResourceGroupDeployment** command, this will extract parameter values from the JSON parameters file, and will start executing the template accordingly. Defining and using multiple parameter files with your different environments <!-- deleted by customization (test --><!-- keep by customization: begin --> (e.g. Test <!-- keep by customization: end -->, <!-- deleted by customization production --><!-- keep by customization: begin --> Production <!-- keep by customization: end -->, etc.) will promote template reuse and simplify complex multi-environment solutions.

When deploying, please keep in mind that a new Azure <!-- deleted by customization storage account --><!-- keep by customization: begin --> Storage Account <!-- keep by customization: end --> needs to be created <!-- deleted by customization, --> so the name you provide as the storage account parameter must be unique and meet all requirements for an Azure <!-- deleted by customization storage account --><!-- keep by customization: begin --> Storage Account <!-- keep by customization: end --> (lowercase letters and numbers only).

During and after deployment, you can check all the requests that were made during provisioning, including any errors that occurred.  

To do that, go to the [Azure Management Portal](https://manage.windowsazure.cn) and do the following:

<!-- deleted by customization
- Click **Browse** on the left-hand navigation bar, and then scroll down and click **Resource Groups**.  
- Click the resource group that you just created, to bring up the "Resource Group” blade.  
- By clicking  the "Events” bar graph in the **Monitoring** part of the "Resource Group” blade, you can see the events for your deployment <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->
- By clicking individual events, you can drill further down into the details of each operation made on behalf of the template.
-->
<!-- keep by customization: begin -->
- Click "Browse” on the left-hand navigation bar, scroll down and click on "Resource Groups”.  
- After clicking on the Resource Group that you just created, it will bring up the "Resource Group” blade.  
- By clicking on the "Events” bar graph in the "Monitoring” part of the "Resource Group” blade, you can see the events for your deployment <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->
- Clicking on individual events lets you drill further down into the details of each individual operation made on behalf of the template
<!-- keep by customization: end -->

After your tests, if you need to remove this resource group and all of its resources (the storage account, virtual machine, and virtual network), use this single command:

	Remove-AzureResourceGroup -Name "<resource group name>" -Force

<!-- deleted by customization
### Step 3-b: Deploy a DataStax cluster by using a template via the Azure CLI

To deploy a DataStax cluster via the Azure CLI, first create a resource group by specifying a name and a location:
-->
<!-- keep by customization: begin -->
### Step 3-b: Deploy a DataStax cluster with a template using the Azure CLI

To deploy a Datastax cluster via the Azure CLI, first create a Resource Group by specifying a name and a location:
<!-- keep by customization: end -->

	azure group create dsc "China North"

Pass this <!-- deleted by customization resource group --><!-- keep by customization: begin --> Resource Group <!-- keep by customization: end --> name, the location of the JSON template file, and the location of the parameters file (see the above <!-- deleted by customization Azure --> PowerShell section for details) into the following command:

	azure group deployment create dsc -f .\azuredeploy.json -e .\azuredeploy-parameters.json

You can check the status of individual resources deployments <!-- deleted by customization by using --><!-- keep by customization: begin --> with <!-- keep by customization: end --> the following command:

	azure group deployment list dsc

## A tour of the <!-- deleted by customization DataStax --><!-- keep by customization: begin --> Datastax <!-- keep by customization: end --> template structure and file organization

In order to design a robust and reusable Resource Manager template, additional thinking is needed to organize the series of complex and interrelated tasks required during the deployment of a complex solution like DataStax. <!-- deleted by customization By leveraging --><!-- keep by customization: begin --> Leveraging <!-- keep by customization: end --><!-- deleted by customization Resource Manager template linking --><!-- keep by customization: begin --> ARM **template linking** <!-- keep by customization: end --> and <!-- deleted by customization resource looping --><!-- keep by customization: begin --> **resource looping** <!-- keep by customization: end --> in addition to script execution through related extensions, it's possible to implement a modular approach that can be reused with virtually any complex template-based deployment.

<!-- deleted by customization
This section steps you through the structure of the azuredeploy.json file for the DataStax cluster.
-->
<!-- keep by customization: begin -->
This diagram describes the relationships between all the files downloaded from GitHub for this deployment:

![datastax-files](./media/virtual-machines-datastax-template/datastax-files.png)

This section steps you through the structure of the **azuredeploy.json** file for the Datastax cluster.
<!-- keep by customization: end -->

### "parameters" section

The "parameters" section of <!-- deleted by customization azuredeploy.json --><!-- keep by customization: begin --> **azuredeploy.json** <!-- keep by customization: end --> specifies modifiable parameters that are used in this template. The aforementioned <!-- deleted by customization azuredeploy-parameters.json --><!-- keep by customization: begin --> **azuredeploy-parameters.json** <!-- keep by customization: end --> file is used to pass values into the "parameters" section of azuredeploy.json during template execution.

### "variables" section

The "variables" section specifies variables that can be used throughout this template. This contains a number of fields (JSON data types or fragments) that will be set to constants or calculated values at execution time. Here is the "variables" section for this <!-- deleted by customization DataStax --><!-- keep by customization: begin --> Datastax <!-- keep by customization: end --> template:

	"variables": {
	"templateBaseUrl": "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/datastax-on-ubuntu/",
	"sharedTemplateUrl": "[concat(variables('templateBaseUrl'), 'shared-resources.json')]",
	"clusterNodesTemplateUrl": "[concat(variables('templateBaseUrl'), 'ephemeral-nodes-resources.json')]",
	"opsCenterTemplateUrl": "[concat(variables('templateBaseUrl'), 'opscenter-resources.json')]",
	"opsCenterInstallTemplateUrl": "[concat(variables('templateBaseUrl'), 'opscenter-install-resources.json')]",
	"opsCenterVmSize": "Standard_A1",
	"networkSettings": {
		"virtualNetworkName": "[parameters('virtualNetworkName')]",
		"addressPrefix": "10.0.0.0/16",
		"subnet": {
			"dse": {
				"name": "dse",
				"prefix": "10.0.0.0/24",
				"vnet": "[parameters('virtualNetworkName')]"
			}
		},
		"statics": {
			"clusterRange": {
				"base": "10.0.0.",
				"start": 5
			},
			"opsCenter": "10.0.0.240"
		}
	},
	"osSettings": {
		"imageReference": {
			"publisher": "Canonical",
			"offer": "UbuntuServer",
			"sku": "14.04.2-LTS",
			"version": "latest"
		},
		"scripts": [
			"[concat(variables('templateBaseUrl'), 'dsenode.sh')]",
			"[concat(variables('templateBaseUrl'), 'opscenter.sh')]",
			"https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/shared_scripts/ubuntu/vm-disk-utils-0.1.sh"
		]
	},
	"sharedStorageAccountName": "[concat(parameters('storageAccountPrefix'),'cmn')]",
	"nodeList": "[concat(variables('networkSettings').statics.clusterRange.base, variables('networkSettings').statics.clusterRange.start, '-', parameters('clusterNodeCount'))]"
	},

Drilling down into this example, you can see two different approaches. In this first fragment, the <!-- deleted by customization **osSettings** --><!-- keep by customization: begin --> "osSettings” <!-- keep by customization: end --> variable is a nested JSON element <!-- deleted by customization that contains four --><!-- keep by customization: begin --> containing 4 <!-- keep by customization: end --> key-value pairs:

	"osSettings": {
	      "imageReference": {
	        "publisher": "Canonical",
	        "offer": "UbuntuServer",
	        "sku": "14.04.2-LTS",
	        "version": "latest"
	      },

	 
In this second fragment, the <!-- deleted by customization **scripts** --><!-- keep by customization: begin --> "scripts" <!-- keep by customization: end --> variable is a JSON array where each element will be calculated at <!-- deleted by customization run time through --><!-- keep by customization: begin --> runtime using <!-- keep by customization: end --> a template language function (concat) and the value of another variable plus string constants:

	      "scripts": [
	        "[concat(variables('templateBaseUrl'), 'dsenode.sh')]",
	        "[concat(variables('templateBaseUrl'), 'opscenter.sh')]",
	        "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/shared_scripts/ubuntu/vm-disk-utils-0.1.sh"
	      ]

### "resources" section

The <!-- deleted by customization "resources" --><!-- keep by customization: begin --> **"resources"** <!-- keep by customization: end --> section is where most of the action is happening. Looking carefully inside this section, you can immediately identify two different cases <!-- deleted by customization. The --><!-- keep by customization: begin -->: the <!-- keep by customization: end --> first one is an element defined of type `Microsoft.Resources/deployments` that basically means the invocation of a nested deployment within the main one. Through the <!-- deleted by customization **templateLink** --><!-- keep by customization: begin --> "templateLink" <!-- keep by customization: end --> element (and related version property), it's possible to specify a linked template file that will be invoked <!-- deleted by customization by --> passing a set of parameters as input, as seen in this fragment:

	{
	      "name": "shared",
	      "type": "Microsoft.Resources/deployments",
	      "apiVersion": "2015-01-01",
	      "properties": {
	        "mode": "Incremental",
	        "templateLink": {
	          "uri": "[variables('sharedTemplateUrl')]",
	          "contentVersion": "1.0.0.0"
	        },
	        "parameters": {
	          "region": {
	            "value": "[parameters('region')]"
	          },
	          "networkSettings": {
	            "value": "[variables('networkSettings')]"
	          },
	          "storageAccountName": {
	            "value": "[variables('sharedStorageAccountName')]"
	          }
	        }
	      }
	    },

From this first example, it is clear how <!-- deleted by customization azuredeploy.json --><!-- keep by customization: begin --> **azuredeploy.json** <!-- keep by customization: end --> in this scenario has been organized as a sort of orchestration mechanism, invoking a number of other template files <!-- deleted by customization. Each --><!-- keep by customization: begin -->, each <!-- keep by customization: end --><!-- deleted by customization file is --><!-- keep by customization: begin --> one <!-- keep by customization: end --> responsible for part of the required deployment activities.

In particular, the following linked templates will be used for this deployment:

-	**shared-resource.json**: <!-- deleted by customization Contains --><!-- keep by customization: begin --> contains <!-- keep by customization: end --> the definition of all resources that will be shared across the deployment. Examples are storage accounts used to store <!-- deleted by customization a --> VM's OS disks and virtual networks.
-	**opscenter-resources.json**: <!-- deleted by customization Deploys --><!-- keep by customization: begin --> deploys <!-- keep by customization: end --> an OpsCenter VM and all related resources, including a network interface and public IP address.
-	**opscenter-install-resources.json**: <!-- deleted by customization Deploys --><!-- keep by customization: begin --> deploys <!-- keep by customization: end --> the OpsCenter VM extension (custom script for Linux) that will invoke the specific bash script file <!-- deleted by customization (opscenter.sh) --><!-- keep by customization: begin --> (**opscenter.sh**) <!-- keep by customization: end --> required to <!-- deleted by customization set up --><!-- keep by customization: begin --> setup <!-- keep by customization: end --> the OpsCenter service within that VM.
-	**ephemeral-nodes-resources.json**: <!-- deleted by customization Deploys --><!-- keep by customization: begin --> deploys <!-- keep by customization: end --> all cluster node VMs and connected resources (network cards, private IPs, etc.). This template will also deploy VM extensions (custom scripts for Linux) and invoke a bash script <!-- deleted by customization (dsenode.sh) --><!-- keep by customization: begin --> (**dsenode.sh**) <!-- keep by customization: end --> to physically install Apache Cassandra bits on each node.

Let's drill down into how this last template is used, as it is one of the most interesting from a template development perspective. One important concept to highlight is how a single template file can deploy multiple copies of a single resource type, and for each instance can set unique values for required settings. This concept is known as <!-- deleted by customization **resource looping** --><!-- keep by customization: begin --> **Resource Looping** <!-- keep by customization: end -->.

When <!-- deleted by customization ephemeral-nodes-resources.json --><!-- keep by customization: begin --> **ephemeral-nodes-resources.json** <!-- keep by customization: end --> is invoked from within the main <!-- deleted by customization azuredeploy.json --><!-- keep by customization: begin --> **azuredeploy.json** <!-- keep by customization: end --> file, a parameter called <!-- deleted by customization *nodeCount* --><!-- keep by customization: begin --> **nodeCount** <!-- keep by customization: end --> is provided as part of the parameters list. Within the child template, <!-- deleted by customization *nodeCount* --><!-- keep by customization: begin --> nodeCount <!-- keep by customization: end --> (the number of nodes to deploy in the cluster) will be used inside the <!-- deleted by customization **copy** --><!-- keep by customization: begin --> **"copy”** <!-- keep by customization: end --> element of each resource that needs to be deployed in multiple copies, as highlighted in the fragment below. For all settings where you need unique values for different instances of the deployed resource, the **copyindex()** function can be used to obtain a numeric value indicating the current index in that particular resource loop creation. In the following fragment, you can see this concept applied to multiple VMs being created for the <!-- deleted by customization DataStax --><!-- keep by customization: begin --> Datastax <!-- keep by customization: end --> cluster nodes:

			   {
			      "apiVersion": "2015-05-01-preview",
			      "type": "Microsoft.Compute/virtualMachines",
			      "name": "[concat(parameters('namespace'), 'vm', copyindex())]",
			      "location": "[parameters('region')]",
			      "copy": {
			        "name": "[concat(parameters('namespace'), 'vmLoop')]",
			        "count": "[parameters('nodeCount')]"
			      },
			      "dependsOn": [
			        "[concat('Microsoft.Network/networkInterfaces/', parameters('namespace'), 'nic', copyindex())]",
			        "[concat('Microsoft.Compute/availabilitySets/', parameters('namespace'), 'set')]",
			        "[concat('Microsoft.Storage/storageAccounts/', variables('storageAccountName'))]"
			      ],
			      "properties": {
			        "availabilitySet": {
			          "id": "[resourceId('Microsoft.Compute/availabilitySets', concat(parameters('namespace'), 'set'))]"
			        },
			        "hardwareProfile": {
			          "vmSize": "[parameters('vmSize')]"
			        },
			        "osProfile": {
			          "computername": "[concat(parameters('namespace'), 'vm', copyIndex())]",
			          "adminUsername": "[parameters('adminUsername')]",
			          "adminPassword": "[parameters('adminPassword')]"
			        },
			        "storageProfile": {
			          "imageReference": "[parameters('osSettings').imageReference]",
			          "osDisk": {
			            "name": "osdisk",
			            "vhd": {
			              "uri": "[concat('http://',variables('storageAccountName'),'.blob.core.chinacloudapi.cn/vhds/', variables('vmName'), copyindex(), '-osdisk.vhd')]"
			            },
			            "caching": "ReadWrite",
			            "createOption": "FromImage"
			          },
			          "dataDisks": [
			            {
			              "name": "datadisk1",
			              "diskSizeGB": 1023,
			              "lun": 0,
			              "vhd": {
			                "Uri": "[concat('http://', variables('storageAccountName'),'.blob.core.chinacloudapi.cn/','vhds/', variables('vmName'), copyindex(), 'DataDisk1.vhd')]"
			              },
			              "caching": "None",
			              "createOption": "Empty"
			            }
			          ]
			        },
			        "networkProfile": {
			          "networkInterfaces": [
			            {
			              "id": "[resourceId('Microsoft.Network/networkInterfaces',concat(parameters('namespace'), 'nic', copyindex()))]"
			            }
			          ]
			        }
			      }
			    },

Another important concept in resource creation is the ability to specify dependencies and precedencies between resources, as you can see in the **dependsOn** JSON array. In this particular template, each node will also have an attached 1TB disk (see "dataDisks") that can be used for hosting backups and snapshots of the Apache Cassandra instance.

Attached disks are formatted as part of the node preparation activities triggered by the execution of the <!-- deleted by customization dsenode.sh --><!-- keep by customization: begin --> **dsenode.sh** <!-- keep by customization: end --> script file. The first row of that script invokes another script:

	bash vm-disk-utils-0.1.sh

<!-- deleted by customization The --> vm-disk-utils-0.1.sh <!-- deleted by customization file --> is part of the **shared_scripts\ubuntu** folder in the <!-- deleted by customization azure-quickstart-templates GitHub --><!-- keep by customization: begin --> azure-quickstart-tempates github <!-- keep by customization: end --> repo, and contains very useful functions for disk mounting, formatting, and striping. These functions can be used in all templates in the repo.

Another interesting fragment to explore is the one related to CustomScriptForLinux VM extensions. These are installed as a separate type of resource, with a dependency on each cluster node (and the OpsCenter instance). They leverage the same resource looping mechanism described for virtual machines:

	{
	"type": "Microsoft.Compute/virtualMachines/extensions",
	"name": "[concat(parameters('namespace'), 'vm', copyindex(), '/installdsenode')]",
	"apiVersion": "2015-05-01-preview",
	"location": "[parameters('region')]",
	"copy": {
		"name": "[concat(parameters('namespace'), 'vmLoop')]",
		"count": "[parameters('nodeCount')]"
	},
	"dependsOn": [
		"[concat('Microsoft.Compute/virtualMachines/', parameters('namespace'), 'vm', copyindex())]",
		"[concat('Microsoft.Network/networkInterfaces/', parameters('namespace'), 'nic', copyindex())]"
	],
	"properties": {
		"publisher": "Microsoft.OSTCExtensions",
		"type": "CustomScriptForLinux",
		"typeHandlerVersion": "1.2",
		"settings": {
			"fileUris": "[parameters('osSettings').scripts]",
			"commandToExecute": "bash dsenode.sh"
		}
	}
	}

By familiarizing yourself with the other files included in this deployment, you will be able to understand all the details and best practices required to organize and orchestrate complex deployment strategies for <!-- deleted by customization multi-node --><!-- keep by customization: begin --> multi-nodes <!-- keep by customization: end --> solutions, based on any technology, <!-- deleted by customization by --> leveraging Azure Resource Manager templates. While not mandatory, a recommended approach is to structure your template files as highlighted by the following diagram:

![datastax-template-structure](./media/virtual-machines-datastax-template/datastax-template-structure.png)

In essence, this approach suggests to:

-	Define your core template file as a central orchestration point for all specific deployment activities, leveraging template linking to invoke <!-- deleted by customization sub-template --><!-- keep by customization: begin --> sub template <!-- keep by customization: end --> executions <!-- deleted by customization. -->
-	Create a specific template <!-- deleted by customization file --><!-- keep by customization: begin --> files <!-- keep by customization: end --> that will deploy all resources shared across all other specific deployment tasks <!-- deleted by customization (storage --><!-- keep by customization: begin --> (e.g. storage <!-- keep by customization: end --> accounts, <!-- deleted by customization virtual network --><!-- keep by customization: begin --> vnet <!-- keep by customization: end --> configuration, etc.). This can be heavily reused between deployments that have similar requirements in terms of common infrastructure.
<!-- deleted by customization
-	Include optional resource templates for spot requirements specific to a given resource.
-	For identical members of a group of resources (nodes in a cluster, etc.) <!-- deleted by customization, --> create specific templates that leverage resource looping in order to deploy multiple instances with unique properties <!-- deleted by customization. -->
-	For all post-deployment tasks (product installation, configurations, etc.), leverage script deployment extensions and create scripts specific to each technology.

For more information, see [Azure Resource Manager template language](/documentation/articles/resource-group-authoring-templates).
-->
<!-- keep by customization: begin -->
-	Include optional resource templates for spot requirements specific of a given resource
-	For identical members of a group of resources (nodes in a cluster, etc.) <!-- deleted by customization, --> create specific templates that leverage resource looping in order to deploy multiple instances with unique properties <!-- deleted by customization. -->
-	For all post deployment tasks (e.g. product installation, configurations, etc.) leverage script deployment extensions and create scripts specific to each technology

For more information, see [Azure Resource Manager Template Language](https://msdn.microsoft.com/zh-CN/library/azure/dn835138.aspx).
<!-- keep by customization: end -->
