'''
Created on 2. mars 2011

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

def longestSumToPrime(below):
    primeList=getPrimeList(below+1)
    truthList=primeList[0]
    primeList=primeList[1]
    print clock()
    sums=[]
    longest=2
    for x in range(0,len(primeList)):
        sums.append(sum(primeList[x:x+2]))
    z=2
    while True:
        for x in range(0,len(sums)):
            sums[x]=sums[x]+primeList[x+z]
            if sums[x]>below:
                sums=sums[0:x]
                break
            if truthList[sums[x]]:
                longest=sums[x]
        z+=1
        if len(sums)==0:
            break
    return longest

def main():
    clock()
    print longestSumToPrime(10000000)
    print clock()
if __name__ == '__main__':
    main()