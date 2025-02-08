#matrix_cuantity = int(input("Please type the number of matrix that you want to sum: "))

row = int(input("Please type the number of rows in the matrix: "))
column = int(input("Please type the number of columns in the matrix: "))
matrix_a = []
matrix_b = []
matrix_c = []

for row_1 in range(row):
    fila = []
    for column_1 in range(column):
        fila.append(int(input(f"Type the element in the row {row_1 + 1} and column {column_1 + 1}: ")))
    matrix_a.append(fila)

for row_2 in matrix_a:
    for element_in_matrix in row_2:
        print(element_in_matrix, end = " ")
    print()

for row_1 in range(row):
    fila = []
    for column_1 in range(column):
        fila.append(int(input(f"Type the element in the row {row_1 + 1} and column {column_1 + 1}: ")))
    matrix_b.append(fila)
for row_2 in matrix_b:
    for element_in_matrix in row_2:
        print(element_in_matrix, end = " ")
    print()

for row in range(len(matrix_a)):
    fila = []
    for column in range(len(matrix_a[0])):
        fila.append(matrix_a[row][column]+ matrix_b[row][column])
    matrix_c.append(fila)
for row_2 in matrix_c:
    for element_in_matrix in row_2:
        print(element_in_matrix, end = " ")
    print()