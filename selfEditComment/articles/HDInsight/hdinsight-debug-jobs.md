<properties
	pageTitle="Debug Hadoop in HDInsight: View logs and interpret error messages | Windows Azure"
	description="Learn about the error messages you might receive when administering HDInsight using PowerShell, and steps you can take to recover."
	services="hdinsight"
	tags="azure-portal"
	editor="cgronlun"
	manager="paulettm"
	authors="mumian"
	documentationCenter=""/>

<tags
	ms.service="hdinsight"
	ms.date="09/22/2015"
	wacn.date=""/>

# Debug Hadoop in HDInsight: View logs and interpret error messages

The error messages itemized in this topic are provided to help the users of Hadoop in Azure HDInsight understand possible error conditions that they can encounter when administering the service using Azure PowerShell and to advise them on the steps which can be taken to recover from the error.
<!-- deleted by customization

Some of these error messages could also be seen in the Azure preview portal when it is used to manage HDInsight clusters. But other error messages you might encounter there are less granular due to the constraints on the remedial actions possible in this context. Other error messages are provided in the contexts where the mitigation is obvious. If the constraints on parameters are violated, for example, the message pops-up in on the right side of the box where the value was entered. Here is a case where too many data nodes have been requested. The remedy is to reduce the number to an allowed value that is 33 or less.

![HDInsight preview portal error message][image-hdi-debugging-error-messages-portal]

