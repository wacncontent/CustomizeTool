<properties 
	 pageTitle="How to Map Content Delivery Network (CDN) Content to a Custom Domain" 
	 description="This topic demonstrate how to map a CDN content to a Custom Domain." 
	 services="cdn" 
	 documentationCenter="" 
	 authors="camsoper" 
	 manager="dwrede" 
	 editor=""/>
<tags
	ms.service="cdn"
	ms.date="12/02/2015"
	wacn.date=""/>

#How to map Custom Domain to Content Delivery Network (CDN) endpoint

You can map a custom domain to a CDN endpoint in order to use your own domain name in URLs to cached content, rather than using the CDN endpoint provided to you. <!-- deleted by customization  To do this, you will create a CNAME record with your domain registrar and map your custom domain and subdomain to the CDN endpoint.  A CNAME record is a DNS feature that maps a source domain to a destination domain. In this case, the source domain is your custom domain and subdomain (subdomain is always required). The destination domain is your CDN endpoint. -->

<!-- deleted by customization
> [AZURE.NOTE]
-->
<!-- keep by customization: begin -->
There are two ways to map your custom domain to a CDN endpoint. 

1. **Create a CNAME record with your domain registrar and map your custom domain and subdomain to the CDN endpoint** 
	
	A CNAME record is a DNS feature that maps a source domain to a destination domain. In this case, the source domain is your custom domain and subdomain (subdomain is always required). The destination domain is your CDN endpoint.  

	The process of mapping your custom domain to your CDN endpoint can, however, result in a brief period of downtime for the domain while you are registering the domain in the Azure Management Portal. 
2. **Add an intermediate registration step with Azure cdnverify**

	If your custom domain is currently supporting an application with a service-level agreement (SLA) that requires that there be no downtime, then you can use the Azure **cdnverify** subdomain to provide an intermediate registration step so that users will be able to access your domain while the DNS mapping takes place.  

> AZURE.NOTE   
> 
<!-- keep by customization: end -->
-	You must create a CNAME record with your domain registrar to map your domain to the CDN endpoint. CNAME records map specific subdomains such as www.mydomain.com or myblog.mydomain.com. It is not possible to map a CNAME record to a root domain, such as mydomain.com.
-	A subdomain can only be associated with one CDN endpoint. The CNAME record that you create will route all traffic addressed to the subdomain to the specified endpoint. <!-- deleted by customization  For example, if --><!-- keep by customization: begin --> E.g. If <!-- keep by customization: end --> you associate www.mydomain.com with your CDN endpoint, then you cannot associate it with other Azure endpoints, such as a storage account endpoint or a cloud service endpoint. However, you can use different subdomains from the same domain for different service endpoints. You can also map different subdomains to the same CDN endpoint.

The procedures in this topic will show you how to:    

