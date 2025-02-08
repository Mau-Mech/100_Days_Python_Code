print("This is a number comparison, Im going to tell you the higher number of 3")
num_1 = int(input("Please type the number #1: " ))
num_2 = int(input("Please type the number #2: " ))
num_3 = int(input("Please type the number #3: " ))

if num_1 < num_2:
    num_1 = num_2

if num_1 < num_3:
    num_1 = num_3


print(f"The higher number its: {num_1} ")
