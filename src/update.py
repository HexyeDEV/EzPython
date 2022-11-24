import os
from tkinter import messagebox
from tkinter import Tk as tk

import customtkinter
import requests
from customtkinter import CTkLabel as Label

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.title("Update")
window.geometry("500x500")
window.resizable(False, False)
Label(window, text="Update", text_font=("Arial", 20), bg="#bebebe").pack()
Label(window, text="", bg="#bebebe").pack()
Label(window, text="Looking for updates...", bg="#bebebe").pack()
req = requests.get(
    "https://raw.githubusercontent.com/HexyeDEV/EzPython/main/version.json"
).json()

current_version = open("version.txt", "r").read()
f = open("version.txt", "w")

if req["version"] != current_version:
    messagebox.showinfo("Update", "Update available, Installing it Now")
    f.write(req["version"])
    new_file = requests.get(
        "https://raw.githubusercontent.com/HexyeDEV/EzPython/main/src/EzPython.py"
    ).text
    open("EzPython.py", "w").write(new_file)
    messagebox.showinfo("Update", "Update installed")
    window.destroy()
    os.system("python3 EzPython.py")
    exit()
else:
    messagebox.showinfo("Update", "No updates available")
    os.system("python3 EzPython.py")
    window.destroy()
    exit()
