import tkinter as tk
import tkinter.messagebox


class OnGoingCallPage(tk.Frame):
    def endCall(self):
        # print("Hagning up call")
        # print(self.controller.my_voip)
        self.controller.my_voip.hangup_call()
        self.controller.show_frame("DialPage")

    def answer_call(self):
        self.controller.my_voip.answer_call()
        # self.update_status()

    def update_status(self):
        call = self.controller.my_voip.get_call()
        if call:
            self.status.set(call.get_state())

    def hold_call(self):
        self.controller.my_voip.hold_call()

    def unhold_call(self):
        self.controller.my_voip.unhold_call()

    def send_dtmf(self):
        self.controller.my_voip.send_the_mf(self.DTMF.get())

    def setup_ui(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)

        self.columnconfigure(0, weigh=1)
        self.columnconfigure(1, weigh=1)

        label_title = tk.Label(self, text="Ongoing Call")
        label_title.grid(row=0, column=0, columnspan=2, sticky=("N", "S", "E", "W"), pady=(10, 0), padx=(10, 10))

        label_status = tk.Label(self, textvariable=self.status)
        label_status.grid(row=1, column=0, columnspan=2, sticky=("N", "S", "E", "W"), pady=(10, 0), padx=(10, 10))

        button_answer = tk.Button(self, text="Answer Call", command=lambda: self.answer_call())
        button_answer.grid(row=2, column=0, sticky=("N", "S", "E", "W"), pady=(10, 0), padx=(10, 10))

        button_end_call = tk.Button(self, text="End Call", command=lambda: self.endCall())
        button_end_call.grid(row=2, column=1, sticky=("N", "S", "E", "W"), pady=(10, 0), padx=(0, 10))

        button_hold = tk.Button(self, text="Hold Call", command=lambda: self.hold_call())
        button_hold.grid(row=3, column=0, sticky=("N", "S", "E", "W"), pady=(10, 0), padx=(10, 10))

        button_unhold = tk.Button(self, text="Unhold Call", command=lambda: self.unhold_call())
        button_unhold.grid(row=3, column=1, sticky=("N", "S", "E", "W"), pady=(10, 0), padx=(0, 10))

        entry_dtmf = tk.Entry(self, textvariable=self.DTMF)
        entry_dtmf.grid(row=4, column=0, sticky=("E", "W"), pady=(10, 0), padx=(10, 10))

        button_send_dtmf = tk.Button(self, text="Send DTMF", command=lambda: self.send_dtmf())
        button_send_dtmf.grid(row=4, column=1, sticky=("E", "W"), pady=(10, 0), padx=(0, 10))

        # button_back = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("DialPage"))
        # button_back.grid(row=6, column=0, columnspan=2)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # print(self.controller.Appel1.get_state())
        # print(self.controller.Appel1.get_remote_uri())

        # self variables
        self.DTMF = tk.StringVar()
        self.status = tk.StringVar()

        self.setup_ui()
        self.update_status()
