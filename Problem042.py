'''
Created on 26. feb. 2011

@author: Ketil
'''

from time import clock


def readFile(filename):
    f = open(filename, "r")
    fileContents = f.read()
    f.close()
    return fileContents

def getTriangleList(maxValue):
    triangleNumbers, n, triangleNumber = [], 1, 0
    while triangleNumber<maxValue:
        triangleNumber=n*(n+1)*1/2
        triangleNumbers.append(triangleNumber)
        n+=1
    return triangleNumbers

def triangleWords(filename):
    words =readFile(filename)
    wordList=[]
    sumList=[]
    word=""
    for x in words:
        if x=="\"" and word!="":
            wordList.append(word)
            z=0
            for y in word:
                z+=ord(y)-64
            sumList.append(z)
            word=""
        if x!="\"" and x!=",":
            word+=x
    maxValue = max(sumList)
    triangleNumbers=getTriangleList(maxValue)
    numberOfTriangleWords=0
    for x in triangleNumbers:
        for y in sumList:
            if x==y:
                numberOfTriangleWords+=1
    return numberOfTriangleWords

def main():
    clock()
    print triangleWords("Problem42Words.txt")
    print clock()
if __name__ == '__main__':
    main()