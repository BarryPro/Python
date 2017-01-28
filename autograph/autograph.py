# -*- coding:utf-8 -*-
from Tkinter import * #引入GUI模块
import tkMessageBox #引入GUI模块的信息提示模块
import urllib,urllib2 #引入web URL模块
import re #引入正则表达式模块

def getImg():
    #if 条件（逻辑值bool）
    name = nameEntry.get().encode('utf-8')#对得到的名字进行utf-8转码
    if not nameEntry.get():#判断输入框是否有值 bool（nameEntry.get()）字符串为空‘’ 假
        tkMessageBox.showinfo('温馨提示','请先输入姓名再继续！')
        return
    #爬虫原理来抓取网页全部的内容
    html = urllib2.urlopen('http://www.uustv.com/',data='word=%s&sizes=60&fonts=jfcs.ttf&fontcolor=%%23000000' %name).read()
    reg = r'<div class="tu">﻿<img src="(.*?)"'#通过正则表达式来获取图片的相对路径
    imgurl = 'http://www.uustv.com/%s' %re.findall(reg,html)[0]
    #现由utf-8解码到字节码的形式在把字节码转化成gbk的形式（因为微软的文件格式的gbk）
    urllib.urlretrieve(url=imgurl,filename='%s.gif' %name.decode('utf-8').encode('gbk'))

root = Tk() #创建窗口
root.title('belong-签名设计') #修改窗口标题
root.geometry('+1200+200') #小写x +窗口位置
Label(root,text='姓 名:',font=('微软雅黑',15)).grid() #置父 grid pack 不能混合使用
nameEntry = Entry(root,font=('微软雅黑',15))
nameEntry.grid(row=0,column=1) #输入框/文本框/编辑框 entry单行文本框 text/多行文本框
button = Button(root,text='一键设计签名',font=("微软雅黑",15),width='15',height='1',command=getImg)
button.grid(row=3,column=1)
mainloop() #显示

