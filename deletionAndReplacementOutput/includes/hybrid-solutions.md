deletion:

deleted:

		Each message is received by a single recipient.

reason: ()

deleted:

		can optionally use a filter

reason: ()

deleted:

		you should use a topic instead

reason: ()

deleted:

		that you can reach directly from outside the datacenter

reason: ()

deleted:

		in the cloud

reason: ()

deleted:

		between applications

reason: ()

deleted:

		[Event Hubs overview]: https://msdn.microsoft.com/zh-cn/library/azure/dn836025.aspx

reason: ()

replacement:

deleted:

		an application or service

replaced by:

		software

reason: ()

deleted:

		applications or services

replaced by:

		software

reason: ()

deleted:

		## Service Bus fundamentals
		Different situations call for different styles of communication. Sometimes, letting applications send and receive messages through a simple queue is the best solution. In other situations, an ordinary queue isn't enough; a queue with a publish-and-subscribe mechanism is better. And in some cases, all that's really needed is a connection between applications&#151;queues aren't required. Service Bus provides all three options, letting your applications interact in several different ways.

replaced by:

		##Table of Contents      
		- [Service Bus Fundamentals](#fundamentals)
		- [Queues](#queues)
		- [Topics](#topics)
		- [Relays](#relays)
		
		
		## <a name="fundamentals"></a>Service Bus Fundamentals
		Different situations call for different styles of communication. Sometimes, letting applications send and receive messages through a simple queue is the best solution. In other situations, an ordinary queue isn't enough; a queue with a publish-and-subscribe mechanism is better. And in some cases, all that's really needed is a connection between applications-queues aren't required. Service Bus provides all three options, letting your applications interact in several different ways.

reason: ()

deleted:

		four

replaced by:

		three

reason: ()

deleted:

		*subscriptions*-a single topic can have multiple subscriptions

replaced by:

		*subscriptions*

reason: ()

deleted:

		receive

replaced by:

		see

reason: ()

deleted:

		- *Event Hubs*, which provide event and telemetry ingress to the cloud at massive scale, with low latency and high reliability.
		
		When you create a queue, topic,  relay <!-- deleted by customization, or Event Hub -->, you give it a name. Combined with whatever you called your namespace, this name creates a unique identifier for the object. Applications can provide this name to Service Bus, then use that queue, topic,  relay <!-- deleted by customization, or Event Hub --> to communicate with one another.
		
		To use any of these objects, Windows applications can use Windows Communication Foundation (WCF). For queues, topics, and Event Hubs Windows applications can also use Service Bus-defined messaging APIs. To make these objects easier to use from non-Windows applications, Microsoft provides SDKs for Java, Node.js, and other languages. You can also access queues, topics, and Event Hubs using REST APIs over HTTP.

replaced by:

		When you create a queue, topic, or relay <!-- deleted by customization, or Event Hub -->, you give it a name. Combined with whatever you called your namespace, this name creates a unique identifier for the object. Applications can provide this name to Service Bus, then use that queue, topic, or relay <!-- deleted by customization, or Event Hub --> to communicate with one another.
		
		To use any of these objects, Windows applications can use Windows Communication Foundation (WCF). For queues and topics, Windows applications can also use a Service Bus-defined Messaging API. Queues and topics can be accessed via HTTP as well, and to make them easier to use from non-Windows applications, Microsoft provides SDKs for Java, Node.js, and other languages.

reason: ()

deleted:

		## Queues

replaced by:

		## <a name="queues"></a>Queues

reason: ()

deleted:

		receiver-for

replaced by:

		receiver-queues don't provide

reason: ()

deleted:

		## Topics

replaced by:

		## <a name="topics"></a>Topics

reason: ()

deleted:

		For example, this

replaced by:

		This

reason: ()

deleted:

		therefore

replaced by:

		so

reason: ()

deleted:

		all the messages

replaced by:

		everything

reason: ()

deleted:

		## Relays
		
		Both queues and topics provide one-way asynchronous communication through a broker. Traffic flows in just one direction, and there's no direct connection between senders and receivers. But what if you don't want this? Suppose your applications need to both send and receive messages, or perhaps you want a direct link between them and you don't need a broker to store messages . To address scenarios such as this, Service Bus provides relays, as [Figure 4](#Fig4) shows.

replaced by:

		## <a name="relays"></a>Relays
		
		Both queues and topics provide one-way asynchronous communication through a broker. Traffic flows in just one direction, and there's no direct connection between senders and receivers. But what if you don't want this? Suppose your applications need to both send and receive , or perhaps you want a direct link between them"you don't need a place to store messages in between. To address problems like this, Service Bus provides relays, as [Figure 4](#Fig4) shows.

reason: ()

deleted:

		application without

replaced by:

		application"data sent through the relay"without

reason: ()

deleted:

		enables applications to locate

replaced by:

		allows locating

reason: ()

deleted:

		For example, consider

replaced by:

		Think about

reason: ()

deleted:

		## Event Hubs
		
		Event Hubs is a highly scalable ingestion system that can process millions of events per second, enabling your application to process and analyze the massive amounts of data produced by your connected devices and applications. For example, you could use an Event Hub to collect live engine performance data from a fleet of cars. Once collected into Event Hubs, you can transform and store data using any real-time analytics provider or storage cluster. For more information about Event Hubs, see the [Event Hubs overview][].
		
		## Summary
		
		Connecting applications has always been part of building complete solutions, and the range of scenarios that require applications and services to communicate with each other is set to increase as more applications and devices are connected to the Internet. By providing cloud-based technologies for achieving this through queues, topics, relays, and Event Hubs, Service Bus aims to make this essential function easier to implement and more broadly available.

replaced by:

		Connecting applications has always been part of building complete solutions, and it's hard to see this problem ever going away. By providing cloud-based technologies for doing this through queues, topics, and relays, Service Bus aims at making this essential function easier and more broadly available.

reason: ()

