import requests
import time
import keyboard
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import mouse
from pynput.mouse import Listener
import tkinter, win32api, win32con, pywintypes
import threading
from tkinter import Tk, Text, Label, END


# https://gmail.com/

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    url = requests.get(input("Enter the URL: "))
except ValueError:
    url = requests.get(input("Try again. Enter a URL address: "))

driver.get(url)





start_time = time.time()

chosen_time = float(input("Enter how many hours per day you want to spend on this URL: "))


Blocker()


print(f"Tracking time on {url}. Close the browser window to stop tracking.")
keycount = 0
clicks = 0

try:
    while True:
        # Check if the browser window is still open
        
        try: #for keylogging
            if keyboard.is_pressed():
                keycount += 1
                break
        except:
            break
        
        def onclick():
            global clicks
            clicks += 1
        
        root = tkinter.Tk()
        mouse.on_click(onclick)
        root.mainloop()
                
                
                
        if driver.current_url == "data:,":
            break
        time.sleep(1)
except Exception as e:
    print(f"Error: {e}")
finally:
    # Record the end time
    end_time = time.time()
    # Calculate the time spent
    time_spent = end_time - start_time
    driver.quit()
    print(f"Time spent on {url}: {time_spent:.2f} seconds")
    if time_spent < chosen_time/3600:
        print("You have failed to meet your personal requirements. Punishments will be applied.")
    elif time_spent >= chosen_time/3600 and keycount <100:
        print("You have failed to meet your personal requirements. Punishments will be applied.")
    elif time_spent >= chosen_time/3600 and keycount >=100:
        print("Congrats. You have reached your personal requirements. Rewards will be applied.")
        Unblock()
        
        
from tkinter import *
import requests

window = Tk()
window.geometry('650x400')
window.minsize(650,400)
window.maxsize(650,400)
window.title("Website Blocker")


try:
    site = requests.get(input("Enter the website you want to block as a punishment: "))
except ValueError:
    site = requests.get(input("Try again. Enter a URL address: "))
    
     
host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'


def Blocker():
  website_lists = enter_Website.get(1.0,END)
  Website = list(website_lists.split(","))
  with open (host_path , 'r+') as host_file:
   file_content = host_file.read()
   for web in Website:
     if web in file_content:
       display=Label(window, text = 'Already Blocked' , font = 'arial')
       display.place(x=200,y=200)
       pass
   else:
       host_file.write(ip_address + " " + web + '\n')
       Label(window, text = "Blocked", font = 'arial').place(x=230,y =200)
       

def Unblock():
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
     file_content = host_file.readlines()
    for web in Website:
        if web in website_lists:
            with open (host_path , 'r+') as f:
                for line in file_content:
                    if line.strip(',') != website_lists:
                        f.write(line)
                        Label(window, text = "UnBlocked", font = 'arial').place(x=350,y =200)
                        pass
    else:
           display=Label(window, text = 'Already UnBlocked' , font = 'arial')
           display.place(x=350,y=200)


label1=Label(window, text ='Enter Website :' , font ='arial 13 bold')
label1.place(x=5 ,y=60)
enter_Website = Text(window,font = 'arial',height='2', width = '40')
enter_Website.place(x= 140,y = 60)


block_button = Button(window, text = 'Block',font = 'arial',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'grey')
block_button.place(x = 230, y = 150)
unblock_button = Button(window, text = 'UnBlock',font = 'arial',pady = 5,command = Unblock ,width = 6, bg = 'royal blue1', activebackground = 'grey')
unblock_button.place(x = 350, y = 150)



window.mainloop()
