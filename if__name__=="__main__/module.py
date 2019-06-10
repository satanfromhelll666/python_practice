
def three():
    
    print('this is module 3')
    print(__name__)

def four():
    print('this is module 4')

def main():
    three()
    four()

if __name__ == '__main__':
    main()
    

