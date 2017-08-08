import time

def checkPalindrome(x,y):
    number=x*y
    a=list(str(number))
    b=len(a)
    for i in range(0,b):
        if a[i]!=a[(b-1-i)]:
            return 0
    return 1
    
def largestPalindrome(digits):
    product=pow(10,(digits-1)*2)
    largestNumber = 0
    smallestNumber=pow(10,digits-1)
    factors = [0,0]
    found=0
    for i in range(0,digits):
        largestNumber=largestNumber+9*pow(10,i)  
    for x in range(largestNumber,smallestNumber,-1):
        if pow(x,2)<product and found == 1:
            break
        for y in range(x,smallestNumber,-1):
            isPalindrome=checkPalindrome(x,y)
            if x*y<product:
                break
            if isPalindrome==1:
                product=x*y
                factors = [x,y]
                found=1
                break
        
    print factors
    return product


def main():      
    time.clock()
    print largestPalindrome(4)
    print time.clock()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()