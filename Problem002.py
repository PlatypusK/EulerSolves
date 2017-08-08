'''
Created on 29. des. 2010

@author: Ketil
'''
'''
Created on 29. des. 2010

@author: Ketil
'''

def fibonacci(doublelastnumber, lastnumber, sum, max):
    newnumber=doublelastnumber+lastnumber
    if newnumber > max:
        return sum
    if newnumber % 2 == 0:
        sum+=newnumber
    sum=fibonacci(lastnumber,newnumber,sum, max)
    return sum
        
    
# Define a main() function that prints a little greeting.
def main():
 print fibonacci(1,2,2,4000000)      
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()