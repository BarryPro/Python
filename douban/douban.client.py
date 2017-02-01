# -*- coding:utf-8 -*-

import requests
from HTMLParser import HTMLParser
from PIL import Image

class DoubanClient(object):
    def __init__(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                  'Origin':'https://accounts.douban.com'}
        self.session = requests.session() #会话
        self.session.headers.update(headers)

    def login(self,username,password,
              source='None',
              redir='https://www.douban.com/',
              login='登录'
        ):
        url='https://accounts.douban.com/login'
        r = self.session.get(url)
        # print r.text
        captcha_id,captcha_url = _get_captcha(r.content)
        print captcha_url
        print captcha_id
        if captcha_id:
            r = self.session.get(captcha_url)
            with open('captcha.jpg','wb') as f:
                f.write(r.content) #图片的二进制形式
            try:
                im = Image.open('captcha.jpg')
                im.show()
                im.close()
            except Exception,e:
                print '自己打开图片路径'

            captcha_solution = raw_input(u'请输入验证码[%s]:'%captcha_url)
        url = 'https://accounts.douban.com/login'
        data = {'form_email':username,
                'form_password':password,
                'source':source,
                'redir':redir,
                'login':login
                }
        if captcha_id:
            data['captcha-id'] = captcha_id
            data['captcha-solution'] = captcha_solution


        self.session.post(url,data)
        print self.session.cookies.items()

    def edit_sigture(self,username,sigture):
        url = 'https://www.douban.com/j/people/%s/edit_signature' %username
        r = self.session.get(url)
        data = {'ck':_get_ck(r.content),'signature':sigture}
        url = 'https://www.douban.com/j/people/%s/edit_signatu' %username
        headers = {'Host':'www.douban.com',
                   'Referer':'https://www.douban.com/people/%s/' %username,
                   'X-Requested-With':'XMLHttpRequest'
                   }
        r = self.session.post(url,data,headers = headers)
        print r.text


def _get_ck(content):
    class Captcha_ck(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.ck = None

        def handle_starttag(self, tag, attrs):
            if tag == 'input' and _attr(attrs, 'type') == 'hidden' and _attr(attrs, 'name') == 'ck':
                self.ck = _attr(attrs, 'value')

    p = Captcha_ck()  # 实例化
    p.feed(content)
    return p.ck

def _attr(attrs,attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None

def _get_captcha(content):
    class CaptchaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.captcha_url = None
            self.captcha_id = None
        def handle_starttag(self,tag,attrs):
           if tag == 'img' and _attr(attrs,'id') == 'captcha_image' and _attr(attrs,'class') == 'captcha_image':
               self.captcha_url = _attr(attrs,'src')
           if tag == 'input' and _attr(attrs,'type') == 'hidden' and _attr(attrs,'name') == 'captcha-id':
               self.captcha_id = _attr(attrs,'value')
    p = CaptchaParser() #实例化
    p.feed(content)
    return p.captcha_id,p.captcha_url
douban = DoubanClient()
douban.login('belong.belong@outlook.com','Belong941029')
douban.edit_sigture('157020973','belongLOVE')


