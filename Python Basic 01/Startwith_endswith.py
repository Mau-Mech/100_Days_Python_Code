string = "Diana se peina sola"
resultado = 0
stars_with = "Ejemplos con starswith():"
ends_with = "Ejemplos con endswith(): "

print(f"\n{stars_with.rjust(50, '=')}")

resultado = string.startswith("D")
print(f"{string} comienza con la su cadena D ; {resultado}")

resultado = string.startswith("d")
print(f"{string} comienza con la su cadena d ; {resultado}")

resultado = string.startswith("Diana")
print(f"{string} comienza con la su cadena Diana ; {resultado}")

resultado = string.startswith("se" , 6)
print(f"{string} comienza con la su cadena se, desde la posicion 6 ; {resultado}")

resultado = string.startswith("se" , 6 ,7)
print(f"{string} comienza con la su cadena se, desde la posicion 6 hasta la posicion 7; {resultado}")

resultado = string.startswith("se" , 100, 100)
print(f"{string} comienza con la su cadena se, desde la posicion 100 hasta la posicion 100; {resultado}")

resultado = string.startswith("se" , -4 , -1)
print(f"{string} comienza con la su cadena se, desde la posicion -4 hasta la posicion -1 ; {resultado}")



print(f"\n{ends_with.rjust(50, '=')}")

resultado = string.endswith("A")
print(f"{string} termina con la su cadena A ; {resultado}")

resultado = string.endswith("a")
print(f"{string} termina con la su cadena a ; {resultado}")

resultado = string.endswith("sola")
print(f"{string} termina con la su cadena sola ; {resultado}")

resultado = string.endswith("sola", 10)
print(f"{string} termina con la su cadena sola, desde la posicion 10 ; {resultado}")

resultado = string.endswith("s", 9 ,14)
print(f"{string} termina con la su cadena s, desde la posicion 9 hasta la posicion 14  ; {resultado}")

resultado = string.endswith("s", 100 ,100)
print(f"{string} termina con la su cadena s, desde la posicion 100 hasta la posicion 100  ; {resultado}")

resultado = string.endswith("s", -4 ,-2)
print(f"{string} termina con la su cadena s, desde la posicion -4 hasta la posicion -2  ; {resultado}")












