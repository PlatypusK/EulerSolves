'''
Created on 27. jan. 2011

@author: Ketil
'''

from time import clock


def digitsFibonacci(digits,term1=1,term2=1,whichTerm=2):
    while len(str(term2))<digits:
        term3=term1+term2
        term1=term2
        term2=term3
        whichTerm+=1
    return whichTerm


def main():
    clock()
    print digitsFibonacci(1000)
    print clock()
if __name__ == '__main__':
    main()