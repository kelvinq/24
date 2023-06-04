import logging
import sys
from operator import __add__
from operator import __sub__
from operator import __truediv__
from operator import __mul__

if len(sys.argv) != 5:
    print("Enter 4 digits separated by spaces.\nEg python3 24.py 1 2 3 4\n")
    sys.exit()

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

def solveOps(opers, x, y):
    try:
        if opers == "p":
            return __add__(x,y)
        if opers == "m":
            return __sub__(x,y)
        if opers == "t":
            return __mul__(x,y)
        if opers == "d":
            try:
                return __truediv__(x,y)
            except ZeroDivisionError:
                return 9999
    except BaseException:
        logging.exception("An exception was thrown!")

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

def solve24R(solveTry):
    """
    To solve the classic 5, 5, 5, 1 problem.
    """
    a = solveOps(solveTry[0][0], solveTry[1][1], solveTry[1][0])
    b = solveOps(solveTry[0][1], solveTry[1][2], a)
    c = solveOps(solveTry[0][2], solveTry[1][3], b)
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

def intoWordsR(solveTry):
    """
    Function to construct human readable solution.
    """
    a = solveOps(solveTry[0][0], solveTry[1][0], solveTry[1][1])
    b = solveOps(solveTry[0][1], solveTry[1][2], a)
    c = solveOps(solveTry[0][2], solveTry[1][3], b)
    message = "Solution found! \n"+\
           str(solveTry[1][0])+" "+\
           OpsintoWords(solveTry[0][0])+" "+\
           str(solveTry[1][1])+" "+" = "+\
           str(a)+"\n"+\
           str(solveTry[1][2])+" "+\
           OpsintoWords(solveTry[0][1])+" "+\
           str(a)+" "+" = "+\
           str(b)+"\n"+\
           str(solveTry[1][3])+" "+\
           OpsintoWords(solveTry[0][2])+" "+\
           str(b)+" "+" = "+\
           str(c)+"\n\n"
    print(message)

solutionCount = 0
#solGridTries = [[('d', 'm', 't'), (1, 5, 5, 5)]]
for solveTry in solGridTries:
    if solve24(solveTry) == 24:
            solutionCount += 1 
            intoWords(solveTry)
    """
    Some strange bugs here though it comes with more solutions.
    """
    elif solve24R(solveTry) == 24:
            solutionCount += 1 
            intoWordsR(solveTry)
    # else:
    #     print (".")
if solutionCount == 0:
    print("No solution found.")