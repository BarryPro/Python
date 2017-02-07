# -*- coding:utf-8 -*-
from tkinter import *

root = Tk()
widget = Label(root) #置父
widget.config(text="My first GUI!")
widget.pack(side=TOP,expand=YES,fill=BOTH)
root.mainloop()
