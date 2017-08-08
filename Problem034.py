'''
Created on 30. jan. 2011

@author: Ketil
'''

from time import clock
from math import factorial



def factorialSums():
    foo=[factorial(x) for x in range(0,10)]
    print foo
    nineFac=foo[-1]
    fooLength=len(foo)
    total=0
    for x in range(3,nineFac):
        foo2=repr(x)
        sum=0
        for y in foo2:
            sum+=foo[int(y)]
        if int(x)==sum:
            print x
            total+=x
    return total


def main():
    clock()
    print factorialSums()
    print clock()
if __name__ == '__main__':
    main()