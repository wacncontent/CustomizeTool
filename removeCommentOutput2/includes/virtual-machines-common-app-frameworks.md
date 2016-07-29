<!-- Ibiza portal: tested -->

## Applications

From this table you can find more information about the parameters that are used in the template, you can inspect the template before you deploy it.

| Application | View the template |
|:---|:---:|
| Active Directory | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/active-directory-new-domain-ha-2-dc) |
| Apache | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/apache2-on-ubuntu-vm) |
| Couchbase | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/couchbase-on-ubuntu) |
| DataStax | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/datastax) |
| Django | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/django-app) |
| Docker | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/docker-simple-on-ubuntu) |
| Elasticsearch | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/elasticsearch) |
| Jenkins | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/jenkins-on-ubuntu) |
| Kafka | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/kafka-on-ubuntu) |
| LAMP | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/lamp-app) |
| MongoDB | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/mongodb-on-ubuntu) |
| Redis | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/redis-high-availability) |
| SharePoint | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/sharepoint-three-vm) |
| Spark | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/spark-ubuntu-multidisks) |
| Tomcat | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/openjdk-tomcat-ubuntu-vm) |
| WordPress | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/wordpress-single-vm-ubuntu) 
| ZooKeeper | [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/zookeeper-cluster-ubuntu-vm) |

In addition to these templates, you can search through the [GitHub Repo](https://github.com/Azure/azure-quickstart-templates/).

## Azure PowerShell

Run these commands to create the resource group and the deployment after you replace the text in brackets with the resource group name, location, deployment name, and template name:

	New-AzureRmResourceGroup -Name {resource-group-name} -Location {location}
	New-AzureRmResourceGroupDeployment -Name {deployment-name} -ResourceGroupName {resource-group-name} -TemplateUri "https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/{template-name}/azuredeploy.json"

When you run the **New-AzureRmResourceGroupDeployment** command, you are prompted to enter values for the parameters in the template. Depending on the template, it can take some time for Azure to deploy the resources.

## Azure CLI

[Install Azure CLI](/documentation/articles/xplat-cli-install/), log in, and make sure you enable Resource Manager commands. For information about how to do this, see [Use the Azure CLI for Mac, Linux, and Windows with Azure Resource Manager](/documentation/articles/xplat-cli-azure-resource-manager/).

Run these commands to create the resource group and the deployment after you replace the text in brackets with the resource group name, location, deployment name, and template name:

	azure group create {resource-group-name} {location}
	azure group deployment create --template-uri https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/{template-name}/azuredeploy.json {resource-group-name} {deployment-name}

When you run the **azure group deployment create** command, you are prompted to enter values for the parameters in the template. Depending on the template, it can take some time for Azure to deploy the resources.

## Next steps

Discover all the templates at your disposal on [GitHub](https://github.com/Azure/azure-quickstart-templates).

Learn more about [Azure Resource Manager](/documentation/articles/resource-group-template-deploy/).
