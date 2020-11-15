class Matrix:
    def __init__(self, rows, columns):
        self.matrix = [[0 for i in range(columns)] 
                        for j in range(rows)]
    
    @property
    def rows(self):
        return len(self.matrix)
    @property
    def columns(self):
        return len(self.matrix[0])
    
    def set_data(self):
        print(f"Enter values: ")
        self.matrix = [[int(input())for k in range(self.columns)] 
                        for i in range(self.rows)]
    
    def __str__(self):
        for i in range(self.rows):
            print(self.matrix[i])
        return ""
    
    def __add__(matrix, matrix2):
        if(matrix.columns == matrix2.columns) and (matrix.rows == matrix2.rows):
            temp = Matrix(matrix.columns, matrix.rows)
            temp.matrix = [matrix.matrix[i][j] + matrix2.matrix[i][j] 
                            for j in range(matrix.columns) for i in range(matrix.rows)]
            return temp
        raise ValueError("unequal order")

    def __sub__(matrix, matrix2):
        if(matrix.columns == matrix2.columns) and (matrix.rows == matrix2.rows):
            temp = Matrix(matrix.columns, matrix.rows)
            temp.matrix = [matrix.matrix[i][j] - matrix2.matrix[i][j] 
                            for j in range(matrix.columns) for i in range(matrix2.rows)]
            return temp
        raise ValueError("unequal order")

    def __mul__(matrix, matrix2):
        if(matrix.rows != matrix2.columns) or (matrix.columns != matrix2.rows):
            return "Multiplication isn't possible"
        temp = Matrix(matrix.rows, matrix2.columns)
        for i in range(matrix.rows):
            for j in range(matrix2.columns):
                t = 0
                for k in range(matrix.columns):
                    t += matrix.matrix[i][k]*matrix2.matrix[k][j]
                temp.matrix[i][j] = t
        return temp
    
matrix = Matrix(2, 2)
matrix.set_data()
matrix2 = Matrix(2, 2)
matrix2.set_data()

if __name__ == "__main__":
    print("matrix data: ", matrix, sep="\n")
    print("matrix2 data: ", matrix2, sep="\n")
    print("matrix + matrix2: ")
    print(matrix + matrix2, sep="\n")
    print("matrix - matrix2: ")
    print(matrix - matrix2)
    print("matrix * matrix2: ")
    print(matrix * matrix2)
    matrix.matrix = [[1, 2, 3]]
    matrix2.matrix = [[1], [2]]
    print("matrix: ", matrix, "matrix2: ", matrix2, "matrix * matrix2: ", matrix * matrix2, sep="\n")
