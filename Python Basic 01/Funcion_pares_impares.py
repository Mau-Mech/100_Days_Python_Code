ejemplo = [3,7,9,5,8,3,12]

def pares_impares (ejemplo):
    pares = []
    impares = []
    for elemento in range(len(ejemplo)):
        if ejemplo[elemento] % 2 == 0:
         pares.append(ejemplo[elemento])
        else:
         impares.append(ejemplo[elemento])
    return pares , impares


pares,impares = pares_impares(ejemplo)
print(pares)
print(impares)