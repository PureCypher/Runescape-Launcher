#    Copyright 2022 Runescape-Launcher contributors
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import tkinter as tk
from tkinter.messagebox import showerror
from tkinter import ttk
from sys import platform
import os
from time import sleep
import subprocess
import sqlite3
from cryptography.fernet import Fernet

class Application(tk.Frame):   
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title("Runescape Launcher")
        self.master.geometry('400x300+400+400') #self.master.geometry('300x200+400+400')
        self.master.protocol("WM_DELETE_WINDOW", self.quit)
        self.master.attributes('-topmost', True)

    def create_widgets(self):
        tabControl = ttk.Notebook(root) 
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)

        tabControl.add(tab1, text ='Start')
        tabControl.add(tab2, text ='Manager') 
        tabControl.pack(expand = 1, fill ="both")

        Launch = ttk.Label(tab1, text="Launch Runescape")                                  
        Launch.grid(row=1, column=1, pady=20, sticky="n")                         
        EnLaunch = ttk.Entry(tab1)                                                 
        EnLaunch.grid(row=1, column=2, pady=20, padx=5, sticky="w")      

        def sleepy_time():
            sleep(slider.get())

        def WindowOS_Launcher(accountAmount):
            print(accountAmount)
            try:
                amount = int(accountAmount)
            except ValueError:
                showerror(title='Erro', message=f'Please input a number not {str(accountAmount)}')
            else:
                print(f'Launching {amount} Runescape clients')
                clients = int(amount / 15)
                for mainLoop in range(int(amount)):
                    os.startfile("rs-launch://www.runescape.com/k=5/l=$(Language:0)/jav_config.ws")
                    sleep(5)
                    if mainLoop == 16:
                        if clients != 0:
                            # specify your cmd command
                            try:
                                cmdCommand = "C:\\Program Files\\LockHunter\\Lockhunter.exe -d -sm -x C:\\ProgramData\\Jagex\\launcher\\instance.lock"
                                subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                                sleep(10)
                                amount -= 1
                            except Exception as e:
                                print(e)

        def linux_os_launcher(accountAmount):
            try:
                amount = int(accountAmount)
            except ValueError:
                print(f'Please input a number not {str(accountAmount)}')
            else:
                for mainLoop in range(amount):
                    subprocess.Popen('runescape-launcher') # This should launch runescape launcher on Debian distros, Using the Download guide of runescape.com/download
                    sleep(5)
                    for client in range(int(amount /15)):
                        user = os.uname()
                        pathfind = "/home/" + str(user[1]).lower() + "/Jagex/launcher/instance.lock"
                        os.remove(pathfind)

        def mac_os_launcher(accountAmount):
            try:
                amount = int(accountAmount)
            except ValueError:
                showerror(title='Erro', message=f'Please input a number not {str(accountAmount)}')
            else:
                for mainLoop in range(amount):
                    os.system("open -n -a Runescape")
                    sleep(5)
                    for client in range(int(amount / 15)):
                        user = os.uname()
                        pathfind = "/User/" + str(user[1]).lower() + "/Jagex/launcher/instance.lock"
                        os.remove(pathfind)

        def runescape():
            amount = EnLaunch.get()
            if platform == "linux":
                linux_os_launcher(amount)
            elif platform == "darwin":
                mac_os_launcher(amount)
            elif platform == "win32":               
                WindowOS_Launcher(amount)

        slider = tk.Scale(tab1, orient="horizontal", from_=0, to=60) 
        slider.grid(row=2, column=1)

        launch = tk.Button(tab1, text="Launch", command=runescape)
        launch.grid(row=2, column=2, pady=10, ipadx=20, sticky="n")

        quit = tk.Button(tab1, text="Cancel", command=self.master.quit)
        quit.grid(row=3, column=2, pady=10, ipadx=20, sticky="n")

        def load_key():
            '''
            Account Storage tab
            '''
            username = os.getenv('username')
            if os.path.exists(f"C:\\Users\\{username}\\AppData\\Local\\secret.key"):
                file = open(f"C:\\Users\\{username}\\AppData\\Local\\secret.key", "rb")
                
                return file.read()
            else:
                new_key()

        def new_key():
            """
            Generates a key and save it into a file
            """

            key = Fernet.generate_key()
            with open(f"C:\\Users\\{username}\\AppData\\Local\\secret.key", "wb") as key_file:
                key_file.write(key)
            load_key()

        def encrypt(message):
            '''encrypt'''
            message = str.encode(message)
            key = load_key()
            e = Fernet(key)
            enCrypt = e.encrypt(message)
            return enCrypt

        def decrypt(message):
            '''decrypt'''
            key = load_key()
            f = Fernet(key)
            DeCrypted = f.decrypt(message)
            return DeCrypted

        
        def add_acc(email, password):
            '''
            Show Account database
            '''
            if email and password:
                username = os.getenv('username')
                conn = sqlite3.connect(f"C:\\Users\\{username}\\AppData\\Roaming\\important.db")
                c = conn.cursor()
                
                c.execute("INSERT INTO account (email, password) VALUES (?, ?)", (encrypt(email), encrypt(password)))
                conn.commit()
            else:
                showerror(title='Error', message='Please put something in both input fields')

        def sql_data():
            username = os.getenv('username')
            if os.path.exists(f"C:\\Users\\{username}\\AppData\\Roaming\\important.db"):
                conn = sqlite3.connect(f"C:\\Users\\{username}\\AppData\\Roaming\\important.db")
                c = conn.cursor()
                
                x = 3
                y = 3
                zSize = self.master.winfo_height()

                Email = tk.Label(tab2, text='Email : ')
                Email.grid(row=0, column=0)
                EmailInput = ttk.Entry(tab2)
                EmailInput.grid(row=0, column=1, pady=10) 

                Pass = tk.Label(tab2, text='Password : ')
                Pass.grid(row=1, column=0)
                PassInput = ttk.Entry(tab2)
                PassInput.grid(row=1, column=1, pady=10) 

                EmailHeader = tk.Label(tab2, text='Email :')
                EmailHeader.grid(column=0, row=2, ipadx=20, padx=20)

                PassHeader = tk.Label(tab2, text='Password :')
                PassHeader.grid(column=1, row=2, ipadx=20, padx=20)
                passEr = lambda: add_acc(EmailInput.get(), PassInput.get())
                Input = ttk.Button(tab2, text='Add account', command=passEr)
                Input.grid(row=0, column=2, sticky='w')
                
                canvas = tk.Canvas(tab2, width=tab2.winfo_width(), height=tab2.winfo_height())
                canvas.grid(column=0, row=4, rowspan=10)

                Scroll = tk.Scrollbar(tab2, orient='vertical')
                Scroll.config(command=canvas.yview)
                canvas.config(yscrollcommand=Scroll.set)
                Scroll.grid(row=4, column=2, rowspan=10, sticky='nse')

                emailResult = c.execute('''SELECT email FROM account;''')
                
                for email in emailResult:
                    email = email[0]
                    Wmail = tk.Label(canvas, text=decrypt(email))
                    Wmail.grid(column=0, row=x, padx=20)
                    x += 1
                
                passResult = c.execute('''SELECT password FROM account;''')
                
                for passw in passResult:
                    passw = passw[0]
                    Passw = tk.Label(canvas, text=decrypt(passw))
                    Passw.grid(column=1, row=y, padx=20)
                    y += 1
                
            else:
                conn = sqlite3.connect(f"C:\\Users\\{username}\\AppData\\Roaming\\important.db")
                c = conn.cursor()
                c.execute('''CREATE TABLE account (email text, password text)''')
                conn.commit()
                conn.close()
                sql_data()

        sql_data()
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
