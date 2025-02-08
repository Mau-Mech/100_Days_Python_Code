import time
def factorial(n):
    if n ==0 or n == 1:
       return 1
    else:
       #print(n)
       return n * factorial(n-1)

start=time.time()

resultado = factorial (996)

end = time.time()
tiempo_total = (end - start) * 10
print(tiempo_total)
print(resultado)