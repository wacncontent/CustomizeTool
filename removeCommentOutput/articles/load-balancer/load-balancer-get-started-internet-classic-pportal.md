<properties 
   pageTitle="Get started creating Internet facing load balancer in classic deployment model using the preview portal | Windows Azure"
   description="Learn how to create an Internet facing load balancer in classic deployment model using the preview portal"
   services="load-balancer"
   documentationCenter="na"
   authors="joaoma"
   manager="carolz"
   editor=""
   tags="azure-service-management"
/>
<tags
	ms.service="load-balancer"
	ms.date="11/03/2015"
	wacn.date=""/>

#Get started creating Internet facing load balancer (classic) in the preview portal

[AZURE.INCLUDE [load-balancer-get-started-internet-classic-selectors-include.md](../includes/load-balancer-get-started-internet-classic-selectors-include.md)]

[AZURE.INCLUDE [load-balancer-get-started-internet-intro-include.md](../includes/load-balancer-get-started-internet-intro-include.md)]

[AZURE.INCLUDE [azure-arm-classic-important-include](../includes/azure-arm-classic-important-include.md)] This article covers the classic deployment model.
 You can also [Get started creating a load balancer with Azure resource manager powerShell](/documentation/articles/load-balancer-get-started-internet-arm-ps).
 
[AZURE.INCLUDE [load-balancer-get-started-internet-scenario-include.md](../includes/load-balancer-get-started-internet-scenario-include.md)]



## Create a load balancer endpoint using Preview portal	

To create an Internet facing load balancer (classic) deployment model from the preview portal, follow the steps below.

1. From a browser, navigate to http://manage.windowsazure.cn and, if necessary, sign in with your Azure account.

2. Go to virtual machines (classic) blade > select a virtual machine.

3. In the virtual machines "essentials" blade >  select  "all settings"

4. Click in "load balanced sets".

5. To create a new load balancer, click  "join" icon on the top of the load balanced sets blade.

6. Select the "load balanced set type" public for Internet facing load balancer. 

7. Click in "configure required settings" to open "choose a load balanced set" and click on "create a load balanced set".

8. In "create a load balanced set" blade, create a name for the load balancer set. Fill out the name, public port, probe protocol, probe port.

9. Change probe interval and retries if needed.

10. (optional) if you want, you can configure access control rules from load balancer set creation blade.

11. Click ok to go back to "join load balanced set" blade.

12. click ok and wait for new load balancer resource to show in the "load balancer sets" blade.
 
## Next steps

[Get started configuring an internal load balancer](/documentation/articles/load-balancer-internal-getstarted)

[Configure a load balancer distribution mode](/documentation/articles/load-balancer-distribution-mode)

[Configure idle TCP timeout settings for your load balancer](/documentation/articles/load-balancer-tcp-idle-timeout)
