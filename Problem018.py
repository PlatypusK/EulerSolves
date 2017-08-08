'''
Created on 20. jan. 2011

@author: Ketil
'''


from time import clock


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


#def checkPath(matrix,x,y,sum1=0,sum2=0):
#    b=x+1
#    for a in range(y+1,len(matrix)):
#        print matrix[a][b]
#        sum2+=matrix[a][b]
#        b+=1
#    b=x
#    print "path completed"
#    for a in range(y+1,len(matrix)):
#        print matrix[a][b]
#        sum1+=matrix[a][b]
#    return[sum1,sum2]
#    
#        
#def maxTotal(filename,x=0,y=0):
#    matrix=getMatrix(filename)
#    totalPath=[]
#    for a in matrix:
#        path=checkPath(matrix,x,y)
#        print "second path completed"
#        if path[0]<path[1]:      
#            totalPath.append(matrix[y][x])
#            x+=1
#            y+=1 
#        else:
#            totalPath.append(matrix[y][x])
#            y+=1
#    return totalPath

def maxTotal(filename):
    matrix=getMatrix(filename)
    for y in range(len(matrix)-1,0,-1):
        for x in range(0,len(matrix[y-1])):
            matrix[y-1][x]=matrix[y-1][x]+max(matrix[y][x],matrix[y][x+1])
    return matrix[0][0]



def main():
    clock()
    foo= maxTotal("Problem18Number.txt")
    print foo
    print clock()
if __name__ == '__main__':
    main()