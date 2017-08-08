'''
Created on 10. jan. 2011

@author: Ketil
'''

def triplet(sum):
    for a in range(1,sum):
        for b in range(a,sum):
            if sum**2-2*sum*a-2*sum*b+2*a*b == 0:
                return [a, b, sum-a-b]

def main():      
    abc = triplet(10000) 
    print abc
    print sum(abc)
    print reduce(lambda x,y: x*y, abc)
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()