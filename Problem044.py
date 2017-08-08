'''
Created on 27. feb. 2011

@author: Ketil
'''

from time import clock
from math import sqrt

def getPentagonalNumbers(amount):
    return [x*(3*x-1)/2 for x in range(1,amount)]

        
def isPentagonal(P):
    x1=(1+sqrt(1-4*3*(-2*P)))/(2*3)
    if int(x1)/x1==1.0000:
        return True
    else:
        return False
   
   
def smallestDiff():
    numbers=getPentagonalNumbers(3000)
    for x in range(0,2999):
        for y in range(x,2999):
            if isPentagonal(numbers[x]+numbers[y]) and isPentagonal(numbers[y]-numbers[x]):
                print x
                print y
                print numbers[x]
                print numbers[y] 
                return numbers[y]-numbers[x]
                



def main():
    clock()
    print smallestDiff()
    print clock()
if __name__ == '__main__':
    main()