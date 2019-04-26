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