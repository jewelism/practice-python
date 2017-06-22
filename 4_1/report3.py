# -*- coding: utf-8 -*- #

from tkinter import *
root = Tk()
def key(event):
    if event.char == '\uf702':
        print("여기서 뒤집기")
        label["text"] = var[::-1]

def callback(event):
    label.focus_set()
    print ("click - ", event.x, event.y)


var = "Love Java"
label = Label(root,width=100,height=100)
label["text"] = var
label.bind("<Key>", key)
label.bind("<Button-1>", callback)
label.pack()

root.mainloop()