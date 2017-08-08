'''
Created on 29. jan. 2011

@author: Ketil
'''
from time import clock


def distinctTerms(aLow,aHigh,bLow,bHigh):
    aList=[x for x in range(aLow,aHigh+1)]
    bList=[x for x in range(bLow,bHigh+1)]
    termsList=[]
    for x in aList:
        for y in bList:
            termsList.append(x**y)
    return len(set(termsList))


def main():
    clock()
    print distinctTerms(2,100,2,100)
    print clock()
if __name__ == '__main__':
    main()