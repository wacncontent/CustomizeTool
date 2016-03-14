<properties
   pageTitle="Deploy popular application frameworks using templates | Windows Azure"
   description="Create popular application frameworks by using Azure Resource Manager templates to install Active Directory, Docker, and many more."
   services="virtual-machines"
   documentationCenter="virtual-machines"
   authors="squillace"
   manager="timlt"
   editor=""
   tags="azure-resource-manager" />

<tags
	ms.service="virtual-machines"
	ms.date="02/03/2016"
	wacn.date=""/>

# Deploy popular application frameworks by using Azure Resource Manager templates

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-rm-include.md)] classic deployment model.

Workloads usually require many resources to function according to design. Azure Resource Manager templates make it possible for you to not only define how applications are configured, but also how the resources are deployed to support configured applications. This article introduces you to the most popular templates in the gallery and gives you information for using the Azure Management Portal, Azure PowerShell, or Azure CLI to deploy them.

| Apache web server | This template uses the Azure Linux CustomScript extension to deploy an Apache web server. The template creates an Ubuntu VM, installs Apache2, and creates a simple HTML file.| [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/apache2-on-ubuntu-vm) | 
| Couchbase cluster | This template deploys a Couchbase cluster on Ubuntu virtual machines. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/couchbase-on-ubuntu) |
| DataStax cluster | This template installs a DataStax cluster on Ubuntu VMs by using the Azure Linux CustomScript extension. [Detailed walkthrough.](/documentation/articles/virtual-machines-datastax-template)| [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/datastax-on-ubuntu) |
| DataStax Enterprise cluster | This template installs a DataStax Enterprise cluster on Ubuntu VMs by using the Azure Linux CustomScript extension. [Detailed walkthrough.](/documentation/articles/virtual-machines-datastax-enterprise-template)| [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/datastax-enterprise) |
| Django app | This template deploys a Django application on an Ubuntu VM by using the Azure Linux CustomScript extension. It does a silent install of Python and Apache. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/django-app) |
| Docker containers | This template allows you to deploy an Ubuntu VM with Docker (by using the Docker extension) and three Docker containers pulled directly from Docker Hub and deployed via Docker Compose. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/docker-simple-on-ubuntu) |
| Elasticsearch cluster | This template deploys an Elasticsearch cluster on Ubuntu VMs and uses template linking to create data node scale units. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/elasticsearch) |
| Hortonworks HDP | This template creates a multiserver Hortonworks HDP 2.2 Apache Hadoop deployment on CentOS virtual machines, and it configures the HDP installation across a cluster.|  [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/hortonworks-on-centos) | 
| Jenkins master and slave nodes | This template deploys a Jenkins master node on an Ubuntu VM and multiple Jenkins slave nodes on two additional VMs. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/jenkins-on-ubuntu) |
| Kafka cluster | This template deploys a Kafka cluster on Ubuntu VMs by using the Azure Linux CustomScript extension. The template also creates one publicly accessible VM that acts as a "jumpbox" so you can SSH into the Kafka nodes for diagnostics or troubleshooting purposes.| [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/kafka-on-ubuntu) |
| LAMP stack on Ubuntu | This template uses the Azure Linux CustomScript extension to deploy a LAMP application by creating an Ubuntu VM, doing a silent install of MySQL, Apache, and PHP, and then creating a simple PHP script. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/lamp-app) |
| MongoDB | This template deploys MongoDB on an Ubuntu virtual machine by using the Linux CustomScript extension. [Detailed walkthrough.](/documentation/articles/virtual-machines-mongodb-template)| [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/mongodb-on-ubuntu) |
| Redis cluster | This template deploys a Redis cluster on Ubuntu virtual machines. The template also creates one publicly accessible VM that acts as a "jumpbox" so you can SSH into the Redis nodes for diagnostics or troubleshooting purposes. [Detailed walkthrough.](/documentation/articles/virtual-machines-redis-template)| [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/redis-high-availability) | 
| SharePoint farm | This template creates three new Azure VMs, each with a public IP address, a load balancer, and a virtual network. It configures one VM to be an Active Directory DC for a new forest and domain, one with SQL Server domain joined, and the third with a SharePoint farm and site. All VMs have public-facing RDP. [Detailed walkthrough.](/documentation/articles/virtual-machines-rmtemplate-sharepoint-walkthrough) | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/sharepoint-three-vm) | 
| Spark cluster | This template deploys a Spark cluster on Ubuntu virtual machines. The template also creates one publicly accessible VM that acts as a "jumpbox" so you can SSH into the Spark nodes for diagnostics or troubleshooting purposes. [Detailed walkthrough.](/documentation/articles/virtual-machines-spark-template)| [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/spark-ubuntu-multidisks) | 
| Tomcat and OpenJDK installation | This template installs OpenJDK and Tomcat on an Ubuntu VM. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/openjdk-tomcat-ubuntu-vm) |
| WordPress | This template deploys a complete LAMP stack to a single Ubuntu VM and then installs and initializes WordPress. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/wordpress-single-vm-ubuntu) |
| ZooKeeper cluster | This template creates a three-node ZooKeeper cluster on Ubuntu VMs. | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/zookeeper-cluster-ubuntu-vm) |

