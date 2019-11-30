import tkinter as tk
import tkinter.messagebox


class OnGoingCallPage(tk.Frame):
    def endCall(self):
        print("Hagning up call")
        print(self.controller.my_voip)
        self.controller.my_voip.hangup_call()

    def answer_call(self):
        self.controller.my_voip.answer_call()
        # self.update_status()

    def update_status(self):
        pass

    def hold_call(self):
        self.controller.my_voip.hold_call()

    def unhold_call(self):
        self.controller.my_voip.unhold_call()

    def send_dtmf(self):
        print(self.DTMF.get())
        self.controller.my_voip.send_the_mf(self.DTMF.get())

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # print(self.controller.Appel1.get_state())
        # print(self.controller.Appel1.get_remote_uri())

        tk.Label(self, text="OnGoingCall").grid(row=0, column=0, sticky="W", pady=(10, 0), padx=(10, 10))
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

        self.DTMF = tk.StringVar()
        entry_dtmf = tk.Entry(self, textvariable=self.DTMF)
        entry_dtmf.grid(row=7, column=0, columnspan=2)

        buttonSendDTMF = tk.Button(self, text="Send the MF", command=lambda: self.send_dtmf())
        buttonSendDTMF.grid(row=8, column=0, columnspan=2)