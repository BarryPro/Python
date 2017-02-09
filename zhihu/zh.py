# -*- coding:utf-8 -*-

import requests
import re
import urllib2
import HTMLParser #实现文件的解析
import sys
reload(sys)
sys.setdefaultencoding('utf-8') #输出的内容是utf-8格式

url = 'http://daily.zhihu.com/'

def getHtml(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    requests = urllib2.Request(url,headers=header)
    response = urllib2.urlopen(requests)#打开地址
    text = response.read()#读取源码
    # print text
    return text

#通过html解析超链接
def getUrls(html):
    pattern = re.compile('<a href="/story/(.*?)"')#提高效率
    items = re.findall(pattern,html)#用于匹配
    urls = [] #连接的list
    for item in items:
        urls.append('http://daily.zhihu.com/story/'+item) #拼接连接
        #print(urls[-1])
    return urls

#解析日报内容
def getContent(url):
    html = getHtml(url)
    pattern = re.compile('<h1 class="headline-title">(.*?)</h1>')
    items = re.findall(pattern,html)
    print items[0]

    #匹配文章的内容
    pattern = re.compile('<div class="content">\\n<p>(.*?)</div>',re.S)#将正则表达式，编译成正则表达式对象(re.S多行匹配)
    items_withtag = re.findall(pattern,characterProcessing(html))
    for item in items_withtag:
        print item


#去掉正文中间的杂质
def characterProcessing(html):
    htmlParser = HTMLParser.HTMLParser()
    pattern = re.compile('<p>(.*?)</p>|<li>(.*?)</li>.*?',re.S)
    items = re.findall(pattern,html)
    result = []
    for index in items:
        if index != '':
            for content in index:
                tag = re.search('<.*?>',content)
                http = re.search('<.*?http.*?',content)
                html_tag = re.search('&',content)
                if html_tag:
                    content = htmlParser.unescape(content)

                if http:
                    continue
                elif tag:
                    pattern = re.compile('(.*?)<.*?>(.*?)</.*?>(.*)')
                    items = re.findall(pattern,content)
                    content_tags = ''
                    if len(items)>0:
                        for item in items:
                            if len(item)>0:
                                for item_s in item:
                                    content_tags = content_tags + item_s
                            else:
                                content_tags = content_tags + item_s
                        content_tags = re.sub('<.*?>','',content_tags)
                        result.append(content_tags)
                    else:
                        continue
                else:
                    result.append(content)
    return result


html = getHtml(url)
urls = getUrls(html)
for url in urls:
    try:
        getContent(url)
    except:
        pass
