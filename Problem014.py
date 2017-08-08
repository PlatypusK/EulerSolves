'''
Created on 19. jan. 2011

@author: Ketil
'''
from time import clock


def getMax(below):
    print below
    iterationsArray=[-1 for x in range(0,below)]
    iterationsMax=0
    maxNumber=0
    for y in range(1,below):
        iterations=0
        last=y
        while last != 1:
            iterations+=1
            if last<below and iterationsArray[last]!=-1:
                iterations+=iterationsArray[last]
                break
            elif last%2==0:
                last=last/2
            else:
                last=3*last+1
        iterationsArray[y]=iterations
        if iterations > iterationsMax:
            iterationsMax=iterations
            maxNumber=y
    return maxNumber

def main():
    clock()
    print getMax(1000000)
    print clock()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()