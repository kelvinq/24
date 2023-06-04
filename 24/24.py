import sys
from operator import __add__
from operator import __sub__
from operator import __truediv__
from operator import __mul__

i = int(sys.argv[1])
j = int(sys.argv[2])
k = int(sys.argv[3])
l = int(sys.argv[4])
numArray = [i,j,k,l]

"""
m + n = A
A + o = B
B + p = 24
"""

numGrid = numArray
opGrid = ['p','m','t','d']
solGridN = []
solGridO = []
solGridTries = []

'''Build the grid'''
from itertools import permutations
from itertools import product

solGridN = list(permutations(numGrid))
solGridO = list(product(opGrid,repeat=3))

for i in solGridO:
    for j in solGridN:
        solGridTries.append([i,j])
        #print(solGridTries)

#print("Done "+str(len(solGridTries))+" in total.")

def solveOps(opers, x, y):
    try:
        if opers == "p":
            return __add__(x,y)
        if opers == "m":
            return __sub__(x,y)
        if opers == "t":
            return __mul__(x,y)
        if opers == "d":
            return __truediv__(x,y)
    except:
        print("Check operators or that parameters are integers.")

def solve24(solveTry):
    '''
    try = [('d', 't', 'd'), (4, 1, 3, 2)]

    m + n = A
    A + o = B
    B + p = 24
    '''
    a = solveOps(solveTry[0][0], solveTry[1][0], solveTry[1][1])
    b = solveOps(solveTry[0][1], a, solveTry[1][2])
    c = solveOps(solveTry[0][2], b, solveTry[1][3])
    return c

def OpsintoWords(opers):
    """
    Simple helper function to convert symbols into human text.
    """
    try:
        if opers == "p":
            opers = "+"
            return opers
        if opers == "m":
            opers = "-"
            return opers
        if opers == "t":
            opers = "x"
            return opers
        if opers == "d":
            opers = "÷"
            return opers
    except:
        print("Check operators.")


def intoWords(solveTry):
    """
    Function to construct human readable solution.
    """
    a = solveOps(solveTry[0][0], solveTry[1][0], solveTry[1][1])
    b = solveOps(solveTry[0][1], a, solveTry[1][2])
    c = solveOps(solveTry[0][2], b, solveTry[1][3])
    message = "Solution found! \n"+\
           str(solveTry[1][0])+" "+\
           OpsintoWords(solveTry[0][0])+" "+\
           str(solveTry[1][1])+" "+" = "+\
           str(a)+"\n"+\
           str(a)+" "+\
           OpsintoWords(solveTry[0][1])+" "+\
           str(solveTry[1][2])+" "+" = "+\
           str(b)+"\n"+\
           str(b)+" "+\
           OpsintoWords(solveTry[0][2])+" "+\
           str(solveTry[1][3])+" "+" = "+\
           str(c)+"\n\n"
    print(message)

for solveTry in solGridTries:
    if solve24(solveTry) == 24:
        intoWords(solveTry)
    # else:
    #     print (".")
