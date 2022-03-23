from re import S
import tkinter as tk
from time import strftime

window = tk.Tk()

window.geometry("520x70")
label = tk.Label(window, font=("Terminal", 48), bg="black", fg="darkred")
label.pack()
def counter():
    tijd = strftime("%H:%M:%S:%p")
    var = tk.StringVar(value=tijd)
    label.config(textvariable= var)

    window.after(1000, counter)

counter()

window.mainloop()