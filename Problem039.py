'''
Created on 2. feb. 2011

@author: Ketil
'''

from time import clock

def maxSolutions(p):
    p=p+1
    pHalf=p/2
    solutions=[]
    for x in range(1,p):
        for a in range(1,pHalf):
            for b in range(a,pHalf): 
                c=x-a-b   
                if c>0 and a**2+b**2==c**2:
                    solutions.append([x,a,b,c])                   
    print solutions
    maxP=0
    count=0
    maxCount=0
    thisP=0
    for x in solutions:
        if x[0]!=thisP:
            thisP=x[0]
            count=1
        count+=1
        if count>maxCount:
            maxP=thisP
            maxCount=count
    return maxP
    

def main():  
    clock()
    print maxSolutions(1000)
    print clock()

if __name__ == '__main__':
    main()