'''
Created on 23. jan. 2011

@author: Ketil
'''

from time import clock

def readFile(filename):
    f = open(filename, "r")
    fileContents = f.read()
    f.close()
    return fileContents


def nameScore(filename):
    names =readFile(filename)
    print names
    nameList=[]
    name=""
    for x in names:
        if x=="\"" and name!="":
            nameList.append(name)
            name=""
        if x!="\"" and x!=",":
            name+=x
    print nameList
    nameList.sort()
    a=0
    valueArray=[]
    for x in nameList:
        a+=1
        valueWord=0
        for y in x:
            valueLetter=ord(y)-64
            valueWord+=valueLetter
        valueArray.append(valueWord*a)
#    print len(valueArray)
#    print len(nameList)
#    print valueArray
#    print nameList
    print sum(valueArray)
    

def main():
    clock()
    nameScore("names.txt")
    print clock()
if __name__ == '__main__':
    main()