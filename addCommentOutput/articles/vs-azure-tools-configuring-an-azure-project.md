<properties
   pageTitle="Configure an Azure Cloud Service Project with Visual Studio | Windows Azure"
   description="Learn how to configure an Azure cloud service project in Visual Studio, depending on your requirements for that project."
   services="visual-studio-online"
   documentationCenter="na"
   authors="kempb"
   manager="douge"
   editor="tglee" />
<tags
	ms.service="multiple"
	ms.date="09/29/2015"
	wacn.date=""/>

<!-- deleted by customization
# Configure an Azure Cloud Service Project with Visual Studio

You can configure an Azure cloud service project, depending on your requirements for that project. You can set properties for the project for the following categories:

- **Publish a cloud service to Azure**

  You can set a property to make sure that an existing cloud service deployed to Azure is not accidentally deleted.

- **Run or debug a cloud service on the local computer**

  You can select a service configuration to use and indicate whether you want to start the Azure storage emulator.

- **Validate a cloud service package when it is created**

  You can decide to treat any warnings as errors so that you can make sure that the cloud service package will deploy without any issues. This reduces your wait time if you deploy and then discover that a failure occurred.

The following illustration shows how to select a configuration to use when you run or debug your cloud service locally. You can set any of the project properties that you require from this window, as shown in the illustration.

![Configure a Windows Azure Project](./media/vs-azure-tools-configuring-an-azure-project/IC713462.png)

## To configure an Azure cloud service project

1. To configure a cloud service project from **Solution Explorer**, open the shortcut menu for the cloud service project and then choose **Properties**.

  A page with the name of the cloud service project appears in the Visual Studio editor.

1. Choose the **Development** tab.

1. To make sure that you don't accidentally delete an existing deployment in Azure, in the prompt before deleting an existing deployment list, choose **True**.

1. To select the service configuration that you want to use when you run or debug your cloud service locally, in the **Service configuration** list choose the service configuration.

  >[AZURE.NOTE] If you want to create a service configuration to use, see How to: Manage Service Configurations and Profiles. If you want to modify a service configuration for a role, see [How to configure the roles for an Azure cloud service with Visual Studio](/documentation/articles/vs-azure-tools-configure-roles-for-cloud-service).

1. To start the Azure storage emulator when you run or debug your cloud service locally, in the **Start Azure storage emulator**, choose **True**.

1. To make sure that you cannot publish if there are package validation errors, in **Treat warnings as errors**, choose **True**.

1. To make sure that your web role uses the same port each time it starts locally in IIS Express, in **Use web project ports**, choose **True**. To use a specific port for a particular web project, open the shortcut menu for the web project, choose the **Properties** tab, choose the **Web** tab, and change the port number in the **Project Url** setting in the **IIS Express** section. For example, enter `http://localhost:14020` as the project URL.

1. To save any changes that you have made to the properties of the cloud service project, choose the **Save** button on the toolbar.
-->
<!-- keep by customization: begin -->
# Configuring an Azure Cloud Service Project Using Multiple Service Configurations

An Azure cloud service project includes two configuration files: ServiceDefinition.csdef and ServiceConfiguration.cscfg. These files are packaged with your Azure cloud service application and deployed to Azure.

- The **ServiceDefinition.csdef** file contains the metadata that is required by the Azure environment for the requirements of your cloud service application, including what roles it contains. This file also contains configuration settings that apply to all instances. These configuration settings can be read at runtime using the Azure Service Hosting Runtime API. This file cannot be updated while your service is running in Azure.

- The **ServiceConfiguration.cscfg** file sets values for the configuration settings defined in the service definition file and specifies the number of instances to run for each role. This file can be updated while your cloud service is running in Azure.

The Azure Tools for Visual Studio provide property pages that you can use to set configuration settings stored in these files. To access the property pages, on the shortcut menu of the role reference in **Solution Explorer**, choose **Properties**, as shown in the following figure. As an alternative, you can double-click the role reference.

![VS_Solution_Explorer_Roles_Properties](./media/vs-azure-tools-configuring-an-azure-project/IC784076.png)

