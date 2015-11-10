While it's possible to paste a MongoLab URI into your code, we recommend configuring it in the environment for ease of management. This way, if the URI changes, you can update it through the Azure Management Portal without going to the code.


1. In the Azure Management Portal, select <!-- deleted by customization **Web Apps** --><!-- keep by customization: begin --> **Websites** <!-- keep by customization: end -->.
<!-- deleted by customization
1. Click the name of the web app in the Web Apps list.  
![WebAppEntry][entry-website]  
The Web App dashboard displays.
-->
<!-- keep by customization: begin -->
1. Click the name of the website in the website list.  
![WebSiteEntry][entry-website]  
The Website Dashboard displays.
<!-- keep by customization: end -->

1. Click **Configure** in the menu bar.  
<!-- deleted by customization
![WebAppDashboardConfig][focus-mongolab-websitedashboard-config]
-->
<!-- keep by customization: begin -->
![WebSiteDashboardConfig][focus-mongolab-websitedashboard-config]
<!-- keep by customization: end -->

1. Scroll down to the Connection Strings section.  
<!-- deleted by customization
![WebAppConnectionStrings][focus-mongolab-websiteconnectionstring]
-->
<!-- keep by customization: begin -->
![WebSiteConnectionStrings][focus-mongolab-websiteconnectionstring]
<!-- keep by customization: end -->

1. For **Name**, enter MONGOLAB_URI.
1. For **Value**, paste the connection string we obtained in the previous section.
1. Select **Custom** in the **Type** drop-down list (instead of the default **SQLAzure**).
1. Click **Save** on the toolbar.  
<!-- deleted by customization
![SaveWebApp][button-website-save]
-->
<!-- keep by customization: begin -->
![SaveWebSite][button-website-save]
<!-- keep by customization: end -->

**Note:** Azure adds the **CUSTOMCONNSTR_** prefix to this variable, which is why the code above references **CUSTOMCONNSTR_MONGOLAB_URI.**

[entry-website]: ./media/howto-save-connectioninfo-mongolab/entry-website.png
[focus-mongolab-websitedashboard-config]: ./media/howto-save-connectioninfo-mongolab/focus-mongolab-websitedashboard-config.png
[focus-mongolab-websiteconnectionstring]: ./media/howto-save-connectioninfo-mongolab/focus-mongolab-websiteconnectionstring.png
[button-website-save]: ./media/howto-save-connectioninfo-mongolab/button-website-save.png
