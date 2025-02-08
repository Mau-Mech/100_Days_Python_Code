import time

number = int (input("Provide the number: "))


factorial = 1
start=time.time()
for value in range(1,number):
    #print (value)
    factorial = factorial * (value + 1 )

print(f"El factorial es =", factorial)

end = time.time()
tiempo_total = (end - start) * 1000
print(tiempo_total)
