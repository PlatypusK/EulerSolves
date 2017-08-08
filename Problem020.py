'''
Created on 21. jan. 2011

@author: Ketil
'''
from time import clock
import math

def getFactorialDigits(number, sum=0):
    number=str(math.factorial(number))
    for x in number:
        sum+=int(x)
    return sum
    




def main():
    clock()
    foo= getFactorialDigits(100)
    print foo
    print clock()
if __name__ == '__main__':
    main()