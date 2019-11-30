import tkinter as tk
import tkinter.messagebox


class DialPage(tk.Frame):
    def enter_number(self, number):
        self.TextNumber.set(self.TextNumber.get() + number)

    def backspace(self):
        self.TextNumber.set(self.TextNumber.get().strip())
        pass

    def make_call(self):
        extension = self.TextNumber.get()
        if extension == "":
            return

        if self.controller.my_voip.make_call(extension):
            self.controller.show_frame("OnGoingCallPage")
            self.TextNumber.set("")
        else:
            tk.messagebox.showwarning("Warning", "Call failed.")

    def setup_ui(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        button_1 = tk.Button(self, text="1")
        button_1.grid(row=1, column=0, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 0))
        button_2 = tk.Button(self, text="2")
        button_2.grid(row=1, column=1, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 0))
        button_3 = tk.Button(self, text="3")
        button_3.grid(row=1, column=2, sticky=("N", "S", "E", "W"), padx=(10, 10), pady=(10, 0))

        button_4 = tk.Button(self, text="4")
        button_4.grid(row=2, column=0, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 0))
        button_5 = tk.Button(self, text="5")
        button_5.grid(row=2, column=1, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 0))
        button_6 = tk.Button(self, text="6")
        button_6.grid(row=2, column=2, sticky=("N", "S", "E", "W"), padx=(10, 10), pady=(10, 0))

        button_7 = tk.Button(self, text="7")
        button_7.grid(row=3, column=0, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 0))
        button_8 = tk.Button(self, text="8")
        button_8.grid(row=3, column=1, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 0))
        button_9 = tk.Button(self, text="9")
        button_9.grid(row=3, column=2, sticky=("N", "S", "E", "W"), padx=(10, 10), pady=(10, 0))

        button_asterisk = tk.Button(self, text="*")
        button_asterisk.grid(row=4, column=0, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 0))
        button_0 = tk.Button(self, text="0")
        button_0.grid(row=4, column=1, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 0))
        button_pound = tk.Button(self, text="#")
        button_pound.grid(row=4, column=2, sticky=("N", "S", "E", "W"), padx=(10, 10), pady=(10, 0))

        button_settings = tk.Button(self, text="Settings")
        button_settings.grid(row=5, column=0, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 10))
        button_call = tk.Button(self, text="Call")
        button_call.grid(row=5, column=1, sticky=("N", "S", "E", "W"), padx=(10, 0), pady=(10, 10))
        button_backspace = tk.Button(self, text="<")
        button_backspace.grid(row=5, column=2, sticky=("N", "S", "E", "W"), padx=(10, 10), pady=(10, 10))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.TextNumber = tk.StringVar()

        self.setup_ui()

        e1 = tk.Entry(self, textvariable=self.TextNumber)
        e1.grid(row=0, column=0, columnspan=3, sticky=("N", "S", "E", "W"), padx=(10, 10), pady=(10, 0))

        '''
        buttonConnect = tk.Button(self, text="Appel",
                                  command=lambda: self.makeCall())
        buttonConnect.grid(row=2, columnspan=2)
        buttonConnect = tk.Button(self, text="Setting",
                                  command=lambda: controller.show_frame("LoginPage"))
        buttonConnect.grid(row=3, columnspan=2)
        '''
