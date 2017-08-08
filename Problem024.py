'''
Created on 24. jan. 2011

@author: Ketil
'''

from time import clock


def nextPermutation(a):
    foo=len(a)
    temp=[]
    x=1
    while x<foo-1:
        if a[-1]<a[-2]:
            temp.append(a.pop())
        else:
            temp.append(a.pop())
            min=a[-1]
            for y in temp:
                if y>min:
                    min=y
                    break
            for y in temp:
                if y<min and a[-1]<y :
                    min=y
            z=a[-1]
            temp.append(z)       
            a[-1]=min
            temp.sort()
            temp.remove(min)
            while len(a)<foo:
                a.append(temp.pop(0))
            return a
        x-=1    
    return a

def lexicographicPermutation(permutation,digits):
    digits.sort
    x=1
    while True:
        x+=1
        digits=nextPermutation(digits)
        if x==permutation:
            print x
            return digits

def main():
    clock()
    print lexicographicPermutation(123415,[0,1,2,3,4,5,6,7,8,9])
    print clock()
if __name__ == '__main__':
    main()