'''
Created on 13. jan. 2011

@author: Ketil
'''

import time

def getPrimeList(below): # Creates a list of all prime numbers below this number
    truthList=[True for x in xrange(0, below)]
    truthList[0]=False
    truthList[1]=False
    primeList=[]
    for i in xrange(2,below):
        if truthList[i]:
            x=i
            y=2
            while y*x<below:
                truthList[y*x]=False
                y=y+1            
            primeList.append(i)
    return primeList

def main():      
    time.clock()
    print sum(getPrimeList(2000000)) 
    print time.clock()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()