# -*- coding: utf-8 -*- #
from random import randint

cnt = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(100):
    cnt[randint(1,6)+randint(1,6)-2] += 1
for j in cnt:
    print(j)