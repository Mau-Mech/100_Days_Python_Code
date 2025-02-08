row = int(input("Please type the number of rows in the matrix: "))
column = int(input("Please type the number of columns in the matrix: "))

matrix = []

for row_1 in range(row):
    fila = []
    for column_1 in range(column):
        fila.append(int(input(f"Type the element in the row {row_1 + 1} and column {column_1 + 1}: ")))
    matrix.append(fila)
#print(matrix)


for row_2 in matrix:
    print("[", end = "")
    for element_in_matrix in row_2:            
        print(element_in_matrix, end= "", sep = ",")
    print("]")