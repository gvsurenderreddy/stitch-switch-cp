import os
import sys
import threading


class StitchDPCLI(threading.Thread):

    def __init__(self):
        super(StitchDPCLI, self).__init__()

    def run(self):
         while (1):
            var = raw_input("stich-dp>")
            if (var == "exit"):
                sys.exit(0)
            var += "\n"
            print "you entered", var

