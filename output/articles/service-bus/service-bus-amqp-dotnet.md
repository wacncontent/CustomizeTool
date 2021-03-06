<properties 
   pageTitle="Service Bus with .NET and AMQP 1.0 | Windows Azure"
   description="Using Service Bus from .NET with AMQP."
   services="service-bus"
   documentationCenter="na"
   authors="sethmanheim"
   manager="timlt"
   editor="tysonn" /> 
<tags
	ms.service="service-bus"
	ms.date="10/15/2015"
	wacn.date=""/>

# Using Service Bus from .NET with AMQP 1.0

[AZURE.INCLUDE [service-bus-selector-amqp](../includes/service-bus-selector-amqp.md)]

## Downloading the Service Bus SDK

AMQP 1.0 support is available in the Service Bus SDK version 2.1 or later. You can download the latest SDK from [NuGet][].

## Configuring .NET applications to use AMQP 1.0

By default, the Service Bus .NET client library communicates with the Service Bus service using a dedicated SOAP-based protocol. To use AMQP 1.0 instead of the default protocol requires explicit configuration on the Service Bus connection string, as described in the next section. Other than this change, application code remains basically unchanged when using AMQP 1.0.

In the current release, there are a few API features that are not supported when using AMQP. These unsupported features are listed later in the section [Unsupported features, restrictions, and behavioral differences](#unsupported-features-restrictions-and-behavioral-differences). Some of the advanced configuration settings also have a different meaning when using AMQP.

### Configuration using App.config

It is good practice for applications to use the App.config configuration file to store settings. For Service Bus applications, you can use App.config to store the settings for the Service Bus **ConnectionString** value. An example App.config file is as follows:

	<?xml version="1.0" encoding="utf-8" ?>
	<configuration>
	    <appSettings>
	        <add key="Microsoft.ServiceBus.ConnectionString"
	             value="Endpoint=sb://[namespace].servicebus.chinacloudapi.cn/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=[SAS key];TransportType=Amqp" />
	    </appSettings>
	</configuration>

The value of the `Microsoft.ServiceBus.ConnectionString` setting is the Service Bus connection string that is used to configure the connection to Service Bus. The format is as follows:

	Endpoint=sb://[namespace].servicebus.chinacloudapi.cn/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=[SAS key];TransportType=Amqp

Where `[namespace]` and `SharedAccessKey` are obtained from the [Azure Management Portal][]. For more information, see [How to use Service Bus queues][].

When using AMQP, append the connection string with `;TransportType=Amqp`. This notation informs the client library to make its connection to Service Bus using AMQP 1.0.

## Message serialization

When using the default protocol, the default serialization behavior of the .NET client library is to use the [DataContractSerializer][] type to serialize a [BrokeredMessage][] instance for transport between the client library and the Service Bus service. When using the AMQP transport mode, the client library uses the AMQP type system for serialization of the [brokered message][BrokeredMessage] into an AMQP message. This serialization enables the message to be received and interpreted by a receiving application that is potentially running on a different platform, for example, a Java application that uses the JMS API to access Service Bus.

When you construct a [BrokeredMessage][] instance, you can provide a .NET object as a parameter to the constructor to serve as the body of the message. For objects that can be mapped to AMQP primitive types, the body is serialized into AMQP data types. If the object cannot be directly mapped into an AMQP primitive type; that is, a custom type defined by the application, then the object is serialized using the [DataContractSerializer][], and the serialized bytes are sent in an AMQP data message.

To facilitate interoperability with non-.NET clients, use only .NET types that can be serialized directly into AMQP types for the body of the message. The following table details those types and the corresponding mapping to the AMQP type system.

| .NET Body Object Type          | Mapped AMQP Type                          | AMQP Body Section Type                                                                                                                                    |
|--------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| bool                           | boolean                                   | AMQP Value                                                                                                                                                |
| byte                           | ubyte                                     | AMQP Value                                                                                                                                                |
| ushort                         | ushort                                    | AMQP Value                                                                                                                                                |
| uint                           | uint                                      | AMQP Value                                                                                                                                                |
| ulong                          | ulong                                     | AMQP Value                                                                                                                                                |
| sbyte                          | byte                                      | AMQP Value                                                                                                                                                |
| short                          | short                                     | AMQP Value                                                                                                                                                |
| int                            | int                                       | AMQP Value                                                                                                                                                |
| long                           | long                                      | AMQP Value                                                                                                                                                |
| float                          | float                                     | AMQP Value                                                                                                                                                |
| double                         | double                                    | AMQP Value                                                                                                                                                |
| decimal                        | decimal128                                | AMQP Value                                                                                                                                                |
| char                           | char                                      | AMQP Value                                                                                                                                                |
| DateTime                       | timestamp                                 | AMQP Value                                                                                                                                                |
| Guid                           | uuid                                      | AMQP Value                                                                                                                                                |
| byte[]                         | binary                                    | AMQP Value                                                                                                                                                |
| string                         | string                                    | AMQP Value                                                                                                                                                |
| System.Collections.IList       | list                                      | AMQP Value: items contained in the collection can only be those that are defined in this table.                                                             |
| System.Array                   | array                                     | AMQP Value: items contained in the collection can only be those that are defined in this table.                                                             |
| System.Collections.IDictionary | map                                       | AMQP Value: items contained in the collection can only be those that are defined in this table.Note: only String keys are supported.                        |
| Uri                            | Described string(see the following table) | AMQP Value                                                                                                                                                |
| DateTimeOffset                 | Described long(see the following table)   | AMQP Value                                                                                                                                                |
| TimeSpan                       | Described long(see the following)         | AMQP Value                                                                                                                                                |
| Stream                         | binary                                    | AMQP Data (may be multiple). The Data sections contain the raw bytes read from the Stream object.                                                           |
| Other Object                   | binary                                    | AMQP Data (may be multiple). Contains the serialized binary of the object that uses the DataContractSerializer or a serializer supplied by the application. |

| .NET Type      | Mapped AMQP Described Type                                                                                              | Notes                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Uri            | `<type name="uri" class=restricted source="string"> <descriptor name="com.microsoft:uri" /></type>`                       | Uri.AbsoluteUri         |
| DateTimeOffset | `<type name="datetime-offset" class=restricted source="long"> <descriptor name="com.microsoft:datetime-offset" /></type>` | DateTimeOffset.UtcTicks |
| TimeSpan       | `<type name="timespan" class=restricted source="long"> <descriptor name="com.microsoft:timespan" /></type> `              | TimeSpan.Ticks          |

## Unsupported features, restrictions, and behavioral differences

The following features of the Service Bus .NET API are not currently supported when using AMQP:

-   Transactions.

-   Send via transfer destination.

-   Receive by message sequence number.

-   Message and session browse.

-   Session state.

-   Batch-based APIs.

-   Scaled-out receive.

-   Runtime manipulation of subscription rules.

-   Session lock renewal.

Specifically, the following APIs are not currently supported when using AMQP:

- [Microsoft.ServiceBus.Messaging.MessagingFactory.AcceptMessageSession][]
- [Microsoft.ServiceBus.Messaging.MessagingFactory.CreateMessageSender(System.String,System.String)][]

- [Microsoft.ServiceBus.Messaging.MessageSender.SendBatch(System.Collections.Generic.IEnumerable{Microsoft.ServiceBus.Messaging.BrokeredMessage})][]

- [Microsoft.ServiceBus.Messaging.MessageReceiver.Receive(System.Int64)][]
- [Microsoft.ServiceBus.Messaging.MessageReceiver.ReceiveBatch][]
- [Microsoft.ServiceBus.Messaging.MessageReceiver.CompleteBatch(System.Collections.Generic.IEnumerable{System.Guid})][]
- [Microsoft.ServiceBus.Messaging.MessageReceiver.Peek][]
- [Microsoft.ServiceBus.Messaging.MessageReceiver.PeekBatch][]

- [Microsoft.ServiceBus.Messaging.QueueClient.Peek][]
- [Microsoft.ServiceBus.Messaging.QueueClient.PeekBatch][]

- [Microsoft.ServiceBus.Messaging.TopicClient.SendBatch(System.Collections.Generic.IEnumerable{Microsoft.ServiceBus.Messaging.BrokeredMessage})][]

- [Microsoft.ServiceBus.Messaging.SubscriptionClient.Receive(System.Int64)][]
- [Microsoft.ServiceBus.Messaging.SubscriptionClient.ReceiveBatch][]
- [Microsoft.ServiceBus.Messaging.SubscriptionClient.CompleteBatch(System.Collections.Generic.IEnumerable{System.Guid})][]
- [Microsoft.ServiceBus.Messaging.SubscriptionClient.Peek][]
- [Microsoft.ServiceBus.Messaging.SubscriptionClient.PeekBatch][]
- [Microsoft.ServiceBus.Messaging.SubscriptionClient.AddRule][]
- [Microsoft.ServiceBus.Messaging.SubscriptionClient.RemoveRule(System.String)][]

- [Microsoft.ServiceBus.Messaging.MessageSession.GetState][]
- [Microsoft.ServiceBus.Messaging.MessageSession.SetState(System.IO.Stream)][]
- [Microsoft.ServiceBus.Messaging.MessageSession.RenewLock][]

- [Microsoft.ServiceBus.Messaging.BrokeredMessage.RenewLock][]

There are also some small differences in the behavior of the Service Bus .NET API when using AMQP, compared to the default protocol:

-   The [OperationTimeout][] property is ignored.

-   `MessageReceiver.Receive(TimeSpan.Zero)` is implemented as `MessageReceiver.Receive(TimeSpan.FromSeconds(10))`.

## Controlling AMQP protocol settings

The .NET APIs expose several settings to control the behavior of the AMQP protocol:

-   **MessageReceiver.PrefetchCount**: Controls the initial credit applied to a link. The default is 0.

-   **MessagingFactorySettings.AmqpTransportSettings.MaxFrameSize**: Controls the maximum AMQP frame size offered during the negotiation at connection open time. The default is 65,536 bytes.

-   **MessagingFactorySettings.AmqpTransportSettings.BatchFlushInterval**: If transfers are batchable, this value determines the maximum delay for sending dispositions. Inherited by senders/receivers by default. Individual sender/receiver can override the default, which is 20 milliseconds.

-   **MessagingFactorySettings.AmqpTransportSettings.UseSslStreamSecurity**: Controls whether AMQP connections are established over an SSL connection. The default is **true**.

## Next steps

Ready to learn more? Visit the following links:

- [Service Bus AMQP overview]
- [AMQP 1.0 support for Service Bus partitioned queues and topics]
- [AMQP in Service Bus for Windows Server]

  [How to Use Service Bus Queues]: service-bus-dotnet-how-to-use-queues.md
  [DataContractSerializer]: https://msdn.microsoft.com/zh-cn/library/azure/system.runtime.serialization.datacontractserializer.aspx
  [BrokeredMessage]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.brokeredmessage.aspx
  [Microsoft.ServiceBus.Messaging.MessagingFactory.AcceptMessageSession]: https://msdn.microsoft.com/zh-cn/library/azure/jj657638.aspx
  [Microsoft.ServiceBus.Messaging.MessagingFactory.CreateMessageSender(System.String,System.String)]: https://msdn.microsoft.com/zh-cn/library/azure/jj657703.aspx
  [Microsoft.ServiceBus.Messaging.MessageSender.SendBatch(System.Collections.Generic.IEnumerable{Microsoft.ServiceBus.Messaging.BrokeredMessage})]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.messagesender.sendbatch.aspx
  [Microsoft.ServiceBus.Messaging.MessageReceiver.Receive(System.Int64)]: https://msdn.microsoft.com/zh-cn/library/azure/hh322665.aspx
  [Microsoft.ServiceBus.Messaging.MessageReceiver.ReceiveBatch]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.messagereceiver.receivebatch.aspx
  [Microsoft.ServiceBus.Messaging.MessageReceiver.CompleteBatch(System.Collections.Generic.IEnumerable{System.Guid})]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.messagereceiver.completebatch.aspx
  [Microsoft.ServiceBus.Messaging.MessageReceiver.Peek]: https://msdn.microsoft.com/zh-cn/library/azure/jj908731.aspx
  [Microsoft.ServiceBus.Messaging.MessageReceiver.PeekBatch]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.messagereceiver.peekbatch.aspx
  [Microsoft.ServiceBus.Messaging.QueueClient.Peek]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.queueclient.peek.aspx
  [Microsoft.ServiceBus.Messaging.QueueClient.PeekBatch]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.queueclient.peekbatch.aspx
  [Microsoft.ServiceBus.Messaging.TopicClient.SendBatch(System.Collections.Generic.IEnumerable{Microsoft.ServiceBus.Messaging.BrokeredMessage})]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.topicclient.sendbatch.aspx
  [Microsoft.ServiceBus.Messaging.SubscriptionClient.Receive(System.Int64)]: https://msdn.microsoft.com/zh-cn/library/azure/hh293110.aspx
  [Microsoft.ServiceBus.Messaging.SubscriptionClient.ReceiveBatch]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.subscriptionclient.receivebatch.aspx
  [Microsoft.ServiceBus.Messaging.SubscriptionClient.CompleteBatch(System.Collections.Generic.IEnumerable{System.Guid})]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.subscriptionclient.completebatch.aspx
  [Microsoft.ServiceBus.Messaging.SubscriptionClient.Peek]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.subscriptionclient.peek.aspx
  [Microsoft.ServiceBus.Messaging.SubscriptionClient.PeekBatch]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.subscriptionclient.peekbatch.aspx
  [Microsoft.ServiceBus.Messaging.SubscriptionClient.AddRule]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.subscriptionclient.addrule.aspx
  [Microsoft.ServiceBus.Messaging.SubscriptionClient.RemoveRule(System.String)]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.subscriptionclient.removerule.aspx
  [Microsoft.ServiceBus.Messaging.MessageSession.GetState]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.messagesession.getstate.aspx
  [Microsoft.ServiceBus.Messaging.MessageSession.SetState(System.IO.Stream)]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.messagesession.setstate.aspx
  [Microsoft.ServiceBus.Messaging.MessageSession.RenewLock]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.messagesession.renewlock.aspx
  [Microsoft.ServiceBus.Messaging.BrokeredMessage.RenewLock]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.brokeredmessage.renewlock.aspx
  [OperationTimeout]: https://msdn.microsoft.com/zh-cn/library/azure/microsoft.servicebus.messaging.messagingfactorysettings.operationtimeout.aspx
[NuGet]: http://nuget.org/packages/WindowsAzure.ServiceBus/

[Azure Management Portal]: http://manage.windowsazure.cn
[Service Bus AMQP overview]: service-bus-amqp-overview.md
[AMQP 1.0 support for Service Bus partitioned queues and topics]: service-bus-partitioned-queues-and-topics-amqp-overview.md
[AMQP in Service Bus for Windows Server]: https://msdn.microsoft.com/zh-cn/library/dn574799.aspx