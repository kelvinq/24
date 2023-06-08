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