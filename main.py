import tkinter as tk
from tkinter import ttk
from sys import platform
import os
from time import sleep
import subprocess


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.geometry('300x150+100+100')

    def create_widgets(self):
        self.Launch = tk.Label(self, text="Launch Runescape")                                  
        self.Launch.grid(row=1, column=1, pady=20, sticky="n")                         
        self.EnLaunch = tk.Entry(self)                                                 
        self.EnLaunch.grid(row=1, column=2, pady=20, ipadx=20, sticky="w")           
        
        def sleepy_time():
            sleep(self.slider.get())
                        
        def WindowOS_Launcher(accountAmount):
            try:
                amount = int(accountAmount)
            except ValueError:
                print(f'Please input a number not {str(accountAmount)}')
            else:
                print(f'Launching {amount} Runescape clients')
                for mainLoop in range(int(amount)):
                    os.startfile("rs-launch://www.runescape.com/k=5/l=$(Language:0)/jav_config.ws")
                    sleep(30)
                    for client in range(int(amount /15)):
                        # specify your cmd command
                        cmdCommand = "C:\\Program Files\\LockHunter\\Lockhunter.exe -d -sm -x C:\\ProgramData\\Jagex\\launcher\\instance.lock"
                        subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)

        def LinuxOS_Launcher(accountAmount):
            try:
                amount = int(accountAmount)
            except ValueError:
                print(f'Please input a number not {str(accountAmount)}')
            else:
                for mainLoop in range(amount):
                    subprocess.Popen('runescape-launcher') # This should launch runescape launcher on Debian distros, Using the Download guide of Runescape.com/download
                    sleep(30)
                    for client in range(int(amount /15)):
                        user = os.uname()
                        pathfind = "/home/" + str(user[1]).lower() + "/Jagex/launcher/instance.lock"
                        os.remove(pathfind)

        def MacOs_Launcher(accountAmount):
            try:
                amount = int(accountAmount)
            except ValueError:
                print(f'Please input a number not {str(accountAmount)}')
            else:
                for mainLoop in range(amount):
                    os.system("open -n -a Runescape")
                    sleep(30)
                    for client in range(int(amount / 15)):
                        user = os.uname()
                        pathfind = "/User/" + str(user[1]).lower() + "/Jagex/launcher/instance.lock"
                        os.remove(pathfind)
                        
        def Runescape():
            amount = self.EnLaunch.get()
            if platform == "linux":
                LinuxOS_Launcher(amount)
            elif platform == "darwin":
                MacOs_Launcher(amount)
            elif platform == "win32":
                WindowOS_Launcher(amount)

        self.slider = tk.Scale(self, orient="horizontal", from_=0, to=60) 
        self.slider.grid(row=2, column=1)

        self.launch = tk.Button(self, text="Launch", command=Runescape)
        self.launch.grid(row=2, column=2, pady=10, ipadx=20, sticky="n")
        
        self.quit = tk.Button(self, text="Cancel", command=self.master.destroy)
        self.quit.grid(row=3, column=2, pady=10, ipadx=20, sticky="n")
        
root = tk.Tk()
root.title("Runescape Launcher")
app = Application(master=root)
app.mainloop()
