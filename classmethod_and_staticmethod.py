class c:
    a=6
    def __init__(self):
       self.a=5
       self.b=6
    
    '''
    we use classmethod for print or use the class variable..
    here instance varibale is int(a) and class variable is also int(a) using this classmethod we can choose the class variable
    '''
    @classmethod
    def geta(cls): 
        return cls.a

    def word(self):
        return "echo echo"
    # or

    @staticmethod
    def pri():
        print('echo echo from staticmethod')

c1 = c()

print(c1.a)
#print(c1.a) here i could not get the class varibale it will print instance varibale
print(c1.geta()) 
print(c1.word())

c.pri() #here c is class and here use staticmethod 

