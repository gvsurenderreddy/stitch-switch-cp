import netaddr as net_ip

class StitchDeviceAdj:
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port

class StitchDevice:
    def __init__(self, device_id, ip6_addr):
        self.device_id = device_id
        self.ip6_addr = net_ip.IPNetwork(ip6_addr)
        self.whitelist = {}


    def add_device_access(self, device):
        #make sure the device of type StitchDevice, and that it exists in the device table.
        #make sure that the device does not belong to the same network as the device itself. 
        #A device has access to all devices in its network.
        try:
            if (device.ip6_addr.network == self.ip6_addr.network):
                return
            else:
                #devices belongs to a different netowrk, add it explicitly to the white list
                self.whitelist[device.device_it] = device
        except TypeError as e:
            print "Error using device handle %s" % (e)

    def set_ip_addr(self, ip_addr):
        self.ip6_addr = net_ip.IPNetwork(ip_addr)

    def set_device_id(self, device_id):
        self.device_id = device_id

    def set_whitelist(self, whitelist):
        self.whitelist = whitelist
        

    def set_device_adj(self, adj):
        if type(adj) is StitchDeviceAdj:
            self.adj = adj
        else:
            raise TypeError
            
        
class StitchDeviceTable:
    def __init__(self):
        self.device_table = {}

    def get_device(self, device_id):
        if device_id in self.device_table.keys():
            return self.device_table[device_id]
        else:
            return None

    def add_device(self, device):
        self.device_table[device.device_id] = device
