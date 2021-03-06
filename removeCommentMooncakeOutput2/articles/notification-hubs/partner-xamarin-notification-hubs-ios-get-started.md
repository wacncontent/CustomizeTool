<properties
	pageTitle="Get started with Notification Hubs for Xamarin iOS apps | Windows Azure"
	description="In this tutorial, you learn how to use Azure Notification Hubs to send push notifications to a Xamarin iOS application."
	services="notification-hubs"
	documentationCenter="xamarin"
	authors="ysxu"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="notification-hubs"
	ms.date="10/19/2015"
	wacn.date=""/>

# Get started with Notification Hubs

[AZURE.INCLUDE [notification-hubs-selector-get-started](../includes/notification-hubs-selector-get-started.md)]

##Overview

This tutorial shows you how to use Azure Notification Hubs to send push notifications to an iOS application.
You'll create a blank Xamarin.iOS app that receives push notifications by using the Apple Push Notification Service (APNs). When you're finished, you'll be able to use your notification hub to broadcast push notifications to all the devices running your app. The finished code is available in the [NotificationHubs app][GitHub] sample.

This tutorial demonstrates the simple broadcast scenario in using Notification Hubs.

##Prerequisites

This tutorial requires the following:

+ [Xcode 6.0][Install Xcode]
+ An iOS 7.0 (or later version) capable device
+ iOS Developer Program membership
+ [Xamarin.iOS]
+ [Azure Mobile Services Component]

   > [AZURE.NOTE] Because of configuration requirements for push notifications, you must deploy and test push notifications on an iOS capable device (iPhone or iPad) instead of in the simulator.

Completing this tutorial is a prerequisite for all other Notification Hubs tutorials for Xamarin.iOS apps.

> [AZURE.IMPORTANT] To complete this tutorial, you must have an active Azure account. If you don't have an account, you can create a trial account in just a couple of minutes. For details, see [Azure Trial](/pricing/1rmb-trial/?WT.mc_id=A643EE910&amp;returnurl=http%3A%2F%2Fazure.microsoft.com%2Fen-us%2Fdocumentation%2Farticles%2Fpartner-xamarin-notification-hubs-ios-get-started).

The Apple Push Notification Service uses certificates to authenticate your mobile service. Follow these instructions to create the necessary certificates and upload them to your mobile service. For the official APNs feature documentation, see [Apple Push Notification Service].


##<a name="certificates"></a>Generate the Certificate Signing Request file

First you must generate the Certificate Signing Request (CSR) file, which is used by Apple to generate a signed certificate.

1. From the Utilities folder, run the Keychain Access tool.

2. Click **Keychain Access**, expand **Certificate Assistant**, and then click **Request a Certificate from a Certificate Authority**.

  	![][5]

3. Select your **User Email Address**, type **Common Name** and **CA Email Address** values, make sure that **Saved to disk** is selected, and then click **Continue**.

  	![][6]

4. Type a name for the CSR file in **Save As**, select the location in **Where**, and then click **Save**.

  	![][7]

  	This saves the CSR file in the selected location. The default location is on the desktop. Remember the location that you have chosen for this file.

Next, register your app with Apple, enable push notifications, and upload this exported CSR to create a push certificate.

##<a name="register"></a>Register your app for push notifications

To be able to send push notifications to an iOS app from Mobile Services, you must register your application with Apple and also register for push notifications.  

1. If you have not already registered your app, navigate to the <a href="https://idmsa.apple.com/IDMSWebAuth/login?&appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2F%2Faccount%2Foverview.action" target="_blank">iOS Provisioning Portal</a> at the Apple Developer Center, sign in with your Apple ID, click **Identifiers**, click **App IDs**, and finally click the **+** sign to register a new app.

   	![][105]

2. Type a name for your app in **Description** and a value for **Bundle Identifier**, check the **Push Notifications** option in the **App Services** section, and then click **Continue**.

   	![][106]

   	![][107]

   	![][108]


	This generates your app ID and requests that you submit the information. Click **Submit**.

   	![][109]

	Once you click **Submit**, you will see the **Registration complete** screen, as shown below. Click **Done**.

   	![][110]

	> [AZURE.NOTE] If you choose to supply a **Bundle Identifier** value other than **MobileServices.Quickstart**, you must also update the bundle identifier value in your Xcode project.

3. Locate the app ID that you just created, and click its row.

   	![][111]

	Clicking the app ID will display details about the app and the app ID:

   	![][112]

   	![][113]

