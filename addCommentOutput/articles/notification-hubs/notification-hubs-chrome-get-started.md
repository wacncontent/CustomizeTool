<properties
	pageTitle="Get started with Azure Notification Hubs for Chrome apps | Windows Azure"
	description="In this tutorial, you learn how to use Azure Notification Hubs to push notifications to a Chrome App."
	services="notification-hubs"
	documentationCenter=""
	authors="wesmc7777"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="notification-hubs"
	ms.date="10/20/2015"
	wacn.date=""/>

# Get started with Notification Hubs for Chrome apps

<!-- deleted by customization
[AZURE.INCLUDE [notification-hubs-selector-get-started](../includes/notification-hubs-selector-get-started.md)]
-->
<!-- keep by customization: begin -->
[AZURE.INCLUDE [notification-hubs-selector-get-started](../includes/notification-hubs-selector-get-started)]
<!-- keep by customization: end -->

This topic shows you how to use Azure Notification Hubs to send push notifications to a Chrome App.

One of the key benefits of using Chrome App notifications is that the notifications show up within the context of the Google Chrome browser. You don't need to have the Chrome App running or open in the browser (though the Chrome browser itself must be running). You also get a consolidated view of all your notifications in the Chrome Notifications window.

>[AZURE.NOTE] This is not a generic in-browser push notification and is specific to Chrome <!-- deleted by customization Appsâsee --><!-- keep by customization: begin --> Appssee <!-- keep by customization: end --> [Chrome Apps Overview] for details. Chrome Apps were previously known as "Packaged Apps" and are different from simpler "Hosted Apps". See [Installable web sites] for the difference. Chrome Apps can also run on mobile (Android and iOS) via Apache Cordova. See [Chrome Apps on Mobile] to learn more.

In this tutorial, we will create a Chrome app that receives push notifications by using Google Cloud Messaging (GCM). When you complete the tutorial, you will be able to broadcast push notifications to all the Chrome users who have installed this Chrome App.

The tutorial walks you through these basic steps to enable push notifications:

