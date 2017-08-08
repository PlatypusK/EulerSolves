'''
Created on 29. des. 2010

@author: Ketil
'''

import math

def findPrime(number):#code only gives smallest factors, not prime factors
    primelist = []
    i=2
    
    while(i<number):
        product=1
        if number % i == 0:
            primelist.append(i)
            n=2
            while number % math.pow(i, n)==0:
                primelist.append(i)
                n=n+1
            for x in range(0, len(primelist)):
                product=product*primelist[x]
            if product == number:
                break
        i=i+1
    primelist.sort()
    return primelist

def main():      
    print findPrime(600851475143)
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()