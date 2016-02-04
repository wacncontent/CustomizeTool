<properties
   pageTitle="Application upgrade: data serialization | Windows Azure"
   description="Best practices for data serialization and how it affects rolling application upgrades."
   services="service-fabric"
   documentationCenter=".net"
   authors="jessebenson"
   manager="timlt"
   editor=""/>

<tags
	ms.service="service-fabric"
	ms.date="10/15/2015"
	wacn.date=""/>


<!-- deleted by customization
# How data serialization affects application upgrade
-->
<!-- keep by customization: begin -->
# Service Fabric Application Upgrade: Data Serialization
<!-- keep by customization: end -->

In a [rolling application upgrade](/documentation/articles/service-fabric-application-upgrade), the upgrade is applied to a subset of nodes, one upgrade domain at a time. During this process, some upgrade domains will be on the newer version of your application, and some upgrade domains will be on the older version of your application. At this time, the new version of your application must be able to read the old version of your data, and the old version of your application must be able to read the new version of your data. If the data format is not forwards and backwards compatible, the upgrade may fail or data may be lost. This article discusses what constitutes your data format and best practices for ensuring your data is forwards and backwards compatible.


## What makes up your data format?

In Service Fabric, the data that is persisted and replicated comes from your C# classes. For applications using [Reliable Collections](/documentation/articles/service-fabric-reliable-services-reliable-collections), that is the objects in the reliable dictionaries and queues. For applications using <!-- deleted by customization [Reliable --><!-- keep by customization: begin --> [Stateful Reliable <!-- keep by customization: end --> Actors](/documentation/articles/service-fabric-reliable-actors-introduction), that is the backing state for the actor. These C# classes must be serializable to be persisted and replicated. Therefore, the data format is defined by the fields and properties that are serialized, as well as how they are serialized. For example, in an `IReliableDictionary<int, MyClass>` the data is a serialized `int` and a serialized `MyClass`.

<!-- deleted by customization
### Code changes that result in a data format change
-->
<!-- keep by customization: begin -->
### Data format changes
<!-- keep by customization: end -->

Since the data format is determined by C# classes, changes to the classes may cause a data format change. Care must be taken to ensure a rolling upgrade can handle the data format change. Examples that may cause data format changes:

- Adding or removing fields or properties
- Renaming fields or properties
- Changing the types of fields or properties
- Changing the class name or namespace

<!-- deleted by customization
### Data Contract is the default serializer

The serializer is generally responsible for reading the data and deserializing it into the current version, even if the data is in an older or *newer* version. The default serializer is the [Data Contract serializer](https://msdn.microsoft.com/zh-cn/library/ms733127.aspx), which has well-defined versioning rules. Reliable Collections allows the serializer to be overridden, but Reliable Actors currently does not. The data serializer plays an important role in enabling rolling upgrades. The Data Contract serializer is the serializer recommended for Service Fabric applications.
-->
<!-- keep by customization: begin -->
### Default serializer

The serializer is generally responsible for reading the data and deserializing it into the current version, even if the data is in an older or *newer* version. The default serializer is the [Data Contract serializer](https://msdn.microsoft.com/zh-cn/library/ms733127.aspx), which has well-defined versioning rules. Reliable Collections allows the serializer to be overridden, but Reliable Actors currently does not. The data serializer plays an important role in enabling rolling upgrades. The Data Contract Serializer is the serializer recommended for Service Fabric applications.
<!-- keep by customization: end -->


## How the data format affects rolling upgrade

During a rolling upgrade, there are two main scenarios where the serializer may encounter an older or *newer* version of your data:

1. After a node is upgraded and starts back up, the new serializer will load the data that was persisted to disk by the old version.
2. During the rolling upgrade, the cluster <!-- deleted by customization will --><!-- keep by customization: begin --> may <!-- keep by customization: end --> contain a mix of the old and new versions of your code. Since replicas may be placed in different upgrade domains, <!-- deleted by customization and replicas send data to each other, --> both the new <!-- deleted by customization and/or --><!-- keep by customization: begin --> and <!-- keep by customization: end --> old version of your data may be encountered by the <!-- keep by customization: begin --> serializer (which itself may be the <!-- keep by customization: end --> new <!-- deleted by customization and/or --><!-- keep by customization: begin --> or <!-- keep by customization: end --> old <!-- deleted by customization version of your serializer --><!-- keep by customization: begin --> version) <!-- keep by customization: end -->.

> [AZURE.NOTE] The "new version" and "old version" here refer to the version of your code that is running. The "new serializer" refers to the serializer code executing in the new version of your application. The "new data" refers to the serialized C# class from the new version of your application.

The two versions of code and data format must be both forward and backward compatible. If they are not compatible, the rolling upgrade may fail or data may be lost. The rolling upgrade may fail because the code or serializer may throw exceptions or fault when encountering the other version. Data may be lost if, for example, a new property was added but the old serializer discards it during deserialization.


## Data Contract

Data Contract is the recommended solution for ensuring your data is compatible. It has well-defined versioning rules for adding, removing, and changing fields. It also has support for dealing with unknown fields, hooking into the serialization and deserialization process, and for class inheritance. For more information, see [Using Data Contract](https://msdn.microsoft.com/zh-cn/library/ms733127.aspx).


## Next steps

[Upgrade Tutorial](/documentation/articles/service-fabric-application-upgrade-tutorial)

[Upgrade Parameters](/documentation/articles/service-fabric-application-upgrade-parameters)

[Advanced Topics](/documentation/articles/service-fabric-application-upgrade-advanced)
