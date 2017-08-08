'''
Created on 26. feb. 2011

@author: Ketil
'''

from time import clock
from math import factorial

def intToArray(a):
    b=str(a)
    a=[]
    for x in b:
        a.append(int(x))
    return a

def arrayToInt(a):
    b=list(a)
    return int(''.join(map(str,b)))

def listSwap(swapThisList,index1,index2):
    swapThisList[index1],swapThisList[index2]=swapThisList[index2],swapThisList[index1]
    return swapThisList


def permutation(number,maxPermutation):
    a=list(number)
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
    return a

def divisibilityTests(basePermutation):
    totalPermutations=factorial(len(basePermutation))
    total=0
    print totalPermutations
    skip1=True
    skip2=True
    x=300000
    while x<totalPermutations:
        thisPermutation=permutation(basePermutation, x)
        if thisPermutation[3]%2==0 and sum(thisPermutation[2:5])%3==0 and (thisPermutation[5]==0 or thisPermutation[5]==5) and  arrayToInt(thisPermutation[4:7])%7==0 and arrayToInt(thisPermutation[5:8])%11==0 and arrayToInt(thisPermutation[6:9])%13==0 and arrayToInt(thisPermutation[7:10])%17==0:
            foo=arrayToInt(thisPermutation)
            print foo
            total+=foo
            skip1=True
            skip2=True
        x+=1
    return total   
    

def main():
    clock()
    print divisibilityTests([0,1,2,3,4,5,6,7,8,9])
    print clock()
if __name__ == '__main__':
    main()