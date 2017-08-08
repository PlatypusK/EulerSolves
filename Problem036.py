'''
Created on 1. feb. 2011

@author: Ketil
'''

from time import clock


def checkPalindrome(number):
    a=list(str(number))
    b=len(a)
    for i in range(0,b):
        if a[i]!=a[(b-1-i)]:
            return False
    return True

def denary2binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr


def checkBinaryPalindrome(binaryString):
    a=list(binaryString)
    b=len(a)
    for i in range(0,b):
        if a[i]!=a[(b-1-i)]:
            return False
    return True

def getPalindromes(below):
    sum=0
    for x in range(1,1000000):
        if checkPalindrome(x):
            if checkBinaryPalindrome(denary2binary(x)):
                sum+=x
    return sum

def main():
    clock()
    print getPalindromes(10000)
    print clock()
if __name__ == '__main__':
    main()