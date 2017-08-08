'''
Created on 29. jan. 2011

@author: Ketil
'''
from time import clock





def getSum(maxSides):
    maxDiagonals=(maxSides-1)*2+1
    thisDiagonal=1
    numberDiagonal=0
    x=0
    sum=0
    while numberDiagonal<maxDiagonals:
        for y in range(1,5):
            thisDiagonal=thisDiagonal+x
            sum+=thisDiagonal
            numberDiagonal+=1
            if thisDiagonal==1:
                break
        x+=2
    return sum
    


def main():
    clock()
    print getSum(1001)
    print clock()
if __name__ == '__main__':
    main()