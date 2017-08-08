'''
Created on 28. feb. 2011

@author: Ketil
'''

import math
from time import clock

def getPrimeList(below): # Creates a list of all prime numbers below this number
    truthList=[True for x in xrange(0, below)]
    truthList[0]=False
    truthList[1]=False
    primeList=[]
    for i in xrange(2,below):
        if truthList[i]:
            x=i
            y=2
            while y*x<below:
                truthList[y*x]=False
                y=y+1            
            primeList.append(i)
    return [truthList, primeList]


def findDistinctPrime(number, truthList):
    if truthList[number]:
        return["prime"]
    primelist = []
    i=2
    while True:
        product=1
        if number % i == 0 and truthList[i]:
            primelist.append(i)
            n=2
            while number % math.pow(i, n)==0:
                primelist.append(i)
                n=n+1
            for x in primelist:
                product=product*x
            if product == number:
                primelist=set(primelist)
                return len(primelist)
        i=i+1
    


def fourFactors(below):
    foo=getPrimeList(below)
    truthList=foo[0]
    primeCount,x=0,2
    while True:
        foo=findDistinctPrime(x,truthList)
        if foo!=4:
            primeCount=0
        else:
            primeCount+=1
        if primeCount==4:
            return x-3
        x+=1



def main():
    clock()
    print fourFactors(1000000)
    print clock()
if __name__ == '__main__':
    main()