
1. In the Solution view, expand the **Components** folder in the Xamarin.Android app and make sure that Azure Mobile Services package is installed. 

2. Right-click the **Components** folder, click  **Get More Components...**, search for the **Google Cloud Messaging Client** component and add it to the project. 

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 3 <!-- keep by customization: end -->. Open the ToDoActivity.cs project file and add the following using statement to the class:

		using Gcm.Client;

<!-- deleted by customization 2 --><!-- keep by customization: begin --> 4 <!-- keep by customization: end -->. In the **ToDoActivity** class, add the following new code:

        // Create a new instance field for this activity.
        static ToDoActivity instance = new ToDoActivity();

        // Return the current activity instance.
        public static ToDoActivity CurrentActivity
        {
            get
            {
                return instance;
            }
        }
        // Return the Mobile Services client.
        public MobileServiceClient CurrentClient
        {
            get
            {
                return client;
            }
        }

	This enables you to access the Mobile Services client instance from the service process.

<!-- deleted by customization 3 --><!-- keep by customization: begin --> 5 <!-- keep by customization: end -->. Change the existing Mobile Services client declaration to public, as follows:

		public MobileServiceClient client { get; private set; }

<!-- deleted by customization 4.	Add --><!-- keep by customization: begin --> 6.	Add <!-- keep by customization: end --> the following code to the **OnCreate** method, after the **MobileServiceClient** is created:

        // Set the current instance of TodoActivity.
        instance = this;

        // Make sure the GCM client is set up correctly.
        GcmClient.CheckDevice(this);
        GcmClient.CheckManifest(this);

        // Register the app for push notifications.
        GcmClient.Register(this, ToDoBroadcastReceiver.senderIDs);

Your **ToDoActivity** is now prepared for adding push notifications.