In addition to these templates, you can search through the [gallery templates](https://azure.microsoft.com/documentation/templates/).

## Azure Management Portal

Deploying a template by using the Azure Management Portal is easy to do by just sending a URL to it. You need the name of the template file to deploy it. You can find the name by looking at the pages in the template gallery or by looking in the Github repository. Change {template name} in this URL to the name of the template that you want to deploy and then enter it into your browser:

    https://manage.windowsazure.cn/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F{template name}%2Fazuredeploy.json

You should see the custom deployment blade:

![](./media/virtual-machines-workload-template-ad-domain/azure-portal-template.png)

1.	For the **Template** pane, click **Save**.
2.	Click **Parameters**. On the **Parameters** pane, enter new values, select from allowed values, or accept default values, and then click **OK**.
3.	If needed, click **Subscription** and select the correct Azure subscription.
4.	Click **Resource group** and select an existing resource group. Alternately, click **Or create new** to create a new one for this deployment.
5.	If needed, click **Location** and select the correct Azure location.
6.	If needed, click **Legal terms** to review the terms and agreement for using the template.
7.	Click **Create**.

Depending on the template, it can take some time for Azure to deploy the resources.

## Azure PowerShell

[AZURE.INCLUDE [powershell-preview](../includes/powershell-preview-inline-include.md)]

Run these commands to create the resource group and the deployment after you replace the text in brackets with the resource group name, location, deployment name, and template name:

	New-AzureRmResourceGroup -Name {resource-group-name} -Location {location}
	New-AzureRmResourceGroupDeployment -Name {deployment-name} -ResourceGroupName {resource-group-name} -TemplateUri "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/{template-name}/azuredeploy.json"

When you run the **New-AzureRmResourceGroupDeployment** command, you are prompted to enter values for the parameters in the template. Depending on the template, it can take some time for Azure to deploy the resources.

## Azure CLI

[Install Azure CLI](/documentation/articles/xplat-cli-install), log in, and make sure you enable Resource Manager commands. For information about how to do this, see [Use the Azure CLI for Mac, Linux, and Windows with Azure Resource Manager](/documentation/articles/xplat-cli-azure-resource-manager).

Run these commands to create the resource group and the deployment after you replace the text in brackets with the resource group name, location, deployment name, and template name:

	azure group create {resource-group-name} {location}
	azure group deployment create --template-uri https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/{template-name}/azuredeploy.json {resource-group-name} {deployment-name}

When you run the **azure group deployment create** command, you are prompted to enter values for the parameters in the template. Depending on the template, it can take some time for Azure to deploy the resources.

## Next steps

Discover all the templates at your disposal on [GitHub](https://github.com/Azure/azure-quickstart-templates).

Learn more about [Azure Resource Manager](/documentation/articles/resource-group-template-deploy).