In situations where the error is specific to Azure HDInsight, it might be a good idea to understand what the error is about. Refer to [HDInsight error codes](#hdi-error-codes) to understand the different error codes, and how to fix those. In some situations, you might want to access the Hadoop logs itself. You can do so directly from the Azure preview portal.

## View cluster health and job logs

* **Access the Hadoop UI**. From the Azure preview portal, click an HDInsight cluster name to open the cluster blade. From the cluster blade, click **Dashboard**.

	![Launch cluster dashboard](./media/hdinsight-debug-jobs/hdi-debug-launch-dashboard.png)
  
	When prompted, enter the cluster administrator credentials. In the Query Console that opens, click **Hadoop UI**.

	![Start Hadoop UI](./media/hdinsight-debug-jobs/hdi-debug-launch-dashboard-hadoop-ui.png)

* **Access the Yarn UI**. From the Azure preview portal, click an HDInsight cluster name to open the cluster blade. From the cluster blade, click **Dashboard**. When prompted, enter the cluster administrator credentials. In the Query Console that opens, click **YARN UI**.

	You can use the YARN UI to do the following:

	* **Get cluster status**. From the left pane, expand **Cluster**, and click **About**. This present cluster status details like total allocated memory, cores used, state of the cluster resource manager, cluster version etc.

		![Launch cluster dashboard](./media/hdinsight-debug-jobs/hdi-debug-yarn-cluster-state.png)

	* **Get node status**. From the left pane, expand **Cluster**, and click **Nodes**. This lists all the nodes in the cluster, HTTP address of each node, resources allocated to each node, etc.

	* **Monitor job status**. From the left pane, expand **Cluster**, and then click **Applications** to list all the jobs in the cluster. If you want to look at jobs in a specific state (such as new, submitted, running, etc.), click the appropriate link under **Applications**. You can further click the job name to find out more about the job such including the output, logs, etc.

* **Access the HBase UI**. From the Azure preview portal, click an HDInsight HBase cluster name to open the cluster blade. From the cluster blade, click **Dashboard**. When prompted, enter the cluster administrator credentials. In the Query Console that opens, click **HBase UI**
-->

## <a id="hdi-error-codes"></a>HDInsight error codes

The errors a user can encounter in Azure PowerShell or in the <!-- deleted by customization preview portal --><!-- keep by customization: begin --> Management Portal <!-- keep by customization: end --> are listed alphabetically by name below. The errors are in turn linked to an entry in the [Discription and Mitigation of Errors](#discription-mitigation-errors) section that provide the following information for the error:

- **Description**: the error message users see
- **Mitigation**: what steps can be taken to recover from the error.



- [AtleastOneSqlMetastoreMustBeProvided](#AtleastOneSqlMetastoreMustBeProvided)
- [AzureRegionNotSupported](#AzureRegionNotSupported)
- [ClusterContainerRecordNotFound](#ClusterContainerRecordNotFound)
- [ClusterDnsNameInvalidReservedWord](#ClusterDnsNameInvalidReservedWord)
- [ClusterNameUnavailable](#ClusterNameUnavailable)
- [ClusterUserNameInvalid](#ClusterUserNameInvalid)
- [ClusterUserNameInvalidReservedWord](#ClusterUserNameInvalidReservedWord)
- [ContainerNameMisMatchWithDnsName](#ContainerNameMisMatchWithDnsName)
- [DataNodeDefinitionNotFound](#DataNodeDefinitionNotFound)
- [DeploymentDeletionFailure](#DeploymentDeletionFailure)
- [DnsMappingNotFound](#DnsMappingNotFound)
- [DuplicateClusterContainerRequest](#DuplicateClusterContainerRequest)
- [DuplicateClusterInHostedService](#DuplicateClusterInHostedService)
- [FailureToUpdateDeploymentStatus](#FailureToUpdateDeploymentStatus)
- [HdiRestoreClusterAltered](#HdiRestoreClusterAltered)
- [HeadNodeConfigNotFound](#HeadNodeConfigNotFound)
- [HeadNodeConfigNotFound](#HeadNodeConfigNotFound)
- [HostedServiceCreationFailure](#HostedServiceCreationFailure)
- [HostedServiceHasProductionDeployment](#HostedServiceHasProductionDeployment)
- [HostedServiceNotFound](#HostedServiceNotFound)
- [HostedServiceWithNoDeployment](#HostedServiceWithNoDeployment)
- [InsufficientResourcesCores](#InsufficientResourcesCores)
- [InsufficientResourcesHostedServices](#InsufficientResourcesHostedServices)
- [InternalErrorRetryRequest](#InternalErrorRetryRequest)
- [InvalidAzureStorageLocation](#InvalidAzureStorageLocation)
- [InvalidNodeSizeForDataNode](#InvalidNodeSizeForDataNode)
- [InvalidNodeSizeForHeadNode](#InvalidNodeSizeForHeadNode)
- [InvalidRightsForDeploymentDeletion](#InvalidRightsForDeploymentDeletion)
- [InvalidStorageAccountBlobContainerName](#InvalidStorageAccountBlobContainerName)
- [InvalidStorageAccountConfigurationSecretKey](#InvalidStorageAccountConfigurationSecretKey)
- [InvalidVersionHeaderFormat](#InvalidVersionHeaderFormat)
- [MoreThanOneHeadNode](#MoreThanOneHeadNode)
- [OperationTimedOutRetryRequest](#OperationTimedOutRetryRequest)
- [ParameterNullOrEmpty](#ParameterNullOrEmpty)
- [PreClusterCreationValidationFailure](#PreClusterCreationValidationFailure)
- [RegionCapabilityNotAvailable](#RegionCapabilityNotAvailable)
- [StorageAccountNotColocated](#StorageAccountNotColocated)
- [SubscriptionIdNotActive](#SubscriptionIdNotActive)
- [SubscriptionIdNotFound](#SubscriptionIdNotFound)
- [UnableToResolveDNS](#UnableToResolveDNS)
- [UnableToVerifyLocationOfResource](#UnableToVerifyLocationOfResource)
- [VersionCapabilityNotAvailable](#VersionCapabilityNotAvailable)
- [VersionNotSupported](#VersionNotSupported)
- [VersionNotSupportedInRegion](#VersionNotSupportedInRegion)
- [WasbAccountConfigNotFound](#WasbAccountConfigNotFound)



## <a id="discription-mitigation-errors"></a>Diagnosis and Mitigation of Errors


### <a id="AtleastOneSqlMetastoreMustBeProvided"></a>AtleastOneSqlMetastoreMustBeProvided
- **Description**: Please provide Azure SQL database details for at least one component in order to use custom settings for Hive and Oozie metastores.
- **Mitigation**: The user needs to supply a valid SQL Azure metastore and retry the request.  

### <a id="AzureRegionNotSupported"></a>AzureRegionNotSupported
- **Description**: Could not create cluster in region *nameOfYourRegion*. Use a valid HDInsight region and retry request.
- **Mitigation**: Customer should create the cluster region that currently supports them: <!-- deleted by customization Southeast Asia, West Europe, --> China North, China East<!-- deleted by customization , or China North -->.  

### <a id="ClusterContainerRecordNotFound"></a>ClusterContainerRecordNotFound
- **Description**: The server could not find the requested cluster record.  
- **Mitigation**: Retry the operation.

### <a id="ClusterDnsNameInvalidReservedWord"></a>ClusterDnsNameInvalidReservedWord
- **Description**: Cluster DNS name *yourDnsName* is invalid. Please ensure name starts and ends with alphanumeric and can only contain '-' special character  
- **Mitigation**: Make sure that you have used a valid DNS name for your cluster that starts and ends with alphanumeric and contains no special characters other than the dash '-' and then retry the operation.

### <a id="ClusterNameUnavailable"></a>ClusterNameUnavailable
- **Description**: Cluster name *yourClusterName* is unavailable. Please pick another name.  
- **Mitigation**: The user should specify a clustername that is unique and does not exist and retry. If the user is using the preview portal, the UI will notify them if a cluster name is already being used during the create steps.


### <a id="ClusterPasswordInvalid"></a>ClusterPasswordInvalid
- **Description**: Cluster password is invalid. Password must be at least 10 characters long and must contain at least one number, uppercase letter, lowercase letter and special character with no spaces and should not contain the username as part of it.  
- **Mitigation**: Provide a valid cluster password and retry the operation.

### <a id="ClusterUserNameInvalid"></a>ClusterUserNameInvalid
- **Description**: Cluster username is invalid. Please ensure username doesn't contain special characters or spaces.  
- **Mitigation**: Provide a valid cluster username and retry the operation.

### <a id="ClusterUserNameInvalidReservedWord"></a>ClusterUserNameInvalidReservedWord
- **Description**: Cluster DNS name *yourDnsClusterName* is invalid. Please ensure name starts and ends with alphanumeric and can only contain '-' special character  
- **Mitigation**: Provide a valid DNS cluster username and retry the operation.

### <a id="ContainerNameMisMatchWithDnsName"></a>ContainerNameMisMatchWithDnsName
- **Description**: Container name in URI *yourcontainerURI* and DNS name *yourDnsName* in request body must be the same.  
- **Mitigation**: Make sure that your container Name and your DNS name are the same and retry the operation.

### <a id="DataNodeDefinitionNotFound"></a>DataNodeDefinitionNotFound
- **Description**: Invalid cluster configuration. Unable to find any data node definitions in node size.  
- **Mitigation**: Retry the operation.

### <a id="DeploymentDeletionFailure"></a>DeploymentDeletionFailure
- **Description**: Deletion of deployment failed for the Cluster  
- **Mitigation**: Retry the delete operation.

### <a id="DnsMappingNotFound"></a>DnsMappingNotFound
- **Description**: Service configuration error. Required DNS mapping information not found.  
- **Mitigation**: Delete cluster and create a new cluster.

### <a id="DuplicateClusterContainerRequest"></a>DuplicateClusterContainerRequest
- **Description**: Duplicate cluster container creation attempt. Record exists for *nameOfYourContainer* but Etags do not match.
- **Mitigation**: Provide a unique name for the container and retry the create operation.

### <a id="DuplicateClusterInHostedService"></a>DuplicateClusterInHostedService
- **Description**: Hosted service *nameOfYourHostedService* already contains a cluster. A hosted service cannot contain multiple clusters  
- **Mitigation**: Host the cluster in another hosted service.

### <a id="FailureToUpdateDeploymentStatus"></a>FailureToUpdateDeploymentStatus
- **Description**: The server could not update the state of the cluster deployment.  
- **Mitigation**: Retry the operation. If this happens multiple times, contact CSS.

### <a id="HdiRestoreClusterAltered"></a>HdiRestoreClusterAltered
- **Description**: Cluster *yourClusterName* was deleted as part of maintenance. Please recreate the cluster.
- **Mitigation**: Recreate the cluster.

### <a id="HeadNodeConfigNotFound"></a>HeadNodeConfigNotFound
- **Description**: Invalid cluster configuration. Required head node configuration not found in node sizes.
- **Mitigation**: Retry the operation.

### <a id="HostedServiceCreationFailure"></a>HostedServiceCreationFailure
- **Description**: Unable to create hosted service *nameOfYourHostedService*. Please retry request.  
- **Mitigation**: Retry the request.

### <a id="HostedServiceHasProductionDeployment"></a>HostedServiceHasProductionDeployment
- **Description**: Hosted Service *nameOfYourHostedService* already has a production deployment. A hosted service cannot contain multiple production deployments. Retry the request with a different cluster name.
- **Mitigation**: Use a different cluster name and retry the request.

### <a id="HostedServiceNotFound"></a>HostedServiceNotFound
- **Description**: Hosted Service *nameOfYourHostedService* for the cluster could not be found.  
- **Mitigation**: If the cluster is in error state, delete it and then try again.

### <a id="HostedServiceWithNoDeployment"></a>HostedServiceWithNoDeployment
- **Description**: Hosted Service *nameOfYourHostedService* has no associated deployment.  
- **Mitigation**: If the cluster is in error state, delete it and then try again.

### <a id="InsufficientResourcesCores"></a>InsufficientResourcesCores
- **Description**: The SubscriptionId *yourSubscriptionId* does not have cores left to create cluster *yourClusterName*. Required: *resourcesRequired*, Available: *resourcesAvailable*.  
- **Mitigation**: Free up resources in your subscription or increase the resources available to the subscription and try to create the cluster again.

### <a id="InsufficientResourcesHostedServices"></a>InsufficientResourcesHostedServices
- **Description**: Subscription ID *yourSubscriptionId* does not have quota for a new HostedService to create cluster *yourClusterName*.  
- **Mitigation**: Free up resources in your subscription or increase the resources available to the subscription and try to create the cluster again.

### <a id="InternalErrorRetryRequest"></a>InternalErrorRetryRequest
- **Description**: The server encountered an internal error. Please retry request.  
- **Mitigation**: Retry the request.

### <a id="InvalidAzureStorageLocation"></a>InvalidAzureStorageLocation
- **Description**: Azure Storage location *dataRegionName* is not a valid location. Make sure the region is correct and retry request.
- **Mitigation**: Select a Storage location that supports HDInsight, check that your cluster is co-located and retry the operation.

### <a id="InvalidNodeSizeForDataNode"></a>InvalidNodeSizeForDataNode
- **Description**: Invalid VM size for data nodes. Only 'Large VM' size is supported for all data nodes.  
- **Mitigation**: Specify the supported node size for the data node and retry the operation.

### <a id="InvalidNodeSizeForHeadNode"></a>InvalidNodeSizeForHeadNode
- **Description**: Invalid VM size for head node. Only 'ExtraLarge VM' size is supported for head node.  
- **Mitigation**: Specify the supported node size for the head node and retry the operation

### <a id="InvalidRightsForDeploymentDeletion"></a>InvalidRightsForDeploymentDeletion
- **Description**: Subscription ID *yourSubscriptionId* being used does not have sufficient permissions to execute delete operation for cluster *yourClusterName*.  
- **Mitigation**: If the cluster is in error state, drop it and then try again.  

### <a id="InvalidStorageAccountBlobContainerName"></a>InvalidStorageAccountBlobContainerName
- **Description**: External storage account blob container name *yourContainerName* is invalid. Make sure name starts with a letter and contains only lowercase letters, numbers and dash.  
- **Mitigation**: Specify a valid storage account blob container name and retry the operation.

### <a id="InvalidStorageAccountConfigurationSecretKey"></a>InvalidStorageAccountConfigurationSecretKey
- **Description**: Configuration for external storage account *yourStorageAccountName* is required to have secret key details to be set.  
- **Mitigation**: Specify a valid secret key for the storage account and retry the operation.

### <a id="InvalidVersionHeaderFormat"></a>InvalidVersionHeaderFormat
- **Description**: Version header *yourVersionHeader* is not in valid format of yyyy-mm-dd.  
- **Mitigation**: Specify a valid format for the version-header and retry the request.

### <a id="MoreThanOneHeadNode"></a>MoreThanOneHeadNode
- **Description**: Invalid cluster configuration. Found more than one head node configuration.  
- **Mitigation**: Edit the configuration so that onloy one head node is specified.

### <a id="OperationTimedOutRetryRequest"></a>OperationTimedOutRetryRequest
- **Description**: The operation could not be completed within the permitted time or the maximum retry attempts possible. Please retry request.  
- **Mitigation**: Retry the request.

### <a id="ParameterNullOrEmpty"></a>ParameterNullOrEmpty
- **Description**: Parameter *yourParameterName* cannot be null or empty.  
- **Mitigation**: Specify a valid value for the parameter.

### <a id="PreClusterCreationValidationFailure"></a>PreClusterCreationValidationFailure
- **Description**: One or more of the cluster creation request inputs is not valid. Make sure the input values are correct and retry request.  
- **Mitigation**: Make sure the input values are correct and retry request.

### <a id="RegionCapabilityNotAvailable"></a>RegionCapabilityNotAvailable
- **Description**: Region capability not available for region *yourRegionName* and Subscription ID *yourSubscriptionId*.  
- **Mitigation**: Specify a region that supports HDInsight clusters. The publicly supported regions are: <!-- deleted by customization Southeast Asia, West Europe, --> China North, China East<!-- deleted by customization , or China North -->.

### <a id="StorageAccountNotColocated"></a>StorageAccountNotColocated
- **Description**: Storage account *yourStorageAccountName* is in region *currentRegionName*. It should be same as the cluster region *yourClusterRegionName*.  
- **Mitigation**: Either specify a storage account in the same region that your cluster is in or if your data is already in the storage account, create a new cluster in the same region as the existing storage account. <!-- deleted by customization If you are using the preview portal, the UI will notify them of this issue in advance. -->

### <a id="SubscriptionIdNotActive"></a>SubscriptionIdNotActive
- **Description**: Given Subscription ID *yourSubscriptionId* is not active.  
- **Mitigation**: Re-activate your subscription or get a new valid subscription.

### <a id="SubscriptionIdNotFound"></a>SubscriptionIdNotFound
- **Description**: Subscription ID *yourSubscriptionId* could not be found.  
- **Mitigation**: Check that your subscription ID is valid and retry the operation.

### <a id="UnableToResolveDNS"></a>UnableToResolveDNS
- **Description**: Unable to resolve DNS *yourDnsUrl*. Please ensure the fully qualified URL for the blob endpoint is provided.  
- **Mitigation**: Supply a valid blob URL. The URL MUST be fully valid, including starting with *http://* and ending in *.com*.

### <a id="UnableToVerifyLocationOfResource"></a>UnableToVerifyLocationOfResource
- **Description**: Unable to verify location of resource *yourDnsUrl*. Please ensure the fully qualified URL for the blob endpoint is provided.  
- **Mitigation**: Supply a valid blob URL. The URL MUST be fully valid, including starting with *http://* and ending in *.com*.

### <a id="VersionCapabilityNotAvailable"></a>VersionCapabilityNotAvailable
- **Description**: Version capability not available for version *specifiedVersion* and Subscription ID *yourSubscriptionId*.  
- **Mitigation**: Choose a version that is available and retry the operation.

### <a id="VersionNotSupported"></a>VersionNotSupported
- **Description**: Version *specifiedVersion* not supported.
- **Mitigation**: Choose a version that is supported and retry the operation.

### <a id="VersionNotSupportedInRegion"></a>VersionNotSupportedInRegion
- **Description**: Version *specifiedVersion* is not available in Azure region *specifiedRegion*.  
- **Mitigation**: Choose a version that is supported in the region specified and retry the operation.

### <a id="WasbAccountConfigNotFound"></a>WasbAccountConfigNotFound
- **Description**: Invalid cluster configuration. Required WASB account configuration not found in external accounts.  
- **Mitigation**: Verify that the account exists and is properly specified in configuration and retry the operation.

## <a id="resources"></a>Additional Debugging Resources

* [Azure HDInsight SDK documentation][hdinsight-sdk-documentation]

[hdinsight-sdk-documentation]: http://msdnstage.redmond.corp.microsoft.com/zh-cn/library/dn479185.aspx

[image-hdi-debugging-error-messages-portal]: ./media/hdinsight-debug-jobs/hdi-debug-errormessages-portal.png
