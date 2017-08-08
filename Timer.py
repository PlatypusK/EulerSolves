'''
Created on 29. des. 2010

@author: Ketil
'''


import timeit
import time

def main():      
#Save the code you want to test beforehand and import it in timeit
    timer = timeit.Timer("Problem004", "import Problem004")
    #You want the fastest time, not the average.
#Your system will theoretically execute code at the same rate each time
#It doesn't because of other processes,
#so get the run with the least interference

    print min(timer.repeat())
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()
    
    #Save the code you want to test beforehand and import it in timeit

