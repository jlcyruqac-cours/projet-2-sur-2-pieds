from tkinter import *
import tkinter.font as font

def raise_frame(frame):
    frame.tkraise()

class DialPage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        # Creation of init_window

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Uzim - DialNumber")

        myFont = font.Font(family='Helvetica', size=30, weight='bold')
        myFont1 = font.Font(family='Helvetica', size=15, weight='bold')

        dialNumber = StringVar
        e1 = Entry(root, width=8, textvariable=dialNumber)
        e1['font'] = myFont

        Button1= Button(root, text="1", command = self)
        Button1['font'] = myFont

        Button2 = Button(root, text="2", command = self)
        Button2['font'] = myFont

        Button3 = Button(root, text="3", command = self)
        Button3['font'] = myFont

        Button4 = Button(root, text="4", command = self)
        Button4['font'] = myFont

        Button5 = Button(root, text="5", command = self)
        Button5['font'] = myFont

        Button6 = Button(root, text="6", command = self)
        Button6['font'] = myFont

        Button7 = Button(root, text="7", command = self)
        Button7['font'] = myFont

        Button8 = Button(root, text="8", command = self)
        Button8['font'] = myFont

        Button9 = Button(root, text="9", command = self)
        Button9['font'] = myFont

        ButtonStar = Button(root, text="*", command = self)
        ButtonStar['font'] = myFont

        Button0 = Button(root, text="0", command = self)
        Button0['font'] = myFont

        ButtonH = Button(root, text="#", command = self)
        ButtonH['font'] = myFont

        ButtonSettings = Button(root, text="Setting", command=self)
        ButtonSettings['font'] = myFont1
        ButtonAPPEL = Button(root, text="APPEL", command=self)
        ButtonAPPEL['font'] = myFont1
        ButtonBV = Button(root, text="BV", command=self)
        ButtonBV['font'] = myFont1

        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)
        e1.grid(row=0, column=0, columnspan=3, sticky='EWNS')
        Button1.grid(row=1, column=0, columnspan=1, sticky='EWNS', pady=(10,0), padx=(5,10))
        Button2.grid(row=1, column=1, columnspan=1, sticky='EWNS', pady=(10,0), padx=(0,10))
        Button3.grid(row=1, column=2, columnspan=1, sticky='EWNS', pady=(10,0), padx=(0,5))
        Button4.grid(row=2, column=0, columnspan=1, sticky='EWNS', pady=(10,0), padx=(5,10))
        Button5.grid(row=2, column=1, columnspan=1, sticky='EWNS', pady=(10,0), padx=(0,10))
        Button6.grid(row=2, column=2, columnspan=1, sticky='EWNS', pady=(10,0), padx=(0,5))
        Button7.grid(row=3, column=0, columnspan=1, sticky='EWNS', pady=(10,0), padx=(5,10))
        Button8.grid(row=3, column=1, columnspan=1, sticky='EWNS', pady=(10,0), padx=(0,10))
        Button9.grid(row=3, column=2, columnspan=1, sticky='EWNS', pady=(10,0), padx=(0,5))
        ButtonStar.grid(row=4, column=0, columnspan=1, sticky='EWNS', pady=(10,5), padx=(5,10))
        Button0.grid(row=4, column=1, columnspan=1, sticky='EWNS', pady=(10,5), padx=(0,10))
        ButtonH.grid(row=4, column=2, columnspan=1, sticky='EWNS', pady=(10,5), padx=(0,5))
        ButtonSettings.grid(row=5, column=0, columnspan=1, sticky='EWNS', pady=(5, 5), padx=(0, 5))
        ButtonAPPEL.grid(row=5, column=1, columnspan=1, sticky='EWNS', pady=(5, 5), padx=(0, 5))
        ButtonBV.grid(row=5, column=2, columnspan=1, sticky='EWNS', pady=(5, 5), padx=(0, 5))

    def client_exit(self):
        exit()

    def setText(self):
        print("hello")
       #dialNumber.set()

class LoginPage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        # Creation of init_window

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Uzim - Login/Setting")

        myFont1 = font.Font(family='Helvetica', size=15, weight='bold')
        myFont2 = font.Font(family='Helvetica', size=25, weight='bold')

        varLogin = StringVar()
        labelLogin = Label(root, textvariable=varLogin, relief=RAISED)
        labelLogin['font'] = myFont1
        varLogin.set("Login : ")

        varPW = StringVar()
        labelPW = Label(root, textvariable=varPW, relief=RAISED)
        labelPW['font'] = myFont1
        varPW.set("Password : ")

        E_varLogin = StringVar()
        eLogin = Entry(root, width=8, textvariable=E_varLogin)
        eLogin['font'] = myFont2

        E_varPW = StringVar()
        ePW = Entry(root, width=8, textvariable=E_varPW)
        ePW['font'] = myFont2

        ButtonConnect = Button(root, text="Connexion",  command=lambda:raise_frame(DialPage))
        ButtonConnect['font'] = myFont1

        varRENVOI = StringVar()
        labelRENVOI = Label(root, textvariable=varRENVOI, relief=RAISED)
        labelRENVOI['font'] = myFont1
        varRENVOI.set("Renvoi d'appel : ")

        E_varRENVOI = StringVar()
        eRenvoi = Entry(root, width=8, textvariable=E_varRENVOI)
        eRenvoi['font'] = myFont2

        varIP = StringVar()
        labelIP = Label(root, textvariable=varIP, relief=RAISED)
        labelIP['font'] = myFont1
        varIP.set("Addresse IP : ")

        E_varIP = StringVar()
        eIP = Entry(root, width=8, textvariable=E_varIP)
        eIP['font'] = myFont1



        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)
        labelIP.grid(row=0, column=0, columnspan=1, sticky='EWNS', pady=(0, 0), padx=(0, 0))
        eIP.grid(row=0, column=1, columnspan=2, sticky='EWNS')
        labelLogin.grid(row=1, column=0, columnspan=1, sticky='EWNS', pady=(0, 0), padx=(0, 0))
        labelPW.grid(row=2, column=0, columnspan=1, sticky='EWNS', pady=(0, 0), padx=(0, 0))
        eLogin.grid(row=1, column=1, columnspan=2, sticky='EWNS')
        ePW.grid(row=2, column=1, columnspan=2, sticky='EWNS')
        ButtonConnect.grid(row=3, column=0, columnspan=2, sticky='EWNS', pady=(5, 5), padx=(5, 5))
        labelRENVOI.grid(row=4, column=0, columnspan=1, sticky='EWNS', pady=(0, 0), padx=(0, 0))
        eRenvoi.grid(row=4, column=1, columnspan=2, sticky='EWNS')




root = Tk()
root.resizable(0, 0)
app = LoginPage(root)
root.mainloop()