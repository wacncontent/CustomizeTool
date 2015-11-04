<properties
   pageTitle="QoS Requirements for ExpressRoute | Windows Azure"
   description="This page provides detailed requirements for configuring and managing QoS for ExpressRoute circuits."
   documentationCenter="na"
   services="expressroute"
   authors="cherylmc"
   manager="carolz"
   editor=""/>
<tags
	ms.service="expressroute"
	ms.date="10/06/2015"
	wacn.date=""/>

# ExpressRoute QoS requirements

Skype for Business has various workloads that require differentiated QoS treatment. If you plan to consume voice services through ExpressRoute, you should adhere to the requirements described below.

![](./media/expressroute-qos/expressroute-qos.png)

**Note:** QoS requirements apply to the Microsoft peering only.

The following table provides a list of DSCP markings used by Skype for Business. Refer to [Managing QoS for Skype for Business](https://technet.microsoft.com/zh-cn/library/gg405409.aspx) for more information.

| **Traffic Class** | **Treatment (DSCP Marking)** | **Skype for Business Workloads** |
|---|---|---|
| **Voice** | EF (46) | Skype / Lync voice |
| **Interactive** | AF41 (34) | Video |
|   | AF21 (18) | App sharing | 
|   | CS3 (24) | SIP signaling |
| **Default** | AF11 (10) | File transfer|
|   | CS0 (0) | Anything else| 


- You should classify the workloads and mark the right DSCP values. Follow the guidance provided [here](https://technet.microsoft.com/zh-cn/library/gg405409.aspx) on how to set DSCP markings in your network.

- You should configure and support multiple QoS queues within your network. Voice must be a standalone class and receive the EF treatment specified in RFC 3246. 

- You can decide the queuing mechanism, congestion detection policy, and bandwidth allocation per traffic class. But, the DSCP marking for Skype for Business workloads must be preserved. If you are using DSCP markings not listed above, e.g. AF31 (26), you must rewrite this DSCP value to 0 before sending the packet to Microsoft. Microsoft only sends packets marked with the DSCP value shown in the above table. 

## Next steps

- Refer to the requirements for [Routing](/documentation/articles/expressroute-routing) and [NAT](/documentation/articles/expressroute-nat).
- See the following links to configure your ExpressRoute connection.

	- [Create an ExpressRoute circuit](/documentation/articles/expressroute-howto-circuit-classic)
	- [Configure routing](/documentation/articles/expressroute-howto-routing-classic)
	- [Link a VNet to an ExpressRoute circuit](/documentation/articles/expressroute-howto-linkvnet-classic)
