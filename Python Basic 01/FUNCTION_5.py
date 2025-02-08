#PROGRAMA QUE DETERMINA SI UN NUMERO ES PRIMO O NO 

def primo(n):
    if n <= 1:
        print ("Los numeros primos son mayores o diferentes a 1 ")
    elif n == 2: 
     return print("Si es un numero primo")
    elif n%2 == 1: 
     return print("Si es un numero primo")
    else: 
     return print("No es un numero primo")

number = int(input("Escribe el numero que quieres saber si es primo o no: "))

result = primo(number)