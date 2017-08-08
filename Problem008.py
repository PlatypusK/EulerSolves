'''
Created on 5. jan. 2011

@author: Ketil
'''

def readFile(filename):
    f = open(filename, "r")
    fileContents = f.read()
    fileContents=list(fileContents)
    x=fileContents.count("\n")
    for i in range(0,x):
        fileContents.remove("\n")
    fileContents="".join(fileContents)
    return fileContents

def greatestNumber():
    mainNumber=list(readFile("Problem8Number.txt"))
    product=1
    greatestProduct=0
    numberLength = len(mainNumber)
    for x in range(0,numberLength-4):
        for y in range(x,x+5):
            product=int(mainNumber[y])*product
        if product>greatestProduct:
            greatestProduct=product
        product=1
    return greatestProduct
def main():      
    print greatestNumber()
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()