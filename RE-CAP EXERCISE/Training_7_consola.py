# PROGRAMA QUE IMPRIME UN CUADRADO EN LA CONSOLA

def square(n):
    for colum in range(n):
        for row in range(n):
            print("*", end=" ")
        print()
        


val = int(input("Type the value of the square: "))

square(val)