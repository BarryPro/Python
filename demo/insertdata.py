# -*- coding:utf-8 -*-

import os
import sqlite3

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()

sql = '''
    insert into employee(empid, firstname, lastname, dept, manager, phone)
    values(1,'belong','Foster-Johnson',1,1,'555-555')
'''
cursor.execute(sql)

sql = "select * from employee "
cursor.execute(sql)
conn.commit()

rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
