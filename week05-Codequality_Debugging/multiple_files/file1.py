import complexbehaviour

#from complexbehaviour import GLOBAL_VAR

GLOBAL_VAR = 2

def main():
    if 2 < 1:
        complexbehaviour.do_complicated_stuff()
    
    print(GLOBAL_VAR)
    print(complexbehaviour.GLOBAL_VAR)
    
    
if __name__ == '__main__':
    main()
    