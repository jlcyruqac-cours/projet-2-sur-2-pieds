import pjsua

# add the most.voip library root dir to the current python path...
import sys
sys.path.append("../vendor/most-voip/python/src")

# import the Voip Library
from most.voip.api import VoipLib

# instantiate the lib
my_voip = VoipLib()

# build a dictionary containing all parameters needed for the Lib initialization

voip_params = {  u'username': u'1000',  # a name describing the user
                 u'sip_server_address': u'192.168.1.183',  # the ip of the remote sip server (default port: 5060)
                 u'sip_server_user': u'1000', # the username of the sip account
                 u'sip_server_pwd': u'12345',  #  the password of the sip account
                 u'sip_server_transport' :u'udp', # the transport type (default: tcp)
                 u'log_level' : 1,  # the log level (greater values provide more informations)
                 u'debug' : False  # enable/disable debugging messages
                 }


print(voip_params)


# define a method used for receive event notifications from the lib:
def notify_events(voip_event_type, voip_event, params):
    print "Received Event Type:%s -> Event: %s Params: %s" % (voip_event_type, voip_event, params)


# initialize the lib passing the dictionary and the callback method defined above:
my_voip.init_lib(voip_params, notify_events)
print(my_voip.register_account())


my_extension = "1234"
my_voip.make_call(my_extension)

import time
# wait until the call is active
while(True):
    time.sleep(1)
