'''
Created on 14. jan. 2011

@author: Ketil
'''
import time

def readFile(filename):
    f = open(filename, "r")
    fileContents = f.read()
    f.close()
    return fileContents

def getMatrix(filename):
    matrixTemp=readFile(filename)
    matrixTemp=list(matrixTemp)
    matrix=[]
    matrix.append([])
    matrix[0].append("")
    y=0
    z=0
    for x in range(0,len(matrixTemp)):
        if matrixTemp[x] != " " and matrixTemp[x]!="\n":
            matrix[z][y]=matrix[z][y]+matrixTemp[x]
        elif matrixTemp[x] == " ":
            matrix[z].append("")
            y+=1
        else:
            z+=1
            matrix.append([])
            matrix[z].append("")
            y=0
    for a in range(0,len(matrix)):
        for b in range(0,len(matrix[a])):
            matrix[a][b]=int(matrix[a][b])
    return matrix
    
def findProductMax(filename, numbers):
    biggest=0
    biggestArray=[]
    matrix=getMatrix(filename)
    for a in range(0,len(matrix)): #Checks horizontal
        for b in range(0,len(matrix[a])-numbers+1):
            product=1
            c=[]
            for i in range(0,numbers):
                product=product*matrix[a][b+i]
                c.append(matrix[a][b+i])
            if biggest < product:
                biggest=product
                biggestArray=c
    for a in range(0,len(matrix)-numbers+1): #Checks vertical
        for b in range(0,len(matrix[a])):
            product=1
            c=[]
            for i in range(0,numbers):
                product=product*matrix[a+i][b]
                c.append(matrix[a+i][b])
            if biggest < product:
                biggest=product
                biggestArray=c
    for a in range(0,len(matrix)-numbers+1): #Checks right diagonal
        for b in range(0,len(matrix[a])-numbers+1):
            product=1
            c=[]
            for i in range(0,numbers):
                product=product*matrix[a+i][b+i]
                c.append(matrix[a+i][b+i])
            if biggest < product:
                biggest=product
                biggestArray=c
    for a in range(0,len(matrix)-numbers+1): #Checks left diagonal
        for b in range(numbers-1,len(matrix[a])):
            product=1
            c=[]
            for i in range(0,numbers):
                product=product*matrix[a+i][b-i]
                c.append(matrix[a+i][b-i])
            if biggest < product:
                biggest=product
                biggestArray=c           
    return biggest, biggestArray

    

def main():
    time.clock()      
    a=findProductMax("Problem11Number.txt", 4)
    print a[0]
    print a[1]
    print time.clock()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()