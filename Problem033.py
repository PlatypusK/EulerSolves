'''
Created on 30. jan. 2011

@author: Ketil
'''

from time import clock

def badCancelling(x,y):
    
    for a in x:
        if y.count(a)>0:
            x.remove(a)
            y.remove(a)       
    xStr=""
    yStr=""
    for a in x:
        xStr+=str(a)
    for a in y:
        yStr+=str(a)
    if float(yStr)!=0 and len(xStr)==1:
        return float(xStr)/float(yStr)
    else:
        return 0

def goodCancelling(x,y):
    for a in range(x,0,-1):
        if x%a==0 and y%a==0:
            return [x/a,y/a]
    return [x,y]
        
def curiousFractions():
    dividend=[]
    divisor=[]
    for x in range(10,100):
        for y in range(x+1,100):
            foox=list(repr(x))
            fooy=list(repr(y))
            if x%10!=0 and float(x)/float(y)==badCancelling(foox,fooy):
                dividend.append(x)
                divisor.append(y)
    dividend=reduce(lambda x,y:x*y,dividend) 
    divisor=reduce(lambda x,y:x*y,divisor)
    print goodCancelling(dividend,divisor)

def main():
    clock()
    print curiousFractions()
    print clock()
if __name__ == '__main__':
    main()