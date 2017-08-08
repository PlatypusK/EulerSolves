'''
Created on 2. feb. 2011

@author: Ketil
'''


from time import clock

def getValue():
    number=[]
    x=0
    while len(number)<1000005:
        x+=1
        y=repr(x)
        for z in y:
            number.append(int(z))
    product=number[0]*number[9]*number[99]*number[999]*number[9999]*number[99999]*number[999999]
    return product

def main():
    clock()
    print getValue()
    print clock()
if __name__ == '__main__':
    main()