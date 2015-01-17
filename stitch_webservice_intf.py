import os
import threading
import netaddr
import json
import socket
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
        self.stitch_device_table = stitch_device_table

    def update_device_in_dp(self, device):
        #Generate command strings to update the stitch DP.
        print "Adbout to update device in DP"
        self.stitch_dp.add_device(device)
        return None

    def handle_msg(self, json_data):
        device_dic = json.loads(json_data)
        try:
            device_id = device_dic[self.DEVICE_ID_FIELD]
            ip_addr = device_dic[self.IP_ADDR_FIELD]
            white_list = device_dic[self.WHITELIST_FIELD]
            print "Received device info: device_id:%s, ip_addr:%s" % (device_id,
            ip_addr)
        except AttributeError as e:
            print "Looks a like a problem with the JSON message:%s" % (e)
            return
        #check if the device exists.
        device = self.stitch_device_table.get_device(device_id)
        if (device is not None):
            #update the IP address of the device 
            device.set_ip_addr(ip_addr)
            device.set_device_id(device_id)
            device.set_whitelist(white_list)
        else:
            device = StitchDevice(device_id = device_id,\
                ip6_addr = ip_addr)
            device.set_whitelist(white_list)
        self.update_device_in_dp(device) 
        


    def run(self):
        #open the TCP web service port. We might need to convert it to an SSL
        #socket at a later date.
        self.web_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.web_s.bind(('', self.web_port))
            #Don't expect connections from more than 1 web-service.
            self.web_s.listen(1)
            print "Stitch-cp web-service port ready to receive connections....."
            conn, addr = self.web_s.accept()
            print "Received connection from web-service %s" % (str(addr))
        except IOError as e:
            #print and error and return. Ideally we want to wait for 
            print "Web-service listen socket returned error %s" % (e)
            return

       #send the register to the web service
        
        #wait for updates from the web service
        tmp_json_data = ''
        json_data = '' 
        while (1):
            try:
                data = conn.recv(1024)
                if (data is None) or (len(data) == 0):
                    print "Closing connection to %s" % (str(addr))
                    conn.close()
                    print "Waiting for a new connection "
                    conn, addr = self.web_s.accept()


                #keep appending to the temporary JSON data till we 
                #receive end-of-message marker.
                tmp_json_data = "".join((tmp_json_data, data))
                print tmp_json_data

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
                
                
            






            
            






