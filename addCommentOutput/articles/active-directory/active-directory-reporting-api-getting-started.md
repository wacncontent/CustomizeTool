<properties
   pageTitle="Getting started with the Azure AD Reporting API"
   description="How to get started with the Azure Active Directory Reporting API"
   services="active-directory"
   documentationCenter=""
   authors="kenhoff"
   manager="mbaldwin"
   editor=""/>

<tags
	ms.service="active-directory"
	ms.date="12/07/2015"
	wacn.date=""/>


# Getting started with the Azure AD Reporting API

<!-- deleted by customization
*This documentation is part of the [Azure Active Directory Reporting Guide](/documentation/articles/active-directory-reporting-guide).*

Azure Active Directory provides a variety of activity, security and audit reports. This data can be consumed through the Azure Management Portal, but can also be very useful in a many other applications, such as SIEM systems, audit, and business intelligence tools.

The Azure AD Reporting APIs provide programmatic access to these data through a set of REST-based APIs that can be called from a variety programming languages and tools.

This article will walk you through the process of calling the Azure AD Reporting APIs using PowerShell. You can modify the sample PowerShell script to access data from any of the available reports in JSON, XML or text format, as your scenario requires.

To use this sample, you will need an [Azure Active Directory](/documentation/articles/active-directory-whatis)
-->
<!-- keep by customization: begin -->
Azure AD includes a Reporting API that allows you to access your security, activity, and audit reports programmatically. It's a REST-based API, which allows you to query data for use in external reporting or compliance situations.

This article will walk you through the necessary steps in order to make your first authenticated HTTP request to the Azure AD Reporting API. 

You will need:

