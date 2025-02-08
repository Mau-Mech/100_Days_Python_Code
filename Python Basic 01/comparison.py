print("What values do you want to compare?")
num_1 = int(input("Please type the first value: "))

num_2 = int(input("Please type the second value: "))

if num_1 > num_2:
    print("The number:",num_1,"is higher than:",num_2)
if num_1 < num_2:
    print("The number:",num_1,"is lower than:",num_2)
if num_1 == num_2:
    print("The number:",num_1,"is equal at:",num_2)
if num_1 != num_2:
    print("The number:",num_1,"is diferent at:",num_2)
else:
    print("You do not type a number, please try again")

if num_1 <= num_2:
    print("The number:",num_1,"is equal or lower than:",num_2)
if num_1 >= num_2:
    print("The number:",num_1,"is equal or higher than:",num_2)
else:
    print("You do not type a number, please try again")
print("End.")