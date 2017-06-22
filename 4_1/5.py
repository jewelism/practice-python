from tkinter import *
import tkinter.font as font
window = Tk()
canvas = Canvas(window, width = 400, height = 400)
canvas.pack()
size = 20
csfont = font.Font(size = size)
text = canvas.create_text(200, 200, text = 'Love Java', font = csfont)
def sizeUp(event):
    global size
    size = size + 5
    csfont = font.Font(size=size)
    canvas.itemconfig(text, font = csfont)
def sizeDown(event):
    global size
    if(size - 5 < 5):
        return 0
    else:
        size = size - 5
    csfont = font.Font(size=size)
    canvas.itemconfig(text, font=csfont)
canvas.bind_all('<KeyPress-+>', sizeUp)
canvas.bind_all('<KeyPress-->', sizeDown)
window.mainloop()