For information about the underlying schemas for the service definition and service configuration files, see the [Schema Reference](https://msdn.microsoft.com/zh-cn/library/azure/dd179398.aspx). For more information about service configuration, see [How to manage service configurations and profiles](/documentation/articles/vs-azure-tools-service-configurations-and-profiles-how-to-manage).

## Configuring role properties

The property pages for a web role and a worker role are similar, although there are a few differences, pointed out in the following sections. In the **Caching** page, you can configure the Azure caching services.

### Configuration page

On the **Configuration** page, you can set the following properties.

**Instances**

Set the **Instance count** property to the number of instances the service should run for this role.

Set the **VM size** property to **Extra Small**, **Small**, **Medium**, **Large**, or **Extra Large**. For more information, see [Configure Sizes for Cloud Services](https://msdn.microsoft.com/zh-cn/library/azure/ee814754.aspx) .

**Startup Action (Web Role Only)**

Set this property to specify that Visual Studio should launch a web browser for either the HTTP endpoints or the HTTPS endpoints, or both when you start debugging.

The **HTTPS endpoint** option is available only if you have already defined an HTTPS endpoint for your role. You can define an HTTPS endpoint on the **Endpoints** property page.

If you have already added an HTTPS endpoint, the **HTTPS endpoint** option is enabled by default, and Visual Studio will launch a browser for this endpoint when you start debugging, in addition to a browser for your HTTP endpoint. This assumes that both startup options are enabled.

**Diagnostics**

By default, diagnostics is enabled for the Web role. The Azure cloud service project and storage account are set to use the local storage emulator. When you are ready to deploy to Azure, you can click the builder button (**…**) to update the storage account to use Azure storage in the cloud. You can transfer the diagnostics data to the storage account on demand or at automatically scheduled intervals. For more information about Azure diagnostics, see [Collect Logging Data by Using Azure Diagnostics](https://msdn.microsoft.com/zh-cn/library/azure/gg433048.aspx).

### Settings page

On the **Settings** page, you can add configuration settings for your service. Configuration settings are name-value pairs. Code running in the role can read the values of your configuration settings at runtime using classes provided by the [Azure Managed Library](https://msdn.microsoft.com/zh-cn/library/azure/dn602775(v=azure.11).aspx). Specifically, the [GetConfigurationSettingValue](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.windowsazure.serviceruntime.roleenvironment.getconfigurationsettingvalue.aspx) method returns the value of a named configuration setting at runtime.

**Configuring a connection string to a storage account**

A connection string is a configuration setting that provides connection and authentication information for the storage emulator or for an Azure storage account. Whenever your code must access Azure storage services data – that is, blob, queue, or table data – from code running in a role, you will have to define a connection string for that storage account.

A connection string that points to an Azure storage account must use a defined format. For information about how to create connection strings, see [How to Configure Connection Strings](https://msdn.microsoft.com/zh-cn/library/azure/ee758697.aspx).

When you are ready to test your service against the Azure storage services, or when you are ready to deploy your cloud service to Azure, you can change the value of any connection strings to point to your Azure storage account. Click (…), select Enter storage account credentials. Enter your account information that includes your account name and account key. In the Storage Account Connection String dialog box, you can also indicate whether you want to use the default HTTPS endpoints (the default option), the default HTTP endpoints, or custom endpoints. You might decide to use custom endpoints if you have registered a custom domain name for your service, as described in [Configure a custom domain name for blob data in an Azure storage account](/documentation/articles/storage-custom-domain-name).

>[AZURE.IMPORTANT] You must modify your connection strings to point to an Azure storage account before you deploy your service. Failing to do this may cause your role not to start, or to cycle through the initializing, busy, and stopping states.

### Endpoints page

A worker role can have any number of HTTP, HTTPS, or TCP endpoints. Endpoints can be input endpoints, which are available to external clients, or internal endpoints, which are available to other roles that are running in the service.

- To make an HTTP endpoint available to external clients and Web browsers, change the endpoint type to input, and specify a name and a public port number.

- To make an HTTPS endpoint available to external clients and Web browsers, change the endpoint type to input, and specify a name, a public port number, and a management certificate name.

  Note that before you can specify a management certificate, you must define the certificate on the **Certificates** property page.

- To make an endpoint available for internal access by other roles in the cloud service, change the endpoint type to **internal**, and specify a name and possible private ports for this endpoint.

### Local storage page

You can use the Local Storage property page to reserve one or more local storage resources for a role. A local storage resource is a reserved directory in the file system of the Azure virtual machine in which an instance of a role is running. For more information about how to work with local storage resources, see [Configure Local Storage Resources](/documentation/articles/cloud-services-configure-local-storage-resources).

### Certificates page

On the **Certificates** page, you can associate certificates with your role. The certificates that you add can be used to configure your HTTPS endpoints on the **Endpoints** property page.

The **Certificates** property page adds information about your certificates to your service configuration. Note that your certificates are not packaged with your service; you must upload your certificates separately to Azure through the [Azure Management Portal](https://manage.windowsazure.cn/).

To associate a certificate with your role, provide a name for the certificate. You use this name to refer to the certificate when you configure an HTTPS endpoint on the **Endpoints** property page. Next, specify whether the certificate store is **Local Machine** or **Current User** and the name of the store. Finally, enter the certificate's thumbprint. If the certificate is in the **Current User\\Personal (My)** store, you can enter the certificate's thumbprint by selecting the certificate from a populated list. If it resides in any other location, enter the thumbprint value manually.

When you add a certificate from the certificate store, any intermediate certificates are automatically added to the configuration settings for you. These intermediate certificates must also be uploaded to Azure in order to correctly configure your service for SSL.

Any management certificates that you associate with your service apply to your service only when it is running in the cloud. When your service is running in the local development environment, it uses a standard certificate that is managed by the compute emulator.

## Configuring the Azure cloud service project

To configure settings that apply to an entire Azure cloud service project, you first open the shortcut menu for that project node, and then you choose **Properties** to open its property pages. The following table shows those property pages.

|Property Page|Description|
|---|---|
|Application|From this page, you can display information about the version of Azure Tools that this cloud service project uses, and you can upgrade to the current version of the tools.|
|Build Events|From this page, you can set pre-build and post-build events.|
|Development|From this page, you can specify build configuration instructions and the conditions under which any post-build events are run.|
|Web|From this page, you can configure settings that relate to the web server.|
<!-- keep by customization: end -->

## Next steps

<!-- deleted by customization
To learn more about how to configure Azure cloud service projects in Visual Studio, see [Configuring Your Azure project using multiple service configurations](/documentation/articles/vs-azure-tools-multiple-services-project-configurations).
-->
<!-- keep by customization: begin -->
To learn more about configuring Azure cloud service projects, see [Managing roles in the Azure cloud services projects with Visual Studio](/documentation/articles/vs-azure-tools-cloud-service-project-managing-roles).
<!-- keep by customization: end -->