- An [Azure Active Directory](/documentation/articles/active-directory-whatis)
- A way to make HTTP GET and POST requests; either:
	- a bash shell with [curl](http://curl.haxx.se/)
	- [Postman](https://www.getpostman.com/)
	- [A PowerShell cmdlet that makes HTTP requests](https://technet.microsoft.com/zh-cn/library/hh849901.aspx)


<!-- keep by customization: end -->

## Creating an Azure AD application to access the API

<!-- deleted by customization
The Reporting API uses [OAuth](https://msdn.microsoft.com/zh-cn/library/azure/dn645545.aspx) to authorize access to the web APIs. To access information from your directory, you must create an application in your Active Directory, and grant it appropriate permissions to access the AAD data.
-->
<!-- keep by customization: begin -->
In order to authenticate to the Reporting API, we must use the OAuth flow, which requires us to register an application with Azure AD.

<!-- keep by customization: end -->


### Create an application
- Navigate to the [Azure Management Portal](https://manage.windowsazure.cn/) <!-- deleted by customization. -->
- Navigate into your directory <!-- deleted by customization. -->
- Navigate into applications <!-- deleted by customization. -->
- On the bottom bar, click "Add".
	- Click "Add an application my organization is developing".
	- **Name**: Any name is fine. Something like "Reporting API Application" is recommended.
<!-- deleted by customization
	- **Type**: Select "web site and/or Web API".
	- Click the arrow to move to the next page <!-- deleted by customization. -->
	- **Sign-on URL**: ```http://localhost``` <!-- deleted by customization. -->
	- **App ID URI**: ```http://localhost``` <!-- deleted by customization. -->
-->
<!-- keep by customization: begin -->
	- **Type**: Select "Web Site and/or Web API"
	- Click the arrow to move to the next page <!-- deleted by customization. -->
	- **Sign-on URL**: ```http://localhost``` <!-- deleted by customization. -->
	- **App ID URI**: ```http://localhost``` <!-- deleted by customization. -->
<!-- keep by customization: end -->
	- Click the checkmark to finish adding the application.

### <!-- deleted by customization Grant --><!-- keep by customization: begin --> Give <!-- keep by customization: end --> your application permission to use the API
- Navigate to the Applications tab.
- Navigate to your newly created application.
<!-- deleted by customization
- Click the **Configure** tab.
-->
<!-- keep by customization: begin -->
- Navigate to the Configure tab.
<!-- keep by customization: end -->
- In the "Permissions to Other Applications" section:
<!-- deleted by customization
	- In the microsoft Azure Active Directory > Application Permissions, select **Read directory data**.
- Click **Save** on the bottom bar.
-->
<!-- keep by customization: begin -->
	- Add Windows Azure Active Directory > Application Permissions > enable "Read directory data"
	- Add Windows Azure Service Managment API > Delegated Permissions > enable "Access Azure Service Management"
- Click "Save" on the bottom bar.
<!-- keep by customization: end -->


### Get your directory ID, client ID, and client secret

<!-- deleted by customization
The steps below will walk you through obtaining your application's client ID and client secret.  You will also need to know your tenant name, it can be either your *.partner.onmschina.cn or a custom domain name.  Copy these into a separate place; you'll use them to modify the script.
-->
<!-- keep by customization: begin -->
Find your application's client ID, client secret, and your directory ID. Copy these IDs and URLs into a separate place; you'll use them in the next steps.
<!-- keep by customization: end -->

#### Application Client ID
- Navigate to the Applications tab.
- Navigate to your newly created application.
<!-- deleted by customization
- Navigate to the **Configure** tab.
- Your application's client ID is listed on the **Client ID** field.
-->
<!-- keep by customization: begin -->
- Navigate to the Configure tab.
- Your application's client ID is listed on the Client ID field.
<!-- keep by customization: end -->

#### Application client secret
- Navigate to the Applications tab.
- Navigate to your newly created application.
- Navigate to the Configure tab.
- Generate a new secret key for your application by selecting a duration in the "Keys" section.
- The key will be displayed upon saving. Make sure to copy it <!-- deleted by customization and paste it into a safe location -->, because there is no way to retrieve it later.

<!-- deleted by customization

## Modify the script
Edit one of the scripts below to work with your directory by replacing $ClientID, $ClientSecret and $tenantdomain with the correct values from âDelegating Access in Azure ADâ.

### PowerShell Script

    # This script will require the web site and permissions setup in Azure Active Directory
    $ClientID	  	= "your-application-client-id-here"				# Should be a ~35 character string insert your info here
    $ClientSecret  	= "your-application-client-secret-here"			# Should be a ~44 character string insert your info here
    $loginURL		= "https://login.chinacloudapi.cn"
    $tenantdomain	= "your-directory-name-here.partner.onmschina.cn"			# For example, contoso.partner.onmschina.cn

    # Get an Oauth 2 access token based on client id, secret and tenant domain
    $body		= @{grant_type="client_credentials";resource=$resource;client_id=$ClientID;client_secret=$ClientSecret}
    $oauth		= Invoke-RestMethod -Method Post -Uri $loginURL/$tenantdomain/oauth2/token?api-version=1.0 -Body $body

    $7daysago = "{0:s}" -f (get-date).AddDays(-7) + "Z"
    # or, AddMinutes(-5)

    Write-Output $7daysago

    if ($oauth.access_token -ne $null) {
    	$headerParams = @{'Authorization'="$($oauth.token_type) $($oauth.access_token)"}

        $url = "https://graph.chinacloudapi.cn/$tenantdomain/reports/auditEvents?api-version=beta&`$filter=eventTime gt $7daysago"

    	$myReport = (Invoke-WebRequest -UseBasicParsing -Headers $headerParams -Uri $url)
    	foreach ($event in ($myReport.Content | ConvertFrom-Json).value) {
    		Write-Output ($event | ConvertTo-Json)
    	}
        $myReport.Content | Out-File -FilePath auditEvents.json -Force
    } else {
    	Write-Host "ERROR: No Access Token"
    }

### Bash Script

    #!/bin/bash

    # Author: Ken Hoff (kenhoff@microsoft.com)
    # Date: 2015.08.20
    # NOTE: This script requires jq (https://stedolan.github.io/jq/)

    CLIENT_ID="your-application-client-id-here"         # Should be a ~35 character string insert your info here
    CLIENT_SECRET="your-application-client-secret-here" # Should be a ~44 character string insert your info here
    LOGIN_URL="https://login.chinacloudapi.cn"
    TENANT_DOMAIN="your-directory-name-here.partner.onmschina.cn"    # For example, contoso.partner.onmschina.cn

    TOKEN_INFO=$(curl -s --data-urlencode "grant_type=client_credentials" --data-urlencode "client_id=$CLIENT_ID" --data-urlencode "client_secret=$CLIENT_SECRET" "$LOGIN_URL/$TENANT_DOMAIN/oauth2/token?api-version=1.0")

    TOKEN_TYPE=$(echo $TOKEN_INFO | ./jq-win64.exe -r '.token_type')
    ACCESS_TOKEN=$(echo $TOKEN_INFO | ./jq-win64.exe -r '.access_token')

    # get yesterday's date

    YESTERDAY=$(date --date='1 day ago' +'%Y-%m-%d')

    URL="https://graph.chinacloudapi.cn/$TENANT_DOMAIN/reports/auditEvents?api-version=beta&\$filter=eventTime%20gt%20$YESTERDAY"


    REPORT=$(curl -s --header "Authorization: $TOKEN_TYPE $ACCESS_TOKEN" $URL)

    echo $REPORT | ./jq-win64.exe -r '.value' | ./jq-win64.exe -r ".[]"





## Execute the script
Once you finish editing the script, run it and verify that the expected data from the AuditEvents report is returned.

The script returns lists all the available reports, and returns output from the AccountProvisioningEvents report in the PowerShell window in JSON format. It also creates files with the same output in JSON, text and XML. You can comment experiment with modifying the script to return data from other reports, and comment out the output formats that you do not need.

## Notes

- There is no limit on the number of events returned by the Azure AD Reporting API (using OData pagination).
	- For retention limits on reporting data, check out [Reporting Retention Policies](/documentation/articles/active-directory-reporting-retention).
-->
<!-- keep by customization: begin -->
#### Directory ID
- While signed into the Azure Management Portal, you can find your directory ID in the URL.
- Example URL: ```https://manage.windowsazure.cn/@demo.partner.onmschina.cn#Workspaces/ActiveDirectoryExtension/Directory/<<YOUR-AZURE-AD-DIRECTORY-ID>>/apps...```

Copy these IDs and URLs into a separate place; you'll use them in later steps.



## Retrieving an OAuth access token from Azure AD

Next, we need to generate an authorization code, which we will use to retrieve an OAuth access token for our request to the Reporting API.



### Get an authorization code

First, you need an authorization code. You can retrieve this by navigating to a specific URL in your browser, signing in as a global administrator in your directory, and retrieving the authorization code from the URL you were redirected to.

- Substitute this URL with your Azure AD Directory ID and your Application Client ID.
	- ```https://login.chinacloudapi.cn/<<INSERT-YOUR-AZURE-AD-DIRECTORY-ID-HERE>>/oauth2/authorize?client_id=<<INSERT-YOUR-APPLICATION-CLIENT-ID-HERE>>&response_type=code```
- After filling in the fields, open a browser window and navigate to the URL. Your browser will be redirected to a URL which contains your access code; there won't be any page content. This is OK. 

- If prompted, sign in as a global administrator in your directory.
	- If you run into issues, you may need to sign out of the Azure Management Portal or Office Portal and try again.
- Inspect the URL for the redirected page. The URL contains your authorization code.
	- ```http://localhost/?code=<<YOUR-AUTHORIZATION-CODE>>&session_state=<<YOUR-SESSION-STATE>>``` 
- Copy ```YOUR-AUTHORIZATION-CODE``` into a separate place; you'll use it in the next step.



### Get an OAuth access token

Next, you'll retrieve your access token by making an HTTP request to an OAuth endpoint using your authorization token. For this example, we'll use a small unix library called [curl](http://curl.haxx.se/); you can also use [Postman](https://www.getpostman.com/) or a [PowerShell cmdlet that can make HTTP requests](https://technet.microsoft.com/zh-cn/library/hh849901.aspx).

- First, replace ```YOUR-AZURE-AD-DIRECTORY-ID``` with the directory ID you retrieved in a previous step. Then, replace ```YOUR-CLIENT-ID``` with the client ID you retrieved in the previous step. Then, replace ```YOUR-CLIENT-SECRET``` with the client secret you retrieved in the previous step. Finally, replace ```YOUR-AUTHORIZATION-CODE``` with the authorization code you retrieved in the previous step.

```
curl -X POST https://login.chinacloudapi.cn/<<INSERT-YOUR-AZURE-AD-DIRECTORY-ID-HERE>>/oauth2/token  \
	-F redirect_uri=http://localhost
	-F grant_type=authorization_code 
	-F resource=https://management.core.chinacloudapi.cn/
	-F client_id=<<INSERT-YOUR-CLIENT-ID-HERE>>
	-F code=<<INSERT-YOUR-AUTHORIZATION-CODE-HERE>>
	-F client_secret=<<INSERT-YOUR-CLIENT-SECRET-HERE>>
```

- Run the command or make the request using your method of choice.
- You'll recieve a JSON object which includes your access token.

```
{
  "token_type": "Bearer",
  "expires_in": "3600",
  "expires_on": "1428701563",
  "not_before": "1428697663",
  "resource": "https://management.core.chinacloudapi.cn/",
  "access_token": "<<YOUR-ACCESS-TOKEN>>",
  "refresh_token": "AAABA...WjCAA",
  "scope": "user_impersonation",
  "id_token": "eyJ0e...20ifQ."
}
```

- Copy your access token from the JSON object into a separate location; we'll use it to call the Reporting API.



## Make a request to the Reporting API

- Finally, replace ```YOUR-ACCESS-TOKEN``` with your access token in the curl request below.

```
curl -v https://graph.chinacloudapi.cn/<<INSERT-YOUR-DIRECTORY-ID-HERE>>/reports/$metadata?api-version=beta
  -H "x-ms-version: 2013-08-01"
  -H "Authorization: Bearer <<INSERT-YOUR-ACCESS-TOKEN-HERE>>"
```

- Run the command or make the request using your method of choice.
- You'll recieve an OData object containing the contents of your audit report.

```
{
  "@odata.context":"https://graph.chinacloudapi.cn/<<DIRECTORY-ID>>/reports/?api-version=beta/reports/$metadata#auditEvents",
  "value":[
    {
      "id":"SN2GR1RDS104.GRN001.msoprd.msft.net_4515449","timeStampOffset":"2015-04-13T21:27:55.1777659Z","actor":"thekenhoff_outlook.com#EXT#@kenhoffdemo.partner.onmschina.cn","action":"Add service principal","target":"04670e0d84264acb86dac2
ff1a94c9d7","actorDetail":"Other=284c417b-805e-493a-ad8e-328ce8d4b18e; UPN=thekenhoff_outlook.com#EXT#@kenhoffdemo.partner.onmschina.cn; PUID=1003BFFD8CD09753","targetDetail":"SPN=04670e0d84264acb86dac2ff1a94c9d7","tenantId":"c9b13f49-3c25-43
c0-a84f-57faf131dc2b"
    }
  ]
}
```

- Congratulations!
<!-- keep by customization: end -->


## Next Steps
- Curious about what security, audit, and activity reports are available? Check out [Azure AD Security, Audit, and Activity Reports](/documentation/articles/active-directory-view-access-usage-reports)
- See [Azure AD Audit Report Events](/documentation/articles/active-directory-reporting-audit-events) for more details on the Audit Report
- See [Azure AD Reports and Events (Preview)](https://msdn.microsoft.com/zh-cn/library/azure/mt126081.aspx) for more details on the Graph API REST service
<!-- keep by customization: begin -->
- For more information on the OAuth flow with Azure AD using curl: [Windows Azure REST API + OAuth 2.0](https://ahmetalpbalkan.com/blog/azure-rest-api-with-oauth2/) (external link)
<!-- keep by customization: end -->
