'''
Created on 1. feb. 2011

@author: Ketil
'''

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
    return [primeList,truthList]


def truncateLeft(number):
    foo=list(str(number))
    foo.pop(0)
    a=""
    for x in foo:
        a+=str(x)
    if a!="":
        return int(a)
    else:
        return 0

def truncateRight(number):
    foo=list(str(number))
    foo.pop()
    a=""
    for x in foo:
        a+=str(x)
    if a!="":
        return int(a)
    else:
        return 0

def truncatablePrimes():
    foo=getPrimeList(1000000)
    primeList=foo[0]
    truthList=foo[1]
    right=False
    left=False
    truncList=[]
    for x in primeList:
        y=x
        while y>0 and truthList[y]:
            y=truncateRight(y)
        if y==0:
            right=True
        else:
            right=False
        y=x
        while right and y>0 and truthList[y]:
            y=truncateLeft(y)
        if y==0:
            left=True
        if left and right and x>10:
            truncList.append(x)
            left=False
            right=False
    print truncList
    print sum(truncList)


def main():
    clock()
    print truncatablePrimes()
    print clock()
if __name__ == '__main__':
    main()