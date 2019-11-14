import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font30 = tkfont.Font(family='Helvetica', size=30, weight="bold")
        self.title_font25 = tkfont.Font(family='Helvetica', size=25, weight="bold")
        self.title_font15 = tkfont.Font(family='Helvetica', size=15, weight="bold")

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


       # button2 = tk.Button(self, text="Go to Page Two",
                            #command=lambda: controller.show_frame("PageTwo"))

        #button2.pack()

        labelLogin = tk.Label(self, text="Login", font=controller.title_font15)
        labelLogin.pack(side="top", fill="x")
        eLogin = tk.Entry(self, width=8, textvariable='TextLogin', font=controller.title_font30)
        eLogin.pack(side="top", fill="x")
        labelPW = tk.Label(self, text="PassWord", font=controller.title_font15)
        labelPW.pack(side="top", fill="x")
        ePW = tk.Entry(self, width=8, textvariable='TextPW', font=controller.title_font30)
        ePW.pack(side="top", fill="x")



        buttonConnect = tk.Button(self, text="Connexion",
                            command=lambda: controller.show_frame("DialPage"), font=controller.title_font30)
        buttonConnect.pack()


class DialPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is DialPage", font=controller.title_font30)
        label.pack(side="top", fill="x", pady=10)


        eAppel = tk.Entry(self, width=8, textvariable='TextNumber', font=controller.title_font30)
        eAppel.pack(side="top", fill="x")

        buttonAppel = tk.Button(self, text="Appel", font=controller.title_font25,
                           command=lambda: controller.show_frame("OnGoingCallPage"))
        buttonAppel.pack()

        buttonSetting = tk.Button(self, text="Setting", font=controller.title_font15,
                           command=lambda: controller.show_frame("LoginPage"))
        buttonSetting.pack()


class OnGoingCallPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is OnGoingCall Page", font=controller.title_font30)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to DialPage",
                           command=lambda: controller.show_frame("DialPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()