4. Click **Edit**, and then scroll to the bottom of the screen and click **Create Certificate...** under the section **Development Push SSL Certificate**.

   	![][114]

	This displays the Add iOS Certificate assistant.

   	![][115]

	> [AZURE.NOTE] This tutorial uses a development certificate. The same process is used for registering a production certificate. Just make sure that you set the same certificate type when you upload the certificate to Mobile Services.

5. Click **Choose File**, browse to the location in which you saved the CSR file that you created in the first task, and then click **Generate**.

  	![][116]

6. After the certificate is created by the portal, click **Download**, and then click **Done**.

  	![][118]

  	![][119]  

   	This downloads the signing certificate and saves it to your computer in your **Downloads** folder.

  	![][9]

    > [AZURE.NOTE] By default, the downloaded file for a development certificate is named **aps_development.cer**.

7. Double-click the downloaded push certificate **aps_development.cer**.

	This installs the new certificate in the Keychain, as shown below:

   	![][10]

	> [AZURE.NOTE]
	> The name in your certificate might be different, but it will be prefixed with <strong>Apple Development iOS Push Notification Services:</strong>.

	Later, you will use this certificate to generate a .p12 file and upload it to your notification hub to enable push notifications through APNs.

##<a name="profile"></a>Create a provisioning profile for the app

1. Back in the <a href="https://idmsa.apple.com/IDMSWebAuth/login?&appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2F%2Faccount%2Foverview.action" target="_blank">iOS Provisioning Portal</a>, select **Provisioning Profiles**, select **All**, and then click the **+** button to create a new profile. This displays the **Add iOS Provisioning Profile** wizard.

   	![][120]

2. Select **iOS App Development** under **Development** as the provisioning profile type, and click **Continue**.

   	![][121]

3. Select the app ID for the Mobile Services Quickstart app from the **App ID** drop-down list, and click **Continue**.

   	![][122]

4. In the **Select certificates** screen, select the certificate that you created earlier, and click **Continue**.

   	![][123]

5. Select the devices to use for testing, and click **Continue**.

   	![][124]

6. Finally, choose a name for the profile in **Profile Name**, click **Generate**, and click **Done**.

   	![][125]

   	![][126]

  	This creates a new provisioning profile.

7. In Xcode, open the Organizer, select the Devices view, select **Provisioning Profiles** in the **Library** section in the left pane, and import the provisioning profile that you just created.

8. On the left, select your device, and again import the provisioning profile.

9. In Keychain Access, right-click the new certificate, click **Export**, type a name for your certificate, select the **.p12** format, and then click **Save**.

   	![][18]

  	Make a note of the file name and location of the exported certificate.

This ensures that the Xcode project uses the new profile for code signing. Next, you must upload the certificate to your notification hub.

##<a name="configure-hub"></a>Configure your notification hub

1. Sign in to the [Azure Management Portal], and click **+NEW** at the bottom of the screen.

2. Click **App Services**, click **Service Bus**, click **Notification Hub**, and then click **Quick Create**.

   	![][27]

3. Type a name for your notification hub, select your desired region, and then click **Create a New Notification Hub**.

   	![][28]

4. Click the namespace that you just created (usually ***notification hub name*-ns**), and then click the **Configure** tab at the top.

   	![][29]

5. Click the **Notification Hubs** tab at the top, and then click the notification hub that you just created.

   	![][210]

6. Select the **Configure** tab at the top, and then click **Upload** for the Apple notification settings. Then select the **.p12** certificate that you exported earlier, along with the password for the certificate. Make sure to select whether you want to use the **Production** (if you want to send push notifications to users who purchased your app from the store) or the **Sandbox** (during development) push service.

   	![][211]

7. Click the **Dashboard** tab at the top, and then click **Connection Information**. Take note of the two connection strings.

   	![][212]

Your notification hub is now configured to work with APNs, and you have the connection strings to register your app and send notifications.

##<a name="connecting-app"></a>Connect your app to the notification hub

### Create a new project

1. In Xamarin Studio, create a new iOS project and select the **Unified API** > **Single View Application** template.

   	![][31]

2. Add a reference to the Azure Messaging component. In the Solution view, right-click the **Components** folder for your project and choose **Get More Components**. Search for the **Azure Messaging** component and add the component to your project.

3. In **AppDelegate.cs**, add the following using statement:

    using WindowsAzure.Messaging;

4. Declare an instance of **SBNotificationHub**:

		private SBNotificationHub Hub { get; set; }

5. Create a **Constants.cs** class with the following variables:

        // Azure app-specific connection string and hub path
        public const string ConnectionString = "<Azure connection string>";
        public const string NotificationHubPath = "<Azure hub path>";


