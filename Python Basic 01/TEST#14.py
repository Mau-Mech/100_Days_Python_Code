matrix_quantity = int(input("Please type the number of matrix that you want to sum: "))
if matrix_quantity < 1:
    print("The number of Matrix are below of two, please add another matrix")    
else:
    row = int(input("Please type the number of rows in the matrix: "))
    column = int(input("Please type the number of columns in the matrix: "))
    matrix_list = []

    #llenado de matrices
    for matrix_1 in range(matrix_quantity):
     matrix = []
     for row_1 in range(row):
         row_in_matrix=[]
         for column_1 in range(column):
          row_in_matrix.append(int(input(f"For the matrix {matrix_1 + 1}, please type the element in the row {row_1+1} and column {column_1+1}: ")))
         matrix.append(row_in_matrix)
     matrix_list.append(matrix)

    #suma de matrices
    matrix =[]
    for row_2 in range(row):
        new_row = []
        for column_2 in range(column):
          sum_matrix = 0
          for matrix_position in range(len(matrix_list)):
            sum_matrix += matrix_list[matrix_position][row_2][column_2]
          new_row.append(sum_matrix)
        matrix.append(new_row)
    matrix_list.append(matrix)
   
    #imprimir matrices
    for matrix_row in range(row):
       for matrix_list_position in range(len(matrix_list)):
          if matrix_row != 1:
             print(f"{matrix_list[matrix_list_position][matrix_row]}", end = "   ")
          else:
             if matrix_list_position < len(matrix_list) - 2:
                   print(f"{matrix_list[matrix_list_position][matrix_row]}", end = " + ")
             elif matrix_list_position < len(matrix_list) - 1:
                   print(f"{matrix_list[matrix_list_position][matrix_row]}", end = " = ")
             else: 
                   print(f"{matrix_list[matrix_list_position][matrix_row]}", end = "  ")
       print ()