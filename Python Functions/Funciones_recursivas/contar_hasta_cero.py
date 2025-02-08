def contar_hasta_cero(n):
    if n <= 0:
        print("He llegado a cero!")
    else:
        print(n)
        n = n - 1
        contar_hasta_cero(n)


contar_hasta_cero(10)