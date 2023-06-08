"""
Bruteforce way of solving the classic "24" puzzle whereby the player tries to use all 4 given numbers and the operators addition, subtraction, multiplication, and division to reach exactly 24.

For example, if given the numbers 1, 2, 3, and 4, possible solutions are:

Solution 1
1 x 2 = 2
2 x 3 = 6
6 x 4 = 24

Solution 2
1 / 4  = 0.25
2 / 0.25 = 8
8 x 3 = 24

Here we explore all possible solutions by building an array of all possible arrangement of the inputs of 4 numbers i, j, k, and l and another array of all possible arrangements of the operators addition (a), substraction (s), multiplication (m), and division (d).

i [a|s|m|d] j = A
A [a|s|m|d] k = B
B [a|s|m|d] l = 24

As such, Solution 2 will be denoted by the array as:

[('d', 'd', 'm'), (1, 4, 2, 3)]
"""

import logging
import sys
from operator import __add__
from operator import __sub__
from operator import __truediv__
from operator import __mul__
from itertools import permutations
from itertools import product

if len(sys.argv) != 5:
    print("Enter 4 digits separated by spaces.\nEg python3 24.py 1 2 3 4\n")
    sys.exit()

i = int(sys.argv[1])
j = int(sys.argv[2])
k = int(sys.argv[3])
l = int(sys.argv[4])

numArray = [i,j,k,l]
numGrid = numArray
opGrid = ['a','s','m','d']
solGridN = []
solGridO = []
solGridTries = []
solutionCount = 0

'''Build the grid'''

solGridN = list(permutations(numGrid))
solGridO = list(product(opGrid,repeat=3))

for i in solGridO:
    for j in solGridN:
        solGridTries.append([i,j])

def solveOps(opers, x, y):
    try:
        if opers == "a":
            return __add__(x,y)
        if opers == "s":
            return __sub__(x,y)
        if opers == "m":
            return __mul__(x,y)
        if opers == "d":
            try:
                return __truediv__(x,y)
            except ZeroDivisionError:
                return 9999
    except BaseException:
        logging.exception("An exception was thrown!")

#def buildMessageSolution(i,j,k,l,o1,o2,o3,A,B):
def buildMessageSolution(a,o,b,c):
    """
    a [a|s|m|d] b = c
    """
    message = \
        str(a)+" "+\
        OpsintoWords(o)+" "+\
        str(b)+" "+" = "+\
        str(c)
    return message

def solve24andPrint(solveTry):
    """
    i [a|s|m|d] j = A
    A [a|s|m|d] k = B
    B [a|s|m|d] l = C
    """
    i = solveTry[1][0]
    j = solveTry[1][1]
    k = solveTry[1][2]
    l =  solveTry[1][3]
    o1 = solveTry[0][0]
    o2 = solveTry[0][1]
    o3 = solveTry[0][0]
    
    a = solveOps(o1, i, j)
    b = solveOps(o2, a, k)
    c = solveOps(o3, b, l)
    
    if c == 24:
        print("Solution found!")
        print(buildMessageSolution(i,o1,j,a))
        print(buildMessageSolution(a,o2,k,b))
        print(buildMessageSolution(b,o3,l,c))
        print("\n")
        return True
    else:
        a = solveOps(o1, j, i)
        b = solveOps(o2, k, a)
        c = solveOps(o3, l, b)
        #print(c)
        if c == 24:
            print("Solution found!")
            print(buildMessageSolution(j,o1,i,a))
            print(buildMessageSolution(k,o2,a,b))
            print(buildMessageSolution(l,o3,b,c))
            print("\n")
            return True
    return False

def OpsintoWords(opers):
    """
    Simple helper function to convert symbols into human text.
    """
    try:
        if opers == "a":
            opers = "+"
            return opers
        if opers == "s":
            opers = "-"
            return opers
        if opers == "m":
            opers = "x"
            return opers
        if opers == "d":
            opers = "÷"
            return opers
    except:
        print("Check operators.")

for solveTry in solGridTries:
    if solve24andPrint(solveTry) == True:
        solutionCount += 1
if solutionCount == 0:
    print("No solution found.")