from operator import index
import tkinter as tk
import random

window = tk.Tk()

lst = ["auto","penis enlargement pills", "good job idiot u pressed a button", "damn what a press", "fuck you tony", "fuck you ezekiel", "im impressed, do you get it", "damn son", "u are gay!", "why u always lyin"]

window.geometry("300x300")
button = tk.Button(text="click here bitch", bg="black", fg="white")
button.pack()
def antwoord():
    windowAntwoord = tk.Tk()
    windowAntwoord.geometry("300x300")
    var = random.choice(lst)
    label = tk.Label(windowAntwoord, text=var)
    label.config(bg="black", fg="white", font=32)
    label.pack()
    lst.remove(var)
    
button.config(command=antwoord)


window.mainloop()