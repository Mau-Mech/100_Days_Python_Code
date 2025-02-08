print("Calculator with only 1 variable")

print("*options menu*")
print("1. Sum")
print("2. Minus")
print("3. Multiplication")
print("4. Divided")
print("5. Integer Divided")
print("6. Power by")
print("7. Module")

election = int(input("Choose an operation: "))

if election == 1:
    number = int(input("Please type the first number: "))
    number += int(input("Please type the second number number: "))
    print (f"The result of the sum its {number}")
if election == 2:
    number = int(input("Please type the first number: "))
    number -= int(input("Please type the second number number: "))
    print (f"The result of the rest its {number}")
if election == 3:
    number = int(input("Please type the first number: "))
    number *= int(input("Please type the second number number: "))
    print (f"The result of the multiplication its {number}")
if election == 4:
    number = int(input("Please type the first number: "))
    number /= int(input("Please type the second number number: "))
    print (f"The result of the divition its {number}")
if election == 5:
    number = int(input("Please type the first number: "))
    number //= int(input("Please type the second number number: "))
    print (f"The result of the integer divition its {number}")
if election == 6:
    number = int(input("Please type the first number: "))
    number **= int(input("Please type the second number number: "))
    print (f"The result of the power its {number}")
if election == 7:
    number = int(input("Please type the first number: "))
    number %= int(input("Please type the second number number: "))
    print (f"The result of the module its {number}")

else: 
    print("The option does not exist, try again. ")