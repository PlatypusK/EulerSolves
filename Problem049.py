'''
Created on 1. mars 2011

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
    return [truthList, primeList]


def getFourDigitPrimes():
    foo=getPrimeList(10000)
    foo1=foo[0]
    foo2=foo[1]
    return [foo1,foo2[168:]]
    

def getTerms():
    fourDigitList=getFourDigitPrimes()
    fourDigitTruth=fourDigitList[0]
    fourDigitPrimes=fourDigitList[1]
    checkList=[]
    for x in range(0,len(fourDigitPrimes)):
        for y in range(x+1,len(fourDigitPrimes)):
            if sorted(str(fourDigitPrimes[y]))==sorted(str(fourDigitPrimes[x])):
                foo=fourDigitPrimes[y]-fourDigitPrimes[x]
                if fourDigitPrimes[y]+foo<10000 and fourDigitTruth[fourDigitPrimes[y]+foo] and sorted(str(fourDigitPrimes[y]))==sorted(str(fourDigitPrimes[y]+foo)):
                    checkList.append(str(fourDigitPrimes[x])+str(fourDigitPrimes[y])+str(fourDigitPrimes[y]+foo))
    return checkList
    
    
    
def main():
    clock()
    print getTerms()
    print clock()
if __name__ == '__main__':
    main()