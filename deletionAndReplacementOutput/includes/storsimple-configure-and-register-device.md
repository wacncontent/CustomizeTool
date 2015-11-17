deletion:

deleted:

		If you run into any issues during this step, refer to troubleshooting guidance for [Errors during web proxy configuration](/documentation/articles/storsimple-troubleshoot-deployment#errors-during-the-optional-web-proxy-settings).

reason: ()

deleted:

		> [AZURE.NOTE] You can press Ctrl + C at any time to exit the setup wizard. Any settings that you applied before you issued this command will be retained.

reason: ()

deleted:

		If the device status is **Offline**, wait for a couple of minutes for the device to come online.

reason: ()

replacement:

deleted:

		<!--author=alkohli last changed: 9/17/15-->
		
		
		#### To configure and register the device

replaced by:

		<properties 
		   pageTitle="Configure and register your device"
		   description="Explains how to use Windows PowerShell for StorSimple to configure and register your device."
		   services="storsimple"
		   documentationCenter="NA"
		   authors="SharS"
		   manager="adinah"
		   editor="tysonn" />
		<tags
			ms.service="storsimple"
			ms.date="04/01/2015"
			wacn.date=""/>
		
		
		### To configure and register the device

reason: ()

deleted:

		**Password1**

replaced by:

		*Password1*

reason: ()

deleted:

		6. Type the following command:
		
		     `Invoke-HcsSetupWizard`

replaced by:

		6. Type the following command: **Invoke-HcsSetupWizard**

reason: ()

deleted:

		device](/documentation/articles/storsimple-configure-web-proxy)

replaced by:

		device](https://msdn.microsoft.com/zh-cn/library/azure/dn764937.aspx)

reason: ()

deleted:

		You can reset the StorSimple Snapshot Manager password from the StorSimple Manager service interface. For detailed steps, go to [Change the StorSimple passwords using the StorSimple Manager serivce](/documentation/articles/storsimple-change-passwords).
		
			To troubleshoot any issues during this step, refer to troubleshooting guidance for [Errors related to passwords](/documentation/articles/storsimple-troubleshoot-deployment#errors-related-to-device-administrator-and-storsimple-snapshot-manager-passwords).

replaced by:

		You can reset the StorSimple Snapshot Manager password from the StorSimple Manager service interface.

reason: ()

deleted:

		To troubleshoot any possible device registration failures, refer to [Errors during device registration](/documentation/articles/storsimple-troubleshoot-deployment#errors-during-device-registration). For detailed troubleshooting, you can also refer to [Step-by-step troubleshooting example](/documentation/articles/storsimple-troubleshoot-deployment#step-by-step-storsimple-troubleshooting-example).
		
		12. After the device is registered, a Service Data Encryption key will appear. Copy this key and save it in a safe location.
			
			> [AZURE.WARNING] This key will be required with the service registration key to register additional devices with the StorSimple Manager service. Refer to [StorSimple security](/documentation/articles/storsimple-security) for more information about this key.
		
		     ![StorSimple register device 6](./media/storsimple-configure-and-register-device/HCS_RegisterYourDevice6-include.png)

replaced by:

		> [AZURE.NOTE] You can press Ctrl + C at any time to exit the setup wizard. Any settings that you applied before you issued this command will be retained.
		
		12. After the device is registered, a Service Data Encryption key will appear. Copy this key and save it in a safe location. **This key will be required with the service registration key to register additional devices with the StorSimple Manager service.** Refer to [StorSimple security](/documentation/articles/storsimple-security) for more information about this key.
		
		     ![StorSimple register device 6](./media/storsimple-configure-and-register-device/HCS_RegisterYourDevice6-include.png)

reason: ()

deleted:

		> [AZURE.IMPORTANT] After the device is online, plug in the network cables that you had unplugged in the beginning of this step.
		
		After the device is successfully registered and doesn't come online, you can run the `Test-HcsmConnection -Verbose` to ensure that the network connectivity is healthy. For the detailed usage of this cmdlet, go to [cmdlet reference for Test-HcsmConnection](https://technet.microsoft.com/zh-cn/library/dn715782.aspx).
		
		![Video available](./media/storsimple-configure-and-register-device/Video_icon.png) **Video available**
		
		To watch a video that demonstrates how to configure and register your device through Windows PowerShell for StorSimple, click [here](http://azure.microsoft.com/documentation/videos/initialize-the-storsimple-appliance/).

replaced by:

		> [AZURE.NOTE] If the device status is **Offline**, wait for a couple of minutes for the device to come online.

reason: ()

