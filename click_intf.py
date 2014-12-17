class StitchClick:
    def __init__(self, ip_addr, click_port, buf_len):
        #open the TCP port
        self.click_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        self.buf_len = buf_len
        try:
            click_s.connect((ip_addr, click_port))
            click_s.setblocking(1)
        except IOError as e:
            print "Unable to connect to click on IP %s:%d, error:(%d)%s"\
                % (ip_addr, click_port, e.strerror, e.errno)
            return None

    def send_command(self, command):
        try:
            click_s.sendall(command)
        except IOError as e:
            print "Unable to send to click error:(%d)%s" % (e.errno, e.strerror)
            return None

            #wait for the response. This is a blocking call
        try:
            data = click_s.recv(self.buf_len)
            print data
        except IOError as e:
            if (e.errno != -1):
                return None
            else:
                print "Unable to receive from click, error: (%d)%s" % \
                    (e.errno, e.strerror)
                return None
        return data

        
