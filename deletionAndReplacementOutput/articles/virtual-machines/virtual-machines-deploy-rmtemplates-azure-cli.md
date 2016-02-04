replacement:

deleted:

		If you don't already have an Azure subscription but you do have an MSDN subscription, you can activate your [MSDN subscriber benefits](/pricing/member-offers/msdn-benefits-details/). Or you can sign up for a [trial](/pricing/1rmb-trial/).

replaced by:

		If you don't already have an Azure subscription, you can sign up for a [trial](/pricing/1rmb-trial/).

reason: ()

deleted:

		+ Looking up the NIC "coreo-westu-1430261891570-nic"
		    info:    An nic with given name "coreo-westu-1430261891570-nic" not found, creating a new one
		    + Looking up the virtual network "coreo-westu-1430261891570-vnet"

replaced by:

		+ Looking up the NIC "coreo-chinanorth-1430261891570-nic"
		    info:    An nic with given name "coreo-chinanorth-1430261891570-nic" not found, creating a new one
		    + Looking up the virtual network "coreo-chinanorth-1430261891570-vnet"

reason: (region diff)

deleted:

		/ Creating a new virtual network "coreo-westu-1430261891570-vnet" [address prefix: "10.0.0.0/16"] with subnet "coreo-westu-1430261891570-sne+" [address prefix: "10.0.1.0/24"]
		    + Looking up the virtual network "coreo-westu-1430261891570-vnet"
		    + Looking up the subnet "coreo-westu-1430261891570-snet" under the virtual network "coreo-westu-1430261891570-vnet"

replaced by:

		/ Creating a new virtual network "coreo-chinanorth-1430261891570-vnet" [address prefix: "10.0.0.0/16"] with subnet "coreo-chinanorth-1430261891570-sne+" [address prefix: "10.0.1.0/24"]
		    + Looking up the virtual network "coreo-chinanorth-1430261891570-vnet"
		    + Looking up the subnet "coreo-chinanorth-1430261891570-snet" under the virtual network "coreo-chinanorth-1430261891570-vnet"

reason: (region diff)

deleted:

		+ Looking up the public ip "coreo-westu-1430261891570-pip"
		    info:    PublicIP with given name "coreo-westu-1430261891570-pip" not found, creating a new one
		    + Creating public ip "coreo-westu-1430261891570-pip"
		    + Looking up the public ip "coreo-westu-1430261891570-pip"
		    + Creating NIC "coreo-westu-1430261891570-nic"
		    + Looking up the NIC "coreo-westu-1430261891570-nic"

replaced by:

		+ Looking up the public ip "coreo-chinanorth-1430261891570-pip"
		    info:    PublicIP with given name "coreo-chinanorth-1430261891570-pip" not found, creating a new one
		    + Creating public ip "coreo-chinanorth-1430261891570-pip"
		    + Looking up the public ip "coreo-chinanorth-1430261891570-pip"
		    + Creating NIC "coreo-chinanorth-1430261891570-nic"
		    + Looking up the NIC "coreo-chinanorth-1430261891570-nic"

reason: (region diff)

deleted:

		+ Looking up the NIC "coreo-westu-1430261891570-nic"
		    + Looking up the public ip "coreo-westu-1430261891570-pip"

replaced by:

		+ Looking up the NIC "coreo-chinanorth-1430261891570-nic"
		    + Looking up the public ip "coreo-chinanorth-1430261891570-pip"

reason: (region diff)

deleted:

		:coreo-westu-1430261891570-pip.chinanorth.chinacloudapp.cn

replaced by:

		:coreo-chinanorth-1430261891570-pip.chinanorth.chinacloudapp.cn

reason: (region diff)

deleted:

		:/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/coreos-quick/providers/Microsoft.Network/networkInterfaces/coreo-westu-1430261891570-nic

replaced by:

		:/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/coreos-quick/providers/Microsoft.Network/networkInterfaces/coreo-chinanorth-1430261891570-nic

reason: (region diff)

deleted:

		:coreo-westu-1430261891570-nic

replaced by:

		:coreo-chinanorth-1430261891570-nic

reason: (region diff)

deleted:

		:coreo-westu-1430261891570-pip.chinanorth.chinacloudapp.cn

replaced by:

		:coreo-chinanorth-1430261891570-pip.chinanorth.chinacloudapp.cn

reason: (region diff)

