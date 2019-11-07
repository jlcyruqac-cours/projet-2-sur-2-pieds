from tkinter import *
import tkinter.font as font



class Window(Frame):



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        # Creation of init_window

    def init_window(self):
        # changing the title of our master widget
        self.master.title(" Uzim")

        ################################
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)
        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")
        # added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)
        ############################

        myFont = font.Font(family='Helvetica', size=30, weight='bold')

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

    def client_exit(self):
        exit()

    def setText(self):
        print("hello")
       #dialNumber.set()







root = Tk()

root.resizable(0, 0)
app = Window(root)
root.mainloop()