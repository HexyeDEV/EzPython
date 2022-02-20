from tkinter import Tk as tk
from tkinter import Label, messagebox
import requests

current_version = "0.0.2"

window = tk()
window.title("Update")
window.geometry("500x500")
window.resizable(False, False)
window.configure(background="#bebebe")
Label(window, text="Update", font=("Arial", 20), bg="#bebebe").pack()
Label(window, text="", bg="#bebebe").pack()
Label(window, text="Looking for updates...", bg="#bebebe").pack()
req = requests.get("https://raw.githubusercontent.com/HexyeDev/EzPython/master/src/version.json").json()

if req['version'] != current_version:
    messagebox.showinfo("Update", "Update available, Installing it Now")
    new_file = requests.get("https://raw.githubusercontent.com/HexyeDev/EzPython/master/src/EzPython.py").text
    open("EzPython.py", 'w').write(new_file)
