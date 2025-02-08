print("========================================")
print("Evaluation, the number is even or uneven")
print("========================================")

number = int(input("Please type any positive and real number:"))

response = number % 2

if response == 0:
    print("The number:",number, "is even")
else:
    print("The number:",number,"is uneven")
    print("End.")
