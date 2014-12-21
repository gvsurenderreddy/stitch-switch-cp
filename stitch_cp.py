#!/usr/bin/python
#This script is a CLI interface to the flowswitch click datapath module. It can
#connect either through a TCP or UNIX socket to communicate with the CLICK
#driver tool to execute handlers.
import os
import sys
import socket
from optparse import OptionParser
from click_intf import StitchClick
from stitch_webservice_intf import StitchWebService
from stitch_device import StitchDeviceTable
from stitch_dp_cli import StitchDPCLI


#main function
if __name__=='__main__':

    parser = OptionParser(usage="%prog [options]")
    parser.add_option("-i", "--ip-address", action="store", type = "string",
            dest="click_ip", help="IP address used to connect to click",
            default="127.0.0.1")
    parser.add_option("-p","--port", action="store", type="int", 
            dest="click_port", 
            help="TCP port to connect to clik", default=5000)
    parser.add_option("-w","--web-service-ip", action="store", type="string", 
            dest="web_service_ip", 
            help="IP address of stitch-web-service", default="127.0.0.1")
    parser.add_option("-s","--web-service-port", action="store", type="int", 
            dest="web_service_port", 
            help="IP address of stitch-web-service", default="52000")
    (options, args) = parser.parse_args()

    stitch_table = StitchDeviceTable()
    stitch_dp = StitchClick(options.click_ip, options.click_port, 4096)
    #web-service
    stitch_ws = StitchWebService(ip_addr = options.web_service_ip,\
        web_port = options.web_service_port,\
        stitch_dp = stitch_dp,\
        stitch_device_table = stitch_table)

    cli = StitchDPCLI()

    #start the threads.
    stitch_ws.daemon = True
    stitch_ws.start()
    cli.start()
    #check if either of the threads are alive
    cli.join()
    print "CLI has exited, the ending stitch-cp ....."
    sys.exit(0)
    
        
