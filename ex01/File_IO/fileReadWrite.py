# -*- coding: utf-8 -*-
import os
path = os.getcwd()+'/text.txt'
print path
f = open(path)
print
print f.read()
f = open(path,'a+')
f.write('\nfile write a line,')
