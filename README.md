StitchNetOS-CP
==============

This is python front-end to manage the StitchNetOS datapath module. The python front-end also integrates
the StitchNetOS datapath module to the Stitch web-service.  This provides the following functionalities:
* Provides a CLI frontend to configure IP addressses on the StitchNetOS-DP
* Provides a communication channel with the Stitch web-service (over TCP) to allow the the Stitch web-service 
to add devices and device whitedb-list to the Stitch datapath.


***CONFIGURING VLAN **********
WRITE vlan_table.config VLAN 10, NETWORK 192.168.75.12/24, PORT 0


***CONFIGURING DEFAULT ROUTE*****
WRITE vlan_table.default_route DEFAULT_GW 192.168.75.1

