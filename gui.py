import tkinter as tk
from tkinter import messagebox

def show_link():
    link = entry.get()
    messagebox.showinfo("Entered Link", f"You entered: {link}")

root = tk.Tk()
root.title("Link Entry")

label = tk.Label(root, text="Enter a link:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_link)
button.pack(pady=20)

root.mainloop()
