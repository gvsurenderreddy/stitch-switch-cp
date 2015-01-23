import os
import sys
import threading
import logging



class StitchDPCLI(threading.Thread):

    def __init__(self, stitch_dp):
        super(StitchDPCLI, self).__init__()
        self.stitch_dp = stitch_dp
        self.logger = logging.getLogger("StitchDPCLI")
        self.logger.setLevel(logging.DEBUG)

    def run(self):
         while (1):
            var = raw_input("stich-dp>")
            if (var == "exit"):
                sys.exit(0)
            var += "\n"
            self.logger.debug("command:%s" % var)
            #send the command to the DP
            ret = self.stitch_dp.send_command(var)
            print ret

