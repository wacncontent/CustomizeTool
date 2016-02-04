<properties
   pageTitle="Deploy a custom application to Azure Service Fabric | Windows Azure"
   description="Walkthrough on how to package an existing application so it can be deployed on an Azure Service Fabric cluster"
   services="service-fabric"
   documentationCenter=".net"
   authors="bmscholl"
   manager="timlt"
   editor=""/>

<tags
	ms.service="service-fabric"
	ms.date="11/17/2015"
	wacn.date=""/>

# Deploy a custom application to Service Fabric

<!You can run any type of existing application, such as Node.js, Java, or native applications in Azure Service Fabric. Service Fabric treats those applications like stateless services and places them on nodes in a cluster, based on availability and other metrics. This article describes how to package and deploy an existing application to a Service Fabric cluster.

## Benefits of running a custom application in Service Fabric
Azure Service Fabric can be used to deploy existing applications. Applications that currently runs on, for instance, an Azure Web or Worker role, can be 'packaged' so that they can be deployed on an Service Fabric cluster. 
Existing applications running on a Service Fabric cluster can benefit from features such as health monitoring and ALM (Application Lifecycle Management) so it is an important scenario that is fully supported.
This tutorial explains the process and basic concepts that are involved with taking an existing application and package it .
This article that is an overview of the process, we will follow up with specific examples on how to take an existing applications (for instance a node.js or Java) app and package it so it can be hosted on a Service Fabric cluster.

There are several advantages that come with running an application in a Service Fabric cluster:

- High availability. Applications that are run in Service Fabric are highly available out of the box. Service Fabric makes sure that one instance of an application is always up and running.
- Health monitoring. Out of the box, Service Fabric health monitoring detects if an application is up and running and provides diagnostics information in case of failure.   
- Application lifecycle management. Besides providing upgrades with no downtime, Service Fabric also allows you to roll back to the previous version if there is an issue during an upgrade.    
- Density. You can run multiple applications in a cluster, which eliminates the need for each application to run on its own hardware.

In this article, we cover the basic steps to package an existing application and deploy it to Service Fabric.  


## Quick overview of application and service manifest files

Before we can start and learn how to package an existing application, we need to go through an brief introduction of the Service Fabric's deployment model.
Service Fabric deployment model relies mainly on two files:


* Application Manifest. The application manifest is used to describe the application and lists the services that compose it plus other parameters,  such as the number of instances, that are used to define how the service(s) should be deployed.In the Service Fabric world,  an application is the 'upgradable unit'. An application can be upgraded as a single unit where potential failures (and potential rollbacks) are managed by the platform to guarantee that the upgrade process either completely success or, if it fails, it does not leave the application is an unknown/unstable state.

<?xml version="1.0" encoding="utf-8"?>
<!<ServiceManifest xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" Name="NodeApp" Version="1.0.0.0" xmlns="http://schemas.microsoft.com/2011/01/fabric">
	<ApplicationManifest ApplicationTypeName="actor2Application" ApplicationTypeVersion="1.0.0.0" xmlns="http://schemas.microsoft.com/2011/01/fabric" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	  <ServiceManifestImport>
	  <DefaultServices>
	</ApplicationManifest>

* Service Manifest. Service Manifest describes the components of a service. It includes data such as name and type of the service (information that Service Fabric uses to manage the service), its code, configuration and data components plus some additional parameters that can be used to configure the service once it is deployed. We are not going into the details of all the different parameters available in the service manifest, we will go through the subset that is required to make an existing application to run on Service Fabric
	<?xml version="1.0" encoding="utf-8"?>
   <ServiceTypes>
      <StatelessServiceType ServiceTypeName="NodeApp" UseImplicitHost="true"/>
   </ServiceTypes>
   <CodePackage Name="code" Version="1.0.0.0">
      <SetupEntryPoint>
         <ExeHost>
             <Program>scripts\launchConfig.cmd</Program>
         </ExeHost>
      </SetupEntryPoint>
      <EntryPoint>
         <ExeHost>
            <Program>node.exe</Program>
            <Arguments>bin/www</Arguments>
            <WorkingFolder>CodePackage</WorkingFolder>
         </ExeHost>
      </EntryPoint>
   </CodePackage>
   <Resources>
      <Endpoints>
         <Endpoint Name="NodeAppTypeEndpoint" Protocol="http" Port="3000" Type="Input" />
      </Endpoints>
   </Resources>
			\code
			\config
			\data
