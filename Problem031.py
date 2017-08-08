'''
Created on 29. jan. 2011

@author: Ketil
'''

from time import clock


def waysToMake(amount,pick, total=0, ways=0, pickList=[]):
    total+=pick
    
    if total==amount:
        return 1
    elif total>amount:
        return 0
    else:
        if 1>=pick:
            ways+=waysToMake(amount,1,total)
        if 2>=pick:
            ways+=waysToMake(amount,2,total)
        if 5>=pick:
            ways+=waysToMake(amount,5,total)
        if 10>=pick:
            ways+=waysToMake(amount,10,total)
        if 20>=pick:
            ways+=waysToMake(amount,20,total)
        if 50>=pick:
            ways+=waysToMake(amount,50,total)
        if 100>=pick:
            ways+=waysToMake(amount,100,total)
        if 200>=pick:
            ways+=waysToMake(amount,200,total)
    return ways
    

def main():
    clock()
    print waysToMake(200,0)
    print clock()
if __name__ == '__main__':
    main()