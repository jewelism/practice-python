# -*- coding: utf-8 -*- #
# s = "sub2"
# def sub():
#     print(s)
#     
# sub()

def sub( mylist ):
    # 리스트가 함수로 전달된다. 
    mylist = [1, 2, 3, 4];   # 새로운 리스트가 매개변수로 할당된다. 
    print ("함수 내부에서의 mylist: ", mylist);
    return

# 여기서 sub() 함수를 호출한다. 
mylist = [10, 20, 30, 40];
sub( mylist );
print ("함수 외부에서의 mylist: ", mylist);

def fib(n):    # 피보나치 수열을 화면에 출력한다. 
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

fib(10)

ss = "100"

if(ss!=100):
    print("hello");