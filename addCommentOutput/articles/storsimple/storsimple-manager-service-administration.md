<properties 
   pageTitle="StorSimple Manager service administration | Windows Azure"
   description="Learn how to manage your StorSimple device by using the StorSimple Manager service in the Azure Management Portal."
   services="storsimple"
   documentationCenter=""
   authors="alkohli"
   manager="carolz"
   editor="" />
<tags
	ms.service="storsimple"
	ms.date="09/11/2015"
	wacn.date=""/>

# Use the StorSimple Manager service to administer your StorSimple device

## Overview

This article describes the StorSimple Manager service interface, including how to connect to it, the various options available, and links out to the specific workflows that can be performed via this UI. This guidance is applicable to both; the StorSimple physical and the virtual device.

After reading this article, you will learn to:

- Connect to StorSimple Manager service
- Navigate the StorSimple Manager UI
- Administer your StorSimple device via the StorSimple Manager service


## Connect to StorSimple Manager service

The StorSimple Manager service runs in <!-- deleted by customization Windows --><!-- keep by customization: begin --> Microsoft <!-- keep by customization: end --> Azure and connects to multiple StorSimple devices. You use a central <!-- deleted by customization Windows --><!-- keep by customization: begin --> Microsoft <!-- keep by customization: end --> Azure Management Portal running in a browser to manage these devices. To connect to the StorSimple Manager service, do the following.

#### To connect to the service

