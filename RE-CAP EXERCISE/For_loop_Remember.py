import random

letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

list = []
list2 = []

letras = int(input("Cuantas letras quieres imprimir: "))

for i in range(letras+1):
    list.append(i)
    list2.append(letters[random.randint(0,len(letters))])


print(list)
print(list2)