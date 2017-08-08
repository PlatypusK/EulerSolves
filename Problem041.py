'''
Created on 2. feb. 2011

@author: Ketil
'''

from time import clock
from math import factorial
from math import sqrt

def intToArray(a):
    b=str(a)
    a=[]
    for x in b:
        a.append(int(x))
    return a

def arrayToInt(a):
    return int(''.join(map(str,a)))

def listSwap(swapThisList,index1,index2):
    swapThisList[index1],swapThisList[index2]=swapThisList[index2],swapThisList[index1]
    return swapThisList


def nextPermutation(number,maxPermutation):
    a=intToArray(number)
    foo=len(a)
    permutation,x=1,0
    if factorial(foo)<maxPermutation:
        return "There are not that many permutations"
    while permutation<maxPermutation:
        y=(maxPermutation-permutation)/factorial(foo-x)
        yMod=(maxPermutation-permutation)%factorial(foo-x)
        if y>0:
            permutation=maxPermutation-yMod
            a=listSwap(a,x-1,x+y-1)
            while y+x-1>x:
                if a[y+x-1]<a[y+x-2]:
                    a=listSwap(a,y+x-1,y+x-2)
                y-=1  
        x+=1
    return arrayToInt(a)

def checkPrime(n):
    rt=int(sqrt(n))
    if n<2:
        return False
    for i in range(2,rt+1):
        if n % i == 0:
            return False
    return True


def pandigitalPrime(start):
    while True:
        for x in range(factorial(len(str(start))),2,-1):
            foo=nextPermutation(start,x)
            if checkPrime(foo):
                return foo
        start=intToArray(start)
        start.pop()
        start=arrayToInt(start)
        

def main():
    clock()
    print pandigitalPrime(12345678)
    print clock()
if __name__ == '__main__':
    main()