1. Navigate to [http://azure.microsoft.com/](http://azure.microsoft.com/)

1. Using your Microsoft account credentials, log on to the <!-- deleted by customization Windows --><!-- keep by customization: begin --> Microsoft <!-- keep by customization: end --> Azure Management Portal (located at the top-right of the pane).

1. Scroll down the left navigation pane to access the StorSimple Manager service.


## Navigate StorSimple Manager service UI

The navigational hierarchy for the StorSimple Manager service UI is shown in the following table.

- **StorSimple Manager** landing page takes you to the UI service-level pages applicable to all devices within a service.

- **Devices** page takes you to the <!-- deleted by customization device-level --><!-- keep by customization: begin --> device–level <!-- keep by customization: end --> UI pages applicable to a specific device.

- **Volume Containers** page takes you to the volume page that shows all the volumes associated with a device.


#### StorSimple Manager service navigational hierarchy

|Landing page|Service-level pages|Device-level pages|Device-level pages|
|---|---|---|---|
|StorSimple Manager service|Service dashboard|Device dashboard||
||Devices →|Monitor|
||Backup catalog|Volume containers→|Volumes|
||Configure (Service)|Backup policies||
||Jobs|Configure (Device)|
||Alerts|Maintenance|

![Video available](./media/storsimple-manager-service-administration/Video_icon.png) **Video available**

To watch a video that walks you through the StorSimple Manager service user interface, click [here](http://azure.microsoft.com/documentation/videos/storsimple-manager-service-overview/).

## Administer StorSimple device using StorSimple Manager service

The following table shows a summary of all the common management tasks and complex workflows that can be performed within the StorSimple Manager service UI. These tasks are organized based on the UI pages on which they are initiated.

For more information about each workflow, click the appropriate procedure in the table.

#### StorSimple Manager workflows

|If you want to do this ...|Go to this UI page ...|Use this procedure.|
|---|---|---|
|Create a service</br>Delete a service</br>Get service registration key</br>Regenerate service registration key|StorSimple Manager service|[Deploy a StorSimple Manager <!-- deleted by customization service](/documentation/articles/storsimple-manage-service) --><!-- keep by customization: begin --> service](storsimple-manage-service.md) <!-- keep by customization: end -->
|Change the service data encryption key</br>View the operation logs|StorSimple Manager service → Dashboard|[Use the StorSimple Manager service <!-- deleted by customization dashboard](/documentation/articles/storsimple-service-dashboard)| --><!-- keep by customization: begin --> dashboard](storsimple-service-dashboard.md)| <!-- keep by customization: end -->
|Deactivate a device</br>Delete a device|StorSimple Manager service → Devices|[Deactivate or delete a <!-- deleted by customization device](/documentation/articles/storsimple-deactivate-and-delete-device)| --><!-- keep by customization: begin --> device](storsimple-deactivate-and-delete-device.md)| <!-- keep by customization: end -->
|Learn about disaster recovery and device failover</br>Failover to a physical device</br>Failover to a virtual device</br>Business continuity disaster recovery (BCDR)|StorSimple Manager service → Devices|[Failover and disaster recovery for your StorSimple <!-- deleted by customization device](/documentation/articles/storsimple-device-failover-disaster-recovery)| --><!-- keep by customization: begin --> device](storsimple-device-failover-disaster-recovery.md)| <!-- keep by customization: end -->
|List backups for a volume</br>Select a backup set</br>Delete a backup set|StorSimple Manager service → Backup Catalog|[Manage <!-- deleted by customization backups](/documentation/articles/storsimple-manage-backup-catalog)| --><!-- keep by customization: begin --> backups](storsimple-manage-backup-catalog.md)| <!-- keep by customization: end -->
|Clone a volume|StorSimple Manager service → Backup Catalog|[Clone a <!-- deleted by customization volume](/documentation/articles/storsimple-clone-volume)| --><!-- keep by customization: begin --> volume](storsimple-clone-volume.md)| <!-- keep by customization: end -->
|Restore a backup set|StorSimple Manager service → Backup Catalog|[Restore a backup <!-- deleted by customization set](/documentation/articles/storsimple-restore-from-backup-set)| --><!-- keep by customization: begin --> set](storsimple-restore-from-backup-set.md)| <!-- keep by customization: end -->
|About  storage accounts</br>Add a storage account</br>Edit a storage account</br>Delete a storage account</br>Key rotation of storage accounts|StorSimple Manager service → Configure|[Manage storage <!-- deleted by customization accounts](/documentation/articles/storsimple-manage-storage-accounts)| --><!-- keep by customization: begin --> accounts](storsimple-manage-storage-accounts.md)| <!-- keep by customization: end -->
|About bandwidth templates</br>Add a bandwidth template</br>Edit a bandwidth template</br>Delete a bandwidth template</br>Use a default bandwidth template</br>Create an all-day bandwidth template that starts at a specified time|StorSimple Manager service → Configure|[Manage bandwidth <!-- deleted by customization templates](/documentation/articles/storsimple-manage-bandwidth-templates)| --><!-- keep by customization: begin --> templates](storsimple-manage-bandwidth-templates.md)| <!-- keep by customization: end -->
|About access control records</br>Create an access control record</br>Edit an access control record</br>Delete an access control record|StorSimple Manager service → Configure|[Manage access control <!-- deleted by customization records](/documentation/articles/storsimple-manage-acrs)| --><!-- keep by customization: begin --> records](storsimple-manage-acrs.md)| <!-- keep by customization: end -->
|View job details</br>Cancel a job|StorSimple Manager service → Jobs|[Manage <!-- deleted by customization jobs](/documentation/articles/storsimple-manage-jobs) --><!-- keep by customization: begin --> jobs](storsimple-manage-jobs.md) <!-- keep by customization: end -->
|Receive alert notifications</br>Manage alerts</br>Review alerts|StorSimple Manager service → Alerts|[View and manage StorSimple <!-- deleted by customization alerts](/documentation/articles/storsimple-manage-alerts) --><!-- keep by customization: begin --> alerts](storsimple-manage-alerts.md) <!-- keep by customization: end -->
|View connected initiators</br>Find the device serial number</br>Find the target IQN|StorSimple Manager service → Devices → Dashboard|[Use the StorSimple device <!-- deleted by customization dashboard](/documentation/articles/storsimple-device-dashboard)| --><!-- keep by customization: begin --> dashboard](storsimple-device-dashboard.md)| <!-- keep by customization: end -->
|Create monitoring charts|StorSimple Manager service → Devices → Monitor|[Monitor your StorSimple <!-- deleted by customization device](/documentation/articles/storsimple-monitor-device)| --><!-- keep by customization: begin --> device](storsimple-monitor-device.md)| <!-- keep by customization: end -->
|Add a volume container</br>Modify a volume container</br>Delete a volume container|StorSimple Manager service → Devices → Volume Containers|[Manage volume <!-- deleted by customization containers](/documentation/articles/storsimple-manage-volume-containers)| --><!-- keep by customization: begin --> containers](storsimple-manage-volume-containers.md)| <!-- keep by customization: end -->
|Add a volume</br>Modify a volume</br>Take a volume offline</br>Delete a volume</br>Monitor a volume|StorSimple Manager service → Devices → Volume Containers → Volumes|[Manage <!-- deleted by customization volumes](/documentation/articles/storsimple-manage-volumes)| --><!-- keep by customization: begin --> volumes](storsimple-manage-volumes.md)| <!-- keep by customization: end -->
|Modify device settings</br>Modify time settings</br>Modify DNS.md settings</br>Configure network interfaces|StorSimple Manager service → Devices → Configure|[Modify device configuration for your StorSimple <!-- deleted by customization device](/documentation/articles/storsimple-modify-device-config)| --><!-- keep by customization: begin --> device](storsimple-modify-device-config.md)| <!-- keep by customization: end -->
|View web proxy settings|StorSimple Manager service → Devices → Configure|[Configure web proxy for your <!-- deleted by customization device](/documentation/articles/storsimple-configure-web-proxy)| --><!-- keep by customization: begin --> device](storsimple-configure-web-proxy.md)| <!-- keep by customization: end -->
|Modify device administrator password</br>Modify StorSimple Snapshot Manager password|StorSimple Manager service → Devices → Configure|[Change StorSimple <!-- deleted by customization passwords](/documentation/articles/storsimple-change-passwords)| --><!-- keep by customization: begin --> passwords](storsimple-change-passwords.md)| <!-- keep by customization: end -->
|Configure remote management|StorSimple Manager service → Devices → Configure|[Connect remotely to your StorSimple <!-- deleted by customization device](/documentation/articles/storsimple-remote-connect)| --><!-- keep by customization: begin --> device](storsimple-remote-connect.md)| <!-- keep by customization: end -->
|Configure alert settings|StorSimple Manager service → Devices → Configure|[View and manage StorSimple <!-- deleted by customization alerts](/documentation/articles/storsimple-manage-alerts)| --><!-- keep by customization: begin --> alerts](storsimple-manage-alerts.md)| <!-- keep by customization: end -->
|Configure CHAP for your StorSimple device|StorSimple Manager service → Devices → Configure|[Configure CHAP for your StorSimple <!-- deleted by customization device](/documentation/articles/storsimple-configure-chap)| --><!-- keep by customization: begin --> device](storsimple-configure-chap.md)| <!-- keep by customization: end -->
|Add a backup policy</br>Add or modify a schedule</br>Delete a backup policy</br>Take a manual backup</br>Create a custom backup policy with multiple volumes and schedules|StorSimple Manager service → Devices → Backup policies|[Manage backup <!-- deleted by customization policies](/documentation/articles/storsimple-manage-backup-policies)| --><!-- keep by customization: begin --> policies](storsimple-manage-backup-policies.md)| <!-- keep by customization: end -->
|Stop device controllers</br>Restart device controllers</br>Shut down device controllers</br>Reset your device to factory defaults</br>(Above are for on-premises device only)|StorSimple Manager service → Devices → Maintenance|[Manage StorSimple device <!-- deleted by customization controller](/documentation/articles/storsimple-manage-device-controller)| --><!-- keep by customization: begin --> controller](storsimple-manage-device-controller.md)| <!-- keep by customization: end -->
|Learn about StorSimple hardware components</br>Monitor hardware status</br>(Above are for on-premises device only)|StorSimple Manager service → Devices → Maintenance|[Monitor hardware <!-- deleted by customization components](/documentation/articles/storsimple-monitor-hardware-status)| --><!-- keep by customization: begin --> components](storsimple-monitor-hardware-status.md)| <!-- keep by customization: end -->
|Create a support package|StorSimple Manager service → Devices → Maintenance|[Create and manage a Support <!-- deleted by customization package](/documentation/articles/storsimple-create-manage-support-package)| --><!-- keep by customization: begin --> package](storsimple-create-manage-support-package.md)| <!-- keep by customization: end -->
|Install software updates|StorSimple Manager service → Devices → Maintenance|[Update your <!-- deleted by customization device](/documentation/articles/storsimple-update-device)| --><!-- keep by customization: begin --> device](storsimple-update-device.md)| <!-- keep by customization: end -->


##Next steps
If you experience any issues with the day-to-day operation of your StorSimple device or with any of its hardware components, refer to:

<!-- deleted by customization
- [Troubleshoot an operational device](/documentation/articles/storsimple-troubleshoot-operational-device)
- [Use StorSimple monitoring indicator LEDs](/documentation/articles/storsimple-monitoring-indicators)
-->
<!-- keep by customization: begin -->
- [Troubleshoot an operational device](storsimple-troubleshoot-operational-device.md)
- [Use StorSimple monitoring indicator LEDs](storsimple-monitoring-indicators.md)
<!-- keep by customization: end -->

If you cannot resolve the issues and you need to create a service request, refer to:

<!-- deleted by customization
-  [Contact Microsoft Support](/documentation/articles/storsimple-contact-microsoft-support)
-->
<!-- keep by customization: begin -->
-  [Contact Microsoft Support](storsimple-contact-microsoft-support.md)
<!-- keep by customization: end -->
