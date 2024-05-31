# goal: Write a function that takes an nxn matrix as input and outputs the inverse matrix.

# input: n numbers
n = int(input("Enter number of rows/columns: "))

# define the MatrixMinor function
def MatrixMinor(matrix, i, j):
    minor = []
    for k in range(len(matrix)):
        if k != i: # if the row is not the one we want to remove
            minor.append([]) # add the corresponding row
            for l in range(len(matrix)):
                if l != j: # if the column is not the one we want to remove
                    minor[-1].append(matrix[k][l]) # add the corresponding column and put the element in.
    return minor

# define the MatrixDeterminant function
def MatrixDeterminant(matrix):
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    det = 0

    for j in range(size): # iterate over the elements of the first row
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]] # remove the first row and the jth column

        cofactor = (-1) ** (j % 2) * MatrixDeterminant(sub_matrix) # calculate the cofactor

        det += cofactor * matrix[0][j] # add the cofactor times the element to the determinant

    return det

# define the MatrixCofactor function
def MatrixCofactor(matrix):
    cofactor = []
    for i in range(len(matrix)):
        cofactor.append([])
        for j in range(len(matrix)):
            cofactor[-1].append(MatrixDeterminant(MatrixMinor(matrix, i, j))*((-1)**(i+j))) # calculate the cofactor
    return cofactor

# define the MatrixTranspose function
def MatrixTranspose(matrix):
    transpose = []
    for i in range(len(matrix)):
        transpose.append([])
        for j in range(len(matrix)):
            transpose[-1].append(matrix[j][i]) # swap the rows and columns
    return transpose

# define the MatrixAdjoint function
def MatrixAdjoint(matrix):
    return MatrixTranspose(MatrixCofactor(matrix))

# define the MatrixInverse function
def MatrixInverse(matrix):
    if MatrixDeterminant(matrix) == 0:
        print("Matrix is not invertible, determinant is ", MatrixDeterminant(matrix))
        return matrix
    det = MatrixDeterminant(matrix)
    adjoint = MatrixAdjoint(matrix)
    inverse = adjoint
    for i in range(len(inverse)):
        for j in range(len(inverse)):
            inverse[i][j] /= det # divide each element by the determinant
    return inverse

# define the ReadMatrix function
def ReadMatrix(matrix):
    for i in range(n):
        print("[", end="")
        for j in range(n):
            print("\t", matrix[i][j], "\t", end="")
        print("]\n")

# take user input
inputmatrix = []
for i in range(n):
    inputmatrix.append([])
    for j in range(n):
        inputmatrix[i].append(int(input("Enter number: ")))

print("The input is: ")
ReadMatrix(inputmatrix)

# apply inverse function
print("The inverse is: ")
ReadMatrix(MatrixInverse(inputmatrix))