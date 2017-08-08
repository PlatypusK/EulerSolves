'''
Created on 20. jan. 2011

@author: Ketil
'''

from time import clock


def numberToString(number):
    tenStrings=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    hundredStrings="hundred"
    add="and"
    lowNumberStrings=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    
    digitString=str(number)
    digitList=[]
    for x in digitString:
        digitList.append(int(x))
    if number < 20:
        return lowNumberStrings[number]
    if 19 < number < 100 and digitList[1]!=0:
        return tenStrings[digitList[0]-2]+lowNumberStrings[digitList[1]]
    if 19 < number < 100:
        return tenStrings[digitList[0]-2]
    if 99 < number < 1000 and digitList[1]+digitList[2]!=0 and digitList[1]<2:
        lowNumber=digitList[2]+digitList[1]*10
        return lowNumberStrings[digitList[0]]+hundredStrings+add+lowNumberStrings[lowNumber]
    if   99 < number < 1000 and digitList[2]==0 and digitList[1]==0:
        return lowNumberStrings[digitList[0]]+hundredStrings  
    if   99 < number < 1000 and digitList[2]==0 and digitList[1]>1:
        return lowNumberStrings[digitList[0]]+hundredStrings+add+tenStrings[digitList[1]-2]
    if 99 < number < 1000 and digitList[2]!=0 and digitList[1]>1:
        return lowNumberStrings[digitList[0]]+hundredStrings+add+tenStrings[digitList[1]-2]+lowNumberStrings[digitList[2]]
    if number==1000:
        return "OneThousand"
    
    return "what number?"
    


def numbersInStrings(start, end):
    sum=0
    for x in range(start,end+1):
        foo=numberToString(x)
        sum+=len(foo)
    return sum
    
def main():
    clock()
    foo= numbersInStrings(1,1000)
    print foo
    print clock()
if __name__ == '__main__':
    main()