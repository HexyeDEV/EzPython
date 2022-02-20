from cProfile import label
from tkinter import Tk as tk
from tkinter import Toplevel, Button, Label, Entry, messagebox
import os

from click import edit

window = tk()

# Commands
def new_file(filename, entry):
    entry.delete(0, 'end')
    open(filename + ".py", 'a').close()
    messagebox.showinfo("New File", "New file created")

def add_print(text, filename, entry):
    file = open(filename, 'a')
    entry.delete(0, 'end')
    file.write(f"print(f\"{text}\")" + "\n")
    file.close()
    messagebox.showinfo("Add text on Console", "Text on Console added", parent=editwindow)

def add_variable(variable, filename, entry):
    file = open(filename, 'a')
    entry.delete(0, 'end')
    var = variable.split(",")[0]
    val = variable.split(",")[1].replace(" ", "")
    try:
        val = int(val)
    except:
        try:
            val = float(val)
        except:
            val = "\"" + val + "\""
    file.write(f"{var} = {val}" + "\n")
    file.close()
    messagebox.showinfo("Add variable", "Variable added", parent=editwindow)

def add_input(variable, filename, entry):
    file = open(filename, 'a')
    entry.delete(0, 'end')
    var = variable.split(",")[0]
    val = variable.split(",")[1].replace(" ", "")
    file.write(f"{var} = input(\"{val}\")" + "\n")
    file.close()
    messagebox.showinfo("Add input", "Input added", parent=editwindow)


def open_file(filename, entry):
    entry.delete(0, 'end')
    global window
    try:
        global editwindow
        editwindow = Toplevel(window)
        editwindow.title(filename[:-3])
        editwindow.geometry("750x750")
        editwindow.resizable(False, False)
        editwindow.configure(background="#bebebe")
        Label(editwindow, text=filename[:-3], font=("Arial", 20), bg="#bebebe").pack()
        Label(editwindow, text="", bg="#bebebe").pack()
        Label(editwindow, text="Text to show on Console (use {variable_name} to show a variable)", bg="#bebebe").pack()
        textprint = Entry(editwindow)
        textprint.pack()
        Button(editwindow, text="Add text on Console", command=lambda: add_print(textprint.get(), filename, textprint)).pack()
        Label(editwindow, text="", bg="#bebebe").pack()
        Label(editwindow, text="Create Variable (write: variable_name, variable value)", bg="#bebebe").pack()
        addvariable = Entry(editwindow)
        addvariable.pack()
        Button(editwindow, text="Add variable", command=lambda: add_variable(addvariable.get(), filename, addvariable)).pack()
        Label(editwindow, text="", bg="#bebebe").pack()
        Label(editwindow, text="Add input Variable (write: variable_name, Input String)", bg="#bebebe").pack()
        addinput = Entry(editwindow)
        addinput.pack()
        Button(editwindow, text="Add input", command=lambda: add_input(addinput.get(), filename, addinput)).pack()
    except:
        messagebox.showerror("Open File", "File not found")

def update(window):
    window.destroy()
    os.system("python3 update.py")
    exit()



window.geometry("750x750")
window.title("EzPython")
window.resizable(False, False)
window.configure(background="#bebebe")
Label(window, text="EzPython", font=("Arial", 20), bg="#bebebe").pack()
Label(window, text="", bg="#bebebe").pack()
Label(window, text="New File Name", bg="#bebebe").pack()
filename = Entry(window)
filename.pack()
Button(window, text="New File", command=lambda: new_file(filename.get().replace(" ", "_"), filename)).pack()
Label(window, text="", bg="#bebebe").pack()
Label(window, text="Open File Name", bg="#bebebe").pack()
openfilename = Entry(window)
openfilename.pack()
Button(window, text="Open File", command=lambda: open_file(openfilename.get().replace(" ", "_") + ".py", openfilename)).pack()
Label(window, text="", bg="#bebebe").pack()
Button(window, text="Update Software", command=lambda: update(window)).pack()

window.mainloop()