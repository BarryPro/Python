# -*- coding:utf-8 -*-

import tkinter
from tkinter import *

state = ''
buttons = []

def choose(i):
    global state
    state = i
    for btn in buttons:
        btn.deselect()
    buttons[i].select() #单选框被选择

root = Tk()
for i in range(4):
    radio = Radiobutton(root,text=str(i),
                        value=str(i),command=(lambda i = i:choose(i)))
    radio.pack(side=BOTTOM)#单选框
    buttons.append(radio)

root.mainloop()
print("you chose the following number",state)
