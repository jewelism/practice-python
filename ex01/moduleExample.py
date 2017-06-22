# -*- coding: utf-8 -*-
import math
print math.pi
print
################calendar############
import calendar
print calendar.prmonth(2017,3)
print
############ GUI ############
# from Tkinter import *
# widget = Label(None, text='I love Python!')
# widget.pack()
# widget.mainloop()
import os
cwd = os.getcwd()
print cwd
print os.listdir(cwd)
os.rename('gugudan.py','99dan.py')
print os.listdir(cwd)
os.rename('99dan.py','gugudan.py')
print os.listdir(cwd)

import string
print string.capitalize('python')        # 첫 글자를 대문자로
print string.replace('simple', 'i', 'a') #'simple'의 'i'를 'a'로 바꿈
print string.split('break into words')   # 문자열을 분리한 리스트 구함

import re, globAndPath
p = re.compile('.*m.*a.*') ###정규식
for i in globAndPath.globAndPath('*'):
    m = p.match(i)
    if m:
        print m.group()

import webbrowser
url='http://www.naver.com'
# webbrowser.open(url)

import random
print "random number is :",random.random()
print random.randrange(1,7)

abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc)
print abc
print random.choice(abc)

print random.choice([True, False])