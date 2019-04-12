#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.

#Good luck.
from math import sqrt
class Matrix():
    def __init__(self, arg1, arg2, arg3, arg4):
        self.dimension = 2
        self._matrix = [[arg1,arg2],[arg3,arg4]]
    
    def __add__(self, other):
        for index in range(self.dimension):
            self._matrix[index] = [sum(x) for x in zip(self._matrix[index], other._matrix[index])]
        return self
        
    def __mul__(self, other):
        matrix = [[0,0],[0,0]]
        for k in range(self.dimension):
            for h in range(self.dimension):
                for j in range(self.dimension):
                   matrix[h][k] += self._matrix[h][j] * other._matrix[j][k]
        self._matrix = matrix
        return self

    def __str__(self):
        msg = ""
        for row in self._matrix:
            msg += "{}\n".format(str(row))
        return msg

if __name__ == "__main__":
    matrix_1 = Matrix(1,1,1,1)
    matrix_2 = Matrix(1,1,1,1)
    print(matrix_1)
    matrix_1 = matrix_2 + matrix_1 
    print(matrix_1)
    matrix_1 = matrix_2 * matrix_1 
    print(matrix_1)