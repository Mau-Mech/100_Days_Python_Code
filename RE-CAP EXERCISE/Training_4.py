#FUNCION QUE DETERMINA SI UN NUMERO ES PAR O IMPAR

def impar(value):
    if value % 2 == 0:
        print(f"El valor {value} es par.")
    else:
        print(f"El valor {value} es impar.")


num = int(input("escribe el numero que quieres verificar; "))

impar(num)