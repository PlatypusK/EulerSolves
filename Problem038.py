'''
Created on 2. feb. 2011

@author: Ketil
'''

from time import clock

def  pandigital(max=0):
    for x in range(1,9999):
        foo=""
        y=1
        while len(foo)<9:
            foo+=repr(x*y)
            y+=1          
        if y>1 and len(foo)==9 and len(set(foo))==9 and len(set(foo))==9:
            if int(foo)>max and foo.count("0")==0:
                max=int(foo)
    return max

def main():
    clock()
    print pandigital()
    print clock()
if __name__ == '__main__':
    main()