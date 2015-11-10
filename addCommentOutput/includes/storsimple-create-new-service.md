<!-- deleted by customization
<!--author=alkohli last changed: 9/17/15-->


#### To create a new service

1. Using your Microsoft account credentials, log on to the Management Portal at this URL: [http://azure.microsoft.com/](http://azure.microsoft.com/).
-->
<!-- keep by customization: begin -->
<properties 
   pageTitle="Create a new StorSimple Manager service"
   description="Describes how to create a new instance of the StorSimple Manager service."
   services="storsimple"
   documentationCenter="NA"
   authors="SharS"
   manager="adinah"
   editor="tysonn" />
<tags
	ms.service="storsimple"
	ms.date="04/01/2015"
	wacn.date=""/>


### To create a new service

1. Use your Microsoft account credentials to log on to the Windows Azure Management Portal here: [Azure Management Portal](https://manage.windowsazure.cn/).
<!-- keep by customization: end -->

2. In the Management Portal, click **New** > **Data Services** > **StorSimple Manager** > **Quick Create**.

3. In the form that is displayed, do the following:
  1. Supply a unique **Name** for your service. This is a friendly name that can be used to identify the service. The name can have between 2 and 50 characters that can be letters, numbers, and hyphens. The name must start and end with a letter or a number.
<!-- deleted by customization
  2. Supply a **Location** for your service. In general, choose a Location closest to the geographical region where you want to deploy your device. You may also want to factor in the following: 
	 
		- If you have existing workloads in Azure that you also intend to deploy with your StorSimple device, you should use that datacenter.
		- Your StorSimple Manager service and Azure storage can be in two separate locations. In such a case, you are required to create the StorSimple Manager and Azure storage account separately. To create an Azure storage account, go to the Azure Storage service in the Management Portal and follow the steps in [Create an Azure Storage account](/documentation/articles/storage-create-storage-account#create-a-storage-account). After you create this account, add it to the StorSimple Manager service by following the steps in [Configure a new storage account for the service](/documentation/articles/storsimple-deployment-walkthrough#configure-a-new-storage-account-for-the-service).
		 
-->
<!-- keep by customization: begin -->
  2. Supply a **Location** for your service. Location refers to the geographical region where you want to deploy your device.
<!-- keep by customization: end -->
  3. Choose a **Subscription** from the drop-down list. The subscription is linked to your billing account. This field is not present if you have only one subscription.
  4. Select **Create a new storage account** to automatically create a storage account with the service. This storage account will have a special name such as "storsimplebwv8c6dcnf." <!-- deleted by customization If you need your data in a different location, uncheck this box. -->
  5. Click **Create StorSimple Manager** to create the service.

<!-- deleted by customization
   ![Create StorSimple Manager](./media/storsimple-create-new-service/HCS_CreateAService-include.png)
-->
<!-- keep by customization: begin -->
       ![create a service](./media/storsimple-create-new-service/HCS_CreateAService-include.png)
<!-- keep by customization: end -->

  You will be directed to the **Service** landing page. The service creation will take a few minutes. After the service is successfully created, you will be notified appropriately and the status of the service will change to **Active**.
 
<!-- deleted by customization
   ![Service creation](./media/storsimple-create-new-service/HCS_StorSimpleManagerServicePage-include.png)

![Video available](./media/storsimple-create-new-service/Video_icon.png) **Video available**

To watch a video that demonstrates how to create a new StorSimple Manager service, click [here](http://azure.microsoft.com/documentation/videos/create-a-storsimple-manager-service/).
-->
<!-- keep by customization: begin -->
       ![service creation](./media/storsimple-create-new-service/HCS_StorSimpleManagerServicePage-include.png)

<!-- keep by customization: end -->