<properties 
   pageTitle="Overview of Event Hubs authentication and security model | Windows Azure"
   description="Event Hubs FAQ"
   services="event-hubs"
   documentationCenter="na"
   authors="sethmanheim"
   manager="timlt"
   editor="" />
<tags
	ms.service="event-hubs"
	ms.date="10/07/2015"
	wacn.date=""/>

# Event Hubs authentication and security model overview

The Event Hubs security model meets the following requirements:

- Only devices that present valid credentials can send data to an Event Hub.
- A device cannot impersonate another device.
- A rogue device can be blocked from sending data to an Event Hub.

## Device authentication

The Event Hubs security model is based on a combination of [Shared Access Signature <!-- deleted by customization (SAS)](/documentation/articles/service-bus-shared-access-signature-authentication) --><!-- keep by customization: begin --> (SAS)](https://msdn.microsoft.com/zh-cn/library/dn170477.aspx) <!-- keep by customization: end --> tokens and event publishers. An event publisher defines a virtual endpoint for an Event Hub. The publisher can only be used to send messages to an Event Hub. It is not possible to receive messages from a publisher.

Typically, an Event Hub employs one publisher per device. All messages that are sent to any of the publishers of an Event Hub are enqueued within that Event Hub. Publishers allow fine-grained access control and throttling.

Each device is assigned a unique token, which is uploaded to the device. The tokens are produced such that each unique token grants access to a different unique publisher. A device that possesses a token can only send to one publisher, but no other publisher. If multiple devices share the same token, then each of these devices shares a publisher.

Although not recommended, it is possible to equip devices with tokens that grant direct access to an Event Hub. Any device that holds such a token can send messages directly into that Event Hub. Such a device will not be subject to throttling. Furthermore, the device cannot be blacklisted from sending to that Event Hub.

All tokens are signed with a SAS key. Typically, all tokens are signed with the same key. Devices are not aware of the key; this prevents devices from manufacturing tokens.

<!-- deleted by customization
### Create the SAS key
-->
<!-- keep by customization: begin -->
### Creating the key
<!-- keep by customization: end -->

When creating a namespace, Service Bus generates a 256-bit SAS key named **RootManageSharedAccessKey**. This key grants send, listen, and manage rights to the namespace. You can create additional keys. It is recommended that you produce a key that grants send permissions to the specific Event Hub. For the remainder of this topic, it is assumed that you named this key `EventHubSendKey`.

The following example creates a send-only key when creating the Event Hub:

<!-- deleted by customization ``` --><!-- keep by customization: begin --> ```C# <!-- keep by customization: end -->
// Create namespace manager.
string serviceNamespace = "YOUR_NAMESPACE";
string namespaceManageKeyName = "RootManageSharedAccessKey";
string namespaceManageKey = "YOUR_ROOT_MANAGE_SHARED_ACCESS_KEY";
Uri uri = ServiceBusEnvironment.CreateServiceUri("sb", serviceNamespace, string.Empty);
TokenProvider td = TokenProvider.CreateSharedAccessSignatureTokenProvider(namespaceManageKeyName, namespaceManageKey);
NamespaceManager nm = new NamespaceManager(namespaceUri, namespaceManageTokenProvider);

// Create Event Hub with a SAS rule that allows sending to that Event Hub.
EventHubDescription ed = new EventHubDescription("MY_EVENT_HUB") { PartitionCount = 32 };
string eventHubSendKeyName = "EventHubSendKey";
string eventHubSendKey = SharedAccessAuthorizationRule.GenerateRandomKey();
SharedAccessAuthorizationRule eventHubSendRule = new SharedAccessAuthorizationRule(eventHubSendKeyName, eventHubSendKey, new[] { AccessRights.Send });
ed.Authorization.Add(eventHubSendRule); 
nm.CreateEventHub(ed);
```

<!-- deleted by customization
### Generate tokens
-->
<!-- keep by customization: begin -->
### Generating tokens
<!-- keep by customization: end -->

You can generate tokens using the SAS key. You must produce only one token per device. Tokens can then be produced using the following method. All tokens are generated using the **EventHubSendKey** key. Each token is assigned a unique URI.

<!-- deleted by customization
```
public static string SharedAccessSignatureTokenProvider.GetSharedAccessSignature(string keyName, string sharedAccessKey, string resource, TimeSpan tokenTimeToLive)
```
-->
<!-- keep by customization: begin -->
	public static string SharedAccessSignatureTokenProvider.GetSharedAccessSignature(string keyName, string sharedAccessKey, string resource, TimeSpan tokenTimeToLive)
<!-- keep by customization: end -->

When calling this method, the URI should be specified as `//<NAMESPACE>.servicebus.chinacloudapi.cn/<EVENT_HUB_NAME>/publishers/<PUBLISHER_NAME>`. For all tokens, the URI is identical, with the exception of `PUBLISHER_NAME`, which should be different for each token. Ideally, `PUBLISHER_NAME` represents the ID of the device that receives that token.

This method generates a token with the following structure:

<!-- deleted by customization
```
SharedAccessSignature sr={URI}&sig={HMAC_SHA256_SIGNATURE}&se={EXPIRATION_TIME}&skn={KEY_NAME}
```
-->
<!-- keep by customization: begin -->
	SharedAccessSignature sr={URI}&sig={HMAC_SHA256_SIGNATURE}&se={EXPIRATION_TIME}&skn={KEY_NAME}
<!-- keep by customization: end -->

The token expiration time is specified in seconds from Jan 1, 1970. The following is an example of a token:

<!-- deleted by customization
```
SharedAccessSignature sr=contoso&sig=nPzdNN%2Gli0ifrfJwaK4mkK0RqAB%2byJUlt%2bGFmBHG77A%3d&se=1403130337&skn=RootManageSharedAccessKey
```
-->
<!-- keep by customization: begin -->
	SharedAccessSignature sr=contoso&sig=nPzdNN%2Gli0ifrfJwaK4mkK0RqAB%2byJUlt%2bGFmBHG77A%3d&se=1403130337&skn=RootManageSharedAccessKey
<!-- keep by customization: end -->

Typically, the tokens have a lifespan that resembles or exceeds the lifespan of the device. If the device has the capability to obtain a new token, tokens with a shorter lifespan can be used.

### Devices sending data

Once the tokens have been created, each device is provisioned with its own unique token.

When the device sends data into an Event Hub, the device tags its token with the send request. To prevent an attacker from eavesdropping and stealing the token, the communication between the device and the Event Hub must occur over an encrypted channel.

### Blacklisting devices

If a token is stolen by an attacker, the attacker can impersonate the device whose token has been stolen. Blacklisting a device renders the device unusable until the device is given a new token that uses a different publisher.

<!-- deleted by customization
## Authentication of back-end applications

To authenticate back-end applications that consume the data generated by devices, Event Hubs employs a security model that is similar to the model that is used for Service Bus topics. An Event Hubs consumer group is equivalent to a subscription to a Service Bus topic. A client can create a consumer group if the request to create the consumer group is accompanied by a token that grants manage privileges for the Event Hub, or for the namespace to which the Event Hub belongs. A client is allowed to consume data from a consumer group if the receive request is accompanied by a token that grants receive rights on that consumer group, the Event Hub, or the namespace to which the Event Hub belongs.
-->
<!-- keep by customization: begin -->
## Authentication of backend applications

To authenticate backend applications that consume the data generated by devices, Event Hubs employs a security model that is similar to the model that is used for Service Bus topics. An Event Hubs consumer group is equivalent to a subscription to a Service Bus topic. A client can create a consumer group if the request to create the consumer group is accompanied by a token that grants manage privileges for the Event Hub, or for the namespace to which the Event Hub belongs. A client is allowed to consume data from a consumer group if the receive request is accompanied by a token that grants receive rights on that consumer group, the Event Hub, or the namespace to which the Event Hub belongs.
<!-- keep by customization: end -->

The current version of Service Bus does not support SAS rules for individual subscriptions. The same holds true for Event Hubs consumer groups. SAS support will be added for both features in the future.

In the absence of SAS authentication for individual consumer groups, you can use SAS keys to secure all consumer groups with a common key. This approach enables an application to consume data from any of the consumer groups of an Event Hub.

### <!-- deleted by customization Create --><!-- keep by customization: begin --> Creating <!-- keep by customization: end --> service identities, relying parties, and rules in ACS

ACS supports multiple ways to create service identities, relying parties, and rules, but the easiest way to do this is by using the <!-- deleted by customization [SBAZTool](http://code.msdn.microsoft.com/Authorization-SBAzTool-6fd76d93) --><!-- keep by customization: begin --> [SBAZTool](http://code.msdn.microsoft.com/windowsazure/Authorization-SBAzTool-6fd76d93) <!-- keep by customization: end -->. For example:

1. Create a service identity for an **EventHubSender**. This returns the name of the service identity that was created and its key:

<!-- deleted by customization
	```
	sbaztool.exe exe -n <namespace> -k <key>  makeid eventhubsender
	```
-->
<!-- keep by customization: begin -->
		sbaztool.exe exe -n <namespace> -k <key>  makeid eventhubsender
<!-- keep by customization: end -->

2. Grant **EventHubSender** "Send Claims" to the Event Hub:

<!-- deleted by customization
	```
	sbaztool.exe -n <namespace> -k <key> grant Send /AuthTestEventHub eventhubsender
	```
-->
<!-- keep by customization: begin -->
		sbaztool.exe -n <namespace> -k <key> grant Send /AuthTestEventHub eventhubsender
<!-- keep by customization: end -->

3. Create a service identity for a receiver to Consumer Group 1:

<!-- deleted by customization
	```
	sbaztool.exe exe -n <namespace> -k <key> makeid consumergroup1receiver
	```
-->
<!-- keep by customization: begin -->
		sbaztool.exe exe -n <namespace> -k <key> makeid consumergroup1receiver
<!-- keep by customization: end -->

4. Grant `consumergroup1receiver` "Listen Claims" to **ConsumerGroup1**:

<!-- deleted by customization
	```
	sbaztool.exe -n <namespace> -k <key> grant Listen /AuthTestEventHub/ConsumerGroup1 consumergroup1receiver
	```
-->
<!-- keep by customization: begin -->
		sbaztool.exe -n <namespace> -k <key> grant Listen /AuthTestEventHub/ConsumerGroup1 consumergroup1receiver
<!-- keep by customization: end -->

5. Create a service identity for a receiver to **Consumer Group 2**:

<!-- deleted by customization
	```
	sbaztool.exe exe -n <namespace> -k <key>  makeid consumergroup2receiver
	```
-->
<!-- keep by customization: begin -->
		sbaztool.exe exe -n <namespace> -k <key>  makeid consumergroup2receiver
<!-- keep by customization: end -->

6. Grant `consumergroup2receiver` "Listen Claims" to **ConsumerGroup2**:

<!-- deleted by customization
	```
	sbaztool.exe -n <namespace> -k <key> grant Listen /AuthTestEventHub/ConsumerGroup2 consumergroup2receiver
	```
-->
<!-- keep by customization: begin -->
		sbaztool.exe -n <namespace> -k <key> grant Listen /AuthTestEventHub/ConsumerGroup2 consumergroup2receiver
<!-- keep by customization: end -->

## Next steps

To learn more about Event Hubs, visit the following topics:

<!-- deleted by customization
- [Event Hubs overview].
-->
<!-- keep by customization: begin -->
- [Event Hubs Overview]
<!-- keep by customization: end -->
- A complete [sample application that uses Event Hubs].
- A [queued messaging solution] using Service Bus queues.

<!-- deleted by customization
[Event Hubs overview]: /documentation/articles/event-hubs-overview
[sample application that uses Event Hubs]: https://code.msdn.microsoft.com/Service-Bus-Event-Hub-286fd097
[queued messaging solution]: /documentation/articles/service-bus-dotnet-multi-tier-app-using-service-bus-queues
-->
<!-- keep by customization: begin -->
[Event Hubs Overview]: /documentation/articles/event-hubs-overview
[sample application that uses Event Hubs]: https://code.msdn.microsoft.com/windowsazure/Service-Bus-Event-Hub-286fd097
[queued messaging solution]: /documentation/articles/cloud-services-dotnet-multi-tier-app-using-service-bus-queues
 

<!-- keep by customization: end -->