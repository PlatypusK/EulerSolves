'''
Created on 5. jan. 2011

@author: Ketil
'''

def checkPrime(n):    
    for i in range(2,int(pow(n,0.5))+1):
        if n % i == 0:
            return 0
    return 1
    


def numberPrime(whatPrimeNumber):
    thisPrimeNumber=0
    n=0
    result=0
    while thisPrimeNumber<=whatPrimeNumber:
        n=n+1
        if checkPrime(n)==1:
            thisPrimeNumber=thisPrimeNumber+1
            result=n
    return result
def main():      
    print numberPrime(10001)
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()