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
    
    
def circularPrimes(below):
    foo=getPrimeList(below)
    primeList=foo[0]
    truthList=foo[1]
    circularList=[]
    for x in primeList:
        number1=list(repr(x))
        number2=number1
        for y in number2:
            number2.append(number2.pop(0))
            first=""
            for z in number2:
                first+=z
            firstInt=int(first)
            if truthList[firstInt]==False:
                break
            if firstInt==x:
                circularList.append(x)
                break  
    print circularList
    return len(circularList)

def main():
    clock()
    print circularPrimes(1000000)
    print clock()
if __name__ == '__main__':
    main()