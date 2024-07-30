import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pynput.mouse import Listener
import tkinter as tk
from tkinter import Tk, Text, Label, END, Button

# Web driver setup
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
except Exception as e:
    print(f"Error setting up WebDriver: {e}")
    exit(1)

url = input("Enter the URL: ")
try:
    response = requests.get(url)
except requests.RequestException:
    url = input("Try again. Enter a URL address: ")
    response = requests.get(url)

driver.get(url)

start_time = time.time()

chosen_time = float(input("Enter how many hours per day you want to spend on this URL: "))

def Blocker():
    pass

Blocker()

print(f"Tracking time on {url}. Close the browser window to stop tracking.")
keycount = 0
clicks = 0

def on_click(x, y, button, pressed):
    global clicks
    if pressed:
        clicks += 1

listener = Listener(on_click=on_click)
listener.start()

try:
    while True:
        if driver.current_url == "data:,":
            break
        time.sleep(1)
except Exception as e:
    print(f"Error: {e}")
finally:
    end_time = time.time()
    time_spent = end_time - start_time
    driver.quit()
    listener.stop()
    print(f"Time spent on {url}: {time_spent:.2f} seconds")
    if time_spent < chosen_time * 3600:
        print("You have failed to meet your personal requirements. Punishments will be applied.")
    elif time_spent >= chosen_time * 3600 and keycount < 100:
        print("You have failed to meet your personal requirements. Punishments will be applied.")
    elif time_spent >= chosen_time * 3600 and keycount >= 100:
        print("Congrats. You have reached your personal requirements. Rewards will be applied.")
        Unblock()

# Blocker GUI
def Blocker():
    website_lists = enter_Website.get(1.0, END).strip()
    if not website_lists:
        print("No websites entered.")
        return
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web in file_content:
                display = Label(window, text='Already Blocked', font='arial')
                display.place(x=200, y=200)
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(window, text="Blocked", font='arial').place(x=230, y=200)

def Unblock():
    website_lists = enter_Website.get(1.0, END).strip()
    if not website_lists:
        print("No websites entered.")
        return
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.readlines()
    with open(host_path, 'w') as host_file:
        for line in file_content:
            if not any(web in line for web in Website):
                host_file.write(line)
    Label(window, text="UnBlocked", font='arial').place(x=350, y=200)

host_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
ip_address = '127.0.0.1'

window = Tk()
window.geometry('650x400')
window.minsize(650, 400)
window.maxsize(650, 400)
window.title("Website Blocker")

label1 = Label(window, text='Enter Website :', font='arial 13 bold')
label1.place(x=5, y=60)
enter_Website = Text(window, font='arial', height='2', width='40')
enter_Website.place(x=140, y=60)

block_button = Button(window, text='Block', font='arial', pady=5, command=Blocker, width=6, bg='royal blue1', activebackground='grey')
block_button.place(x=230, y=150)
unblock_button = Button(window, text='UnBlock', font='arial', pady=5, command=Unblock, width=6, bg='royal blue1', activebackground='grey')
unblock_button.place(x=350, y=150)

window.mainloop()
