'''
Created on 23. jan. 2011

@author: Ketil
'''

from time import clock
from Problem021 import checkProperFactors

def sumOfIntegers(lessThan, abundantNumbers=[],sumArray=[]):
    for x in range(2,lessThan+1):
        if sum(checkProperFactors(x))>x:
            abundantNumbers.append(x)
    foo=len(abundantNumbers)
    abundantNumbers.sort()
    x=0
    half=lessThan/2
    print clock()
    while abundantNumbers[x] < half:
        for y in range(x,foo):
            z=abundantNumbers[x]+abundantNumbers[y]
            if z<=lessThan:
                sumArray.append(z)
            else:
                break
        x+=1
    sumArray=set(sumArray)
    positiveIntegers=set([i for i in range(1,lessThan)])
    totalSet=positiveIntegers-sumArray
    totalSet=list(totalSet)
    totalSet.sort()
    print totalSet
    print totalSet[-1]
    print sum(totalSet)



def main():
    clock()
    sumOfIntegers(30000)
    print clock()
if __name__ == '__main__':
    main()