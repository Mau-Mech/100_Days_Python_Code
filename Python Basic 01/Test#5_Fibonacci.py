# Version #1
x = 0
y = 1
while x<=1597: 
    print(x, end=" ") 
    z = x + y
    y = x 
    x = z

# Version #2
a, b = 0 , 1
while b<=1597:
    print(a, b, end=" ")
    a = a + b
    b = a + b