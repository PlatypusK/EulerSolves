'''
Created on 28. feb. 2011

@author: Ketil
'''

from time import clock
import bisect

def getTriangleList(amount):
    return [x*(x+1)/2 for x in range(1,amount)]

def getPentagonList(amount):
    return [x*(3*x-1)/2 for x in range(1,amount)]

def getHexagonList(amount):
    return [x*(2*x-1) for x in range(1,amount)]

def binarySearch(value,inList):
#    foo=len(inList)
#    if foo%2!=0:
#        foo=foo+1
#    foo/=2
#    foo2=foo
#    while True:
#        foo2=foo2/2
#        if foo2==0:
#            if inList[foo+1]!=value:
#                return False
#            else:
#                return True
#        if inList[foo]<value:
#            foo+=foo2
#        elif inList[foo]>value:
#            foo-=foo2
#        if inList[foo]==value:
#            return True
    foo=bisect.bisect_left(inList,value)
    if inList[foo]==value:
        return True
    else:
        return False

def trifecta(amountOfNumbers):
    triangles=getTriangleList(amountOfNumbers)
    pentangles=getPentagonList(amountOfNumbers)
    hexangles=getHexagonList(amountOfNumbers)
    for x in triangles:
        if binarySearch(x,pentangles) and binarySearch(x,hexangles) and x!=40755 and x!=1:
            return x


def main():
    clock()
    print trifecta(100000)
    print clock()
if __name__ == '__main__':
    main()