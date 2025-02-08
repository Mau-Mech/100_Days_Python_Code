# Logic operator "and"
print("AND, &")
num_1 = int(input("Type a number higher than 2 and lower than 5: "))
if num_1 > 2 and num_1 < 5 :
    print("the number is correct")
else:
    print("The number is not correct")


# Logic operator "or"
print("Or option")
word = input("In order to complete the condition type 'yes' or 'si':")
if word == "si" or word =="yes":
    print("The word fulfill at least one of the conditions")
else:
    print("The word is not in the given option")



# Logic operator "not"
print("NOT operator")

num_1 = int(input("Type a number equal to 5: "))
if not num_1 ==  5:
    print("The number is different at 5, the condition is met")
else:
    print("The number is equal to 5 the condition is NOT met")
