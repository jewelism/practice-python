# -*- coding: utf-8 -*- #

from tkinter import *

window = Tk()

def sleft(event):
    print("드래그")
    label['bg'] = 'yellow'
def leaveevnet(evnet):
    print("Leave")
    label['bg'] = 'green'

var = StringVar()
var.set(" ")
label = Label(window,textvariable=var,width=100,height=100,bg='green')
label.bind('<B1-Motion>',sleft)
label.bind('<ButtonRelease-1>',leaveevnet)
label.pack()
window.mainloop()