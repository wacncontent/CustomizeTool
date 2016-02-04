<properties
	pageTitle="How to create and deploy a cloud service | Windows Azure"
	description="Learn how to create and deploy a cloud service using the Quick Create method in Azure. These examples use the Azure Management Portal."
	services="cloud-services"
	documentationCenter=""
	authors="Thraka"
	manager="timlt"
	editor=""/>

<tags
	ms.service="cloud-services"
	ms.date="12/07/2015"
	wacn.date=""/>




<!-- deleted by customization
# How to create and deploy a cloud service
-->
<!-- keep by customization: begin -->
# How to Create and Deploy a Cloud Service
<!-- keep by customization: end -->

> [AZURE.SELECTOR]
- [Azure Management Portal](/documentation/articles/cloud-services-how-to-create-deploy)
- [Azure Management Portal](/documentation/articles/cloud-services-how-to-create-deploy-portal)

The Azure Management Portal provides two ways for you to create and deploy a cloud service: *Quick Create* and *Custom Create*.

This article explains how to use the Quick Create method to create a new cloud service and then use **Upload** to upload and deploy a cloud service package in Azure. When you use this method, the Azure Management Portal makes available convenient links for completing all requirements as you go. If you're ready to deploy your cloud service when you create it, you can do both at the same time using Custom Create.

> [AZURE.NOTE] If you plan to publish your cloud service from Visual Studio <!-- deleted by customization Team Services (VSTS) --><!-- keep by customization: begin --> Online (VSO) <!-- keep by customization: end -->, use Quick Create, and then set up <!-- deleted by customization VSTS --><!-- keep by customization: begin --> VSO <!-- keep by customization: end --> publishing from the Azure Quickstart or the dashboard. For more information, see [Continuous Delivery to Azure by Using Visual Studio <!-- deleted by customization Team Services][TFSTutorialForCloudService] --><!-- keep by customization: begin --> Online][TFSTutorialForCloudService] <!-- keep by customization: end -->, or see help for the **Quick Start** page.

## Concepts
Three components are required to deploy an application as a cloud service in Azure:

- **Service Definition**  
  The cloud service definition file (.csdef) defines the service model, including the number of roles.

- **Service Configuration**  
  The cloud service configuration file (.cscfg) provides configuration settings for the cloud service and individual roles, including the number of role instances.

- **Service Package**  
  The service package (.cspkg) contains the application code and configurations and the service definition file.

You can learn more about these and how to create a package [here](/documentation/articles/cloud-services-model-and-package).

## Prepare your app
Before you can deploy a cloud service, you must create the cloud service package (.cspkg) from your application code and a cloud service configuration file (.cscfg). The Azure SDK provides tools for preparing these required deployment files. You can install the SDK from the [Azure Downloads](/downloads/) page, in the language in which you prefer to develop your application code.

Three cloud service features require special configurations before you export a service package:

