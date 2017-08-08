'''
Created on 29. des. 2010

@author: Ketil
'''

import sys

def checknumber(number):
    print number
    if (float(number) / 5.0) - int(number/5)==0:
     return 1
    if (float(number) / 3.0) - int(number/3)==0:
     return 1
    else:
     return 0
 

# Define a main() function that prints a little greeting.
def main():
 sum=0
  # Get the name from the command line, using 'World' as a fallback.
 for i in range(1,1000):
  if checknumber(i)==1:
      sum=sum+i
 print sum
      
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
  

 
