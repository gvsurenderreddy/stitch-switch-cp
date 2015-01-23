import socket
import threading
import logging

class StitchClick:
    def __init__(self, ip_addr, click_port, buf_len):
        #open the TCP port
        self.click_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        self.buf_len = buf_len
        self.rlock = threading.RLock()
        self.stitch_device_table = "stitch_device_table"
        self.logger = logging.getLogger("StitchClick")
        self.logger.setLevel(logging.DEBUG)
        try:
            self.click_s.connect((ip_addr, click_port))
            self.click_s.setblocking(1)
            data = self.click_s.recv(self.buf_len)
            self.logger.debug(data)
        except IOError as e:
            self.logger.error("Unable to connect to click on IP %s:%d, error:(%d)%s"\
                % (ip_addr, click_port, e.strerror, e.errno))
            return None

    def add_device(self, device):
        command = "WRITE "+self.stitch_device_table+".add"+ " ID "+\
                   device.device_id+", IP6 "+str(device.ip6_addr) +"\r"
        data = self.send_command(command)
        self.logger.debug("Received response from dp %s" % (data))

    def send_command(self, command):
        #get the lock
        self.rlock.acquire()
        try:
            self.logger.debug("Trying to send command %s to CLICK"\
            %(command))
            self.click_s.sendall(command)
        except IOError as e:
            self.logger.error("Unable to send to click error:(%d)%s" %\
                (e.errno, e.strerror))
            self.rlock.release()
            return None

            #wait for the response. This is a blocking call
        try:
            data = self.click_s.recv(self.buf_len)
        except IOError as e:
            if (e.errno != -1):
                self.rlock.release()
                return None
            else:
                self.logger.error("Unable to receive from click, error: (%d)%s" % \
                    (e.errno, e.strerror))
                self.rlock.release()
                return None
        #release the lock
        self.rlock.release()
        return data

        
