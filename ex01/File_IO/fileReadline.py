# -*- coding: utf-8 -*-
import os
path = os.getcwd()+'/text.txt'
print path
f = open(path)

for x in range(3):
    line = f.readline()
    print line,

lines = f.readlines() ### lines는 읽어서, list로 저장한다
print lines
import sys
sys.stdout.writelines(lines[:2]) ### 남은것들중에 2미만 출력
print '-----------------'
sys.stdout.writelines(lines[1:3]) ### 남은것들중에 1이상 3미만출력
print '--- 마지막5개출력 ---'
sys.stdout.writelines(lines[-5:])