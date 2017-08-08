'''
Created on 1. mars 2011

@author: Ketil
'''

from time import clock
    
def main():
    clock()
    print repr(sum([x**x for x in range(1,1001)]))[-11:]
    print clock()
if __name__ == '__main__':
    main()