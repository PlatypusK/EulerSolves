'''
Created on 27. jan. 2011

@author: Ketil
'''
from time import clock


def doLongDivision(numerator,denominator):
    a=numerator
    b=denominator
    answerArray=[]
    checkArray=[]
    while True:
        if checkArray.count(float(a)/float(b))>0:
            return answerArray
        c=a/b
        answerArray.append(c)
        checkArray.append(float(a)/float(b))
        c=c*b
        a=a-c
        a=10*a

        
        

def longestRecurringCycle(d):
    max=0
    longest=0
    for x in range(1,d):
        foo=len(doLongDivision(1,x))
        if max<foo:
            max=foo
            longest=x
    return longest

def main():
    clock()
    print longestRecurringCycle(1000)
    print clock()
if __name__ == '__main__':
    main()