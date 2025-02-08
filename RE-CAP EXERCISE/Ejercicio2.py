# Determine if a number is odd or even

number = int(input("Please type the number that you want to determine if its even or odd: "))

result = number%2

if result ==0:
    print(f"The number {number} its even.")
else:
    print(f"The number {number} its odd.")