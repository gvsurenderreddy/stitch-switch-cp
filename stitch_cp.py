#!/usr/bin/python
#This script is a CLI interface to the flowswitch click datapath module. It can
#connect either through a TCP or UNIX socket to communicate with the CLICK
#driver tool to execute handlers.
import os
import sys
import socket
from optparse import OptionParser


#main function
if __name__=='__main__':

    parser = OptionParser(usage="%prog [options]")
    parser.add_option("-i", "--ip-address", action="store", type = "string",
            dest="click_ip", help="IP address used to connect to click",
            default="127.0.0.1")
    parser.add_option("-p","--port", action="store", type="int", 
            dest="click_port", 
            help="TCP port to connect to clik", default=5000)
    (options, args) = parser.parse_args()

    stitch_dp = StitchLick(options.click_ip, options.click_port, 4096)
    while (1):
        var = raw_input("stich-dp>")
        var += "\n"
        print "you entered", var
        data = stitch_dp.send_command(var)
        if (data is None):
            print "Lost connectivity to stitch DP.....!!"
            sys.exit(0)
        print data
        