* code: contains the service code
* config: contains a settings.xml file (and other files if necessary) that the service can access at runtime to retrieve specific configuration settings.
* Data: an additional directory to store additional local data that service may need. Note: Data should be used to store only ephymeral data, Service Fabric does not copy/replicate changes to the data directory if the service needs to be relocated, for instance, during failover.

Note: You can use any arbitrary directory name for Code, Config and Data. You should need to make sure to use the same value in the ApplicationManifest file.

## the process of packaging an existing app
* Create the package directory structure
* Add application's code and configuration files
* update the service manifest file
* update the application manifest
* The name of the service type. This is an 'Id' that Service Fabric uses in order to identify a service
* The command to use to launch the application (ExeHost)
* Any script that needs to be run in order to setup/configure the application (SetupEntrypoint
	<?xml version="1.0" encoding="utf-8"?>
	  <CodePackage Name="Code" Version="1.0.0.0">
	  <ConfigPackage Name="Config" Version="1.0.0.0"/>
	  <Resources>
	</ServiceManifest>


Let's go over the different part of the file that you need to update:

### ServiceTypes:

```
<ServiceTypes>
  <StatelessServiceType ServiceTypeName="NodeApp" UseImplicitHost="true" />
</ServiceTypes>
```

* You can pick any name that you want for `ServiceTypeName`. The value is used in the `ApplicationManifest.xml` file to identify the service.
- You need to specify `UseImplicitHost="true"`. This attribute tells Service Fabric that the service is based on a self-contained app, so all Service Fabric needs to do is to launch it as a process and monitor its health.

### CodePackage
The CodePackage element specifies the location (and version) of the service's code.

<CodePackage Name="Code" Version="1.0.0.0">


The `Name` element is used to specify the name of the directory in the Application Package that contains the service's code. `CodePackage` also has the `version` attribute that can be used to specify the version of the code and, potentially, be used to upgrade the service's code by leveraging Service Fabric's Application LifeCycle Management infrastructure.


### Entrypoint


	<EntryPoint>
	  <ExeHost>
	    <Program>node.exe</Program>
	    <Arguments>server.js</Arguments>
	    <WorkingFolder>CodeBase</WorkingFolder>
	  </ExeHost>
	</EntryPoint>


The `Entrypoint` element in the service manifest file is used to specify how to launch the service. The `ExeHost` element specifies the executable (and arguments) that should be used to launch the service. 

* `Program`:specifies the name of the executable that should be executed in order to start the service. 
* `Arguments`: it specifies the arguments that should be passed to the executable. it can be a list of parameters with arguments.
* `WorkingFolder`: it specifies the working directory for the process that is going to be started. You can specify two values:
	* `CodeBase`: the working directory is going to be set to the Code directory in the application package (`Code` directory in the structure shown below)
	* `CodePackage`: the working directory will be set to the root of the application package	(`MyServicePkg`)
`WorkingDirectory` element is useful to set the correct working directory so relative paths can be used by either the application or initialization scripts.
There is also another value that you can specify for the `WorkingFolder` element (`Work`) but it is not very useful for the scenario of bringing an existing application.


```

The `Name` element is used to specify the name of the directory in the application package that contains the service's code. `CodePackage` also has the `version` attribute. This can be used to specify the version of the code--and can also potentially be used to upgrade the service's code by using Service Fabric's application lifecycle management infrastructure.
### SetupEntrypoint

```xml
<SetupEntryPoint>
   <ExeHost>
       <Program>scripts\launchConfig.cmd</Program>
   </ExeHost>
</SetupEntryPoint>
```
The SetupEntrypoint element is used to specify any executable or batch file that should be executed before the service's code is launched. It is an optional element, so it does not need to be included if there is no initialization/setup required. The SetupEntryPoint is executed every time the service is restarted.

<!There is only one SetupEntrypoint, so setup/config scripts need to be bundled in a single batch file if the application's setup/config requires multiple scripts. Like the Entrypoint element, SetupEntrypoint can execute any type of file--executable files, batch files, and PowerShell cmdlets. In the example above, the SetupEntrypoint is based on a batch file LaunchConfig.cmd that is located in the `scripts` subdirectory of the code directory (assuming the WorkingDirectory element is set to code).

### Entrypoint

```xml
<EntryPoint>
  <ExeHost>
    <Program>node.exe</Program>
    <Arguments>bin/www</Arguments>
    <WorkingFolder>CodeBase</WorkingFolder>
  </ExeHost>
</EntryPoint>
```

The `Entrypoint` element in the service manifest file is used to specify how to launch the service. The `ExeHost` element specifies the executable (and arguments) that should be used to launch the service.

- `Program` specifies the name of the executable that should be executed in order to start the service.
- `Arguments` specifies the arguments that should be passed to the executable. It can be a list of parameters with arguments.
- `WorkingFolder` specifies the working directory for the process that is going to be started. You can specify two values:
	- `CodeBase` specifies that the working directory is going to be set to the code directory in the application package (`Code` directory in the structure shown below).
	- `CodePackage` specifies that the working directory is going to be set to the root of the application package	(`MyServicePkg`).
- `WorkingDirectory` is useful to set the correct working directory so that relative paths can be used by either the application or initialization scripts.

### Endpoints

```xml
<Endpoints>
   <Endpoint Name="NodeAppTypeEndpoint" Protocol="http" Port="3000" Type="Input" />
</Endpoints>

	<SetupEntryPoint>


The `SetupEntrypoint` is used to specify any executable or batch file that should be executed before the service's code is launched. It is an optional element so it does not need to be included if there is no intialization/setup that is required. The Entrypoint is executed every time the service is restarted. There is only one SetupEntrypoint so setup/config scripts needs to be boundled on a single batch file if the application's setup/config requires multiple scripts. Like the `Entrypoint` element, `SetupEntrypoint` can execute any type of file: executable, batch fiules, powershell cmdlet.
## Edit the application manifest file

Once you have configured the `Servicemanifest.xml` file, you need to make some changes to the `ApplicationManifest.xml` file to ensure that the correct service type and name are used.

	<ServiceManifestImport>
  <ServiceManifestRef ServiceManifestName="NodeApp" ServiceManifestVersion="1.0.0.0" />
</ServiceManifestImport>
	<ServiceManifestImport>

### Set up logging
	<DefaultServices>
	* `InstanCount = "1"`: in this case only one instance of the service will be deployed on the cluster. Service Fabric's scheduler determines on which node the service is going to be deployed. A single instance count also makes sense for applications that require a different configuration if they run on multiple instances. In that case it is easier to define multiple services in the same application manifest file and use `InstanceCount = "1"`. So the end result will be to have multiple instances of the same service but each with a specific configuration. A value of `InstanceCount` greater than one makes sense only if the goal is to have multiple instance of the exact same configuration.
For existing applications, it is very useful to be able to see console logs to find out if the application and configuration scripts show any errors.
Console redirection can be configured in the `ServiceManifest.xml` file using the `ConsoleRedirection` element.

	<EntryPoint>
  <ExeHost>
    <Program>node.exe</Program>
    <Arguments>bin/www</Arguments>
    <WorkingFolder>CodeBase</WorkingFolder>
    <ConsoleRedirection FileRetentionCount="5" FileMaxSizeInKb="2048"/>
  </ExeHost>
</EntryPoint>

* `ConsoleRedirection` can be used to redirect console output (both stdout and stderr) to a working directory so they can be used to verify that there are no errors during the setup or execution of the application in the Service Fabric cluster.

	* `FileRetentionCount` determines how many files are saved in the working directory. A value of 5, for instance, means that the log files for the previous five executions are stored in the working directory.
	* `FileMaxSizeInKb` specifies the max size of the log files.

Log files are saved in one of the service's working directories. In order to determine where the files are located, you need to use Service Fabric Explorer to determine which node that the service is running on and which working directory is being used. This process is covered later in this article.

### Deployment
The last step is to deploy your application. The PowerShell script below shows how to deploy your application to the local development cluster and start a new Service Fabric service.

```PowerShell

Connect-ServiceFabricCluster localhost:19000

Write-Host 'Copying application package...'
Copy-ServiceFabricApplicationPackage -ApplicationPackagePath 'C:\Dev\MultipleApplications' -ImageStoreConnectionString 'file:C:\SfDevCluster\Data\ImageStoreShare' -ApplicationPackagePathInImageStore 'Store\nodeapp'

Write-Host 'Registering application type...'
Register-ServiceFabricApplicationType -ApplicationPathInImageStore 'Store\nodeapp'

New-ServiceFabricApplication -ApplicationName 'fabric:/nodeapp' -ApplicationTypeName 'NodeAppType' -ApplicationTypeVersion 1.0

New-ServiceFabricService -ApplicationName 'fabric:/nodeapp' -ServiceName 'fabric:/nodeapp/nodeappservice' -ServiceTypeName 'NodeApp' -Stateless -PartitionSchemeSingleton -InstanceCount 1

```
A Service Fabric service can be deployed in various "configurations." For instance, it can be deployed as single or multiple instances, or it can be deployed in such a way that there is one instance of the service on each node of the Service Fabric cluster.

The `InstanceCount` parameter of the `New-ServiceFabricService` cmdlet is used to specify how many instances of the service should be launched in the Service Fabric cluster. You can set the `InstanceCount` value, depending on the type of application that you are deploying. The two most common scenarios are:

* `InstanceCount = "1"`. In this case, only one instance of the service will be deployed in the cluster. Service Fabric's scheduler determines which node the service is going to be deployed on.

* `InstanceCount ="-1"`. In this case, one instance of the service will be deployed on every node in the Service Fabric cluster. The end result will be having one (and only one) instance of the service for each node in the cluster.

This is a useful configuration for front-end applications (for example, a REST endpoint) because client applications just need to
"connect" to any of the nodes in the cluster in order to use the endpoint. This configuration can also be used when, for instance, all nodes of the Service Fabric cluster are connected to a load balancer so client traffic can be distributed across the service that is running on all nodes in the cluster.

### Check your running application

In Service Fabric Explorer, identify the node where the service is running. In this example, it runs on Node1:

![Node where service is running](./media/service-fabric-deploy-existing-app/runningapplication.png)

If you navigate to the node and browse to the application, you will see the essential node information, including its location on disk.

![Location on disk](./media/service-fabric-deploy-existing-app/locationondisk.png)

If you browse to the directory by using Server Explorer, you can find the working directory and the service's log folder as shown below.

![Location of log](./media/service-fabric-deploy-existing-app/loglocation.png)


## Next steps
In this article, you have learned how to package an existing application and deploy it to Service Fabric. As a next step, you can check out additional content for this topic.

- [Sample for packaging and deploying a custom application on GitHub](https://github.com/Azure-Samples/service-fabric-dotnet-getting-started/tree/master/Custom/SimpleApplication), including a link to the prerelease of the packaging tool
- [Deploy multiple custom applications](/documentation/articles/service-fabric-deploy-multiple-apps)
- [Create your first Service Fabric application using Visual Studio](/documentation/articles/service-fabric-create-your-first-application-in-visual-studio)

<!--Image references-->
[1]: ./media/service-fabric-deploy-an-existing-app/directory-structure-1.PNG
[2]: ./media/service-fabric-deploy-an-existing-app/directory-structure-2.PNG
[3]: ./media/service-fabric-deploy-an-existing-app/service-node-1.PNG
[4]: ./media/service-fabric-deploy-an-existing-app/service-node-2.PNG
[5]: ./media/service-fabric-deploy-an-existing-app/service-node-3.PNG
[6]: ./media/service-fabric-deploy-an-existing-app/service-node-4.PNG

	