6. In **AppDelegate.cs**, update **FinishedLaunching()** to match the following:

        public override bool FinishedLaunching(UIApplication application, NSDictionary launchOptions)
        {
            UIRemoteNotificationType notificationTypes = UIRemoteNotificationType.Alert |
                UIRemoteNotificationType.Badge | UIRemoteNotificationType.Sound;
            UIApplication.SharedApplication.RegisterForRemoteNotificationTypes(notificationTypes);

            return true;
        }

7. Override the **RegisteredForRemoteNotifications()** method in **AppDelegate.cs**:

        public override void RegisteredForRemoteNotifications(UIApplication application, NSData deviceToken)
        {
            Hub = new SBNotificationHub(Constants.ConnectionString, Constants.NotificationHubPath);

            Hub.UnregisterAllAsync (deviceToken, (error) => {
                if (error != null)
                {
                    Console.WriteLine("Error calling Unregister: {0}", error.ToString());
                    return;
                }

                NSSet tags = null; // create tags if you want
                Hub.RegisterNativeAsync(deviceToken, tags, (errorCallback) => {
                    if (errorCallback != null)
                        Console.WriteLine("RegisterNativeAsync error: " + errorCallback.ToString());
                });
            });
        }

8. Override the **ReceivedRemoteNotification()** method in **AppDelegate.cs**:

        public override void ReceivedRemoteNotification(UIApplication application, NSDictionary userInfo)
        {
            ProcessNotification(userInfo, false);
        }

9. Create the following **ProcessNotification()** method in **AppDelegate.cs**:

        void ProcessNotification(NSDictionary options, bool fromFinishedLaunching)
        {
            // Check to see if the dictionary has the aps key.  This is the notification payload you would have sent
            if (null != options && options.ContainsKey(new NSString("aps")))
            {
                //Get the aps dictionary
                NSDictionary aps = options.ObjectForKey(new NSString("aps")) as NSDictionary;

                string alert = string.Empty;

                //Extract the alert text
                // NOTE: If you're using the simple alert by just specifying
                // "  aps:{alert:"alert msg here"}  ", this will work fine.
                // But if you're using a complex alert with Localization keys, etc.,
                // your "alert" object from the aps dictionary will be another NSDictionary.
                // Basically the JSON gets dumped right into a NSDictionary,
                // so keep that in mind.
                if (aps.ContainsKey(new NSString("alert")))
                    alert = (aps [new NSString("alert")] as NSString).ToString();

                //If this came from the ReceivedRemoteNotification while the app was running,
                // we of course need to manually process things like the sound, badge, and alert.
                if (!fromFinishedLaunching)
                {
                    //Manually show an alert
                    if (!string.IsNullOrEmpty(alert))
                    {
                        UIAlertView avAlert = new UIAlertView("Notification", alert, null, "OK", null);
                        avAlert.Show();
                    }
                }
            }
        }

    > [AZURE.NOTE] You can choose to override **FailedToRegisterForRemoteNotifications()** to handle situations such as no network connection.


10. Run the app on your device.

##<a name="send"></a>Send notifications from your backend

You can send notifications by using Notification Hubs from any backend via our <a href="http://msdn.microsoft.com/zh-cn/library/azure/dn223264.aspx">REST interface</a>. In this tutorial, we will send notifications by using a .NET console app and by using a mobile service through a node script.

To send notifications by using a .NET app:

1. Create a new Visual C# console application:

   	![][213]

2. Add a reference to the Azure Service Bus SDK by using the <a href="http://nuget.org/packages/WindowsAzure.ServiceBus/">WindowsAzure.ServiceBus NuGet package</a>. In the Visual Studio main menu, click **Tools**, click **Library Package Manager**, and then click **Package Manager Console**. Then, in the console window, type the following and press Enter:

        Install-Package WindowsAzure.ServiceBus

2. Open the Program.cs file and add the following using statement:

        using Microsoft.ServiceBus.Notifications;

3. In your `Program` class, add the following method:

        private static async void SendNotificationAsync()
        {
            NotificationHubClient hub = NotificationHubClient.CreateClientFromConnectionString("<connection string with full access>", "<hub name>");
            var alert = "{\"aps\":{\"alert\":\"Hello from .NET!\"}}";
            await hub.SendAppleNativeNotificationAsync(alert);
        }

4. Add the following lines in your `Main` method:

         SendNotificationAsync();
		 Console.ReadLine();

5. Press the F5 key to run the app. You should receive an alert on your device. If you are using Wi-Fi, make sure that your connection is working.

You can find all the possible payloads in the Apple [Local and Push Notification Programming Guide].

To send a notification by using a mobile service, follow [Get started with Mobile Services], and then:

1. Sign in to the [Azure Management Portal], and select your mobile service.

