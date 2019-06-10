
from module_test import * 
#when i import a module if there are any function call in the module it will call automaticly ....
#for thats why we use __name__== "__main__" .... if a code run from the main script ..
#the main script ( __name__) variable always return the __main__
#if a code run from the main script and the import script (__name__) variable will return the name of the script   


def one():
    print('this is test 1')
    three()

def two():
    print('this is test 2')
    
def main():
    one()
    two()


main()
    