-	[Register a custom domain for an Azure CDN endpoint](#subheading1)
<!-- keep by customization: begin -->
-	[Register a custom domain for an Azure CDN endpoint using the intermediary cdnverify subdomain](#subheading2)
<!-- keep by customization: end -->
-	[Verify that the custom subdomain references your CDN endpoint](#subheading3) 

##<a name="subheading1"></a>Register a custom domain for an Azure CDN endpoint

<!-- deleted by customization
1.	Log into the [Azure Management Portal](http://manage.windowsazure.cn/).
2.	Click **Browse**, then **CDN Profiles**, then the CDN profile with the endpoint you want to map to a custom domain.  
3.	In the **CDN Profile** blade, click the CDN endpoint with which you want to associate the subdomain.
4.	At the top of the endpoint blade, click the **Add Custom Domain** button.  In the **Add a custom domain** blade, you'll see the endpoint host name, derived from your CDN endpoint, to use in creating a new CNAME record. The format of the host name address will appear as **&lt;EndpointName>.azureedge.net**.  You can copy this host name to use in creating the CNAME record.  

-->
<!-- keep by customization: begin -->
1.	Log into the [Azure Management Portal](http://manage.windowsazure.cn).
2.	In the navigation pane, click **CDN**.
3.	From the list view, click the name of the CDN endpoint with which you want to associate the subdomain, to navigate to the detail page for that endpoint.
4.	On the ribbon, click **Manage Domains** to display the **Manage custom domains** dialog box. In the text of the dialog box, you'll see the host name, derived from your CDN endpoint, to use in creating a new CNAME record. The format of the host name address will appear as **az#####.vo.msecnd.net** (where **az#####** is the identifier for your CDN endpoint). You can copy this host name to use in creating the CNAME record.  
For this procedure, ignore the text that refers to the **cdnverify** subdomain.
<!-- keep by customization: end -->
5.	Navigate to your domain registrar's web site, and locate the section for creating DNS records. You might find this in a section such as **Domain Name**, **DNS**, or **Name Server Management**.
6.	Find the section for managing CNAMEs. You may have to go to an advanced settings page and look for the words CNAME, Alias, or Subdomains.
7.	Create a new CNAME record that maps your chosen subdomain (for example, **www** or **cdn**) to the host name provided in the <!-- deleted by customization **Add a --><!-- keep by customization: begin --> **Manage <!-- keep by customization: end --> custom <!-- deleted by customization domain** blade --><!-- keep by customization: begin --> domains** dialog <!-- keep by customization: end -->.
8.	Return to the <!-- deleted by customization **Add a --><!-- keep by customization: begin --> **Manage <!-- keep by customization: end --> custom <!-- deleted by customization domain** blade --><!-- keep by customization: begin --> domains** dialog <!-- keep by customization: end -->, and enter your custom domain, including the subdomain, in the dialog box. For example, enter the domain name in the format www.mydomain.com or cdn.mydomain.com.

	Azure will verify that the CNAME record exists for the domain name you have entered. If the CNAME is correct, your custom domain is validated and ready to use with your CDN content.  

	Note that in some cases it can take time for the CNAME record to propagate to name servers on the Internet. If your domain is not validated immediately, and you believe the CNAME record is correct, then wait a few minutes and try again.
<!-- keep by customization: begin -->

##<a name="subheading2"></a>Register a custom domain for an Azure CDN endpoint using the intermediary cdnverify subdomain  


1.	Log into the [Azure Management Portal](http://manage.windowsazure.cn/).
2.	In the navigation pane, click **CDN**.
3.	From the list view, click the name of the CDN endpoint with which you want to associate the subdomain, to navigate to the detail page for that endpoint.
4.	On the ribbon, click **Manage Domains** to display the **Manage custom domains** dialog box. In the text of the dialog box, you'll see the host name, derived from your CDN endpoint, to use in creating a new CNAME record using the **cdnverify** intermediary subdomain. The format of the host name address will appear as **cdnverify.az#####.vo.msecnd.net**. You can copy this host name to use in creating the CNAME record.
5.	Navigate to your domain registrar's web site, and locate the section for creating DNS records. You might find this in a section such as **Domain Name**, **DNS**, or **Name Server Management**.
6.	Find the section for managing CNAMEs. You may have to go to an advanced settings page and look for the words **CNAME**, **Alias**, or **Subdomains**.
7.	Create a new CNAME record, and provide a subdomain alias that includes the **cdnverify** subdomain. For example, the subdomain that you specify will be in the format **cdnverify.www** or **cdnverify.cdn**. Then provide the host name, which is your CDN endpoint, in the format **cdnverify.az#####.vo.msecnd.net** (where **az#####** is the identifier for your CDN endpoint). The format of the host name is provided for you in the **Manage custom domains** dialog.
8.	Return to the **Manage custom domains** dialog, and enter your custom domain, including the subdomain, in the dialog box. For example, enter the domain name in the format **www.mydomain.com** or **cdn.mydomain.com**. Note that in this step, you do not need to preface the subdomain with **cdnverify**.  

	Azure will verify that the CNAME record exists for the cdnverify domain name you have entered.
9.	At this point, your custom domain has been verified by Azure, but traffic to your domain is not yet being routed to your CDN endpoint. To complete the process, return to your DNS registrar's web site, and create another CNAME record that maps your subdomain to your CDN endpoint. For example, specify the subdomain as **www** or **cdn**, and the hostname as **az#####.vo.msecnd.net**. With this step, the registration of your custom domain is complete. 
10.	Finally, you can delete the CNAME record you created using **cdnverify**, as it was necessary only as an intermediary step.  

<!-- keep by customization: end -->

##<a name="subheading3"></a>Verify that the custom subdomain references your CDN endpoint

-	After you have completed the registration of your custom domain, you can access content that is cached at your CDN endpoint using the custom domain.
First, ensure that you have public content that is cached at the endpoint. For example, if your CDN endpoint is associated with a storage account, the CDN caches content in public blob containers. To test the custom domain, ensure that your container is set to allow public access and that it contains at least one blob.
-	In your browser, navigate to the address of the blob using the custom domain. For example, if your custom domain is **www.mydomain.com**, the URL to a cached blob will be similar to the following URL:  
	
		http://www.mydomain.com/mypubliccontainer/acachedblob.jpg
-	If your CDN endpoint is associated with a cloud service, then the address of your cached content will be similar to the following URL:

<!-- deleted by customization
		http://www.mydomain.com/mycloudservice
-->
<!-- keep by customization: begin -->
		http://www.mydomain.com/cdn/mycloudservice
<!-- keep by customization: end -->

##See Also


[How to Enable the Content Delivery Network (CDN)  for <!-- deleted by customization Azure](./cdn-create-new-endpoint.md --><!-- keep by customization: begin --> Azure](/documentation/articles/cdn-create-new-endpoint) <!-- keep by customization: end -->
<!-- deleted by customization
)  
-->

 