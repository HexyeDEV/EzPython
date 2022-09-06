from tkinter import Tk as tk
from tkinter import Toplevel, Button, Label, Entry, messagebox
import os
import webbrowser
import json
import requests

window = tk()


# Commands
def new_file(filename, entry):
    entry.delete(0, 'end')
    open(filename + ".py", 'a').close()
    messagebox.showinfo("New File", "New file created")

def add_print(text, filename, entry):
    file = open(filename, 'a')
    entry.delete(0, 'end')
    entry.insert(0, "Text to show on console")
    file.write(f"print(f\"{text}\")" + "\n")
    file.close()
    messagebox.showinfo("Add text on Console", "Text on Console added", parent=editwindow)

def add_variable(name, value, filename, entry, entry2):
    file = open(filename, 'a')
    entry.delete(0, 'end')
    entry2.delete(0, 'end')
    entry.insert(0, 'Variable Value')
    entry2.insert(0, 'Variable Name')
    var = name
    val = value
    try:
        val = int(val)
    except:
        try:
            val = float(val)
        except:
            try:
                if val.startswith("[") and val.endswith("]"):
                    val = val.replace("[", "").replace("]", "")
                    vals = val.split(", ")
                    i = 0
                    for val in vals:
                        vals[i] = val.replace("\"", "")
                        i += 1
                    val = vals
                else:
                    raise Exception
            except:
                try:
                    if val.startswith("{\"") and val.endswith("\"}"):
                        val = json.loads(val)
                    else:
                        raise Exception
                except:
                    val = "\"" + val + "\""
    file.write(f"{var} = {val}" + "\n")
    file.close()
    messagebox.showinfo("Add variable", "Variable added", parent=editwindow)

def add_input(name, value, filename, entry, entry2):
    file = open(filename, 'a')
    entry.delete(0, 'end')
    entry2.delete(0, 'end')
    entry.insert(0, 'Input Variable Name')
    entry2.insert(0, 'Add Input text')
    var = name
    val = value
    file.write(f"{var} = input(f\"{val}\")" + "\n")
    file.close()
    messagebox.showinfo("Add input", "Input added", parent=editwindow)

# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #


# Callback
def on_click(event):
    event.widget.selection_range(0, 'end')
# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #


# On file Open
def open_file(filename, entry):
    entry.delete(0, 'end')
    global window
    try:
        open(filename, 'r').close()
        global editwindow
        editwindow = Toplevel(window)
        editwindow.title(filename[:-3])
        editwindow.geometry("750x750")
        editwindow.resizable(False, False)
        editwindow.configure(background="#bebebe")
        Label(editwindow, text=filename[:-3], font=("Arial", 20), bg="#bebebe").pack()
        Label(editwindow, text="", bg="#bebebe").pack()
        textprint = Entry(editwindow)
        textprint.insert(0, "Text to show on console")
        textprint.pack()
        textprint.bind("<Button-1>", on_click)
        textprint.bind("<FocusIn>", on_click)
        Button(editwindow, text="Add text on Console", command=lambda: add_print(textprint.get(), filename, textprint)).pack()
        Label(editwindow, text="", bg="#bebebe").pack()
        addvalue = Entry(editwindow)
        addvalue.insert(0, "Variable Value")
        addvalue.pack()
        addvalue.bind("<Button-1>", on_click)
        addvalue.bind("<FocusIn>", on_click)
        addname = Entry(editwindow)
        addname.insert(0, "Variable Name")
        addname.pack()
        addname.bind("<Button-1>", on_click)
        addname.bind("<FocusIn>", on_click)
        Button(editwindow, text="Add variable", command=lambda: add_variable(addname.get(), addvalue.get(), filename, addvalue, addname)).pack()
        Label(editwindow, text="", bg="#bebebe").pack()
        addinput = Entry(editwindow)
        addinput.insert(0, "Input Variable Name")
        addinput.pack()
        addinput.bind("<Button-1>", on_click)
        addinput.bind("<FocusIn>", on_click)
        addinptext = Entry(editwindow)
        addinptext.insert(0, "Add Input text")
        addinptext.pack()
        addinptext.bind("<Button-1>", on_click)
        addinptext.bind("<FocusIn>", on_click)
        Button(editwindow, text="Add input", command=lambda: add_input(addinput.get(), addinptext.get(), filename, addinput, addinptext)).pack()
        Label(editwindow, text="", bg="#bebebe").pack()
        Button(editwindow, text="Wiki Guide", command=lambda: webbrowser.open("https://hexye.gitbook.io/ezpython/", new=2)).pack()
    except Exception as e:
        print(e)
        messagebox.showerror("Open File", "File not found")

# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #

# Update Command
def update(window):
    window.destroy()
    os.system("python3 update.py")
    exit()

# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #

    


# Main Window
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
inf = json.load(open("inf.json"))
if inf["acc"] == False:
    accanswer = messagebox.askokcancel("Do you want to accept our Conditions?", "We may be showing you some fast surveys, data of those surveys will not be used to track you down, but only for building ai machines.\nWe may also show you some ads, but we will not track you down.\n\nIf you accept, click OK, if you don't, click Cancel.", parent=window)
    if accanswer:
        inf["acc"] = True
        json.dump(inf, open("inf.json", "w"))
        messagebox.showinfo("Accepted", "Thank you for accepting our Conditions", parent=window)
    else:
        messagebox.showinfo("Not Accepted", "You have not accepted our Conditions, you can still use the program but we are very sad you won't support us :(", parent=window)
if inf["acc"] == True:
    inf = json.load(open("inf.json"))
    server_messages = requests.get("https://raw.githubusercontent.com/HexyeDEV/EzPython/main/arc/messages.json").json()
    for message in server_messages:
        try:
            inf[message]
        except:
            messagebox.showinfo(message, server_messages[message], parent=window)
            inf[message] = True
    json.dump(inf, open("inf.json", "w"))
window.mainloop()

# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #
