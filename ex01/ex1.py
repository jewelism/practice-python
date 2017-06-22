# def con(a):
#     return a/9*5
#
# ftemp = 90
# ctemp = con(90)
# print(ftemp)
# print(ctemp)

# print('안녕하세요? 여러분\n 저는 파이썬을 무척 좋아합니다 \n 9*8은',9*8,'입니다\n안녕히 계세요')
#
# bbb = '철수야'
# print(bbb)

# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.shape('arrow')
# t.shape('turtle')
# t.forward(100)

import turtle
t=turtle.Turtle()
t.shape('turtle')
for i in range(0,9):
    t.forward(100)
    t.right(40)