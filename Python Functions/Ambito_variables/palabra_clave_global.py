y = 20


def funcion():
    global y
    y = 30
    print(y, "Impresion dentro de la funcion")


funcion()
print(y, "Impresion fuera de la funcion")