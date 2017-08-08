'''
Created on 21. jan. 2011

@author: Ketil
'''

from time import clock
from math import sqrt

def checkProperFactors(number):
    if number<2:
        return []
    i=2
    factors=[1]
    while i<=sqrt(number):
        if not number%i:
            factors.append(number/i)
            factors.append(i)
        i+=1
    factors=set(factors)
    factors=list(factors)
    return factors

def sumAmicable(biggest, total=0):
    for x in range(2,biggest+2):
        a=sum(checkProperFactors(x))
        b=sum(checkProperFactors(a))
        if b==x and x!=a:
            total+=x
    return total

def main():
    clock()
    print sumAmicable(10000)
    print clock()
if __name__ == '__main__':
    main()