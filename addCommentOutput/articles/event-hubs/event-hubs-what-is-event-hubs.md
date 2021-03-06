<properties
	pageTitle="What is Azure Event Hubs? | Windows Azure"
	description="Overview of Azure Event Hubs"
	services="event-hubs"
	documentationCenter=".net"
	authors="nberdy"
	manager="timlt"
	editor=""/>

<tags
	ms.service="event-hubs"
	ms.date="11/05/2015"
	wacn.date=""/>

# What is Azure Event Hubs?

Azure Event Hubs is a highly scalable data ingress service that can ingest millions of events per second so that you can process and analyze the massive amounts of data produced by your connected devices and applications. Event Hubs acts as the "front door" for an event pipeline, and once data is collected into an event hub, it can be transformed and stored using any real-time analytics provider or batching/storage adapters. Event Hubs decouples the production of a stream of events from the consumption of those events, so that event consumers can access the events on their own schedule.

## Event Hubs capabilities

Event Hubs is an event processing service that provides event and telemetry ingress to the cloud at massive scale, with low latency and high reliability. This service is especially useful for:

* Application instrumentation
* User experience or workflow processing
* Internet of Things (IoT) scenarios

Some other key Event Hubs capabilities are behavior tracking in mobile apps, traffic information from web farms, in-game event capture in console games, or telemetry data collected from industrial machines or connected vehicles.

Unlike [Service Bus queues and topics](/documentation/articles/service-bus-messaging-overview), Event Hubs is focused on delivering messaging stream handling at scale. Event Hubs capabilities differ from topics in that they are strongly biased towards high throughput and event processing scenarios. As a result, Event Hubs do not implement some of the messaging capabilities that are available for <!-- deleted by customization [topics](/documentation/articles/service-bus-fundamentals-hybrid-solutions#topics) --><!-- keep by customization: begin --> [topics](/documentation/articles/service-bus-fundamentals-service-bus-hybrid-solutions#topics) <!-- keep by customization: end -->. If you need those capabilities, topics remain the optimal choice.

## Next steps

For detailed information about Event Hubs, see the following topics.

- [Event Hubs overview](/documentation/articles/event-hubs-overview)
- [Event Hubs programming guide](/documentation/articles/event-hubs-programming-guide)
- [Event Hubs availability and support FAQ](/documentation/articles/event-hubs-availability-and-support-faq)
- Get started with an [Event Hubs <!-- deleted by customization tutorial][] --><!-- keep by customization: begin --> tutorial] <!-- keep by customization: end -->
- A complete [sample application that uses Event <!-- deleted by customization Hubs][] --><!-- keep by customization: begin --> Hubs] <!-- keep by customization: end -->

<!-- deleted by customization
[Event Hubs tutorial]: event-hubs-csharp-ephcs-getstarted.md
[sample application that uses Event Hubs]: https://code.msdn.microsoft.com/Service-Bus-Event-Hub-286fd097
-->
<!-- keep by customization: begin -->
[Event Hubs tutorial]: /documentation/articles/hdinsight-apache-storm-tutorial-get-started
[sample application that uses Event Hubs]: https://code.msdn.microsoft.com/windowsazure/Service-Bus-Event-Hub-286fd097
<!-- keep by customization: end -->