import os
import threading
import netaddr
import json
from click_intf import StitchClick
from stitch_device import StitchDevice


class StitchWebService (threading.Thread):
    def __init__(self, ip_addr, web_port, stitch_dp, stitch_device_table):
        super(StitchWebService, self).__init__()
        self.ip_addr = ip_addr
        self.web_port = web_port
        self.IP_ADDR_FIELD = "ip_addr"
        self.DEVICE_ID_FIELD = "device_id"
        self.WHITELIST_FIELD = "whitelist"
        self.end = "Stitch-msg-end"
        self.stitch_dp = stitch_dp

    def update_device_in_dp(self, device):
        #Generate command strings to update the stitch DP.

    def handle_msg(self, json_data):
        device_dic = json.load(json_data):
        try:
            device_id = device_dic[self.DEVICE_ID_FIELD]
            ip_addr = device_dic[self.IP_ADDR_FIELD]
            whilte_list = device_dic[self.WHITELIST_FIELD]
        except AttributeError as e:
            print "Looks a like a problem with the JSON message:%s" % (e)
            return
        #check if the device exists.
        if (device = stitch_device_table.get_device(device_id)) is not None:
            #update the IP address of the device 
            device.set_ip_addr(ip_addr)
            device.set_device_id(device_id)
            device.set_whitelist(whitelist)
        else:
            device = StitchDevice(device_id = device_id,\
                ip6_addr = ip_addr)
            device.set_whitelist(whitelist)
        self.update_device_in_dp(device) 
        


    def run(self):
        #open the TCP web service port. We might need to convert it to an SSL
        #socket at a later date.
        self.web_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM
        try:
            self.web_s.connect((ip_addr, web_port))
        except IOError as e:
            #print and error and return. Ideally we want to wait for 
            return

i       #send the register to the web service
        
        #wait for updates from the web service
        tmp_json_data = ''
        json_data = '' 
        while (1):
            try:
                data = self.web_s.recv(1024)

                #keep appending to the temporary JSON data till we 
                #receive end-of-message marker.
                "".join((tmp_json_data, data))

                if self.end in tmp_json_data:
                    #found the end of the message.
                    json_data = tmp_json_data[:tmp_json_data.find(self.end)]
                    #reset it to the remainder of the message. This could be the
                    #succeeding message
                    tmp_json_data =\
                       tmp_json_data[(tmp_json_data.find(self.end)+\
                           len(self.end)):]
                    #process the JSON data 
                    self.handle_msg(json_data)
            except IOError:
                print "Connection to stitch web-service closed."
                return
                
                
            






            
            






