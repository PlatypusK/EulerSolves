'''
Created on 29. des. 2010

@author: Ketil
'''
#        Recursive solution

#def check(number,originalproduct):
#    if number == 1:
#        return originalproduct
#    i=0
#    while i > -1:
#        i=i+1
#        product=originalproduct*i
#        if product % number == 0:
#            product = check(number-1,product)
#            return product 
from time import clock

#        Iterative solution
def check(maxDivisor):
    i=0
    originalProduct=maxDivisor
    divisor=maxDivisor
    product=maxDivisor
    while True:
        i=i+1
        product=originalProduct*i
        if product%divisor==0:
            divisor-=1
            i=0
            originalProduct=product
            if divisor==1:
                return originalProduct
            
    
def main():  
    clock()
    print check(20)
    print clock()

if __name__ == '__main__':
   main()