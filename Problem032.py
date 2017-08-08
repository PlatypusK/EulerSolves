'''
Created on 30. jan. 2011

@author: Ketil
'''
from time import clock


def panDigital(digits):
    aLen=120*digits
    bLen=1200*digits
    aList=[x for x in range(1,aLen)]
    bList=[x for x in range(1,bLen)]
    multiplicand=[]
    multiplier=[]
    answerList=[]
    for x in aList:
        for y in bList:
            answer=x*y
            if answer>1200*digits:
                break
            aStr=repr(x)
            bStr=repr(y)
            answerStr=repr(answer)
            stringRepr=repr(x)+repr(y)+repr(answer)             
            if stringRepr.count("0")==0 and len(set(stringRepr))==digits:
                    multiplicand.append(x)
                    multiplier.append(y)
                    answerList.append(answer) 
    return sum(list(set(answerList)))


def main():
    clock()
    print panDigital(9)
    print clock()
if __name__ == '__main__':
    main()