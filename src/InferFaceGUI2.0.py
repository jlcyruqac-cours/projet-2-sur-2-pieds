import tkinter as tk                # python 3
import tkinter.messagebox
from tkinter import font as tkfont  # python 3
import sys
import time

sys.path.append("../vendor/most-voip-python3/python/src")

from frames.OnGoingCall import OnGoingCallPage
from frames.Dial import DialPage
from frames.Login import LoginPage

from most.voip.api import VoipLib
from most.voip.constants import VoipEvent

# The log level (greater values provide more information)
LogLevel = 99


class Uzim(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font30 = tkfont.Font(family='Helvetica', size=30, weight="bold")
        self.title_font25 = tkfont.Font(family='Helvetica', size=25, weight="bold")
        self.title_font15 = tkfont.Font(family='Helvetica', size=15, weight="bold")

        self.title("Uzim")

        # instantiate the lib
        self.my_voip = VoipLib()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {"LoginPage": LoginPage(parent=container, controller=self),
                       "DialPage": DialPage(parent=container, controller=self),
                       "OnGoingCallPage": OnGoingCallPage(parent=container, controller=self)}

        self.frames["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["DialPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["OnGoingCallPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_error(self, message):
        if isinstance(message, dict) and "error" in message:
            message = message["error"]
        tk.messagebox.showerror("Error", message)


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        print(page_name)
        frame = self.frames[page_name]
        frame.tkraise()

    def login_on_server(self, Username, Password, ServerIP):
        self.voip_params = {u'username': Username,  # a name describing the user
                            u'sip_server_address': ServerIP,
                            # the ip of the remote sip server (default port: 5060)
                            u'sip_server_user': Username,  # the username of the sip account
                            u'sip_server_pwd': Password,  # the password of the sip account
                            u'sip_server_transport': u'udp',  # the transport type (default: tcp)
                            u'log_level': LogLevel, # the log level (greater values provide more informations)
                            u'debug': False  # enable/disable debugging messages
                            }
        print(self.voip_params)

        # implement a method that will capture all the events triggered by the Voip Library
        def notify_events(voip_event_type, voip_event, params):
            print("Received Event Type:%s  Event:%s -> Params: %s" % (voip_event_type, voip_event, params))

            if "error" in params:
                self.show_error(params["error"])
                return

            self.frames["OnGoingCallPage"].update_status()

            # event triggered when the account registration has been confirmed by the remote Sip Server
            if (voip_event == VoipEvent.ACCOUNT_REGISTERED):
                print("Account %s registered: ready to accept call!" % self.my_voip.get_account().get_uri())

            # event triggered when a new call is incoming
            elif (voip_event == VoipEvent.CALL_INCOMING):
                print("INCOMING CALL From %s" % params["from"])
                self.show_frame("OnGoingCallPage")

            # event triggered when the call has been established
            elif (voip_event == VoipEvent.CALL_ACTIVE):
                print("The call with %s has been established" % self.my_voip.get_call().get_remote_uri())

            # events triggered when the call ends for some reasons
            elif (voip_event in [VoipEvent.CALL_REMOTE_DISCONNECTION_HANGUP, VoipEvent.CALL_REMOTE_HANGUP,
                                 VoipEvent.CALL_HANGUP]):
                print("End of call. Destroying lib...")
                # self.my_voip.destroy_lib()

            # event triggered when the library was destroyed
            elif (voip_event == VoipEvent.LIB_DEINITIALIZED):
                print("Call End. Exiting from the app.")
                end_of_call = True

            elif (voip_event == VoipEvent.CALL_DIALING):
                time.sleep(1)

            elif (voip_event == VoipEvent.LIB_INITIALIZATION_FAILED):
                print("Lib init failed. Destroying lib...")
                self.my_voip.destroy_lib()

            # just print informations about other events triggered by the library
            else:
                print("Received unhandled event type:%s --> %s" % (voip_event_type, voip_event))

        # Unregister account
        # self.my_voip.unregister_account()

        # Destroy lib
        self.my_voip.destroy_lib()

        # Recreate lib
        self.my_voip = VoipLib()

        # initialize the lib passing the dictionary and the callback method defined above:
        self.my_voip.init_lib(self.voip_params, notify_events)

        # register the account
        self.my_voip.register_account()


if __name__ == "__main__":
    app = Uzim()
    app.mainloop()