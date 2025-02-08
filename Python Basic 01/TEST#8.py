number = int( input("¿Que tabla de multiplicar quieres ver?: "))

print(f"La tabla de multiplicar del {number} es:")

for index in range(0,11):
    print(f"{number} X {index} = {number*index}")
