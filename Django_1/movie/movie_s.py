# -*- coding:utf-8 -*-
import urllib
import re
from dy.models import DyModels

# import MySQLdb
#
# conn = MySQLdb.connect(
#     host='127.0.0.1',
#     port=3306,
#     db='movie',
#     charset='utf8',
#     user='root',
#     password='root'
# )
#
# cur = conn.cursors()

def getList(pn):
    html = urllib.urlopen('http://www.piaohua.com/html/dongzuo/list_%s.html' % pn).read()
    reg = re.compile(r'<dd><strong><a href="(.*?)">')
    return re.findall(reg,html)

def getContent(url):
    html = urllib.urlopen('http://www.piaohua.com/%s' %url).read()
    pattern = re.compile(r'<h3>(.*?)</h3>')
    content = ''
    link = ''
    title = re.findall(pattern,html)[0]
    pattern = re.compile(r'<div>(.*?)<strong><span style="color: #ff0000">',re.S)
    temp = re.findall(pattern,html)
    if len(temp) > 0:#防止空内容
        content = temp[0]
    pattern = re.compile(r'line-height: 18px" width="100%"><a href="(.*?)">')
    temp = re.findall(pattern,html)
    if len(temp) > 0:#防止空内容
        link = temp[0]
    return title,content,link

def savedata():
    for n in range(1,375):
        for i in getList(n):
            title,content,link = getContent(i)
            print u'正在保存第%d页的%s' %(n,title.decode('utf-8'))
            dymodels = DyModels(title=title,content=content,link=link)
            dymodels.save()# 保存数据到数据库
            # cur.execute("insert into movie(id,title,content,link)")
            # conn.commit()