* [Enable Google Cloud Messaging](#register)
* [Configure your notification hub](#configure-hub)
* [Connect your Chrome App to the notification hub](#connect-app)
* [Send a notification to your Chrome App](#send)
* [Next steps](#next-steps)

This tutorial demonstrates the simple broadcast scenario in using Notification Hubs. Configuring GCM and Azure Notification Hubs is identical to configuring for Android, since [Google Cloud Messaging for Chrome] has been deprecated and the same GCM now supports both Android devices and Chrome instances.

Be sure to follow along with the tutorials in the "Next steps" section to see how to use notification hubs to address specific users and groups of devices.

>[AZURE.NOTE] To complete this tutorial, you must have an active Azure account. If you don't have an account, you can create a trial account in just a couple of minutes. For details, see [Azure Trial](/pricing/1rmb-trial/?WT.mc_id=A0E0E5C02&amp;returnurl=http%3A%2F%2Fazure.microsoft.com%2Fen-us%2Fdocumentation%2Farticles%notification-hubs-chrome-get-started%2F).

##<a id="register"></a>Enable Google Cloud Messaging

1. Navigate to the [Google Cloud Console] website, sign in with your Google account credentials, and then click the **Create Project** button. Provide an appropriate **Project Name**, and then click the **Create** button.

   	![][1]

2. Make a note of the **Project Number** on the **Projects** page for the project that you just created. You will use this as the **GCM Sender ID** in the Chrome App to register with GCM.

   	![][2]

3. In the left pane, click **APIs & auth**, and then scroll down and click the toggle to enable **Google Cloud Messaging for Android**. You don't have to enable **Google Cloud Messaging for Chrome**.

   	![][3]

4. In the left pane, click **Credentials** > **Create New Key** > **Server Key** > **Create**.

   	![][4]

5. Make a note of the server **API Key**. You will configure this in your notification hub next, to enable it to send push notifications to GCM.

   	![][5]

##<a id="configure-hub"></a>Configure your notification hub

1. Sign in to the [Azure Management Portal], and then click **+ NEW** at the bottom left of the screen.

2. Click **Azure Websitess** > **Service Bus** > **Notification Hub** > **Quick Create**. Type a name for your notification hub, select your desired region, and then click **Create a new Notification Hub**.

   	![][6]

4. Go to the notification hub that you just created. Click the namespace that houses your notification hub (usually ***notification hub name*-ns**).

   	![][7]

5. Click the **Notification Hubs** tab at the top.

   	![][8]

6. Click the **Configure** tab at the top.

   	![][9]

7. On the **Configure** tab, scroll down to the **google cloud messaging settings**, enter the **API Key** value that you obtained in the previous section, and then click **Save**.

   	![][10]

8. Select the **Dashboard** tab at the top, and then click **Connection Information** at the bottom.

   	![][11]

9. Take note of **DefaultListenSharedAccessSignature** (which you will need on the Chrome App to register with the notification hub) and **DefaultFullSharedAccessSignature** (which you will need to send notifications).

   	![][12]

Your notification hub is now configured to work with GCM, and you have the required connection strings for further configuration.

##<a id="connect-app"></a>Connect your Chrome App to the notification hub

###Create a new Chrome App

The sample below is based on [Chrome App GCM Sample] and uses the recommended way to create a Chrome App. In the sections below, we will highlight the steps related to Azure Notification Hubs. We recommend that you download the source for this Chrome App from [Chrome App Notification Hub Sample].

The Chrome App is created via JavaScript, and you can use any of your preferred word editors for creating it. Below is what this Chrome App will look like.

   	![][15]

2. Create a folder and name it **ChromePushApp** or anything that you want.

3. Download **cryto-js library** from [crypto-js library] in this folder. This library folder will contain two subfolders: **components** and **rollups**.

4. Create a **manifest.json** file. All Chrome Apps are backed by a manifest file that describes the app metadata and, in particular, the permissions that are available to the app.

		{
		  "name": "NH-GCM Notifications",
		  "description": "Chrome platform app.",
		  "manifest_version": 2,
		  "version": "0.1",
		  "app": {
		    "background": {
		      "scripts": ["background.js"]
		    }
		  },
		  "permissions": ["gcm", "storage", "notifications", "https://*.servicebus.chinacloudapi.cn/*"],
		  "icons": { "128": "gcm_128.png" }
		}

	Note the **permissions** element, which specifies that this Chrome App be able to receive push notifications from GCM. It must also specify the Azure Notification Hubs URI where the Chrome App will make a REST call to register.
	This uses an icon file, gcm_128.png, that you will find at the source that's reused from the original GCM sample. You can use any image that you want.

5. Create a file called **background.js** with the following code:

		// Returns a new notification ID used in the notification.
		function getNotificationId() {
		  var id = Math.floor(Math.random() * 9007199254740992) + 1;
		  return id.toString();
		}

		function messageReceived(message) {
		  // A message is an object with a data property that
		  // consists of key-value pairs.

		  // Concatenate all key-value pairs to form a display string.
		  var messageString = "";
		  for (var key in message.data) {
		    if (messageString != "")
		      messageString += ", "
		    messageString += key + ":" + message.data[key];
		  }
		  console.log("Message received: " + messageString);

		  // Pop up a notification to show the GCM message.
		  chrome.notifications.create(getNotificationId(), {
		    title: 'GCM Message',
		    iconUrl: 'gcm_128.png',
		    type: 'basic',
		    message: messageString
		  }, function() {});
		}

		var registerWindowCreated = false;

		function firstTimeRegistration() {
		  chrome.storage.local.get("registered", function(result) {

		    registerWindowCreated = true;
		    chrome.app.window.create(
		      "register.html",
		      {  width: 520,
		         height: 500,
		         frame: 'chrome'
		      },
		      function(appWin) {}
		    );
		  });
		}

		// Set up a listener for GCM message event.
		chrome.gcm.onMessage.addListener(messageReceived);

		// Set up listeners to trigger the first-time registration.
		chrome.runtime.onInstalled.addListener(firstTimeRegistration);
		chrome.runtime.onStartup.addListener(firstTimeRegistration);

	This is the file that pops up the Chrome App window HTML (**register.html**) and also defines the handler **messageReceived** to handle the incoming push notification.

6. Create a file called **register.html** that defines the UI of the Chrome App. Note that this sample uses *CryptoJS v3.1.2*. If you downloaded any other version, then fix the script src path.

		<html>

		<head>
		<title>GCM Registration</title>
		<script src="register.js"></script>
		<script src="CryptoJS v3.1.2/rollups/hmac-sha256.js"></script>
		<script src="CryptoJS v3.1.2/components/enc-base64-min.js"></script>
		</head>

		<body>

		Sender ID:<br/><input id="senderId" type="TEXT" size="20"><br/>
		<button id="registerWithGCM">Register with GCM</button>
		<br/>
		<br/>
		<br/>

		Notification Hub Name:<br/><input id="hubName" type="TEXT" style="width:400px"><br/><br/>
		Connection String:<br/><textarea id="connectionString" type="TEXT" style="width:400px;height:60px"></textarea>

		<br/>

		<button id="registerWithNH" disabled="true">Register with Azure Notification Hubs</button>

		<br/>
		<br/>

		<textarea id="console" type="TEXT" readonly style="width:500px;height:200px;background-color:#e5e5e5;padding:5px"></textarea>

		</body>

		</html>

7. Create a file called **register.js** with the code below. This file specifies the script behind **register.html**. Chrome Apps do not allow inline execution, so you have to create a separate backing script for your UI.

		var registrationId = "";
		var hubName        = "", connectionString = "";
		var originalUri    = "", targetUri = "", endpoint = "", sasKeyName = "", sasKeyValue = "", sasToken = "";

		window.onload = function() {
		   document.getElementById("registerWithGCM").onclick = registerWithGCM;  
		   document.getElementById("registerWithNH").onclick = registerWithNH;
		   updateLog("You have not registered yet. Please provider sender ID and register with GCM and then with  Notification Hubs.");
		}

		function updateLog(status) {
		  currentStatus = document.getElementById("console").innerHTML;
		  if (currentStatus != "") {
		    currentStatus = currentStatus + "\n\n";
		  }

		  document.getElementById("console").innerHTML = currentStatus  + status;
		}

		function registerWithGCM() {
		  var senderId = document.getElementById("senderId").value.trim();
		  chrome.gcm.register([senderId], registerCallback);

		  // Prevent register button from being clicked again before the registration finishes.
		  document.getElementById("registerWithGCM").disabled = true;
		}

		function registerCallback(regId) {
		  registrationId = regId;
		  document.getElementById("registerWithGCM").disabled = false;

		  if (chrome.runtime.lastError) {
		    // When the registration fails, handle the error and retry the
		    // registration later.
		    updateLog("Registration failed: " + chrome.runtime.lastError.message);
		    return;
		  }

		  updateLog("Registration with GCM succeeded.");
		  document.getElementById("registerWithNH").disabled = false;

		  // Mark that the first-time registration is done.
		  chrome.storage.local.set({registered: true});
		}

		function registerWithNH() {
		  hubName = document.getElementById("hubName").value.trim();
		  connectionString = document.getElementById("connectionString").value.trim();
		  splitConnectionString();
		  generateSaSToken();
		  sendNHRegistrationRequest();
		}

		// From http://msdn.microsoft.com/zh-cn/library/dn495627.aspx
		function splitConnectionString()
		{
		  var parts = connectionString.split(';');
		  if (parts.length != 3)
		  throw "Error parsing connection string";

		  parts.forEach(function(part) {
		    if (part.indexOf('Endpoint') == 0) {
		    endpoint = 'https' + part.substring(11);
		    } else if (part.indexOf('SharedAccessKeyName') == 0) {
		    sasKeyName = part.substring(20);
		    } else if (part.indexOf('SharedAccessKey') == 0) {
		    sasKeyValue = part.substring(16);
		    }
		  });

		  originalUri = endpoint + hubName;
		}

		function generateSaSToken()
		{
		  targetUri = encodeURIComponent(originalUri.toLowerCase()).toLowerCase();
		  var expiresInMins = 10; // 10 minute expiration

		  // Set expiration in seconds.
		  var expireOnDate = new Date();
		  expireOnDate.setMinutes(expireOnDate.getMinutes() + expiresInMins);
		  var expires = Date.UTC(expireOnDate.getUTCFullYear(), expireOnDate
		    .getUTCMonth(), expireOnDate.getUTCDate(), expireOnDate
		    .getUTCHours(), expireOnDate.getUTCMinutes(), expireOnDate
		    .getUTCSeconds()) / 1000;
		  var tosign = targetUri + '\n' + expires;

		  // Using CryptoJS.
		  var signature = CryptoJS.HmacSHA256(tosign, sasKeyValue);
		  var base64signature = signature.toString(CryptoJS.enc.Base64);
		  var base64UriEncoded = encodeURIComponent(base64signature);

		  // Construct authorization string.
		  sasToken = "SharedAccessSignature sr=" + targetUri + "&sig="
		                  + base64UriEncoded + "&se=" + expires + "&skn=" + sasKeyName;
		}

		function sendNHRegistrationRequest()
		{
		  var registrationPayload =
		  "<?xml version=\"1.0\" encoding=\"utf-8\"?>" +
		  "<entry xmlns=\"http://www.w3.org/2005/Atom\">" +
		      "<content type=\"application/xml\">" +
		          "<GcmRegistrationDescription xmlns:i=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://schemas.microsoft.com/netservices/2010/10/servicebus/connect\">" +
		              "<GcmRegistrationId>{GCMRegistrationId}</GcmRegistrationId>" +
		          "</GcmRegistrationDescription>" +
		      "</content>" +
		  "</entry>";

		  // Update the payload with the registration ID obtained earlier.
		  registrationPayload = registrationPayload.replace("{GCMRegistrationId}", registrationId);

		  var url = originalUri + "/registrations/?api-version=2014-09";
		  var client = new XMLHttpRequest();

		  client.onload = function () {
		    if (client.readyState == 4) {
		      if (client.status == 200) {
		        updateLog("Notification Hub Registration succesful!");
		        updateLog(client.responseText);
		      } else {
		        updateLog("Notification Hub Registration did not succeed!");
		        updateLog("HTTP Status: " + client.status + " : " + client.statusText);
		        updateLog("HTTP Response: " + "\n" + client.responseText);
		      }
		    }
		  };

		  client.onerror = function () {
		        updateLog("ERROR - Notification Hub Registration did not succeed!");
		  }

		  client.open("POST", url, true);
		  client.setRequestHeader("Content-Type", "application/atom+xml;type=entry;charset=utf-8");
		  client.setRequestHeader("Authorization", sasToken);
		  client.setRequestHeader("x-ms-version", "2014-09");

		  try {
		      client.send(registrationPayload);
		  }
		  catch(err) {
		      updateLog(err.message);
		  }
		}

	The above script has the following takeaways:
	- *window.onload* defines the button-click events of the two buttons on the UI. One registers with GCM, and the other uses the registration ID that's returned after registration with GCM to register with Azure Notification Hubs.
	- *updateLog* is the function that defines a simple logging function.
	- *registerWithGCM* is the first button-click handler, which makes the **chrome.gcm.register** call to GCM to register this Chrome App instance.
	- *registerCallback* is the callback function that gets called when the above GCM registration call returns.
	- *registerWithNH* is the second button-click handler, which registers with Notification Hubs. It gets **hubName** and **connectionString** (which the user has specified) and crafts the Notification Hubs Registration REST API call.
	- *splitConnectionString* and *generateSaSToken* are a JavaScript implementation of creating a SaS token that must be sent in all REST API calls. For more information, see [Common Concepts](http://msdn.microsoft.com/zh-cn/library/dn495627.aspx).
	- *sendNHRegistrationRequest* is the function that makes an HTTP REST call.
	- *registrationPayload* defines the registration XML payload. For more information, see [Create Registration NH REST API]. We update the registration ID in it with what we received from GCM.
	- *client* is an instance of **XMLHttpRequest** that we use to make the HTTP POST request. Note that we update the **Authorization** header with **sasToken**. Successful completion of this call will register this Chrome App instance with Azure Notification Hubs.


You should see the following view for your folder at the end of this:
   	![][21]

###Set up and test your Chrome App

1. Open your Chrome browser. Open **Chrome extensions** and enable **Developer mode**.

   	![][16]

2. Click **Load unpacked extension** and navigate to the folder where you created the files. You can also optionally use the **Chrome Apps & Extensions Developer Tool**. This tool is a Chrome App in itself (installed from the Chrome Web Store) and provides advanced debugging capabilities for your Chrome App development.

   	![][17]

3. If the Chrome App is created without any errors, then you will see your Chrome App show up.

   	![][18]

4. Enter the **Project Number** that you got earlier from the **Google Cloud Console** as the sender ID, and click **Register with GCM**. You must see the message **Registration with GCM succeeded.**

   	![][19]

5. Enter your **Notification Hub Name** and the **DefaultListenSharedAccessSignature** that you obtained from the <!-- deleted by customization portal --><!-- keep by customization: begin --> Azure Management Portal <!-- keep by customization: end --> earlier, and click **Register with Azure Notification Hub**. You must see the message **Notification Hub Registration successful!** and the details of the registration response, which contains the Azure Notification Hubs registration ID.

   	![][20]  

##<a name="send"></a>Send a notification to your Chrome App

In this tutorial, you send notifications by using a .NET console application. However, you can send notifications by using Notification Hubs from any backend via the <a href="http://msdn.microsoft.com/zh-cn/library/azure/dn223264.aspx">REST interface</a>.

For an example of how to send notifications from an Azure Mobile Services backend that's integrated with Notification Hubs, see "Get started with push notifications in Mobile Services" ([.NET backend](/documentation/articles/mobile-services-javascript-backend-android-get-started-push) | [JavaScript backend](/documentation/articles/mobile-services-javascript-backend-android-get-started-push)).  
For an example of how to send notifications by using the REST APIs, see "How to use Notification Hubs from Java/PHP/Python" ([Java](/documentation/articles/notification-hubs-java-backend-how-to) | [PHP](/documentation/articles/notification-hubs-php-backend-how-to) | [Python](/documentation/articles/notification-hubs-python-backend-how-to)).

1. In Visual Studio, from the **File** menu, select **New** and then **Project**. Under **Visual C#**, click **Windows** and **Console Application**, and then click **OK**.  This creates a new console application project.

2. From the **Tools** menu, click **Library Package Manager** and then **Package Manager Console**. This displays the Package Manager Console.

3. In the console window, execute the following command:

        Install-Package Microsoft.Azure.NotificationHubs

   	This adds a reference to the Azure Service Bus SDK with the <a href="http://nuget.org/packages/  WindowsAzure.ServiceBus/">WindowsAzure.ServiceBus NuGet package</a>.

4. Open the file **Program.cs** and add the following `using` statement:

        using Microsoft.Azure.NotificationHubs;

5. In the **Program** class, add the following method:

        private static async void SendNotificationAsync()
        {
            NotificationHubClient hub = NotificationHubClient.CreateClientFromConnectionString("<connection string with full access>", "<hub name>");
            String message = "{\"data\":{\"message\":\"Hello Chrome from Azure Notification Hubs\"}}";
            await hub.SendGcmNativeNotificationAsync(message);
        }

   	Make sure to replace the *hub name* placeholder with the name of the notification hub that appears in the portal on the **Notification Hubs** tab. Also, replace the connection string placeholder with the connection string called **DefaultFullSharedAccessSignature** that you obtained in the section "Configure your notification hub."

	>[AZURE.NOTE] Make sure that you use the connection string with **Full** access, not **Listen** access. The **Listen** access string does not have permissions to send notifications.

5. Add the following lines in the **Main** method:

         SendNotificationAsync();
		 Console.ReadLine();

6. Make sure that your Chrome browser is open. Your Chrome App doesn't need to be opened for this. You should see the following notification pop up on your desktop.

   	![][13]

7. You can also see all your notifications by using the Chrome Notifications window on the taskbar (in Windows) when Chrome is running.

   	![][14]

## <a name="next-steps"> </a>Next steps

In this simple example, you broadcasted notifications to your Chrome App.
Learn more about Notification Hubs in [Notification Hubs Overview].
To target specific users, refer to the tutorial [Azure Notification Hubs Notify Users]. If you want to segment your users by interest groups, you can read [Azure Notification Hubs breaking news].

<!-- Images. -->
[1]: ./media/notification-hubs-chrome-get-started/GoogleConsoleCreateProject.PNG
[2]: ./media/notification-hubs-chrome-get-started/GoogleProjectNumber.png
[3]: ./media/notification-hubs-chrome-get-started/EnableGCM.png
[4]: ./media/notification-hubs-chrome-get-started/CreateServerKey.png
[5]: ./media/notification-hubs-chrome-get-started/ServerKey.png
[6]: ./media/notification-hubs-chrome-get-started/CreateNH.png
[7]: ./media/notification-hubs-chrome-get-started/NHNamespace.png
[8]: ./media/notification-hubs-chrome-get-started/NamespaceConfigure.png
[9]: ./media/notification-hubs-chrome-get-started/NHConfigure.png
[10]: ./media/notification-hubs-chrome-get-started/NHConfigureGCM.png
[11]: ./media/notification-hubs-chrome-get-started/NHDashboard.png
[12]: ./media/notification-hubs-chrome-get-started/NHConnString.png
[13]: ./media/notification-hubs-chrome-get-started/ChromeNotification.png
[14]: ./media/notification-hubs-chrome-get-started/ChromeNotificationWindow.png
[15]: ./media/notification-hubs-chrome-get-started/ChromeApp.png
[16]: ./media/notification-hubs-chrome-get-started/ChromeExtensions.png
[17]: ./media/notification-hubs-chrome-get-started/ChromeLoadExtension.png
[18]: ./media/notification-hubs-chrome-get-started/ChromeAppLoaded.png
[19]: ./media/notification-hubs-chrome-get-started/ChromeAppGCM.png
[20]: ./media/notification-hubs-chrome-get-started/ChromeAppNH.png
[21]: ./media/notification-hubs-chrome-get-started/FinalFolderView.png

<!-- URLs. -->
[Chrome App Notification Hub Sample]: http://google.com
[Google Cloud Console]: http://cloud.google.com/console
[Azure Management Portal]: https://manage.windowsazure.cn/
[Notification Hubs Overview]: http://msdn.microsoft.com/zh-cn/library/jj927170.aspx
[Chrome Apps Overview]: https://developer.chrome.com/apps/about_apps
[Chrome App GCM Sample]: https://github.com/GoogleChrome/chrome-app-samples/tree/master/samples/gcm-notifications
[Installable web sites]: https://developers.google.com/chrome/apps/docs/
[Chrome Apps on Mobile]: https://developer.chrome.com/apps/chrome_apps_on_mobile
[Create Registration NH REST API]: http://msdn.microsoft.com/zh-cn/library/azure/dn223265.aspx
[crypto-js library]: http://code.google.com/p/crypto-js/
[GCM with Chrome Apps]: https://developer.chrome.com/apps/cloudMessaging
[Google Cloud Messaging for Chrome]: https://developer.chrome.com/apps/cloudMessagingV1
[Azure Notification Hubs Notify Users]: <!-- deleted by customization notification-hubs-aspnet-backend-windows-dotnet-notify-users.md --><!-- keep by customization: begin --> notification-hubs-aspnet-backend-windows-dotnet-notify-users <!-- keep by customization: end -->
[Azure Notification Hubs breaking news]: <!-- deleted by customization notification-hubs-windows-store-dotnet-send-breaking-news.md --><!-- keep by customization: begin --> notification-hubs-windows-store-dotnet-send-breaking-news <!-- keep by customization: end -->