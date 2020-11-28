#!/usr/bin/env python

import tkinter as tk
import platform,socket,re,uuid,logging,psutil


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.geometry("500x200")
        self.master.title("Code checker")
        self.label = tk.Label(self.master, pady = 25, font=("Courier", 22), text = "Enter a valid code").pack()
        self.entry = tk.Entry(self.master, borderwidth = 3)
        self.entry.pack()
        self.button = tk.Button(self.master, text = 'Validate!', font=("Courier", 18), highlightbackground = '#000', command = self.validate_code).pack(pady=10)
        self.answer = tk.Label(self.master, pady = 25, font=("Courier", 22))
        self.answer.pack()
    
    def validate_code(self):
        code = self.entry.get()
        if code == 'hola':
            self.answer.config(text="Code is correct")
            print("CORRECTO")
            try:
                ifname = 'eth0'
                info={}
                info['platform'] = platform.system()
                info['platform-release'] = platform.release()
                info['platform-version'] = platform.version()
                info['architecture'] = platform.machine()
                info['platform-info'] = platform.platform()
                info['mac-version'] = platform.mac_ver()
                info['unix-version'] = platform.libc_ver()
                info['windows-version'] = platform.win32_ver()
                info['hostname'] = socket.gethostname()
                info['ip-address'] = socket.gethostbyname(socket.gethostname())
                info['eth-ip-address'] = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
                if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
                s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
                socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
                info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
                info['processor'] = platform.processor()
                info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
                info['cpu-percentage'] = psutil.cpu_percent()
                info['virtual-memory'] = psutil.virtual_memory()._asdict()
                info['available-memory'] = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
                print(info)
            except Exception as e:
                logging.exception(e)
        else:
            self.answer.config(text="Code is incorrect")
            print("INCORRECTO")

if __name__ == '__main__':

   root = tk.Tk()
   run = Application(root)
   root.mainloop()