# -*- coding:utf-8 -*-
import smtplib
import mailInfo
from email.mime.text import MIMEText

mail_list = ["1278423697@qq.com"] #定义收件人
mail_host ="smtp.qq.com" #定义邮箱服务器
mail_username = "1278423697@qq.com" #发送邮件账号
mail_password = mailInfo.PWD #密码

def send_mail(text,to_mail):
    my = "belong" + "<"+mail_username+">" # 发件人
    msg = MIMEText(text,_subtype="html",_charset="utf-8")
    msg['To'] = ';'.join(to_mail)
    msg['From'] = my
    msg['Subject'] = "belong good"
    try: #异常捕获，出错以后程序不会停止，抛出异常
        s = smtplib.SMTP() #实例化对象保存到s里面
        s.connect(mail_host) #连接发信服务器
        s.login(mail_username,mail_password) #登录邮件发送服务器
        s.sendmail(my,to_mail,msg.as_string()) #发送邮件
        s.close() #关闭连接
        print '发送完成'
    except Exception, e:
        print e

# text = '<a href="https://www.baidu.com">baidu</a>'
# send_mail(text,mail_list)

