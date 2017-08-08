'''
Created on 18. jan. 2011

@author: Ketil
'''
from time import clock

def readFile(filename):
    f = open(filename, "r")
    fileContents = f.read()
    f.close()
    return fileContents

def getNumbers(filename):
    matrixTemp=readFile(filename)
    y=0
    matrix=[""]
    for c in matrixTemp:
        if len(matrix[y])==50:
            matrix.append("")
            y+=1
        if c!="\n":
            matrix[y]=matrix[y]+c
    matrixTemp=[]
    y=0
    for c in range(0,len(matrix)):
        matrixTemp.append(int(matrix[c]))
    return matrixTemp




def main():
    clock()
    a=getNumbers("Problem13Number.txt")
    print sum(a)
    print clock()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()