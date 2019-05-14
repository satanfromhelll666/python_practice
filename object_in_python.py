class computer:
    
    def __init__(self,pro,ram):

        self.x=pro #here self.x is object variable and pro and ram is variable which is pass through the object call;
        self.y=ram
        
    def function(self):
        print('this computer has',self.x,'processor and',self.y, ' ram' )

com1= computer('i5',16)
com1.function()
com2=computer('i3',8)
com2.function()