2. Select the **Scheduler** tab on the top.

   	![][215]

3. Create a new scheduled job, insert a name, and select **On demand**.

   	![][216]

4. When the job is created, click the job name. Then click the **Script** tab on the top bar.

5. Insert the following script inside your scheduler function. Make sure to replace the placeholders with your notification hub name and the connection string for *DefaultFullSharedAccessSignature* that you obtained earlier. Click **Save**.

		var azure = require('azure');
		var notificationHubService = azure.createNotificationHubService('<Hubname>', '<SAS Full access >');
		notificationHubService.apns.send(
	    	null,
    		{"aps":
        		{
          		"alert": "Hello from Mobile Services!"
        		}
    		},
    		function (error)
    		{
	        	if (!error) {
    	        	console.warn("Notification successful");
        		}
    		}
		);


6. Click **Run Once** on the bottom bar. You should receive an alert on your device.

## <a name="next-steps"> </a>Next steps

In this simple example, you broadcasted notifications to all your iOS devices. In order to target specific users, refer to the tutorial [Use Notification Hubs to push notifications to users]. If you want to segment your users by interest groups, you can read [Use Notification Hubs to send breaking news]. Learn more about how to use Notification Hubs in [Notification Hubs Guidance] and in the [Notification Hubs How-To for iOS].

<!-- Anchors. -->
[Generate the certificate signing request]: #certificates
[Register your app and enable push notifications]: #register
[Create a provisioning profile for the app]: #profile
[Configure your Notification Hub]: #configure-hub
[Connecting your app to the Notification Hub]: #connecting-app
[Send notifications from your back-end]: #send
[Next Steps]:#next-steps

<!-- Images. -->
[5]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-step5.png
[6]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-step6.png
[7]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-step7.png

[9]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-step9.png
[10]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-step10.png
[18]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-step18.png
[105]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-05.png
[106]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-06.png
[107]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-07.png
[108]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-08.png
[109]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-09.png
[110]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-10.png
[111]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-11.png
[112]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-12.png
[113]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-13.png
[114]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-14.png
[115]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-15.png
[116]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-16.png

[118]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-18.png
[119]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-19.png

[120]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-20.png
[121]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-21.png
[122]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-22.png
[123]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-23.png
[124]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-24.png
[125]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-25.png
[126]: ./media/partner-xamarin-notification-hubs-ios-get-started/mobile-services-ios-push-26.png

[27]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-create-from-portal.png
[28]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-create-from-portal2.png
[29]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-select-from-portal.png
[210]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-select-from-portal2.png
[211]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-configure-ios.png
[212]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-connection-strings.png


[213]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-create-console-app.png



[215]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-scheduler1.png
[216]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-scheduler2.png


[31]: ./media/partner-xamarin-notification-hubs-ios-get-started/notification-hub-create-ios-app.png




<!-- URLs. -->
[Mobile Services iOS SDK]: http://go.microsoft.com/fwLink/?LinkID=266533
[Submit an app page]: http://go.microsoft.com/fwlink/p/?LinkID=266582
[My Applications]: http://go.microsoft.com/fwlink/p/?LinkId=262039
[Live SDK for Windows]: http://go.microsoft.com/fwlink/p/?LinkId=262253

[Get started with Mobile Services]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-xamarin-ios
[Azure Management Portal]: https://manage.windowsazure.cn/
[Notification Hubs Guidance]: http://msdn.microsoft.com/zh-cn/library/jj927170.aspx
[Notification Hubs How-To for iOS]: http://msdn.microsoft.com/zh-cn/library/jj927168.aspx
[Install Xcode]: https://go.microsoft.com/fwLink/p/?LinkID=266532
[iOS Provisioning Portal]: https://idmsa.apple.com/IDMSWebAuth/login?&appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2F%2Faccount%2Foverview.action

[Use Notification Hubs to push notifications to users]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-push-notifications-app-users-aspnet
[Use Notification Hubs to send breaking news]: /manage/services/notification-hubs/breaking-news-dotnet

[Local and Push Notification Programming Guide]: http://developer.apple.com/library/mac/#documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html#//apple_ref/doc/uid/TP40008194-CH100-SW1
[Apple Push Notification Service]: https://developer.apple.com/library/ios/#documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/ApplePushService/ApplePushService.html

[Azure Mobile Services Component]: http://components.xamarin.com/view/azure-mobile-services/
[GitHub]: http://go.microsoft.com/fwlink/p/?LinkId=331329
[Xamarin.iOS]: http://xamarin.com/download
[WindowsAzure.Messaging]: https://github.com/infosupport/WindowsAzure.Messaging.iOS
