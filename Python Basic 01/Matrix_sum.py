matrix_a=[[1,2,3],[4,5,6],[7,8,9]]
matrix_b=[[9,8,7],[6,5,4],[3,2,1]]
matrix_c = []

for row in range(len(matrix_a)):
    fila = []
    for column in range(len(matrix_a[0])):
        fila.append(matrix_a[row][column]+ matrix_b[row][column])
    matrix_c.append(fila)
print(matrix_c)