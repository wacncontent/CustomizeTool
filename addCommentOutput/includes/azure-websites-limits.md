<!-- deleted by customization
Resource|Free|Shared (Preview)|Basic|Standard|Premium (Preview)</th>
---|---|---|---|---|---
[Web, mobile, or API apps](/home/features/app-service/) per [App Service plan](/documentation/articles/web-sites-web-hosting-plan-overview)<sup>1</sup>|10|100|Unlimited<sup>2</sup>|Unlimited<sup>2</sup>|Unlimited<sup>2</sup>
[Logic apps](/home/features/app-service/) per [App Service plan](/documentation/articles/web-sites-web-hosting-plan-overview)</a><sup>1</sup>|10|10|10|20 per core|20 per core 
[App Service plan](/documentation/articles/web-sites-web-hosting-plan-overview)|1 per region|10 per resource group|10 per resource group|10 per resource group|10 per resource group
Compute instance type|Shared|Shared|Dedicated<sup>3</sup>|Dedicated<sup>3</sup>|Dedicated<sup>3</sup></p>
[Scale-Out](/documentation/articles/web-sites-scale) (max instances)|1 shared|1 shared|3 dedicated<sup>3</sup>|10 dedicated<sup>3</sup>|50 dedicated<sup>3,4</sup>
Storage<sup>5</sup>|1 GB<sup>5</sup>|1 GB<sup>5</sup>|10 GB<sup>5</sup>|50 GB<sup>5</sup>|500 GB<sup>4,5</sup></p>
CPU time (day)<sup>6</sup>|60 minutes|240 minutes|Unlimited, pay at standard [rates](/documentation/articles/app-service)</a>|Unlimited, pay at standard rates|Unlimited, pay at standard rates
Memory (1 hour)|1024 MB per App Service plan|1024 MB per app|N/A|N/A|N/A
Bandwidth|165 MB|Unlimited, [data transfer rates](/documentation/articles/data-transfers) apply|Unlimited, data transfer rates apply|Unlimited, data transfer rates apply|Unlimited, data transfer rates apply
Application architecture|32-bit|32-bit|32-bit/64-bit|32-bit/64-bit|32-bit/64-bit
Web Sockets per instance<sup>7</sup>|5|35|350|Unlimited|Unlimited
Concurrent [debugger connections](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio) per application|1|1|1|5|5
[chinacloudsites.cn subdomain with FTP/S and SSL](/documentation/articles/web-sites-configure-ssl-certificate)|X|X|X|X|X
[Custom domain](/documentation/articles/web-sites-custom-domain-name) support||X|X|X|X
Custom domain [SSL support](/documentation/articles/web-sites-configure-ssl-certificate)|||Unlimited|Unlimited, 5 SNI SSL and 1 IP SSL connections included|Unlimited, 5 SNI SSL and 1 IP SSL connections included
Integrated Load Balancer||X|X|X|X
[Always On](/documentation/articles/web-sites-configure)|||X|X|X
[Scheduled Backups](/documentation/articles/web-sites-backup)||||Once per day|Once every 5 minutes<sup>8</sup>
[Auto Scale](/documentation/articles/web-sites-scale)|||X|X|X
[WebJobs](/documentation/articles/web-sites-create-web-jobs)<sup>9</sup>|X|X|X|X|X
[Azure Scheduler](/home/features/scheduler/) support||X|X|X|X
[Endpoint monitoring](/documentation/articles/web-sites-monitor)|||X|X|X
[Staging Slots (Preview)](/documentation/articles/web-sites-staged-publishing)||||5|20
Custom domains per app</a>||500|500|500|500
SLA||<p>|99.9%|99.95%<sup>10</sup>|99.95%<sup>10</sup>

