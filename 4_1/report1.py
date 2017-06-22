# -*- coding: utf-8 -*- #
from tkinter import *

def motion(event):
    var.set("사랑해")
    return

window = Tk()

var = StringVar()
var.set("LoveJava")

label = Label(window,textvariable=var,width=100,height=100)
label.bind('<Motion>',motion)
label.pack()

window.mainloop()