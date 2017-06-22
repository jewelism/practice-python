from tkinter import *
window = Tk()
canvas = Canvas(window, width = 400, height = 400)
canvas.pack()
text = canvas.create_text(200, 200, text = 'Love Java')
def left(event):
    stringTemping = canvas.itemconfigure(text)
    stringTemping = stringTemping["text"][4]
    s = ""
    temp = stringTemping[0]
    for i in range(1, 9):
        s = s + stringTemping[i]
    s = s + temp
    canvas.itemconfig(text, text = s)
canvas.bind_all('<KeyPress-Left>', left)
window.mainloop()