# -*- coding: utf-8 -*- #
from random import randint
a = randint(1,100)
b = randint(1,100)
sa = str(a)
sb = str(b)
num = int(input('덧셈퀴즈'+sa+'+'+sb+'의 값은?'))
if((a+b)==num):
    print('맞았습니다')
else:
    print('틀렸습니다')
