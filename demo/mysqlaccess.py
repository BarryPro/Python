# -*-coding:utf-8 -*-

import pymysql

db_info = {'host':'127.0.0.1',
           'port':3306,
           'db':'video',
           'charset':'utf8',
           'user':'root',
           'password':'root'}
#连接mysql数据库的参数配置信息
conn = pymysql.connect(host=db_info['host'],
                       port=db_info['port'],
                       db=db_info['db'],
                       charset=db_info['charset'],
                       user=db_info['user'],
                       password=db_info['password'])
cur = conn.cursor()# 获取用表来访问数据库

sql = "select * from review "
cur.execute(sql)#执行sql语句
rows = cur.fetchall() #得到表中的所有内容

for dr in rows:
    print(dr)
