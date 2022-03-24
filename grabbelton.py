from cgitb import text
from operator import index
import tkinter as tk
import random

window = tk.Tk()

lst = ["emotional damage","penis enlargement pills", "good job idiot u pressed a button", "damn what a press", "fuck you tony", "fuck you ezekiel", "im impressed, do you get it", "damn son", "u are gay!", "why u always lyin"]

window.geometry("300x300")
button = tk.Button(text="click here bitch", bg="black", fg="white")
button.pack()
def antwoord():
    if len(lst) == 0:
        window2 = tk.Tk()
        window2.geometry("300x300")
        label1 = tk.Label(window2, text="why are u still clicking don't you have a life?")
        label1.config(bg='black', fg='white')
        label1.place(relx=0.5,rely=0.5,anchor='center')
    else:
        windowAntwoord = tk.Tk()
        windowAntwoord.geometry("300x300")
        var = random.choice(lst)
        label = tk.Label(windowAntwoord, text=var)
        label.config(bg="black", fg="white", font=32)
        label.pack()
        lst.remove(var)



    
button.config(command=antwoord)


window.mainloop()