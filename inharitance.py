class a:

    def __init__ (self):
        
        print('this is init from class-a')

    def a1():
        print("this is a1")

class b:

    def __init__(self):
        print('this is init from class-b')

    def b1():
        print('this is b1')

class c(b,a):

    def __init__(self):
        super().__init__()
        print('this is init from class-c')
        

    def c1():
        print('this is c1')


test1=a
test1.a1() #here i can access a1 function from class a and test1 is a object of a

test2=c

test2.a1() #here i can access a1 function from class c and here i inharite class a to class c
test2.c1()
test2.b1()

test2() #here i can call constructor which in class c --use super methos and here we can print a constructor or b constructor.

