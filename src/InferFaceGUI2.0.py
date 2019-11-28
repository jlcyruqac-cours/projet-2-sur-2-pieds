import tkinter as tk                # python 3
import tkinter.messagebox
from tkinter import font as tkfont  # python 3
import sys
import time
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

        self.frames = {"LoginPage": LoginPage(parent=container, controller=self),
                       "DialPage": DialPage(parent=container, controller=self),
                       "OnGoingCallPage": OnGoingCallPage(parent=container, controller=self)}

        self.frames["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["DialPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["OnGoingCallPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_error(self, message):
        if "error" in message:
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
                            u'log_level': 99,  # the log level (greater values provide more informations)
                            u'debug': False  # enable/disable debugging messages
                            }
        print(self.voip_params)
        end_of_call = False  # used as exit condition from the while loop at the end of this example

        # implement a method that will capture all the events triggered by the Voip Library
        def notify_events(voip_event_type, voip_event, params):
            print("Received Event Type:%s  Event:%s -> Params: %s" % (voip_event_type, voip_event, params))

            if "error" in params:
                self.show_error(params["error"])
                return

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
        #print(self.Username.get())
        self.controller.login_on_server(self.Username.get(), self.Password.get(), self.ServerIP.get())
        self.controller.show_frame("DialPage")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        print("init login")

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        self.Username = tk.StringVar()
        self.Password = tk.StringVar()
        self.ServerIP = tk.StringVar()

        tk.Label(self, text="IP Serveur :").grid(row=0, column=0, sticky="W", pady=(10, 0), padx=(10, 0))
        tk.Label(self, text="No Poste :").grid(row=1, column=0, sticky="W", pady=(10, 0), padx=(10, 0))
        tk.Label(self, text="Mot de passe :").grid(row=2, column=0, sticky="W", pady=(10, 0), padx=(10, 0))

        e0 = tk.Entry(self, textvariable=self.ServerIP)
        e1 = tk.Entry(self, textvariable=self.Username)
        e2 = tk.Entry(self, textvariable=self.Password)

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

    def makeCall(self):
        extension = self.TextNumber.get()
        if extension == "":
            return

        if self.controller.my_voip.make_call(extension):
            self.controller.show_frame("OnGoingCallPage")
            self.TextNumber.set("")
        else:
            tk.messagebox.showwarning("Warning", "Call failed.")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.TextNumber = tk.StringVar()

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        e1 = tk.Entry(self, textvariable=self.TextNumber)

        e1.grid(row=0, column=1, sticky=("S", "E", "W"), padx=(0, 0))

        buttonConnect = tk.Button(self, text="Appel",
                                  command=lambda: self.makeCall())

        buttonConnect.grid(row=2, columnspan=2)

        buttonConnect = tk.Button(self, text="Setting",
                                  command=lambda: controller.show_frame("LoginPage"))

        buttonConnect.grid(row=3, columnspan=2)



class OnGoingCallPage(tk.Frame):

    def endCall(self):
        print("Hagning up call")
        print(self.controller.my_voip)
        self.controller.my_voip.hangup_call()

    def answer_call(self):
        self.controller.my_voip.answer_call()
        # self.update_status()

    def update_status(self):
        return

    def hold_call(self):
        self.controller.my_voip.hold_call()

    def unhold_call(self):
        self.controller.my_voip.unhold_call()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # print(self.controller.Appel1.get_state())
        # print(self.controller.Appel1.get_remote_uri())

        tk.Label(self, text="OnGoingCall").grid(row=0, column=0, sticky="W", pady=(0, 0), padx=(0, 0))
        self.etat = tk.Label(self, text="---")
        self.etat.grid(row=1, column=0, sticky="W", pady=(0, 0), padx=(0, 0))

        self.update_status()

        buttonAnswer = tk.Button(self, text="Repondre", command=lambda: self.answer_call())
        buttonAnswer.grid(row=2, column=0)

        btnHold = tk.Button(self, text="Hold", command=lambda: self.hold_call())
        btnHold.grid(row=3, column=0)

        btnUnhold = tk.Button(self, text="Unhold", command=lambda: self.unhold_call())
        btnUnhold.grid(row=4, column=0)

        buttonEndCall = tk.Button(self, text="End Call", command=lambda: self.endCall())
        buttonEndCall.grid(row=5, column=0)

        buttonRetour = tk.Button(self, text="Back", command=lambda: controller.show_frame("DialPage"))
        buttonRetour.grid(row=6, column=0, columnspan=2)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()