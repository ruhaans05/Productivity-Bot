import time
import os
import platform
import tkinter as tk
from tkinter import messagebox


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


def block_website(domain, duration):
    # Determine the hosts file location based on the OS
    hosts_path = "/etc/hosts" if platform.system() != "Windows" else r"C:\Windows\System32\drivers\etc\hosts"
    
    redirect_ip = "127.0.0.1"
    entry = f"{redirect_ip} {domain}\n"
    
    try:
        # Backup the hosts file
        with open(hosts_path, 'r') as file:
            hosts_content = file.readlines()

        # Check if the domain is already blocked
        if any(domain in line for line in hosts_content):
            print(f"{domain} is already blocked.")
            return
        
        # Append the block entry to the hosts file
        with open(hosts_path, 'a') as file:
            file.write(entry)
        
        print(f"{domain} has been blocked.")
        
        # Wait for the specified duration
        time.sleep(duration)
        
        # Remove the block entry from the hosts file
        with open(hosts_path, 'w') as file:
            for line in hosts_content:
                if domain not in line:
                    file.write(line)
        
        print(f"{domain} has been unblocked.")
    
    except PermissionError:
        print("Run as admin in command prompt")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get user input

import tkinter as tk
from tkinter import messagebox

def show_link():
    link = entry.get()
    messagebox.showinfo("Blocking", f"{link}")

root = tk.Tk()
root.title("Productivity Bot")

label = tk.Label(root, text="Enter the link you want to block:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_link)
button.pack(pady=20)


# https://gmail.com/
# c:\Users\shind\Downloads\blocker.py

root.mainloop()




def duration():
    dur = entry.get()
    messagebox.showinfo("Time:", f"{dur} hours blocked")

root = tk.Tk()
root.title("Productivity Bot")

label = tk.Label(root, text="How long would you like to block for (in hours):")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=duration)
button.pack(pady=20)


# https://gmail.com/
# c:\Users\shind\Downloads\blocker.py

root.mainloop()




block_website(show_link, duration)
