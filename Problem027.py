'''
Created on 28. jan. 2011

@author: Ketil
'''

from time import clock

def getPrimeList(below): # Creates a list of all prime numbers below this number
    truthList=[True for x in xrange(0, below)]
    primeList=[]
    for i in xrange(2,below):
        if truthList[i]:
            y=2
            while y*i<below:
                truthList[y*i]=False
                y=y+1            
            primeList.append(i)
    truthList[0]=False 
    truthList[1]=False
    return truthList

def checkPrime(n):    
    for i in range(2,int(pow(n,0.5))+1):
        if n % i == 0:
            return False
    return True

def getCoefficients(a,b,c):
    primes=getPrimeList(c)
    max=0
    aMax=0
    bMax=0
    for x in range(-a,a+1):
        for y in range(0,b+1):
            if primes[y]==True:
                n=0
                fx=n**2+x*n+y
                z=0
                while primes[fx]==True:
                    fx=n**2+x*n+y
                    n+=1
                    z+=1
                    if z>max:
                        max=z
                        aMax=x
                        bMax=y
    print aMax*bMax
    return [aMax,bMax]

def main():
    clock()
    print getCoefficients(10000,10000,1000000) 
    print clock()
if __name__ == '__main__':
    main()