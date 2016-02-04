<properties 
	pageTitle="How to use Queue storage from Python | Windows Azure" 
	description="Learn how to use the Azure Queue service from Python to create and delete queues, and insert, get, and delete messages." 
	services="storage" 
	documentationCenter="python" 
	authors="emgerner-msft" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="storage"
	ms.date="12/11/2015"
	wacn.date=""/>

# How to use Queue storage from Python

[AZURE.INCLUDE [storage-selector-queue-include](../includes/storage-selector-queue-include.md)]

## Overview

This guide shows you how to perform common scenarios using the Azure Queue storage service. The samples are written in Python and use the [Python Azure Storage package][]. The scenarios covered include **inserting**, **peeking**,
**getting**, and **deleting** queue messages, as well as **creating and
deleting queues**. For more information on queues, refer to the [Next Steps][] section.

[AZURE.INCLUDE [storage-queue-concepts-include](../includes/storage-queue-concepts-include.md)]

[AZURE.INCLUDE [storage-create-account-include](../includes/storage-create-account-include.md)]


> [AZURE.NOTE] If you need to install Python or the [Python Azure package][], please see the [Python Installation Guide](/documentation/articles/python-how-to-install).

## How To: Create a Queue

The **QueueService** object lets you work with queues. The following code creates a **QueueService** object. Add the following near the top of any Python file in which you wish to programmatically access Azure Storage:

	from azure.storage.queue import QueueService

The following code creates a **QueueService** object using the storage account name and account key. Replace 'myaccount' and 'mykey' with the real account and key.

	queue_service = QueueService(account_name='myaccount', account_key='mykey')

	queue_service.create_queue('taskqueue')


## How To: Insert a Message into a Queue

To insert a message into a queue, use the <!-- deleted by customization **put\_message** --><!-- keep by customization: begin --> **put_message** <!-- keep by customization: end --> method to
create a new message and add it to the queue.

	queue_service.put_message('taskqueue', 'Hello World')


## How To: Peek at the Next Message

You can peek at the message in the front of a queue without removing it
from the queue by calling the <!-- deleted by customization **peek\_messages** --><!-- keep by customization: begin --> **peek_messages** <!-- keep by customization: end --> method. By default,
<!-- deleted by customization
**peek\_messages** peeks at a single message.
-->
<!-- keep by customization: begin -->
**peek_messages** peeks at a single message.
<!-- keep by customization: end -->

	messages = queue_service.peek_messages('taskqueue')
	for message in messages:
		print(message.message_text)


## How To: Dequeue the Next Message

Your code removes a message from a queue in two steps. When you call
<!-- deleted by customization **get\_messages** --><!-- keep by customization: begin --> **get_messages** <!-- keep by customization: end -->, you get the next message in a queue by default. A
message returned from <!-- deleted by customization **get\_messages** --><!-- keep by customization: begin --> **get_messages** <!-- keep by customization: end --> becomes invisible to any other
code reading messages from this queue. By default, this message stays
invisible for 30 seconds. To finish removing the message from the queue,
you must also call <!-- deleted by customization **delete\_message** --><!-- keep by customization: begin --> **delete_message** <!-- keep by customization: end -->. This two-step process of removing
a message assures that when your code fails to process a message due to
hardware or software failure, another instance of your code can get the
same message and try again. Your code calls <!-- deleted by customization **delete\_message** --><!-- keep by customization: begin --> **delete_message** <!-- keep by customization: end --> right
after the message has been processed.

	messages = queue_service.get_messages('taskqueue')
	for message in messages:
		print(message.message_text)
		queue_service.delete_message('taskqueue', message.message_id, message.pop_receipt)


## How To: Change the Contents of a Queued Message

You can change the contents of a message in-place in the queue. If the
message represents a work task, you could use this feature to update the
status of the work task. The code below uses the <!-- deleted by customization **update\_message** --><!-- keep by customization: begin --> **update_message** <!-- keep by customization: end -->
method to update a message.

	messages = queue_service.get_messages('taskqueue')
	for message in messages:
		queue_service.update_message('taskqueue', message.message_id, 'Hello World Again', message.pop_receipt, 0)

## How To: Additional Options for Dequeuing Messages

There are two ways you can customize message retrieval from a queue.
First, you can get a batch of messages (up to 32). Second, you can set a
longer or shorter invisibility timeout, allowing your code more or less
time to fully process each message. The following code example uses the
<!-- deleted by customization **get\_messages** --><!-- keep by customization: begin --> **get_messages** <!-- keep by customization: end --> method to get 16 messages in one call. Then it processes
each message using a for loop. It also sets the invisibility timeout to
five minutes for each message.

	messages = queue_service.get_messages('taskqueue', numofmessages=16, visibilitytimeout=5*60)
	for message in messages:
		print(message.message_text)
		queue_service.delete_message('taskqueue', message.message_id, message.pop_receipt)

## How To: Get the Queue Length

You can get an estimate of the number of messages in a queue. The
<!-- deleted by customization **get\_queue\_metadata** --><!-- keep by customization: begin --> **get_queue_metadata** <!-- keep by customization: end --> method asks the queue service to return metadata
about the queue, and the **x-ms-approximate-messages-count** should be used as the index into the returned dictionary to find the count.
The result is only approximate because messages can be added or removed after the
queue service responds to your request.

	queue_metadata = queue_service.get_queue_metadata('taskqueue')
	count = queue_metadata['x-ms-approximate-messages-count']

## How To: Delete a Queue

To delete a queue and all the messages contained in it, call the
<!-- deleted by customization
**delete\_queue** method.
-->
<!-- keep by customization: begin -->
**delete_queue** method.
<!-- keep by customization: end -->

	queue_service.delete_queue('taskqueue')

## Next Steps

Now that you have learned the basics of queue storage, follow these links
to learn about more complex storage tasks.

-   Visit the [Azure Storage Team Blog][]

For more information, see also the [Python Developer Center](/develop/python/).

[Azure Storage Team Blog]: http://blogs.msdn.com/b/windowsazurestorage/
[Python Azure package]: https://pypi.python.org/pypi/azure
[Python Azure Storage package]: https://pypi.python.org/pypi/azure-storage 
 
