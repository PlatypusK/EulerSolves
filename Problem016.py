'''
Created on 20. jan. 2011

@author: Ketil
'''

from time import clock

def sumOfDigits(number):
    number=str(number)
    number=list(number)
    for x in range(0,len(number)):
        number[x]=int(number[x])
    return sum(number)

def main():
    clock()
    foo= sumOfDigits(2**1000)
    print foo
    print clock()
if __name__ == '__main__':
    main()