#!/usr/bin/python
from Tkinter import *

# create a root window
root = Tk()
root.title("Hello World")
root.geometry("180x60")
# create a frame in the window to hold other widgets
app = Frame(root)
app.grid()

lbl = Label(app, text = "Hello World!")
lbl.grid()

bttn1 = Button(app, text = "Die")
bttn1.grid()

root.mainloop()
