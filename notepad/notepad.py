# -*- coding:utf-8 -*-

from Tkinter import *
import tkMessageBox
import tkFileDialog #导入文件模块

#新建
def New():
    text.delete(1.0,END) #清空多行文本的内容

#打开
def Open():
    pass

#保存
def Save():
    txt = text.get(1.0,END) #获取内容
    open(tkFileDialog.asksaveasfilename(title='保存文件',filetypes=[('文本文档','*.txt')])+'.txt','w').write(txt)

#另存为
def Saves():
    pass

#关于
def About():
    tkMessageBox.showinfo('作者','belong')

def mos():
    print '11'

root = Tk() #创建窗口（类似于声明）
root.title('notepad')
root.geometry('600x400+1100+300')

#----菜单------------------------------------------------

me = Menu()#菜单（顶级菜单）
root.config(menu=me)

#-----文件菜单--------------------------------------------

filemenu = Menu(me)
filemenu.add_command(label='新建',accelerator='Ctrl + N',command=New)
filemenu.add_command(label='打开',accelerator='Ctrl + O',command=Open)
filemenu.add_command(label='保存',accelerator='Ctrl + S',command=Save)
filemenu.add_command(label='另存为',accelerator='Ctrl + A',command=Saves)
filemenu.add_separator()
filemenu.add_command(label='退出',command=root.quit())
me.add_cascade(label='文件',menu=filemenu)

#-----编辑菜单--------------------------------------------

editmenu = Menu(me)
editmenu.add_command(label='新建',accelerator='Ctrl + N')
editmenu.add_command(label='打开',accelerator='Ctrl + O')
editmenu.add_command(label='保存',accelerator='Ctrl + S')
editmenu.add_command(label='另存为',accelerator='Ctrl + A')
me.add_cascade(label='编辑',menu=editmenu)

#-----帮助------------------------------------------------

helpmenu = Menu(me)
helpmenu.add_command(label='关于',command=About)
me.add_cascade(label='帮助',menu=helpmenu)

#-----文本框----------------------------------------------

text = Text(root)
text.bind('<Motion>',mos())
text.pack(expand=YES,fill=BOTH)#编辑框可以和窗口成比例变化
scr = Scrollbar(text)
text.config(yscrollcommand=scr.set)
scr.config(command=text.yview())
scr.pack(side=RIGHT,fill=X)
mainloop() #显示(是个循环,只有退出了才会执行后面的程序)
