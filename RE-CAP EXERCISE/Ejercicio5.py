print("Fibonaci Series")
x = 0 
y = 1
while x <= 1597:
    print(x , end = ",")
    z = y + x
    y = x
    x = z
print ("End of serie.")