<!-- deleted by customization
- If you want to deploy a cloud service that uses Secure Sockets Layer (SSL) for data encryption, [configure your application](/documentation/articles/cloud-services-configure-ssl-certificate-portal#modify) for SSL.

- If you want to configure Remote Desktop connections to role instances, [configure the roles](/documentation/articles/cloud-services-role-enable-remote-desktop) for Remote Desktop. This can only be done in the Management Portal.

- If you want to configure verbose monitoring for your cloud service, enable Azure Diagnostics for the cloud service. *Minimal monitoring* (the default monitoring level) uses performance counters gathered from the host operating systems for role instances (virtual machines). *Verbose monitoring* gathers additional metrics based on performance data within the role instances to enable closer analysis of issues that occur during application processing. To find out how to enable Azure Diagnostics, see [Enabling diagnostics in Azure](/documentation/articles/cloud-services-dotnet-diagnostics).

To create a cloud service with deployments of web roles or worker roles, you must [create the service package](/documentation/articles/cloud-services-model-and-package#servicepackagecspkg).
-->
<!-- keep by customization: begin -->
- If you want to deploy a cloud service that uses Secure Sockets Layer (SSL) for data encryption, configure your application for SSL. For more information, see [How to Configure an SSL Certificate on an HTTPS Endpoint](https://msdn.microsoft.com/zh-cn/library/azure/ff795779.aspx).

- If you want to configure Remote Desktop connections to role instances, configure the roles for Remote Desktop. For more information about preparing the service definition file for remote access, see [Set Up a Remote Desktop Connection for a Role in Azure](https://msdn.microsoft.com/zh-cn/library/hh124107.aspx).

- If you want to configure verbose monitoring for your cloud service, enable Azure Diagnostics for the cloud service. *Minimal monitoring* (the default monitoring level) uses performance counters gathered from the host operating systems for role instances (virtual machines). "Verbose monitoring* gathers additional metrics based on performance data within the role instances to enable closer analysis of issues that occur during application processing. To find out how to enable Azure Diagnostics, see [Enabling Diagnostics in Azure](/documentation/articles/cloud-services-dotnet-diagnostics).

- To create a cloud service with deployments of web roles or worker roles, you must create the service package. For more information about the files related to the package, see [Set Up a Cloud Service for Azure](http://msdn.microsoft.com/zh-cn/library/hh124108.aspx). To create the package file, see [Package an Azure Application](http://msdn.microsoft.com/zh-cn/library/hh403979.aspx). If you are using Visual Studio to develop your application, see [Publishing a Cloud Service using the Azure Tools](http://msdn.microsoft.com/zh-cn/library/ff683672.aspx).
<!-- keep by customization: end -->

## Before you begin

- If you haven't installed the Azure SDK, click **Install Azure SDK** to open the [Azure Downloads page](/downloads/), and then download the SDK for the language in which you prefer to develop your code. (You'll have an opportunity to do this later.)

- If any role instances require a certificate, create the certificates. Cloud services require a .pfx file with a private key. <!-- deleted by customization [You --><!-- keep by customization: begin --> You <!-- keep by customization: end --> can upload the certificates to <!-- deleted by customization Azure]() --><!-- keep by customization: begin --> Azure <!-- keep by customization: end --> as you create and deploy the cloud service. <!-- keep by customization: begin --> For information about certificates, see [Manage Certificates](http://msdn.microsoft.com/zh-cn/library/gg981929.aspx). <!-- keep by customization: end -->

- If you plan to deploy the cloud service to an affinity group, create the affinity group. You can use an affinity group to deploy your cloud service and other Azure services to the same location in a region. You can create the affinity group in the **Networks** area of the <!-- deleted by customization Azure --> Management Portal, on the **Affinity Groups** page. <!-- keep by customization: begin --> For more information. <!-- keep by customization: end -->


## Step 3: Create a cloud service and upload the deployment package

1. Log <!-- deleted by customization in to --><!-- keep by customization: begin --> into <!-- keep by customization: end --> the [Azure Management Portal][].
2. Click **New > Compute**, and then scroll down to and click **Cloud Service**.

    ![Publish your cloud service](./media/cloud-services-how-to-create-deploy-portal/create-cloud-service.png)

<!-- deleted by customization
3. At the bottom of the information page that displays, click **Create**. 
4. In the new **Cloud Service** blade, enter a value for the **DNS name**.
5. Create a new **Resource Group** or select an existing one.
6. Select a **Location**.
7. Select **Package**, and on the **Upload a package** blade, fill in the required fields.
-->
<!-- keep by customization: begin -->
3. In the new **Cloud Service** blade, enter a value for the **DNS name**
4. Create a new **Resource Group** or select an existing one.
5. Select a **Location**.
6. Select **Package**, and on the **Upload a package** blade, fill in the required fields.
<!-- keep by customization: end -->

     If any of your roles contain a single instance, ensure **Deploy even if one or more roles contain a single instance** is selected.

<!-- deleted by customization 8 --><!-- keep by customization: begin --> 7 <!-- keep by customization: end -->. Make sure that **Start deployment** is selected.
<!-- deleted by customization
9. Click **OK**.

    ![Publish your cloud service](./media/cloud-services-how-to-create-deploy-portal/select-package.png)
-->
<!-- keep by customization: begin -->
8. Click **OK**.

    ![Publish your cloud service](./media/cloud-services-how-to-create-deploy-portal/select-package.png)
<!-- keep by customization: end -->

## Upload a certificate

If your deployment package was [configured to use certificates](/documentation/articles/cloud-services-configure-ssl-certificate-portal#modify), you can upload the certificate now.

1. Select **Certificates**, and on the **Add certificates** blade, select the SSL certificate .pfx file, and then provide the **Password** for the certificate,
2. Click **Attach certificate**, and then click **OK** on the **Add certificates** blade.
3. Click **Create** on the **Cloud Service** blade. When the deployment has reached the **Ready** status, you can proceed to the next steps.

    ![Publish your cloud service](./media/cloud-services-how-to-create-deploy-portal/attach-cert.png)


## Verify your deployment completed successfully

1. Click the cloud service instance.

	The status should show that the service is **Running**.

2. Under **Essentials**, click the **Site URL** to open your cloud service in a web browser.

    ![CloudServices_QuickGlance](./media/cloud-services-how-to-create-deploy-portal/running.png)


[TFSTutorialForCloudService]: <!-- deleted by customization http://go.microsoft.com/fwlink/?LinkID=251796 --><!-- keep by customization: begin --> http://go.microsoft.com/fwlink/?LinkID=251796&clcid=0x409 <!-- keep by customization: end -->

## Next steps

* [General configuration of your cloud service](/documentation/articles/cloud-services-how-to-configure-portal).
* Configure a [custom domain name](/documentation/articles/cloud-services-custom-domain-name-portal).
* [Manage your cloud service](/documentation/articles/cloud-services-how-to-manage-portal).
* Configure [ssl certificates](/documentation/articles/cloud-services-configure-ssl-certificate-portal).