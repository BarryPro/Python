# -*- coding:utf-8 -*-

import os
import sqlite3

conn = sqlite3.connect('sample_database')#连接数据库
cursor = conn.cursor()#操作数据库的操作指针

# Create tables.
cursor.execute('''
  create table employee(
    empid INTEGER ,
    firstname VARCHAR ,
    lastname VARCHAR ,
    dept INTEGER ,
    manager INTEGER ,
    phone VARCHAR )
  ''')
cursor.execute('''
  create table department(
    departmentid INTEGER ,
    name VARCHAR ,
    manager INTEGER
  )
''')
cursor.execute('''
    create table user(
      userid INTEGER ,
      username VARCHAR ,
      employeeid INTEGER
    )
''')

# Create indices.
cursor.execute('''create index userid on user(userid) ''')
cursor.execute('''create index empid on employee(empid)''')
cursor.execute('''create index deptid on department(departmentid)''')
cursor.execute('''create index deptfk on employee(dept)''')
cursor.execute('''create index mgr on employee(manager)''')
cursor.execute('''create index emplid on user(employeeid)''')
cursor.execute('''create index deptmgr on department(manager)''')
conn.commit()
cursor.close()
conn.close()
