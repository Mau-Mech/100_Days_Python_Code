#list_1 = [1,7,4,3,2,8,9,6,6,9,5,3,4,1,7,2,8]

list_1 = "Mauricio Jimenez Calvo"

#list_1.sort()
numbers = dict.fromkeys(list_1, 0)
for num in list_1:
    numbers[num] += 1

print(numbers)



for num_2 in numbers:
    #print(num_2)
    if numbers[num_2] == 1:
        print(num_2)
        break
 

for num_2 in numbers:
    print(f"Este es el valor del contador: {num_2}")
    print(f"Este es el valor del diccionario usando el contador como indice: {numbers[num_2]}")

