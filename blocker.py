import time
import os
import platform
import tkinter as tk
from tkinter import messagebox
from datetime import datetime as dt 
from datetime import timedelta
import threading
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



if is_admin():
    def print_script_path_info():
        # __file__ contains the path to the script
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        script_name = os.path.basename(script_path)

        print(f"Full script path: {script_path}")
        print(f"Script directory: {script_dir}")
        print(f"Script name: {script_name}")

    if __name__ == "__main__":
        print_script_path_info()


    def block_website(duration, url):
        # change hosts path according to your OS 
        if platform.system() == "Windows":
            hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        else:
            hosts_path = "/etc/hosts"
        
        # localhost's IP 
        redirect = "127.0.0.1"
        end_time = dt.now() + timedelta(hours=duration)
        
        try:
            with open(hosts_path, "r+") as file:
                content = file.read()
                if url not in content:
                    file.write(f"{redirect} {url}\n")
            
            #Flush dns cache
            if platform.system() == "Windows":
                os.system("ipconfig /flushdns")

            
            # Removing the block after the duration
            with open(hosts_path, 'r+') as file: 
                content = file.readlines() 
                file.seek(0)
                for line in content: 
                    if url not in line: 
                        file.write(line) 
                file.truncate() 
                
            #flush dns cache (removes other ip addresses/dns caches)
            if platform.system() == "Windows":
                os.system("ipconfig /flushdns")

            print("Blocking completed.")
        except IOError:
            print("Could not modify files. Please try and run with admin privileges.")
            messagebox.showerror("Error. Please run with admin rights.")


    # Get user input

    import tkinter as tk
    from tkinter import messagebox

    def show_link():
        url = entry_link.get()
        try:
            duration = float(entry_duration.get())
            messagebox.showinfo("Blocking until goals achieved:", f"{url}")
            threading.Thread(target=block_website, args=(duration, url)).start()
        except ValueError:
            messagebox.showerror("Invalid, please enter in hours.")

    root = tk.Tk()
    root.title("Productivity Bot")

    label = tk.Label(root, text="Enter the link you want to block:")
    label.pack(pady=10)

    entry_link = tk.Entry(root, width=50)
    entry_link.pack(pady=5)

    label = tk.Label(root, text="How long would you like to block for (in hours):")
    label.pack(pady=10)

    entry_duration = tk.Entry(root, width=50)
    entry_duration.pack(pady=5)

    button = tk.Button(root, text="Submit", command=show_link)
    button.pack(pady=20)


    # https://gmail.com/
    # c:\Users\shind\Downloads\blocker.py

    root.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
