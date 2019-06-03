class vs_code:
    def execute(self):
        print('light weight')
        print('smooth')

class pycharm:
    def execute(self):
        print('heavy wight')
        print('get some adv')
        print('has dracula mode')

class laptop:
    def code(self,ide):

        ide.execute()

ide =  vs_code() #here if i assign ide = pycharm it will print pycharm excute mehtod

lp = laptop

lp.code(lp,ide)

