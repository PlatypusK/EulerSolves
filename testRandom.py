'''
Created on 31. mars 2011

@author: Ketil
'''
from random import random
from math import factorial

def main():
    print random()
    total=0
    for x in range(1000):
        if random()<0.166666667:
            total+=1
    print [factorial(x) for x in range(11)]
    print total

main()