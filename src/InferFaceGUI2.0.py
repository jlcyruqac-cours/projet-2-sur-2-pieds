import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import sys
sys.path.append("../vendor/most-voip-python3/python/src")

# import the Voip Librarye

from most.voip.api import VoipLib
from most.voip.constants import VoipEvent

#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

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

        self.frames = {}
        self.frames["LoginPage"] = LoginPage(parent=container, controller=self)
        self.frames["DialPage"] = DialPage(parent=container, controller=self)
        self.frames["OnGoingCallPage"] = OnGoingCallPage(parent=container, controller=self)

        self.frames["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["DialPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["OnGoingCallPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def login_on_server(self):
        self.voip_params = {u'username': u'1000',  # a name describing the user
                            u'sip_server_address': u'172.16.12.42',
                            # the ip of the remote sip server (default port: 5060)
                            u'sip_server_user': u'1000',  # the username of the sip account
                            u'sip_server_pwd': u'12345',  # the password of the sip account
                            u'sip_server_transport': u'udp',  # the transport type (default: tcp)
                            u'log_level': 1,  # the log level (greater values provide more informations)
                            u'debug': False  # enable/disable debugging messages
                            }
        import time
        end_of_call = False  # used as exit condition from the while loop at the end of this example

        # implement a method that will capture all the events triggered by the Voip Library
        def notify_events(voip_event_type, voip_event, params):
            print("Received Event Type:%s  Event:%s -> Params: %s" % (voip_event_type, voip_event, params))

            # event triggered when the account registration has been confirmed by the remote Sip Server
            if (voip_event == VoipEvent.ACCOUNT_REGISTERED):
                print("Account %s registered: ready to accept call!" % self.my_voip.get_account().get_uri())

            # event triggered when a new call is incoming
            elif (voip_event == VoipEvent.CALL_INCOMING):
                print("INCOMING CALL From %s" % params["from"])
                time.sleep(2)
                print("Answering...")
                self.my_voip.answer_call()

            # event triggered when the call has been established
            elif (voip_event == VoipEvent.CALL_ACTIVE):
                print("The call with %s has been established" % self.my_voip.get_call().get_remote_uri())

                dur = 4
                print("Waiting %s seconds before hanging up..." % dur)
                time.sleep(dur)
                self.my_voip.hangup_call()



            # events triggered when the call ends for some reasons
            elif (voip_event in [VoipEvent.CALL_REMOTE_DISCONNECTION_HANGUP, VoipEvent.CALL_REMOTE_HANGUP,
                                 VoipEvent.CALL_HANGUP]):
                print("End of call. Destroying lib...")
                self.my_voip.destroy_lib()

            # event triggered when the library was destroyed
            elif (voip_event == VoipEvent.LIB_DEINITIALIZED):
                print("Call End. Exiting from the app.")
                end_of_call = True

            # just print informations about other events triggered by the library
            else:
                print("Received unhandled event type:%s --> %s" % (voip_event_type, voip_event))

        # initialize the lib passing the dictionary and the callback method defined above:
        self.my_voip.init_lib(self.voip_params, notify_events)

        # register the account
        self.my_voip.register_account()

        #while (end_of_call == False):
         #   time.sleep(2)


class LoginPage(tk.Frame):

    def connexion(self):
        self.controller.login_on_server()
        self.controller.show_frame("DialPage")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        tk.Label(self, text="IP Serveur :").grid(row=0, column=0, sticky="W", pady=(10, 0), padx=(10, 0))
        tk.Label(self, text="No Poste :").grid(row=1, column=0, sticky="W", pady=(10, 0), padx=(10, 0))
        tk.Label(self, text="Mot de passe :").grid(row=2, column=0, sticky="W", pady=(10, 0), padx=(10, 0))

        e0 = tk.Entry(self)
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e0.grid(row=0, column=1, sticky=("S", "E", "W"), padx=(0, 10))
        e1.grid(row=1, column=1, sticky=("S", "E", "W"), padx=(0, 10))
        e2.grid(row=2, column=1, sticky=("S", "E", "W"), padx=(0, 10))

        buttonConnect = tk.Button(self, text="Connexion",
                                  command=lambda: self.connexion())

        buttonConnect.grid(row=3, columnspan=2)

        tk.Label(self, text="Renvoie Appel : ").grid(row=4, column=0, sticky="W", pady=(10, 0), padx=(10, 0))


        e1 = tk.Entry(self)


        e1.grid(row=4, column=1, sticky=("S", "E", "W"), padx=(0, 10))

        buttonSave = tk.Button(self, text="Save",
                                  command=self)

        buttonSave.grid(row=5, columnspan=2)




class DialPage(tk.Frame):


    def enterNumber(self, number):
        print(number)
        self.TextNumber.set(self.TextNumber.get() + number)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.TextNumber = tk.StringVar()

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        e1 = tk.Entry(self)

        e1.grid(row=0, column=1, sticky=("S", "E", "W"), padx=(0, 0))

        buttonConnect = tk.Button(self, text="Appel",
                                  command=lambda: controller.show_frame("OnGoingCallPage"))

        buttonConnect.grid(row=2, columnspan=2)

        buttonConnect = tk.Button(self, text="Setting",
                                  command=lambda: controller.show_frame("LoginPage"))

        buttonConnect.grid(row=3, columnspan=2)



class OnGoingCallPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="OnGoingCall").grid(row=0, column=0, sticky="W", pady=(0, 0), padx=(0, 0))

        buttonAnswer = tk.Button(self, text="Repondre",
                                 command=self)

        buttonAnswer.grid(row=1, columnspan=2)
        buttonEndCall = tk.Button(self, text="End Call",
                               command=lambda: controller.show_frame("DialPage"))

        buttonEndCall.grid(row=2, columnspan=2)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()