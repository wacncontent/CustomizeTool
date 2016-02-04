deletion:

deleted:

		South

reason: (region diff)

deleted:

		, South

reason: (region diff)

deleted:

		East 2, China

reason: (region diff)

deleted:

		, China North, China East,

reason: (region diff)

deleted:

		China North, West Europe, China East, China North,
		                                                                Japan East, China East
		
		For PowerShell 1.0 Preview, use **Get-AzureRmResourceProvider** to get supported locations.
		
		    PS C:\> Get-AzureRmResourceProvider -ProviderNamespace Microsoft.Web
		
		    ProviderNamespace RegistrationState ResourceTypes               Locations
		    ----------------- ----------------- -------------               ---------
		    Microsoft.Web     Registered        {sites/extensions}          {Brazil South, ...
		    Microsoft.Web     Registered        {sites/slots/extensions}    {Brazil South, ...
		    Microsoft.Web     Registered        {sites/instances}           {Brazil South, ...
		    ...
		
		You can specify a particular type of resource with:
		
		    PS C:\> ((Get-AzureRmResourceProvider -ProviderNamespace Microsoft.Web).ResourceTypes | Where-Object ResourceTypeName -eq sites).Locations
		
		    Brazil South
		    China East
		    China East
		    Japan East
		    China East
		    China North
		    China North
		    China East
		    West Europe
		    China North
		    China North

reason: (region diff)

deleted:

		"China East",
		            "China North",
		            "West Europe",

reason: (region diff)

deleted:

		"China East",
		                "China North",
		                "China North",
		                "West Europe",

reason: (region diff)

replacement:

deleted:

		East, China East..

replaced by:

		North..

reason: (region diff)

deleted:

		East, China East,..

replaced by:

		North,..

reason: (region diff)

deleted:

		Microsoft.ApiManagement/service         {China North, China East, China East 2, Nor... China North, China East, China East 2, Nort...
		    Microsoft.AppService/apiapps            {China East, China North, China East,... China East, China North, China East, ...

replaced by:

		Microsoft.ApiManagement/service         {China East, China North... China East China North,...
		    Microsoft.AppService/apiapps            {China East, China North... China East China North,...

reason: (region diff)

deleted:

		"location": "China East,China East 2,China North,China North,China East,China North,West Europe,China East,China North,Japan East,China East"

replaced by:

		"location": "China East,China North"

reason: (region diff)

