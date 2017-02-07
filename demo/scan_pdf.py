# -*- coding:utf-8 -*-

import os,os.path
import re

def print_pdf(root,dirs,files):
    for file in files:
        path = os.path.join(root,file)
        path = os.path.normcase(path)
        if re.search(r".*fast\.py",path):
            print(path)
print_pdf("D:\\Python","demo",os.listdir("D:\\Python\\demo"))
