# -*- coding: utf-8 -*- #
import glob
g1 = glob.glob('*.*')
g2 = glob.glob('*.txt')
print ('all :',g1)
if not g2:
    print ('txt : empty')
else:
    print ('txt :',g2)
print
import os.path
files = glob.glob('*')
for x in files:
    print (x),
    if os.path.isdir(x):                  # 디렉토리인가?
        print ('<DIR>')
    else:
        print

