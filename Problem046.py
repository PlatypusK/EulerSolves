'''
Created on 28. feb. 2011

@author: Ketil
'''


from time import clock
import bisect

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

def getDoubleSquareList(below):
    foo=[]
    x=1
    while 2*x**2<below:
        foo.append(2*x**2)
        x+=1
    return foo

def getCompositeList(truthList,below):
    compositeList=[]
    for x in range(3,below,2):
        if truthList[x]==False:   
            compositeList.append(x)
    return compositeList

def binarySearch(value,inList):
    foo=bisect.bisect_left(inList,value)
    if inList[foo]==value:
        return True
    else:
        return False

def composite(below):
    foo=getPrimeList(below)
    truthList=foo[0]
    primeList=foo[1]
    doubleSquareList=getDoubleSquareList(below)
    compositeList=getCompositeList(truthList,below)
    sumList=[]
    for x in primeList:
        for y in doubleSquareList:
            sumList.append(x+y)
    sumList=set(sumList)
    sumList=list(sumList)
    sumList.sort()
    for x in compositeList:
        if binarySearch(x,sumList)==False:
            return x

           

def main():
    clock()
    print composite(10000)
    print clock()
if __name__ == '__main__':
    main()