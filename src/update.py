from tkinter import Tk as tk
import customtkinter
from customtkinter import CTkLabel as Label
from tkinter import messagebox
import requests, os, sys

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.title("Update")
window.geometry("500x500")
window.resizable(False, False)
Label(window, text="Update", font=("Arial", 20), bg_color="#bebebe").pack()
Label(window, text="", bg_color="#bebebe").pack()
Label(window, text="Looking for updates...", bg_color="#bebebe").pack()
req = requests.get("https://raw.githubusercontent.com/HexyeDEV/EzPython/main/version.json").json()

current_version = open("version.txt", "r").readlines()[0]
f = open("version.txt", "w")

python = sys.executable

if req['version'] != current_version:
    messagebox.showinfo("Update", "Update available, Installing it Now")
    f.write(req['version'])
    new_file = requests.get("https://raw.githubusercontent.com/HexyeDEV/EzPython/main/src/EzPython.py").text
    open("EzPython.py", 'w').write(new_file)
    messagebox.showinfo("Update", "Update installed")
    window.destroy()
    os.system(f"{python} EzPython.py")
    exit()
else:
    messagebox.showinfo("Update", "No updates available")
    os.system(f"{python} EzPython.py")
    window.destroy()
    exit()
