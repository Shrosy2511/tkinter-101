import tkinter

window = tkinter.Tk()

size = 0
counter = 0
colors = ['red','blue','purple','green','yellow','black']

window.title('achtergrond kleur en grote veranderen.')
window.config(bg='red')
def changeColor():
    global size, counter
    index = int(size/50)
    if index == len(colors):
        print('kabooooom!')
        window.destroy()
    else:
        counter += 1
        size += 50
        window.config(bg=colors[index])
        window.geometry(f'{size}x{size}')
        window.after(2000, changeColor)
        print(f'{counter}')

changeColor()
window.mainloop()