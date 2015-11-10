<!-- deleted by customization
Resource|Default Limit|Maximum Limit
---|---|---
[Virtual machines](/documentation/articles/virtual-machines-about) per cloud service<sup>1</sup>|50|50
Input endpoints per cloud service<sup>2</sup>|150|150

<sup>1</sup>Virtual machines created in Service Management (instead of Resource Manager) are automatically stored in a cloud service. You can add more virtual machines to that cloud service for load balancing and availability. See  [How to Connect Virtual Machines with a Virtual Network or Cloud Service](/documentation/articles/cloud-services-connect-virtual-machine).

<sup>2</sup>Input endpoints allow communications to a virtual machine from outside the virtual machine's cloud service. Virtual machines in the same cloud service or virtual network can automatically communicate with each other. See [How to Set Up Endpoints to a Virtual Machine](/documentation/articles/virtual-machines-set-up-endpoints). 
-->
<!-- keep by customization: begin -->
<table cellspacing="0" border="1">
<tr>
   <th align="left" valign="middle">Resource</th>
   <th align="left" valign="middle">Default Limit</th>
   <th align="left" valign="middle">Maximum Limit</th>
</tr>
<tr>
   <td valign="middle"><p><a href="/documentation/services/virtual-machines/">Virtual machines</a> per cloud service<sup>1</sup></p></td>
   <td valign="middle"><p>50</p></td>
   <td valign="middle"><p>50</p></td>
</tr>
<tr>
   <td valign="middle"><p>Input Endpoints per cloud service<sup>2</sup></p></td>
   <td valign="middle"><p>150</p></td>
   <td valign="middle"><p>150</p></td>
</tr>
</table>

<sup>1</sup>When you create a virtual machine outside of an Azure Resource Group, a cloud service is automatically created to contain the machine. You can then add multiple virtual machines in that same Cloud Service.

<sup>2</sup>Input endpoints are used to allow communication to the virtual machines that is external to the containing cloud service. Virtual machines within the same cloud service automatically allow communication between all UDP and TCP ports for internal communication.
<!-- keep by customization: end -->
