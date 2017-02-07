# -*- coding:utf-8 -*-

import sys
from tkinter import *

popupper = (len(sys.argv) > 1)

def dialog():
    win = Toplevel()#新建自定义对话框
    Label(win,text='Do you Always Do What You are Told?').pack()
    Button(win,text='Now click this one',command=win.destroy).pack()
    if popupper:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print('You better obey me ...')

root = Tk()
Button(root,text='Click me',command=dialog).pack()
root.mainloop()
