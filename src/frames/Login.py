import tkinter as tk
import tkinter.messagebox


class LoginPage(tk.Frame):
    def connexion(self):
        #print(self.Username.get())
        self.controller.login_on_server(self.Username.get(), self.Password.get(), self.ServerIP.get())
        self.controller.show_frame("DialPage")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(3, weight=1)

        self.Username = tk.StringVar()
        self.Password = tk.StringVar()
        self.ServerIP = tk.StringVar()

        tk.Label(self, text="IP Serveur :").grid(row=0, column=0, sticky="W", pady=(10, 0), padx=(10, 0))
        tk.Label(self, text="No Poste :").grid(row=1, column=0, sticky="W", pady=(10, 0), padx=(10, 0))
        tk.Label(self, text="Mot de passe :").grid(row=2, column=0, sticky="W", pady=(10, 0), padx=(10, 0))

        entry_server = tk.Entry(self, textvariable=self.ServerIP)
        entry_username = tk.Entry(self, textvariable=self.Username)
        entry_password = tk.Entry(self, textvariable=self.Password, show="*")

        entry_server.grid(row=0, column=1, sticky=("S", "E", "W"), padx=(0, 10))
        entry_username.grid(row=1, column=1, sticky=("S", "E", "W"), padx=(0, 10))
        entry_password.grid(row=2, column=1, sticky=("S", "E", "W"), padx=(0, 10))

        buttonConnect = tk.Button(self, text="Connexion", command=lambda: self.connexion())
        buttonConnect.grid(row=3, columnspan=2, sticky=("S", "E", "W", "N"), padx=(10, 10), pady=(10, 10))
