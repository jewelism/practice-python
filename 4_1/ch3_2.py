# -*- coding: utf-8 -*- #
from random import randint
num = randint(1,99)
print(num)
num2 = int(input('값을 입력하세요:'))
a = int(num2/10) #입력받은값의 10의자리
b = num2%10  #입력받은값의 1의자리
c = int(num/10) #난수의 10의자리
d = num%10      #난수의 1의자리
if((a==c)and(b==d)or(a==d)and(b==c)): #
    print('1등상 100만원입니다')
elif(a==c):
    print('2등상 50만원입니다')
elif(b==d):
    print('2등상 50만원입니다')
elif(a==d):
    print('2등상 50만원입니다')
elif(b==c):
    print('2등상 50만원입니다')
else:
    print('상품은 없다')