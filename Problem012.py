'''
Created on 16. jan. 2011

@author: Ketil
'''
from time import clock
import math

def findInList(searchList, searchNumber):
    hi = len(searchList)
    lo=0
    while lo < hi:
        mid = (lo+hi)//2
        midval = searchList[mid]
        if midval < searchNumber:
            lo = mid+1
        elif midval > searchNumber: 
            hi = mid
        else:
            return mid
    return -1

def checkFactors(number):
    if number<2:
        return []
    i=2
    factors=[1,number]
    while i<=math.sqrt(number):
        if not number%i:
            factors.append(number/i)
            factors.append(i)

        i+=1
    return len(factors)

def findSmallestWithNumberofFactorsOrMore(factorNumber):
    index=factorNumber
    while True:
        newNumber=(index+1)*index/2
        foo=checkFactors(newNumber)
        if foo >= factorNumber:
            return newNumber
        index+=1

def main():
    print"2"
    clock()
    a=findSmallestWithNumberofFactorsOrMore(500)
    print a
    print clock()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()