<!-- deleted by customization
Resource|Default Limit|Maximum Limit
---|---|---
Cores per [subscription](http://msdn.microsoft.com/zh-cn/library/azure/hh531793.aspx) <sup>1</sup>|20|10,000
[Co-administrators](http://msdn.microsoft.com/zh-cn/library/azure/gg456328.aspx) per subscription|200|200
[Storage accounts](/documentation/articles/storage-create-storage-account) per subscription|100|100
[Cloud services](/documentation/articles/cloud-services-what-is) per subscription|20|200
[Local networks](http://msdn.microsoft.com/zh-cn/library/jj157100.aspx) per subscription|10|500
SQL Database servers per subscription|6|150
DNS servers per subscription|9|100
Reserved IPs per subscription|20|100
ExpressRoute dedicated circuits per subscription|10|25
Hosted service certificates per subscription|400|400
[Affinity groups](/documentation/articles/virtual-networks-migrate-to-regional-vnet) per subscription|256|256
[Batch](/home/features/batch/) accounts per region per subscription|1|50
Alert rules per subscription|250|250
-->
<!-- keep by customization: begin -->
<table cellspacing="0" border="1">
<tr>
   <th align="left" valign="middle">Resource</th>
   <th align="left" valign="middle">Default Limit</th>
   <th align="left" valign="middle">Maximum Limit</th>
</tr>
<tr>
   <td valign="middle"><p>Cores per <a href="http://msdn.microsoft.com/zh-cn/library/azure/hh531793.aspx">subscription</a><sup>1</sup></p></td>
   <td valign="middle"><p>20</p></td>
   <td valign="middle"><p>10,000</p></td>
</tr>
<tr>
   <td valign="middle"><p><a href="http://msdn.microsoft.com/zh-cn/library/azure/gg456328.aspx">Co-administrators</a> per subscription</p></td>
   <td valign="middle"><p>200</p></td>
   <td valign="middle"><p>200</p></td>
</tr>
<tr>
   <td valign="middle"><p><a href="/documentation/articles/storage-create-storage-account/">Storage accounts</a> per subscription</p></td>
   <td valign="middle"><p>100</p></td>
   <td valign="middle"><p>100</p></td>
</tr>
<tr>
   <td valign="middle"><p><a href="/documentation/articles/cloud-services-what-is/">Cloud services</a> per subscription</p></td>
   <td valign="middle"><p>20</p></td>
   <td valign="middle"><p>200</p></td>
</tr>
<tr>
   <td valign="middle"><p><a href="http://msdn.microsoft.com/zh-cn/library/jj157100.aspx">Local networks</a> per subscription</p></td>
   <td valign="middle"><p>10</p></td>
   <td valign="middle"><p>500</p></td>
</tr>
<tr>
   <td valign="middle"><p>SQL Database servers per subscription</p></td>
   <td valign="middle"><p>6</p></td>
   <td valign="middle"><p>150</p></td>
</tr>
<tr>
   <td valign="middle"><p>SQL Databases per server</p></td>
   <td valign="middle"><p>150</p></td>
   <td valign="middle"><p>500</p></td>
</tr>
<tr>
   <td valign="middle"><p>DNS servers per subscription</p></td>
   <td valign="middle"><p>9</p></td>
   <td valign="middle"><p>100</p></td>
</tr>
<tr>
   <td valign="middle"><p>Reserved IPs per subscription</p></td>
   <td valign="middle"><p>20</p></td>
   <td valign="middle"><p>100</p></td>
</tr>
<tr>
   <td valign="middle"><p>Hosted service certificates per subscription</p></td>
   <td valign="middle"><p>400</p></td>
   <td valign="middle"><p>400</p></td>
</tr>
</table>
<!-- keep by customization: end -->

<sup>1</sup>Extra Small instances count as one core towards the core limit despite using a partial core. 