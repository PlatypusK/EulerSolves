'''
Created on 19. jan. 2011

@author: Ketil
'''
from time import clock
import copy

def Create(x,y, item):#Create a matrix with the dimensions x,y and fill it with items
    matrix=[]
    for a in range(0,x):
        matrix.append([])
        for b in range(0,y):
            matrix[a].append(item)
    return matrix
    

def findNumberRoutes(x,y,depthx, depthy,pathLengthMatrix=None):
    paths=0
    if depthx==depthy==0:
        pathLengthMatrix=Create(x+1,y+1,-1)
    if pathLengthMatrix[depthx][depthy]!=-1: 
        paths=pathLengthMatrix[depthx][depthy]
    else:
        if pathLengthMatrix[depthx][depthy]==-1 and x>depthx:
            paths=findNumberRoutes(x,y,depthx+1,depthy,pathLengthMatrix)
        if pathLengthMatrix[depthx][depthy]==-1 and y>depthy:
            paths+=findNumberRoutes(x,y,depthx,depthy+1,pathLengthMatrix)
    pathLengthMatrix[depthx][depthy]=paths
    if depthx==x and depthy==y:
        return 1
    return paths


def main():
    clock()
    foo= findNumberRoutes(300,600,0,0)
    print foo
    print clock()
if __name__ == '__main__':
    main()