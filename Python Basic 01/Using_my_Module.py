from My_first_Module import ciclo_pares

n = int(input("Ingrese un numero: "))
print(f'Los numero pares hasta {n} son: ')

for i in ciclo_pares(n):
    print(i)