<sup>1</sup>Apps and storage quotas are per App Service plan unless noted otherwise.  
<sup>2</sup>The actual number of apps that you can host on these machines depends on the activity of the apps, the size of the machine instances, and the corresponding resource utilization.  
<sup>3</sup>Dedicated instances can be of different sizes. See [Azure Websites Pricing](/home/features/app-service/#price) for more details. Additional instances are available by opening a support request.  
<sup>4</sup>Premium tier allows up to 50 computes instances (subject to availability) and 500 GB of disk space when using Azure Websites Environments, and 20 compute instances and 250 GB storage otherwise.  
<sup>5</sup>The storage limit is the total content size across all apps in the 
same App Service plan. Storage limits can be increased by opening a support request.  
<sup>6</sup>These resources are constrained by physical resources on the dedicated instances (the instance size and the number of instances).  
<sup>7</sup>If you scale an app in the Basic tier to two instances, you have 350 concurrent connections for each of the two instances.  
<sup>8</sup>Premium tier allows backup intervals down up to every 5 minutes when using Azure Websites Environments, and 50 times per day otherwise.  
<sup>9</sup>Run custom executables and/or scripts on demand, on a schedule, or continuously as a background task within your Azure Websites instance. Always On is required for continuous WebJobs execution. Azure Scheduler Free or Standard is required for scheduled WebJobs.  
<sup>10</sup>SLA of 99.95% provided for deployments that use multiple instances with Azure Traffic Manager configured for failover.  

-->
<!-- keep by customization: begin -->
<table cellspacing="0" border="1">
<tr>
   <th align="left" valign="middle">Resource</th>
   <th align="left" valign="middle">Free</th>
   <th align="left" valign="middle">Shared (Preview)</th>
   <th align="left" valign="middle">Basic</th>
   <th align="left" valign="middle">Standard</th>
</tr>
<tr>
   <td valign="middle"><p><a href="/documentation/services/web-sites/">Websites</a><sup>1</sup> per <a href="/documentation/articles/web-sites-web-hosting-plan-overview/">Web Hosting Plan</a></p></td>
   <td valign="middle"><p>10</p></td>
   <td valign="middle"><p>100</p></td>
   <td valign="middle"><p>500<sup>2</sup></p></td>
   <td valign="middle"><p>500<sup>2</sup></p></td>
</tr>
<tr>
   <td valign="middle"><p>Web Hosting Plan</a><sup>3</sup></p></td>
   <td valign="middle"><p>1 per region</p></td>
   <td valign="middle"><p>up to 10</p></td>
   <td valign="middle"><p>up to 10</p></td>
   <td valign="middle"><p>up to 10<sup>3</sup></p></td>
</tr>
<tr>
   <td valign="middle"><p>Compute instance type<sup>4</sup></p></td>
   <td valign="middle"><p>Shared</p></td>
   <td valign="middle"><p>Shared</p></td>
   <td valign="middle"><p>Dedicated</p></td>
   <td valign="middle"><p>Dedicated</p></td>
</tr>
<tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-scale/">Scale-Out</a> (max instances)</p></td>
   <td valign="middle"><p>1 shared</p></td>
   <td valign="middle"><p>1 shared</p></td>
   <td valign="middle"><p>3 dedicated</p></td>
   <td valign="middle"><p>10 dedicated<sup>4</sup></p></td>
</tr>
<tr>
   <td valign="middle"><p>Storage<sup>5</sup></p></td>
   <td valign="middle"><p>1 GB</p></td>
   <td valign="middle"><p>1 GB</p></td>
   <td valign="middle"><p>10 GB</p></td>
   <td valign="middle"><p>50 GB<sup>5</sup></p></td>
</tr>
<tr>
   <td valign="middle"><p>CPU time (day)<sup>6</sup></p></td>
   <td valign="middle"><p>60 minutes</p></td>
   <td valign="middle"><p>240 minutes</p></td>
   <td valign="middle"><p>Unlimited, pay at standard rates</p></td>
   <td valign="middle"><p>Unlimited, pay at standard rates</p></td>
</tr>
<tr>
   <td valign="middle"><p>Memory (1 hour)<sup>7</sup></p></td>
   <td valign="middle"><p>1024 MB<sup>7</sup></p></td>
   <td valign="middle"><p>1024 MB</p></td>
   <td valign="middle"><p>N/A</p></td>
   <td valign="middle"><p>N/A</p></td>
</tr>
<tr>
   <td valign="middle"><p>Bandwidth</p></td>
   <td valign="middle"><p>165 MB</p></td>
   <td valign="middle"><p>Unlimited, pay at standard rates</p></td>
   <td valign="middle"><p>Unlimited, pay at standard rates</p></td>
   <td valign="middle"><p>Unlimited, pay at standard rates</p></td>
</tr><tr>
   <td valign="middle"><p>Application architecture</p></td>
   <td valign="middle"><p>32-bit</p></td>
   <td valign="middle"><p>32-bit</p></td>
   <td valign="middle"><p>32-bit/64-bit</p></td>
   <td valign="middle"><p>32-bit/64-bit</p></td>
</tr>
<tr>
   <td valign="middle"><p>Web Sockets<sup>8</sup></p></td>
   <td valign="middle"><p>5</p></td>
   <td valign="middle"><p>35</p></td>
   <td valign="middle"><p>350</p></td>
   <td valign="middle"><p>Unlimited</p></td>
</tr><tr>
   <td valign="middle"><p>Concurrent <a href="/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio/">debugger connections</a> per application</p></td>
   <td valign="middle"><p>1</p></td>
   <td valign="middle"><p>1</p></td>
   <td valign="middle"><p>1</p></td>
   <td valign="middle"><p>5</p></td>
</tr><tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-configure-ssl-certificate/">chinacloudsites.cn subdomain with FTP/S and SSL</a></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
</tr><tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-custom-domain-name/">Custom domain</a> support</p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
</tr><tr>
   <td valign="middle"><p>Custom domain <a href="/documentation/articles/web-sites-configure-ssl-certificate/">SSL support</a><sup>9</sup></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>5 SNI SSL and 1 IP SSL Connections included</p></td>
</tr><tr>
   <td valign="middle"><p>Integrated Load Balancer</p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
</tr><tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-configure/">Always On</a></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
</tr>
<tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-backup/">Backups</a></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>X</p></td>
</tr><tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-scale/">Auto Scale</a></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
</tr><tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-create-web-jobs/">WebJobs</a><sup>10</sup></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
</tr>
<tr>
   <td valign="middle"><p><a href="http://azure.microsoft.com/services/scheduler/">Azure Scheduler</a> support</p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
</tr><tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-monitor/">Endpoint monitoring</a></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>X</p></td>
   <td valign="middle"><p>X</p></td>
</tr>
<tr>
   <td valign="middle"><p><a href="/documentation/articles/web-sites-staged-publishing/">Staging Slots (Preview)</a></p></td>
   <td valign="middle"><p>0</p></td>
   <td valign="middle"><p>0</p></td>
   <td valign="middle"><p>1</p></td>
   <td valign="middle"><p>5</p></td>
</tr>
<tr>
   <td valign="middle"><p>SLA</p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p></p></td>
   <td valign="middle"><p>99.9%</p></td>
   <td valign="middle"><p>99.9%</p></td>
</tr>
</table>

<sup>1</sup>Web Sites and Storage quotas are per web hosting plan unless noted otherwise.

<sup>2</sup>Basic and Standard sites run on dedicated machines. The actual number of sites that you can host on these machines depends on the activity of the sites, the size of the machine instances, and the corresponding resource utilization.

<sup>3</sup>With the exception of the Free tier, the limits on Web Hosting Plans are per resource group. For more information on creating and managing resource groups, see [Using Resource groups to manage your Azure resources][useresourcegroups]. Note that at the Standard tier, additional Web Hosting Plans are available at request.

<sup>4</sup>Dedicated instances can be Small, Medium, or Large. See the [Azure Web Sites Pricing Page][websitespricing] for more details. Additional instances are available by opening a support request.

<sup>5</sup>All Web Sites share the same storage resources for site content. Therefore, the storage limit is the total size across all sites rather than per web site. Storage limits can be increased by opening a support request.

<sup>6</sup>Although the Basic and Standard tiers do not have a quota for CPU or memory, these resources are constrained by physical resources on the dedicated instances (the instance size and the number of instances).

<sup>7</sup>The memory limit for the Free tier is shared across all free sites in the web hosting plan. The memory limit for the Shared tier is per site.

<sup>8</sup>This value represents concurrent web socket connections per web site instance. For example, if you scaled a Basic web site out to two instances, you would effectively have 700 concurrent connections (350 x 2).

<sup>9</sup>For the Basic tier, standard [SSL pricing applies][sslpricing].

<sup>10</sup>Run custom executables and/or scripts on demand, on a schedule, or continuously as a background task within your Web Sites instance. Always On is required for continuous WebJobs execution. Azure Scheduler Free or Standard is required for scheduled WebJobs.

  [useresourcegroups]: /documentation/articles/azure-preview-portal-using-resource-groups/
  [websitespricing]: http://azure.microsoft.com/home/features/web-site/#price
  [sslpricing]: http://azure.microsoft.com/home/features/web-site/#price
<!-- keep by customization: end -->