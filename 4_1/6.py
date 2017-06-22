from tkinter import *
import random

window = Tk()
canvas = Canvas(window, width = 300, height = 300)
canvas.pack()
text = canvas.create_text(100, 100, text = 'C')

def callback(event):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    canvas.move(text, x, y)
canvas.bind('<Button-1>', callback)
window.mainloop()