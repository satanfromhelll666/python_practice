class a:
    def mobile():
        print('this is class a mobile')

class b(a):
    pass



mob1 = b

mob1.mobile()#here b inharite a this is why it print this is class a mobile


class c:
    def mobile():
        print('this is class c mobile')

class d(c):
    def mobile():
        #dsfdms
        print('this is class d mobile')

mob2 = d

mob2.mobile() #here it print class d fucntion



