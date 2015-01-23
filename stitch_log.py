import logging
import sys


DEBUG='DEBUG'
INFO='INFO'
ERROR='ERROR'
WARNING='WARNING'
CRITICAL='CRITICAL'


def logger_init(filename):
    logging.basicConfig(filename=filename, level=logging.DEBUG,\
    format='%(asctime)s - %(name)s - %(levelname)s-\
        %(message)s', filemode='w')
    logging.info( "Stitch logger initialization complete")

def log_stitch(level, log_msg):
    if (level == INFO):
        logging.info(log_msg)
    elif (level == DEBUG):
        logging.debug(log_msg)
    elif (level == ERROR):
        logging.error(log_msg)
    elif (level == WARNING):
        logging.warning(log_msg)
    elif (level == CRITICAL):
        logging.critical(log_msg)
    else:
        print ("Unknown logging level used ... aborting ...")
        sys.exit(1)
#    except :
#        print "Error while writing to stitch log...exiting:%s" % sys.exc_info()[0] 
#        sys.exit(1)
    
