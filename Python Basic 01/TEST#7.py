string = input("Please type any phase that you whish to reverse: ")
new_string = ""

for i in string:
    new_string = i + new_string
print(f"The reverse string is: {new_string}")