deletion:

deleted:

		This article does not cover client certificate authentication; for information about that, see [How To Configure TLS Mutual Authentication for Web Apps](/documentation/articles/app-service-web-configure-tls-mutual-auth).

reason: ()

deleted:

		>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.
		
		## What's changed
		* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
		* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

reason: ()

replacement:

deleted:

		1.	In your browser, open the [Azure Management Portal](https://manage.windowsazure.cn/).
		2.	Click the **Browse** option on the left side of the page.
		3.	Click the **Web Apps** blade.
		4.	Click the name of your web app.
		5.	In the **Essentials** page, click **Settings**.
		6.	Click **Scale**
			![The scale tab][scale]
		7.	In the **Scale** section, set the App Service plan mode by clicking **Select**.
			![The Pricing tier][sslreserved]

replaced by:

		1. In your browser, open the [Management Portal][portal].
		
		2. In the **Websites** tab, click the name of your website.
		
			![selecting a web site][website]
		
		3. Click the **SCALE** tab.
		
			![The scale tab][scale]
		
		4. In the **general** section, set the web hosting plan mode by clicking **STANDARD**.
		
			![standard mode selected][standard]
		
		5. Click **Save**. When prompted, click **Yes**.

reason: ()

deleted:

		1.	In your browser, open the [Azure Management Portal](https://manage.windowsazure.cn).
		2.	Click the **Browse** option on the left side of the page.
		3.	Click the **Web Apps** blade.
		4.	Click the name of your web app.
		5.	In the **Essentials** page, click **Settings**.	
		6.	Click **Custom domains and SSL**.
			![The config tab][sslconfig]
		7.	In the **certificates** section, click **Upload**
		8.	Using the **Upload a certificate** dialog, select the .pfx certificate file created earlier using the IIS Manager or OpenSSL. Specify the password, if any, that was used to secure the .pfx file. Finally, click the **Save** to upload the certificate.
			![ssl upload][ssluploadcert]
		9. In the **ssl bindings** section of the **SSL Settings** tab, use the dropdowns to select the domain name to secure with SSL, and the certificate to use. You may also select whether to use [Server Name Indication][sni] (SNI) or IP based SSL.
		
			![ssl bindings][sslbindings]

replaced by:

		1.	In your browser, open the [Azure Management Portal][portal].
		
		2. In the **Websites** tab, click the name of your site and then select the **CONFIGURE** tab.
		
			![the configure tab][configure]
		
		3. In the **certificates** section, click **upload a certificate**
		
			![upload a certificate][uploadcert]
		
		4. Using the **Upload a certificate** dialog, select the .pfx certificate file created earlier using the IIS Manager or OpenSSL. Specify the password, if any, that was used to secure the .pfx file. Finally, click the **check** to upload the certificate.
			
			![upload certificate dialog][uploadcertdlg]
		
		5. In the **ssl bindings** section of the **CONFIGURE** tab, use the dropdowns to select the domain name to secure with SSL, and the certificate to use. You may also select whether to use [Server Name Indication][sni](SNI) or IP based SSL.
		
			![ssl bindings][sslbindings]

reason: ()


