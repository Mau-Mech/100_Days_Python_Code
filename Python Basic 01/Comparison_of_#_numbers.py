print("=======================")
print("Comparison of 3 numbers")
print("=======================")
num_1 = int(input("Please provide the first integer number: "))
num_2 = int(input("Please provide the second integer number: "))
num_3 = int(input("Please provide the thirt integer number: "))
if num_1 > num_2:
    major_1 = num_1
else:
    major_1 = num_2
if num_3 > major_1:
    higher_value = num_3
else:
    higher_value = major_1
print("The higher value is; ", higher_value," ")