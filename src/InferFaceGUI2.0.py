import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3

#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font30 = tkfont.Font(family='Helvetica', size=30, weight="bold")
        self.title_font25 = tkfont.Font(family='Helvetica', size=25, weight="bold")
        self.title_font15 = tkfont.Font(family='Helvetica', size=15, weight="bold")

        self.title("Uzim")

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


class LoginPage(tk.Frame):

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
                                  command=lambda: controller.show_frame("DialPage"))

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