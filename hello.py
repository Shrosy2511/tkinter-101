import tkinter as tk

window = tk.Tk()

window.title('hello')
window.geometry("400x400")
label = tk.Label(text='Hello \n Tkinter', font=("Helvetica", 30))
label.config(bg="black", fg="red")
label.place(relx=0.5, rely=0.5, anchor="center")
window.config(bg="grey")

window.mainloop()