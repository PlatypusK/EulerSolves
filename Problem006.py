'''
Created on 5. jan. 2011

@author: Ketil
'''

def diffSquareSum(number):
    sumOfSquares = 0
    squareOfSum = 0
    for i in range(1,number+1):
        sumOfSquares = pow(i,2)+sumOfSquares
    for i in range(1,number+1):
        squareOfSum=squareOfSum+i
    squareOfSum=pow(squareOfSum,2)
    return (squareOfSum-sumOfSquares)

def main():      
    print diffSquareSum(100)
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()