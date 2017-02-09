# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class DyModels(models.Model):#创建数据库和读取数据(大写变成小写存到数据库中变成表)
    id = models.AutoField(primary_key=True)#增加自动加一
    title = models.CharField(max_length=100,null=False)#100个字节
    content = models.TextField(null=False)#不允许为空
    link = models.CharField(max_length=100)
