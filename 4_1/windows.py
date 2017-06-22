# -*- coding: utf-8 -*- #

from tkinter import *
# window=Tk()
# label=Label(window, text="Hello world")
# label.pack()
# label1=Label(window, text="Esay")
# label1.pack()
# window.mainloop()

########################

# window=Tk()
# b1=Button(window, text="this is button")
# b1.pack()
# b2 = Button(window, text="this is second button")
# b2.pack()
# b1.pack(side=LEFT)
# b2.pack(side=BOTTOM, padx=10, pady=10)
# window.mainloop()

class App:
    def __init__(self):
        window=Tk()
        helloB=Button(window, text="Hello", command=self.hello, fg="red")
        helloB.pack(side=LEFT)
        quitB=Button(window, text="quit", command=self.quit, fg="blue")
        quitB.pack(side=LEFT)
        window.mainloop()
    def hello(self):
        print("hello")
    def quit(self):
        print("quit")
        
App()