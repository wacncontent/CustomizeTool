<!-- deleted by customization
<!--author=SharS last changed: 11/16/15-->

#### To create a volume
-->
<!-- keep by customization: begin -->
<properties 
   pageTitle="Create a volume"
   description="Explains how to add a volume on a StorSimple device."
   services="storsimple"
   documentationCenter="NA"
   authors="SharS"
   manager="adinah"
   editor="tysonn" />
<tags
	ms.service="storsimple"
	ms.date="04/01/15"
	wacn.date=""/>

### To create a volume
<!-- keep by customization: end -->

1. On the device **Quick Start** page, click **Add a volume**. This starts the Add a volume wizard.

2. In the Add a volume wizard, under **Basic Settings**<!-- deleted by customization, do the following -->:
   1. <!-- deleted by customization Supply --><!-- keep by customization: begin --> Type <!-- keep by customization: end --> a **Name** for your volume.
<!-- deleted by customization
   2. Specify the **Provisioned Capacity** for your volume in GB or TB. The volume capacity must be between 1 GB and 64 TB for a physical device.
   3. On the drop-down list, select the **Usage Type** for your volume. 
   4. If you are using this volume for archival data, select the **Use this volume for less frequently accessed archival data** check box. For all other use cases, simply select **Tiered Volume**. (Tiered volumes were formerly called primary volumes).
-->
<!-- keep by customization: begin -->
   2. Specify the **Provisioned Capacity** for your volume. **The volume capacity must be between 1 GB and 64 TB.**
   3. On the drop-down list, select the **Usage Type** for your volume. For less frequently accessed archival data, select an **Archive volume**. For all other types of data, select **Primary volume**.
<!-- keep by customization: end -->
   4. Click the arrow icon ![arrow-icon](./media/storsimple-create-volume/HCS_ArrowIcon-include.png) to go to the next page.

<!-- deleted by customization
        ![Add volume](./media/storsimple-create-volume/AddVolume1-include.png)
-->
<!-- keep by customization: begin -->
     ![Add volume](./media/storsimple-create-volume/HCS_AddVolume1M-include.png)
<!-- keep by customization: end -->

3. In the **Additional Settings** dialog box, add a new access control record (ACR):
   1. Supply a **Name** for your ACR.
   2. Under **iSCSI Initiator Name**, provide the iSCSI Qualified Name (IQN) of your Windows host. If you don't have the IQN, <!-- deleted by customization go to --><!-- keep by customization: begin --> follow the steps in <!-- keep by customization: end --> [Get the IQN of a Windows Server <!-- deleted by customization host](#get-the-iqn-of-a-windows-server-host) --><!-- keep by customization: begin --> host](#storsimple-get-iqn.md) <!-- keep by customization: end -->.
<!-- deleted by customization
   3. We recommend that you enable a default backup by selecting the **Enable a default backup for this volume** check box. The default backup will create a policy that executes at 22:30 each day (device time) and creates a cloud snapshot of this volume.
-->
<!-- keep by customization: begin -->
   3. Under **Default backup for this volume?**, select the **Enable** check box. The default backup will create a policy that executes at 22:30 each day (device time) and creates a cloud snapshot of this volume.
<!-- keep by customization: end -->

        > [AZURE.NOTE] After the backup is enabled here, it cannot be reverted. You will need to edit the volume to modify this setting.

<!-- deleted by customization
        ![Add volume](./media/storsimple-create-volume/AddVolume2-include.png)
-->
<!-- keep by customization: begin -->
     ![Add volume](./media/storsimple-create-volume/HCs_AddVolume2M-include.png)
<!-- keep by customization: end -->

4. Click the check icon ![check icon](./media/storsimple-create-volume/HCS_CheckIcon-include.png). A volume will be created with the specified settings.

<!-- deleted by customization
![Video available](./media/storsimple-create-volume/Video_icon.png) **Video available**

To watch a video that demonstrates how to create a StorSimple volume, click [here](http://azure.microsoft.com/documentation/videos/create-a-storsimple-volume/).
-->

