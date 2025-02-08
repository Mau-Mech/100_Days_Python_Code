# Funcion suma de de un numero dado. Imprimir todos los valores de la suma.

def suma_numeros(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_numeros(numero -1)
    

print(suma_numeros(5))
    