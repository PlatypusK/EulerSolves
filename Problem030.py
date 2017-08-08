'''
Created on 29. jan. 2011

@author: Ketil
'''
from time import clock


def sumPowersOfDigits(power, checkToSize=200000):
    stringList=[repr(x) for x in range(2,checkToSize)]
    numbersList=[]
    for x in stringList:
        sum=0
        for y in x:
            sum+=int(y)**power
        if repr(sum)==x:
            numbersList.append(int(x))
    print numbersList  
    return numbersList    
    

def main():
    clock()
    print sum(sumPowersOfDigits(5,300000))
    print clock()
if __name__ == '__main__':
    main()