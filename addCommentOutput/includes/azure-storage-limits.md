<!-- deleted by customization
Resource|Default Limit
---|---
Max number of storage accounts per subscription|100<sup>1</sup>
TB per storage account|500 TB
Max number of blob containers, blobs, file shares, tables, queues, entities, or messages per storage account|Only limit is the 500 TB storage account capacity
Max size of a single blob container, table, or queue|500 TB
Max number of blocks in a block blob or append blob|50,000
Max size of a block in a block blob or append blob|4 MB
Max size of a block blob or append blob|50,000 X 4 MB (approx. 195 GB) 
Max size of a page blob |1 TB
Max size of a table entity|1 MB
Max number of properties in a table entity|252
Max size of a message in a queue|64 KB
Max size of a file share|5 TB
Max size of a file in a file share|1 TB
Max number of files in a file share|Only limit is the 5 TB total capacity of the file share
Max 8 KB IOPS per share|1000
Max number of files in a file share|Only limit is the 5 TB total capacity of the file share
Max number of blob containers, blobs, file shares, tables, queues, entities, or messages per storage account|Only limit is the 500 TB storage account capacity
Max number of stored access policies per container, file share, table, or queue|5
Max 8 KB IOPS per persistent disk (Basic Tier virtual machine)|300<sup>2</sup>
Max 8 KB IOPS per persistent disk (Standard Tier virtual machine)|500<sup>2</sup>
Total Request Rate (assuming 1KB object size) per storage account|Up to 20,000 IOPS, entities per second, or messages per second
Target throughput for single blob|Up to 60 MB per second, or up to 500 requests per second
Target throughput for single queue (1 KB messages)|Up to 2000 messages per second
Target throughput for single table [artition (1 KB entities)|Up to 2000 entities per second
Target throughput for single file share|Up to 60 MB per second
Max ingress<sup>3</sup> per storage account (US Regions)|10 Gbps if GRS/ZRS<sup>4</sup> enabled, 20 Gbps for LRS
Max egress<sup>3</sup> per storage account (US Regions)|20 Gbps if RA-GRS/GRS/ZRS<sup>4</sup> enabled, 30 Gbps for LRS
Max ingress<sup>3</sup> per storage account (European and Asian Regions)|5 Gbps if GRS/ZRS<sup>4</sup> enabled, 10 Gbps for LRS
Max egress<sup>3</sup> per storage account (European and Asian Regions)|10 Gbps if RA-GRS/GRS/ZRS<sup>4</sup> enabled, 15 Gbps for LRS

<sup>1</sup>If you require more than 100 storage accounts, contact [Azure Support](/support/faq/) for assistance.

<sup>2</sup>The total request rate limit for a storage account is 20,000 IOPS. If a virtual machine utilizes the maximum IOPS per disk, then to avoid possible throttling, ensure that the total IOPS across all of the virtual machines' VHDs does not exceed the storage account limit (20,000 IOPS).

You can roughly calculate the number of highly utilized disks supported by a single storage account based on the transaction limit. For example, for a Basic Tier VM, the maximum number of highly utilized disks is about 66 (20,000/300 IOPS per disk), and for a Standard Tier VM, it is about 40 (20,000/500 IOPS per disk). However, note that the storage account can support a larger number of disks if they are not all highly utilized at the same time.

<sup>3</sup>*Ingress* refers to all data (requests) being sent to a storage account. *Egress* refers to all data (responses) being received from a storage account.  

<sup>4</sup>Azure Storage replication options include:

- **RA-GRS**: Read-access geo-redundant storage. If RA-GRS is enabled, egress targets for the secondary location are identical to those for the primary location.
- **GRS**:  Geo-redundant storage. 
- **ZRS**: Zone-redundant storage. Available only for block blobs. 
- **LRS**: Locally redundant storage. 


-->
<!-- keep by customization: begin -->
<table cellspacing="0" border="1">
<tr>
   <th align="left" valign="middle">Resource<sup>1</sup></th>
   <th align="left" valign="middle">Default Limit</th>
</tr>
<tr>
   <td valign="middle"><p>TB per storage account</p></td>
   <td valign="middle"><p>500 TB</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max size of a single blob container, table, or queue</p></td>
   <td valign="middle"><p>500 TB</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max number of blob containers, blobs, file shares, tables, queues, entities, or messages per storage account</p></td>
   <td valign="middle"><p>Only limit is the 500 TB storage account capacity</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max size of a file share</p></td>
   <td valign="middle"><p>5 TB</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max number of files in a file share</p></td>
   <td valign="middle"><p>Only limit is the 5 TB total capacity of the file share</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max 8 KB IOPS per persistent disk (Basic Tier)</p></td>
   <td valign="middle"><p>300<sup>2</sup></p></td>
</tr>
<tr>
   <td valign="middle"><p>Max 8 KB IOPS per persistent disk (Standard Tier)</p></td>
   <td valign="middle"><p>500<sup>2</sup></p></td>
</tr>
<tr>
   <td valign="middle"><p>Total Request Rate (assuming 1KB object size) per storage account</p></td>
   <td valign="middle"><p>Up to 20,000 entities or messages per second</p></td>
</tr>
<tr>
   <td valign="middle"><p>Target Throughput for Single Blob</p></td>
   <td valign="middle"><p>Up to 60 MB per second, or up to 500 requests per second</p></td>
</tr>
<tr>
   <td valign="middle"><p>Target Throughput for Single Queue (1 KB messages)</p></td>
   <td valign="middle"><p>Up to 2000 messages per second</p></td>
</tr>
<tr>
   <td valign="middle"><p>Target Throughput for Single Table Partition (1 KB entities)</p></td>
   <td valign="middle"><p>Up to 2000 entities per second</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max ingress per storage account (US Regions)</p></td>
   <td valign="middle"><p>10 Gbps if GRS<sup>3</sup> enabled, 20 Gbps for LRS</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max egress per storage account (US Regions)</p></td>
   <td valign="middle"><p>20 Gbps if GRS<sup>3</sup> enabled, 30 Gbps for LRS</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max ingress per storage account (European and Asian Regions)</p></td>
   <td valign="middle"><p>5 Gbps if GRS<sup>3</sup> enabled, 10 Gbps for LRS</p></td>
</tr>
<tr>
   <td valign="middle"><p>Max egress per storage account (European and Asian Regions)</p></td>
   <td valign="middle"><p>10 Gbps if GRS<sup>3</sup> enabled, 15 Gbps for LRS</p></td>
</tr>
</table>

<sup>1</sup>For more details on these limits, see [Azure Storage Scalability and Performance Targets](/documentation/articles/storage-scalability-targets).

<sup>2</sup>For virtual machines in the Basic Tier, do not place more than 66 highly used VHDs in a storage account to avoid the 20,000 total request rate limit (20,000/300). For virtual machines in the Standard Tier, do not place more than 40 highly used VHDs in a storage account (20,000/500). For more information, see [Virtual Machine and Cloud Service Sizes for Azure](http://msdn.microsoft.com/zh-cn/library/azure/dn197896.aspx).

<sup>3</sup>GRS is [Geo Redundant Storage](http://blogs.msdn.com/b/windowsazurestorage/archive/2011/09/15/introducing-geo-replication-for-windows-azure-storage.aspx). LRS is [Locally Redundant Storage](http://blogs.msdn.com/b/windowsazurestorage/archive/2012/06/08/introducing-locally-redundant-storage-for-windows-azure-storage.aspx). Note that GRS is also locally redundant.

<!-- keep by customization: end -->